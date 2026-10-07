"""Recompute the Content-Security-Policy in v2/index.html.

The CSP allows the page's single inline <style> and <script> by SHA-256 hash
(no 'unsafe-inline'), so run this after editing either block:

    python tools/update-csp.py
"""
import base64
import hashlib
import pathlib
import re

PAGE = pathlib.Path(__file__).resolve().parent.parent / "v2" / "index.html"


def sha256(body: str) -> str:
    digest = hashlib.sha256(body.encode("utf-8")).digest()
    return "'sha256-" + base64.b64encode(digest).decode() + "'"


html = PAGE.read_text(encoding="utf-8")
style = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
# Only executable scripts need a hash; JSON-LD data blocks are not run
script = re.search(r"<script>(.*?)</script>", html, re.S).group(1)

policy = "; ".join([
    "default-src 'none'",
    "script-src " + sha256(script),
    "style-src " + sha256(style) + " https://fonts.googleapis.com",
    "font-src https://fonts.gstatic.com",
    "img-src 'self' data: https://i.pravatar.cc",
    "connect-src 'none'",
    "form-action 'none'",
    "base-uri 'none'",
    "object-src 'none'",
    "manifest-src 'self'",
    "upgrade-insecure-requests",
])

html, count = re.subn(
    r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(">)',
    lambda m: m.group(1) + policy + m.group(2),
    html,
)
assert count == 1, "CSP meta tag not found"
PAGE.write_text(html, encoding="utf-8", newline="\n")
print(policy)

from browser import document, html
from .code.view import singIn, singUp

base = document["content"]
body = singIn(base)

base <= body

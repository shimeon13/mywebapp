#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import sys
import io
import cgitb
cgitb.enable()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("context-type: text/html")
print("")

form = cgi.FieldStorage()

for key in form:
    value = form[key].value
    print("<p>%s: %s</p>" % (key, value))

htmltext = """\
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>体重計算</title>
    </head>
    <body>
    <form action = "", method = "get">
    性別：<input type="text" name="gender">
    <input type="submit" value="送信">
    </form>
    {{ if gender}}
        性別は{{"gender"}}です。<br>
        予測体重は{{ p }}kgです。<br>
        除脂肪体重は{{ l }}kgです。<br>
        理想体重は{{ i }}kgです。
    {{endif}}
    </body>
    </html>
    """

print(htmltext)

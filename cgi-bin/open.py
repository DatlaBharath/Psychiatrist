#!/usr/bin/python3
print("Content-Type: text/html")
print()
import openai
import subprocess
import cgi
openai.api_key = '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'
data = cgi.FieldStorage()
query = data.getvalue("query")
res = openai.Completion.create(
    prompt = "act as psychiatrist named bora with 30 years experience.Now answer my Query."+query,
    model =  "text-davinci-003",
    max_tokens = 100
)
print('<p style="margin: 0px">' + res["choices"][0]["text"] + '</p>')
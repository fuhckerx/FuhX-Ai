from flask import Flask, request
import urllib.request
import json

app = Flask(__name__)

OPENROUTER_API_KEY = "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"

def ask_ai(question):
    url = "https://openrouter.ai/api/v1/chat/completions"
    payload = {
        "model": "baidu/cobuddy:free",
        "messages": [{"role": "user", "content": question}]
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "X-Title": "fuhx"
        },
        method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))
        return result["choices"][0]["message"]["content"]


@app.route("/")
def home():
    return "fuhx AI — use: /your question", 200

@app.route("/<path:question>")
def answer(question):
    try:
        ans = ask_ai(question)
        return ans, 200, {"Content-Type": "text/plain; charset=utf-8"}
    except Exception as e:
        return str(e), 500, {"Content-Type": "text/plain; charset=utf-8"}
  

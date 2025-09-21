from flask import Flask, render_template, request, Response
import ollama

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("query")

    def generate():
        stream = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": user_query}],
            stream=True
        )
        for chunk in stream:
            if "message" in chunk and "content" in chunk["message"]:
                yield f"data: {chunk['message']['content']}\n\n"
        yield "data: [DONE]\n\n"

    return Response(generate(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True)

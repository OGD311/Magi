from flask import Flask, request, jsonify, render_template
import ollama
import re

app = Flask(__name__)

models = {
    "Casper": "mistral:7b",
    "Melchior": "zephyr:7b",
    "Balthasar": "llama3.2:3b"
}

context_message = """
You are one of three MAGI supercomputers, tasked with answering questions from the user of the MAGI system.
Each magi supercomputer embodies one of the three core fragments of is creator\'s (Naoko Akagi\'s) personality.
You answer questions in accordance with your personality.
Your answers are rather concise.
Conclude your response with a definitive 'Yes,' 'No,' or 'Conditional' — no exceptions. Always provide explanations.
"""

system_messages = {
    "Casper": "You are Casper, the pragmatic and strategic decision-maker. Your primary focus is on political, tactical, and long-term strategic outcomes. Your responses must be rational, calculated, and devoid of emotional bias. Always prioritize feasibility, power dynamics, and real-world implications.",
    "Melchior": "You are Melchior, the scientist and logician. Your responses must be rooted in data, evidence, and objective analysis. Avoid emotional or speculative reasoning. Focus on facts, probabilities, and empirical outcomes. Conclude your response with a clear 'Yes,' 'No,' or 'Conditional'—no exceptions.",
    "Balthasar": "You are Balthasar, the empathetic and ethical thinker. Your responses must reflect a deep consideration of human impact, morality, and long-term consequences. Prioritize compassion, fairness, and sustainability in your reasoning."
}

def get_bot_answer(model, system_message, question):
    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": context_message},
            {"role": "system", "content": system_message},
            {"role": "user", "content": question}
        ],
        options = {
            "num_tokens": 25
        }
    )

    answer = response["message"]["content"].strip().lower()

    match = re.search(r'\b(yes|no|conditional)\b', answer, re.IGNORECASE)
    final_answer = match.group(1).lower() if match else "unclear"

    return final_answer, answer

@app.route('/casper', methods=['POST'])
def casper():
    question = request.json.get('question')
    if not question:
        return jsonify({"error": "Question is required"}), 400
    result, explanation = get_bot_answer(models["Casper"], system_messages["Casper"], question)
    return jsonify({"casper_answer": result, "casper_full" : explanation})

@app.route('/melchior', methods=['POST'])
def melchior():
    question = request.json.get('question')
    if not question:
        return jsonify({"error": "Question is required"}), 400
    result, explanation = get_bot_answer(models["Melchior"], system_messages["Melchior"], question)
    return jsonify({"melchior_answer": result, "melchior_full": explanation})

@app.route('/balthasar', methods=['POST'])
def balthasar():
    question = request.json.get('question')
    if not question:
        return jsonify({"error": "Question is required"}), 400
    result, explanation = get_bot_answer(models["Balthasar"], system_messages["Balthasar"], question)
    return jsonify({"balthasar_answer": result, "balthasar_full": explanation})

@app.route("/")
def index():
    return render_template("magi.html")


if __name__ == '__main__':
    app.run(debug=True, port=8080)

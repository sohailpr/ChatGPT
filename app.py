from flask import Flask, render_template, request, redirect, url_for
import openai

print("Start")
app = Flask(__name__)

# Function to get API key from file
def get_api_key():
    with open("api.txt", "r") as f:
        return f.read().strip()

# Function to get AI response using gpt-3.5-turbo
def get_ai_response(subject, question, option):
    openai.api_key = get_api_key()

    # Create a prompt including the subject, question, and option selected
    prompt = f"Subject: {subject}\nQuestion: {question}\nOption: {option}\nAnswer:"

    # Use the gpt-3.5-turbo model (updated model)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Updated model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form inputs
        subject = request.form["subject"]
        question = request.form["question"]
        option = request.form["option"]

        # Get the response from OpenAI
        result = get_ai_response(subject, question, option)

        return render_template("result.html", result=result)

    return render_template("index.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)

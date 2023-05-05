import openai
import json
from flask import Flask, render_template, request

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = "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"

# Define the home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fitness", methods=['POST'])
def fitness():
    return render_template("fitness.html")


# Define the chatbot endpoint
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Get the user's message from the request
    message = request.form["message"]

    # Set up the OpenAI API request
    prompt = f"User: {message}\nFitness Coach:"
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the response from OpenAI
    response = completions.choices[0].text.strip()

    # Return the response as JSON
    return json.dumps({"response": response})


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    try:
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or the model you want to use
            prompt=user_message,
            max_tokens=150
        )
        bot_response = response.choices[0].text.strip()
        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

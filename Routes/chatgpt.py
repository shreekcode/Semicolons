from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import openai
import os

# Set up OpenAI API key
openai.api_key = os.environ['OPENAI_KEY']

chatgpt_routes = Blueprint('chatgpt_routes', __name__)

# Define API endpoint for ChatGPT integration
@chatgpt_routes.route('/api/chat', methods=['POST'])
@jwt_required()
def chat():
    # Get user input from POST request
    user_input = request.json['message']

    # Define the parameters for the GPT-3 API request
    prompt = f"{user_input}"
    temperature = 0.5
    max_tokens = 50

    # Call the OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the AI response from the API response
    ai_response = response.choices[0].text.strip()

    # Return the AI response to the user
    return jsonify({'ai_response': ai_response})
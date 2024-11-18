from flask import Blueprint, request, jsonify
import requests
import json
import os
from db import get_db_connection

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    if user_message.strip().lower() == '/ceklimit':
        return check_limit(user_message)

    url = 'https://xiex.my.id/api/ai/chat/completions'
    headers = {'Content-Type': 'application/json'}
    data = {
        'apikey': os.getenv('API_KEY', 'default_api_key'),
        'model': 'brainxiex',
        'server': 1,
        'messages': [{'role': 'user', 'content': user_message}]
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_data = response.json()
        assistant_message = response_data['choices'][0]['message']['content']
        token = response_data.get('token', 'no_token')
    except requests.RequestException as e:
        return jsonify({'error': 'Server error. Please try again later.'}), 500

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO messages (role, content) VALUES (?, ?)", ('user', user_message))
    c.execute("INSERT INTO messages (role, content) VALUES (?, ?)", ('assistant', assistant_message))
    conn.commit()
    conn.close()

    return jsonify({'answer': assistant_message, 'token': token})

def check_limit(user_message):
    url = f'https://xiex.my.id/api/ceklimit?apikey={os.getenv("API_KEY", "default_api_key")}'
    try:
        response = requests.post(url)
        response.raise_for_status()
        response_data = response.json()
        limit_message = f"Your current limit is: {response_data['limit']}"
    except requests.RequestException as e:
        return jsonify({'error': 'Server error. Please try again later.'}), 500

    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO messages (role, content) VALUES (?, ?)", ('user', user_message))
    c.execute("INSERT INTO messages (role, content) VALUES (?, ?)", ('assistant', limit_message))
    conn.commit()
    conn.close()

    return jsonify({'answer': limit_message})

@chat_bp.route('/delete_all', methods=['DELETE'])
def delete_all():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM messages")
    conn.commit()
    conn.close()
    return jsonify({'status': 'All messages deleted'})
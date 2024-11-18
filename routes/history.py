
from flask import Blueprint, jsonify
from db import get_db_connection

history_bp = Blueprint('history', __name__)

@history_bp.route('/history', methods=['GET'])
def history():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT role, content FROM messages")
    messages = c.fetchall()
    conn.close()
    return jsonify([{'role': role, 'content': content} for role, content in messages])
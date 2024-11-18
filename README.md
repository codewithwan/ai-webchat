# AI Assistant Chat

This project is a simple AI Assistant Chat application built using Flask for the backend and vanilla JavaScript for the frontend. The application allows users to interact with an AI assistant, view chat history, and delete all messages.

## Features

- **Chat with AI Assistant**: Users can send messages to the AI assistant and receive responses.
- **View Chat History**: Users can view the history of their conversations with the AI assistant.
- **Delete All Messages**: Users can delete all messages from the chat history.

## Project Structure

- **app.py**: The main Flask application file that initializes the app and registers blueprints.
- **chat.py**: Contains the routes for handling chat messages and checking API limits.
- **history.py**: Contains the route for fetching chat history.
- **db.py**: Contains functions for initializing the database and getting a database connection.
- **.env**: Contains environment variables such as `SECRET_KEY` and `API_KEY`.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **static/**: Contains static files like JavaScript and CSS.
    - **script.js**: Handles the frontend logic for sending messages, fetching chat history, and deleting messages.
    - **styles.css**: Contains the styles for the chat application.
- **templates/**: Contains HTML templates.
    - **index.html**: The main HTML template for the chat application.

## Setup

1. **Clone the repository**:
     ```sh
     git clone https://github.com/yourusername/ai-assistant-chat.git
     cd ai-assistant-chat
     ```

2. **Create a virtual environment**:
     ```sh
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

3. **Install dependencies**:
     ```sh
     pip install -r requirements.txt
     ```

4. **Set up environment variables**:
     Create a `.env` file in the root directory and add your `SECRET_KEY` and `API_KEY`:
     ```properties
     SECRET_KEY=your_secret_key
     API_KEY=your_api_key
     ```

5. **Initialize the database**:
     ```sh
     python -c "from db import init_db; init_db()"
     ```

6. **Run the application**:
     ```sh
     flask run
     ```

7. **Open the application**:
     Open your browser and go to `http://127.0.0.1:5000`.

## Usage

- **Send a message**: Type your message in the input box and click "Send".
- **View chat history**: The chat history is automatically loaded when the page is opened.
- **Delete all messages**: Click the "Delete" button to delete all messages from the chat history.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://docs.python-requests.org/)
- [SQLite](https://www.sqlite.org/)
- [Dotenv](https://pypi.org/project/python-dotenv/)

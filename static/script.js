document.addEventListener("DOMContentLoaded", (event) => {
  fetch("/history")
    .then((response) => response.json())
    .then((data) => {
      const chatBox = document.getElementById("chat-box");
      data.forEach((message) => {
        const messageDiv = document.createElement("div");
        messageDiv.className = `message ${message.role}`;
        messageDiv.innerHTML = parseMessage(message.content);
        chatBox.appendChild(messageDiv);
      });
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch((error) => {
      displayErrorMessage("Error fetching chat history.");
      console.error("Error fetching chat history:", error);
    });
});

function sendMessage() {
  const userInput = document.getElementById("user-input");
  const message = userInput.value;
  if (message.trim() === "") return;

  const chatBox = document.getElementById("chat-box");
  const userMessageDiv = document.createElement("div");
  userMessageDiv.className = "message user";
  userMessageDiv.innerHTML = parseMessage(message);
  chatBox.appendChild(userMessageDiv);

  fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: message }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        displayErrorMessage(data.error);
      } else {
        const assistantMessageDiv = document.createElement("div");
        assistantMessageDiv.className = "message assistant";
        assistantMessageDiv.innerHTML = parseMessage(data.answer);
        chatBox.appendChild(assistantMessageDiv);
        console.log("Token:", data.token);
      }
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch((error) => {
      displayErrorMessage("Error sending message.");
      console.error("Error sending message:", error);
    });

  userInput.value = "";
}

function deleteAllMessages() {
  fetch("/delete_all", {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.status);
      const chatBox = document.getElementById("chat-box");
      chatBox.innerHTML = "";
    })
    .catch((error) => {
      displayErrorMessage("Error deleting messages.");
      console.error("Error deleting messages:", error);
    });
}

function parseMessage(message) {
  // Replace **text** with <strong>text</strong>
  message = message.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
  // Replace newlines with <br>
  message = message.replace(/\n/g, "<br>");
  // Replace ```language\ncode\n``` with <pre><code class="language">code</code></pre>
  message = message.replace(
    /```(\w+)\n([\s\S]*?)```/g,
    '<pre><code class="$1">$2</code></pre>'
  );
  return message;
}

function displayErrorMessage(error) {
  const chatBox = document.getElementById("chat-box");
  const errorMessageDiv = document.createElement("div");
  errorMessageDiv.className = "message assistant";
  errorMessageDiv.innerHTML = `<strong>Error:</strong> ${error}`;
  chatBox.appendChild(errorMessageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

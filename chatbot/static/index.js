// Function to get the CSRF token from cookies
function getCSRFToken() {
    const cookie = document.cookie.split(';').find(c => c.trim().startsWith('csrftoken='));
    return cookie ? cookie.split('=')[1] : null;
}

// Function to send a message via a POST request
function sendMessage() {
    const userInput = document.getElementById('chat-input');
    const message = userInput.value.trim();
    const csrfToken = getCSRFToken();

    if (!csrfToken) {
        console.error('CSRF token not found');
        appendMessage('Bot', 'Error: CSRF token not found.');
        return;
    }

    if (message) {
        appendMessage('You', message);

        fetch('/chat/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            setTimeout(() => {
                appendMessage('Bot', data.response);
            }, 500);
        })
        .catch(error => {
            console.error('Error:', error);
            appendMessage('Bot', 'An error occurred while sending your message.');
        });

        userInput.value = '';
    }
}

// Function to append a message to the chat box
function appendMessage(sender, message) {
    const chatMessages = document.querySelector('.chat-box-body');
    if (!chatMessages) {
        console.error('Error: chat-box-body element not found');
        return;
    }

    const messageElement = document.createElement('div');
    messageElement.className = `message ${sender.toLowerCase()}-message`;

    // Get the current time in HH:MM format
    const currentTime = new Date().toLocaleTimeString([], {
        hour: '2-digit',
        minute: '2-digit',
        hour12: true // Change to false for 24-hour format
    });

    // Add the message with timestamp
    messageElement.innerHTML = `
        <div class="message-content">
            <strong>${sender}:</strong> ${message}
        </div>
        <div class="timestamp">${currentTime}</div>
    `;

    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Event listener for chat circle toggle
const chatCircle = document.getElementById('chat-circle');
if (chatCircle) {
    chatCircle.addEventListener('click', function () {
        toggleElement(chatCircle);
        toggleElement(document.querySelector('.chat-box'));
    });
}

// Event listener for chat box close button
const chatBoxToggle = document.querySelector('.chat-box-toggle');
if (chatBoxToggle) {
    chatBoxToggle.addEventListener('click', function () {
       // toggleElement(chatCircle);
        toggleElement(document.querySelector('.chat-box'));
    });
}

// Utility function to toggle visibility of an element with fade effect
function toggleElement(element) {
    if (element.style.display === 'none' || element.style.display === '') {
        element.style.display = 'block';
        element.style.opacity = 0;
        setTimeout(() => { element.style.opacity = 1; }, 10);
    } else {
        element.style.opacity = 0;
        setTimeout(() => { element.style.display = 'none'; }, 300);
    }
}

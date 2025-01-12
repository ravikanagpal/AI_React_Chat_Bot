import React, { useState, useEffect } from 'react';
import './App.css';

const App = () => {
  const [messages, setMessages] = useState([]); // State for messages
  const [error, setError] = useState(''); // State for errors
  const [message, setMessage] = useState(''); // State for input

  const apiUrl = 'http://127.0.0.1:8000/chat';

  // Fetch messages from the backend
  const fetchMessages = async () => {
    try {
      const response = await fetch(`${apiUrl}/history`);
      if (!response.ok) throw new Error('Failed to fetch messages');
      const data = await response.json();
      setMessages(data);
      setError('');
    } catch (err) {
      console.error(err.message);
      setError('Error loading messages. Please try again.');
    }
  };

  // Send a new message to the backend
  const sendMessage = async () => {
    if (!message.trim()) return;
    try {
      const response = await fetch(`${apiUrl}/message`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message }),
      });
      if (!response.ok) throw new Error('Failed to send message');
      setMessage('');
      fetchMessages(); // Reload messages after sending
    } catch (err) {
      console.error(err.message);
      setError('Error sending message. Please try again.');
    }
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  return (
      <div className="App">
        <h1>Chat Application</h1>
        <div id="messages" className="messages">
          {messages.map((msg, index) => (
              <div key={index} className="message">
                <strong>{msg.user}:</strong> {msg.message}
              </div>
          ))}
        </div>
        {error && <div className="error">{error}</div>}
        <div id="inputArea" className="inputArea">
          <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
              placeholder="Type your message here..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
  );
};

export default App;
import React, { useState, useRef, useEffect } from 'react';

const ChatInterface = () => {
  const [messages, setMessages] = useState([
    { id: 1, text: "Hi there! I'm Spambuster 🛡️ Send me a message and I'll tell you if it's spam or genuine.", sender: 'bot' }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    const userMessage = {
      id: Date.now(),
      text: inputValue.trim(),
      sender: 'user'
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsTyping(true);

    try {
      const apiUrl = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';
      const response = await fetch(`${apiUrl}/api/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage.text })
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      
      setTimeout(() => {
        setMessages(prev => [...prev, {
          id: Date.now(),
          text: data.response_text,
          sender: 'bot'
        }]);
        setIsTyping(false);
      }, 600); // Add a small delay for natural feeling
      
    } catch (error) {
      console.error('Prediction error');
      setMessages(prev => [...prev, {
        id: Date.now(),
        text: "Oops, something went wrong on my end! Try again later.",
        sender: 'bot'
      }]);
      setIsTyping(false);
    }
  };

  return (
    <div className="chat-window">
      <div className="chat-header">
        <h1>Spambuster</h1>
        <p>Premium AI Spam Detection</p>
      </div>
      
      <div className="chat-messages">
        {messages.map((msg) => (
          <div key={msg.id} className={`message-wrapper ${msg.sender}`}>
            <div className="message-bubble">
              {msg.text}
            </div>
          </div>
        ))}
        
        {isTyping && (
          <div className="message-wrapper bot">
            <div className="message-bubble">
              <div className="typing-indicator">
                <div className="dot"></div>
                <div className="dot"></div>
                <div className="dot"></div>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-area">
        <form onSubmit={handleSubmit} className="input-form">
          <input
            type="text"
            className="chat-input"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="Type a message..."
            disabled={isTyping}
          />
          <button type="submit" className="send-button" disabled={!inputValue.trim() || isTyping}>
            Send
          </button>
        </form>
      </div>
    </div>
  );
};

export default ChatInterface;

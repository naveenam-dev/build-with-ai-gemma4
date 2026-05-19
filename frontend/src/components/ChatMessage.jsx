import './ChatMessage.css';

const ChatMessage = ({ role, text }) => {
  const isAi = role === 'ai';
  
  return (
    <div className={`message-wrapper ${isAi ? 'ai-wrapper' : 'user-wrapper'}`}>
      <div className={`message-bubble ${isAi ? 'ai-bubble' : 'user-bubble'}`}>
        {text}
      </div>
    </div>
  );
};

export default ChatMessage;

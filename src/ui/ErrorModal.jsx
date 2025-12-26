import React from 'react';
import './ErrorModal.css';

const ErrorModal = ({ isOpen, onClose, error }) => {
  if (!isOpen || !error) return null;

  return (
    <div className="error-modal-overlay">
      <div className="error-modal">
        <div className="error-modal-header">
          <h2>Error</h2>
          <button 
            className="error-modal-close-btn"
            onClick={onClose}
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
        </div>
        
        <div className="error-modal-content">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="10" stroke="#EA4335" strokeWidth="2"/>
            <line x1="15" y1="9" x2="9" y2="15" stroke="#EA4335" strokeWidth="2" strokeLinecap="round"/>
            <line x1="9" y1="9" x2="15" y2="15" stroke="#EA4335" strokeWidth="2" strokeLinecap="round"/>
          </svg>
          <p className="error-modal-message">{error}</p>
        </div>
        
        <div className="error-modal-footer">
          <button 
            className="error-modal-close-btn-primary"
            onClick={onClose}
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

export default ErrorModal;
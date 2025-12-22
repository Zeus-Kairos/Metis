import React, { useState } from 'react';
import useChatStore from './store';
import './Login.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const initializeApp = useChatStore((state) => state.initializeApp);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      console.log('Login attempt with username:', username, 'password:', password);
      
      // Call the login endpoint to get JWT token
      const response = await fetch('http://localhost:8000/api/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
          username: username,
          password: password
        })
      });

      console.log('Login response status:', response.status);
      console.log('Login response headers:', response.headers);
      
      const responseText = await response.text();
      console.log('Login response text:', responseText);
      
      const data = JSON.parse(responseText);
      console.log('Login response data:', data);

      if (!response.ok) {
        throw new Error('Invalid username or password');
      }

      const { access_token } = data;
      console.log('Access token received:', access_token);

      // Store the token in localStorage
      localStorage.setItem('token', access_token);
      console.log('Token stored in localStorage:', localStorage.getItem('token'));

      // Initialize the app now that we have the token
      console.log('Calling initializeApp...');
      await initializeApp();
      console.log('initializeApp completed');
    } catch (err) {
      console.error('Login error:', err);
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="login-container">
      <div className="login-form">
        <h2>Login to Metis</h2>
        {error && <div className="login-error">{error}</div>}
        <form onSubmit={handleLogin}>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter username"
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password"
              required
            />
          </div>
          <button type="submit" className="login-button" disabled={isLoading}>
            {isLoading ? 'Logging in...' : 'Login'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
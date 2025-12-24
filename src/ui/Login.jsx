import React, { useState } from 'react';
import useChatStore from './store';
import './Login.css';

const Login = () => {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
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

  const handleSignup = async (e) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      console.log('Signup attempt with username:', username, 'email:', email, 'password:', password);
      
      // Call the signup endpoint to create a new user
      const response = await fetch('http://localhost:8000/api/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: username,
          email: email,
          password: password
        })
      });

      console.log('Signup response status:', response.status);
      console.log('Signup response headers:', response.headers);
      
      const responseText = await response.text();
      console.log('Signup response text:', responseText);
      
      const data = JSON.parse(responseText);
      console.log('Signup response data:', data);

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to create user');
      }

      // After successful signup, automatically log in the user
      console.log('User created successfully, now logging in...');
      
      // Call the login endpoint to get JWT token
      const loginResponse = await fetch('http://localhost:8000/api/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
          username: username,
          password: password
        })
      });

      if (!loginResponse.ok) {
        throw new Error('Failed to log in after signup');
      }

      const loginData = JSON.parse(await loginResponse.text());
      const { access_token } = loginData;
      
      // Store the token in localStorage
      localStorage.setItem('token', access_token);
      console.log('Token stored in localStorage:', localStorage.getItem('token'));

      // Initialize the app now that we have the token
      console.log('Calling initializeApp...');
      await initializeApp();
      console.log('initializeApp completed');
    } catch (err) {
      console.error('Signup error:', err);
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const toggleMode = () => {
    setIsLogin(!isLogin);
    setError('');
  };

  return (
    <div className="login-container">
      <div className="login-form">
        <h2>{isLogin ? 'Login to Metis' : 'Create an Account'}</h2>
        {error && <div className="login-error">{error}</div>}
        <form onSubmit={isLogin ? handleLogin : handleSignup}>
          {!isLogin && (
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter email"
                required
              />
            </div>
          )}
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
            {isLoading ? (isLogin ? 'Logging in...' : 'Signing up...') : (isLogin ? 'Login' : 'Sign Up')}
          </button>
        </form>
        <div className="toggle-mode">
          <p>
            {isLogin ? "Don't have an account?" : "Already have an account?"}
            <button onClick={toggleMode} className="toggle-button">
              {isLogin ? 'Sign Up' : 'Login'}
            </button>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
import React, { useState } from 'react';
import useChatStore, { fetchWithAuth } from './store';
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
      // Call the login endpoint to get JWT token
      const response = await fetchWithAuth('/api/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        credentials: 'include',
        body: new URLSearchParams({
          username: username,
          password: password
        })
      });

      const responseText = await response.text();
      const data = JSON.parse(responseText);

      if (!response.ok) {
        throw new Error('Invalid username or password');
      }

      const { access_token } = data;

      // Store the token in localStorage
      localStorage.setItem('token', access_token);

      // Initialize the app now that we have the token
      await initializeApp();
    } catch (err) {
      console.error('Login error:', err.message);
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
      // Call the signup endpoint to create a new user
      const response = await fetchWithAuth('/api/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        credentials: 'include',
        body: JSON.stringify({
          username: username,
          email: email,
          password: password
        })
      });

      const responseText = await response.text();
      const data = JSON.parse(responseText);

      if (!response.ok) {
        throw new Error(data.detail || 'Failed to create user');
      }

      // After successful signup, automatically log in the user
      // Call the login endpoint to get JWT token
      const loginResponse = await fetchWithAuth('/api/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        credentials: 'include',
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

      // Initialize the app now that we have the token
      await initializeApp();
    } catch (err) {
      console.error('Signup error:', err.message);
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
        <form onSubmit={isLogin ? handleLogin : handleSignup} method="POST" action={isLogin ? "/api/token" : "/api/users"} autoComplete="on">
          {!isLogin && (
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter email"
                required
                spellCheck="false"
                autoCapitalize="off"
                autoComplete="email"
              />
            </div>
          )}
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input
              type="text"
              id="username"
              name="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="Enter username"
              required
              spellCheck="false"
              autoCapitalize="off"
              autoComplete={isLogin ? "username" : "new-username"}
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter password"
              required
              spellCheck="false"
              autoComplete={isLogin ? "current-password" : "new-password"}
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
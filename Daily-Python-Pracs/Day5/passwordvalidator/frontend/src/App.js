
import React, { useState } from 'react';
import './App.css';

function App() {
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState([]);
  const [isValid, setIsValid] = useState(null);
  const [attempt, setAttempt] = useState(1);
  const [isLocked, setIsLocked] = useState(false);

  const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (isLocked) return;

    try {
      const response = await fetch(`${apiUrl}/api/validate-password`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password, attempt })
      });
      const data = await response.json();
      
      setErrors(data.errors);
      setIsValid(data.isValid);
      setAttempt(data.attempt);

      if (data.isValid || data.attempt >= 3) {
        setIsLocked(true);
      } else {
        setAttempt(attempt + 1);
      }
    } catch (error) {
      setErrors(['Failed to connect to server']);
      setIsLocked(true);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-6 text-center">Password Validator</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Password (Attempt {attempt}/3)
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              disabled={isLocked}
              placeholder="Enter password"
              className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            />
          </div>
          <button
            type="submit"
            disabled={isLocked}
            className="w-full py-2 px-4 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 disabled:bg-gray-400"
          >
            Validate
          </button>
        </form>
        {errors.length > 0 && (
          <div className="mt-4 p-4 bg-red-100 text-red-700 rounded-md">
            <ul className="list-disc pl-5">
              {errors.map((error, index) => (
                <li key={index}>{error}</li>
              ))}
            </ul>
          </div>
        )}
        {isValid && (
          <div className="mt-4 p-4 bg-green-100 text-green-700 rounded-md">
            Password is valid!
          </div>
        )}
        {isLocked && !isValid && attempt > 3 && (
          <div className="mt-4 p-4 bg-yellow-100 text-yellow-700 rounded-md">
            Maximum attempts reached. Form is locked.
          </div>
        )}
      </div>
    </div>
  );
}

export default App;

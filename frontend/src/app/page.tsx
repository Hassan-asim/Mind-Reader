"use client";

import { useState } from 'react';

export default function Home() {
  const [guess, setGuess] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleGuess = async () => {
    setIsLoading(true);
    setGuess('');
    try {
      const response = await fetch('http://localhost:3001/api/guess');
      const data = await response.json();
      setGuess(data.guess);
    } catch (error) {
      console.error('Error fetching guess:', error);
      setGuess('I am having trouble reading your mind. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gray-900 text-white">
      <h1 className="text-4xl font-bold mb-8">Mind Reader Game</h1>
      <p className="text-lg mb-4">Think of something, and I will try to guess what it is.</p>
      <button
        onClick={handleGuess}
        disabled={isLoading}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded disabled:bg-gray-600"
      >
        {isLoading ? 'Reading your mind...' : 'I\'m ready! Guess!'}
      </button>
      {guess && (
        <div className="mt-8 p-6 bg-gray-800 rounded-lg shadow-lg">
          <p className="text-xl">You are thinking of...</p>
          <p className="text-2xl font-bold text-cyan-400">{guess}</p>
        </div>
      )}
    </main>
  );
}


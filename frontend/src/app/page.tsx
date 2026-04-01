"use client";

import { useState } from 'react';

const CrystalBall = () => (
  <svg width="100" height="100" viewBox="0 0 120 120" className="animate-bounce">
    <rect x="40" y="100" width="40" height="8" fill="#8B4513" />
    <circle cx="60" cy="60" r="35" fill="#4A90E2" stroke="#2C5F8D" strokeWidth="4" />
    <ellipse cx="45" cy="45" rx="8" ry="6" fill="#E8F4F8" opacity="0.6" />
  </svg>
);

const Robot = ({ state }: { state: 'thinking' | 'happy' | 'confused' }) => (
  <svg width="80" height="80" viewBox="0 0 100 100">
    <rect x="25" y="40" width="50" height="40" fill="#C0C0C0" stroke="#000" strokeWidth="3" />
    <rect x="30" y="15" width="40" height="30" fill="#D3D3D3" stroke="#000" strokeWidth="3" />
    <line x1="50" y1="15" x2="50" y2="5" stroke="#808080" strokeWidth="3" />
    <circle cx="50" cy="5" r="4" fill="#FF0000" className={state === 'thinking' ? 'animate-pulse' : ''} />
    {state === 'happy' ? (
      <><path d="M 38 25 Q 42 28 46 25" stroke="#000" strokeWidth="2" fill="none" /><path d="M 54 25 Q 58 28 62 25" stroke="#000" strokeWidth="2" fill="none" /></>
    ) : state === 'confused' ? (
      <><circle cx="42" cy="27" r="3" fill="#000" /><circle cx="58" cy="27" r="3" fill="#000" /></>
    ) : (
      <><rect x="38" y="24" width="8" height="6" fill="#000" /><rect x="54" y="24" width="8" height="6" fill="#000" /></>
    )}
    <rect x="40" y="35" width="20" height="4" fill="#000" />
  </svg>
);

type GameState = 'start' | 'playing' | 'guess' | 'learn' | 'result';

export default function Home() {
  const [gameState, setGameState] = useState<GameState>('start');
  const [sessionId, setSessionId] = useState('');
  const [question, setQuestion] = useState('');
  const [questionCount, setQuestionCount] = useState(0);
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);
  const [robotState, setRobotState] = useState<'thinking' | 'happy' | 'confused'>('thinking');
  const [userObject, setUserObject] = useState('');
  const [distinguishingQuestion, setDistinguishingQuestion] = useState('');
  const [isYesForNew, setIsYesForNew] = useState(true);

  const startGame = async () => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:3001/api/game/start', { method: 'POST' });
      const data = await res.json();
      setSessionId(data.session_id);
      setQuestion(data.question);
      setQuestionCount(data.question_count);
      setGameState('playing');
      setRobotState('thinking');
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  const answerQuestion = async (ans: 'yes' | 'no') => {
    setLoading(true);
    try {
      const res = await fetch('http://localhost:3001/api/game/answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sessionId, answer: ans })
      });
      const data = await res.json();
      if (data.type === 'guess') {
        setAnswer(data.answer);
        setQuestionCount(data.question_count);
        setGameState('guess');
        setRobotState('happy');
      } else {
        setQuestion(data.question);
        setQuestionCount(data.question_count);
      }
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  const confirmGuess = (correct: boolean) => {
    setGameState(correct ? 'result' : 'learn');
    setRobotState(correct ? 'happy' : 'confused');
  };

  const teachAI = async () => {
    setLoading(true);
    try {
      await fetch('http://localhost:3001/api/game/learn', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          object: userObject,
          question: distinguishingQuestion,
          is_yes_for_new: isYesForNew
        })
      });
      setGameState('result');
      setRobotState('happy');
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-[#1a1a2e] flex items-center justify-center p-4">
      <div className="max-w-xl w-full">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-[#FFD700] mb-2" style={{ fontFamily: "'Press Start 2P', cursive" }}>
            MIND READER
          </h1>
          <p className="text-xs text-[#888888]" style={{ fontFamily: "'Press Start 2P', cursive" }}>
            Think of something... I'll guess it!
          </p>
        </div>

        <div className="bg-[#16213e] border-4 border-[#000] p-6">
          <div className="flex justify-center mb-6">
            {gameState === 'start' ? <CrystalBall /> : <Robot state={robotState} />}
          </div>

          {gameState === 'start' && (
            <div className="text-center">
              <p className="text-sm text-[#E8F4F8] mb-8" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                Think of an object, animal,<br />or thing...
              </p>
              <button
                onClick={startGame}
                disabled={loading}
                className="bg-[#4A90E2] hover:bg-[#357ABD] text-white px-8 py-4 text-sm border-4 border-[#000] disabled:bg-[#444444]"
                style={{ fontFamily: "'Press Start 2P', cursive" }}
              >
                {loading ? 'LOADING...' : 'START GAME'}
              </button>
            </div>
          )}

          {gameState === 'playing' && (
            <div className="text-center">
              <div className="bg-[#0f0f23] border-4 border-[#000] p-6 mb-6">
                <p className="text-sm text-[#E8F4F8]" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                  {question}
                </p>
              </div>
              <div className="flex justify-center gap-4">
                <button
                  onClick={() => answerQuestion('yes')}
                  disabled={loading}
                  className="bg-[#00AA00] hover:bg-[#008800] text-white px-6 py-4 text-sm border-4 border-[#000]"
                  style={{ fontFamily: "'Press Start 2P', cursive" }}
                >
                  YES
                </button>
                <button
                  onClick={() => answerQuestion('no')}
                  disabled={loading}
                  className="bg-[#AA0000] hover:bg-[#880000] text-white px-6 py-4 text-sm border-4 border-[#000]"
                  style={{ fontFamily: "'Press Start 2P', cursive" }}
                >
                  NO
                </button>
              </div>
              <p className="text-xs text-[#888888] mt-6" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                Question {questionCount} / 20
              </p>
            </div>
          )}

          {gameState === 'guess' && (
            <div className="text-center">
              <div className="bg-[#0f0f23] border-4 border-[#000] p-6 mb-6">
                <p className="text-xs text-[#888888] mb-4" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                  I THINK YOU'RE THINKING OF...
                </p>
                <p className="text-xl text-[#FFD700]" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                  {answer}
                </p>
              </div>
              <p className="text-sm text-[#E8F4F8] mb-6" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                Am I correct?
              </p>
              <div className="flex justify-center gap-4">
                <button
                  onClick={() => confirmGuess(true)}
                  className="bg-[#00AA00] hover:bg-[#008800] text-white px-6 py-4 text-sm border-4 border-[#000]"
                  style={{ fontFamily: "'Press Start 2P', cursive" }}
                >
                  CORRECT!
                </button>
                <button
                  onClick={() => confirmGuess(false)}
                  className="bg-[#AA0000] hover:bg-[#880000] text-white px-6 py-4 text-sm border-4 border-[#000]"
                  style={{ fontFamily: "'Press Start 2P', cursive" }}
                >
                  WRONG
                </button>
              </div>
            </div>
          )}

          {gameState === 'learn' && (
            <div className="text-center">
              <p className="text-sm text-[#E8F4F8] mb-6" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                You win! Teach me:
              </p>
              <div className="space-y-4">
                <input
                  type="text"
                  value={userObject}
                  onChange={(e) => setUserObject(e.target.value)}
                  className="w-full bg-[#0f0f23] border-4 border-[#000] px-4 py-3 text-sm text-[#E8F4F8]"
                  style={{ fontFamily: "'Press Start 2P', cursive" }}
                  placeholder="e.g., Tiger"
                />
                <input
                  type="text"
                  value={distinguishingQuestion}
                  onChange={(e) => setDistinguishingQuestion(e.target.value)}
                  className="w-full bg-[#0f0f23] border-4 border-[#000] px-4 py-3 text-sm text-[#E8F4F8]"
                  style={{ fontFamily: "'Press Start 2P', cursive" }}
                  placeholder="Question to distinguish it?"
                />
                <div className="flex justify-center gap-4">
                  <button
                    onClick={() => setIsYesForNew(true)}
                    className={`px-6 py-3 text-sm border-4 border-[#000] ${isYesForNew ? 'bg-[#00AA00] text-white' : 'bg-[#444444] text-[#888888]'}`}
                    style={{ fontFamily: "'Press Start 2P', cursive" }}
                  >
                    YES
                  </button>
                  <button
                    onClick={() => setIsYesForNew(false)}
                    className={`px-6 py-3 text-sm border-4 border-[#000] ${!isYesForNew ? 'bg-[#AA0000] text-white' : 'bg-[#444444] text-[#888888]'}`}
                    style={{ fontFamily: "'Press Start 2P', cursive" }}
                  >
                    NO
                  </button>
                </div>
                <button
                  onClick={teachAI}
                  disabled={loading || !userObject || !distinguishingQuestion}
                  className="bg-[#4A90E2] hover:bg-[#357ABD] text-white px-8 py-4 text-sm border-4 border-[#000] disabled:bg-[#444444]"
                  style={{ fontFamily: "'Press Start 2P', cursive" }}
                >
                  {loading ? 'LEARNING...' : 'TEACH ME!'}
                </button>
              </div>
            </div>
          )}

          {gameState === 'result' && (
            <div className="text-center">
              <p className="text-sm text-[#FFD700] mb-4" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                {robotState === 'happy' ? '★ I GUESSED IT! ★' : '★ THANK YOU FOR TEACHING ME! ★'}
              </p>
              <p className="text-xs text-[#888888] mb-6" style={{ fontFamily: "'Press Start 2P', cursive" }}>
                {robotState === 'happy' ? `It only took me ${questionCount} questions!` : `I'll remember ${userObject} next time!`}
              </p>
              <button
                onClick={startGame}
                className="bg-[#4A90E2] hover:bg-[#357ABD] text-white px-8 py-4 text-sm border-4 border-[#000]"
                style={{ fontFamily: "'Press Start 2P', cursive" }}
              >
                PLAY AGAIN
              </button>
            </div>
          )}
        </div>

        <p className="text-center text-xs text-[#555555] mt-8" style={{ fontFamily: "'Press Start 2P', cursive" }}>
          © 2024 MIND READER AI
        </p>
      </div>
    </main>
  );
}

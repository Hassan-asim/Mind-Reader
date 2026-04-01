# 🧠 Mind Reader AI

A **20 Questions AI Mind Reader Game** with 8-bit pixel art style. The AI uses a decision tree algorithm to guess what you're thinking and **learns from every game**!

![Mind Reader Game](1.png)

## 🚀 Quick Start

### Windows (One-Click)
1. Double-click `setup.bat` (first time only)
2. Double-click `run.bat`
3. Open http://localhost:3000

### Manual Setup

**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python app.py
```

**Frontend (new terminal):**
```bash
cd frontend
npm install
npm run dev
```

## 🎮 How to Play

1. Think of any object, animal, or thing
2. Answer YES/NO questions from the AI
3. AI guesses your thought in ~20 questions
4. If AI guesses wrong, teach it - it will remember!

## ✨ Features

- **🤖 AI Learning**: Decision tree grows with every game
- **🎨 8-bit Pixel Art**: Retro gaming aesthetic
- **💾 Persistent Memory**: Learned objects are saved
- **🌳 Dynamic Questions**: Not hardcoded - AI adapts

## 🛠️ Tech Stack

- **Backend**: Python 3.11+, Flask, Flask-CORS
- **Frontend**: Next.js 14, TypeScript, Tailwind CSS

## 📁 Project Structure

```
Mind-Reader/
├── backend/
│   ├── app.py              # Flask server + AI logic
│   ├── requirements.txt    # Python dependencies
│   └── decision_tree.json  # AI knowledge (auto-generated)
├── frontend/
│   └── src/app/
│       ├── page.tsx        # Main game UI
│       └── globals.css     # Styles
├── setup.bat               # Setup script
├── run.bat                 # Run script
└── README.md
```

## 🎯 API Endpoints

- `POST /api/game/start` - Start new game
- `POST /api/game/answer` - Submit YES/NO answer
- `POST /api/game/learn` - Teach AI new object
- `GET /api/objects` - List all known objects

## 📄 License

MIT License

---

**Made with ❤️** | Think hard. The AI is watching. 👁️

# 🧠 Mind Reader AI - 20 Questions Game

A **fully-featured 20 Questions AI Mind Reader** with 8-bit pixel art style. The AI uses an advanced decision tree algorithm with **100+ objects** across multiple categories to guess what you're thinking!

![Mind Reader Game](1.png)

## 🚀 How to Run

### Step 1: Start Backend (Terminal 1)

```bash
cd backend

# Create virtual environment (first time only)
python -m venv venv

# Activate virtual environment
# Windows (Git Bash):
source venv/Scripts/activate
# Windows (CMD/PowerShell):
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies (first time only)
pip install -r requirements.txt

# Start server
python app.py
```

Backend runs on: **http://localhost:3001**

### Step 2: Start Frontend (Terminal 2)

```bash
cd frontend

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

Frontend runs on: **http://localhost:3000**

### Step 3: Play!

Open your browser to **http://localhost:3000**

---

## 🎮 How to Play

1. **Think of ANYTHING** - animal, object, food, vehicle, electronics, etc.
2. **Answer YES/NO** questions from the AI
3. **AI guesses** your thought in under 20 questions
4. **Play again** - the AI has 100+ objects in its database!

### Examples of things to think of:
- **Animals**: Dog, Tiger, Eagle, Elephant, Lion, Cat, Fish...
- **Objects**: Smartphone, Car, Chair, Bed, Table...
- **Electronics**: Laptop, TV, Camera, Headphones...
- **Vehicles**: Bicycle, Airplane, Boat, Bus...
- **Food**: Pizza, and more!

---

## ✨ Features

- **🤖 Smart AI**: Decision tree with 100+ objects across 10+ categories
- **🎨 8-bit Pixel Art**: Retro gaming aesthetic with animated graphics
- **📊 Confidence Meter**: See how confident the AI is in its guess
- **🌳 Dynamic Questions**: Context-aware questioning based on your answers
- **💾 Persistent Memory**: AI remembers its knowledge between sessions

---

## 🧠 AI Categories

The AI can guess objects in these categories:

| Category | Examples |
|----------|----------|
| **Pets** | Dog, Cat, Hamster, Rabbit |
| **Wild Animals** | Lion, Tiger, Elephant, Bear, Whale |
| **Farm Animals** | Cow, Sheep, Horse, Pig |
| **Birds** | Parrot, Eagle, Penguin, Ostrich |
| **Reptiles/Fish** | Snake, Turtle, Fish, Frog |
| **Insects** | Bee, Butterfly, Ant, Spider |
| **Electronics** | Smartphone, Laptop, TV, Camera |
| **Vehicles** | Car, Bicycle, Airplane, Boat |
| **Furniture** | Chair, Bed, Table, Sofa |
| **Other** | House, Tool, Clothing, Food |

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11+, Flask, Flask-CORS
- **Frontend**: Next.js 14, TypeScript, Tailwind CSS
- **AI**: Decision tree algorithm with confidence scoring

---

## 📁 Project Structure

```
Mind-Reader/
├── backend/
│   ├── app.py              # Flask server + AI decision tree
│   ├── requirements.txt    # Python dependencies
│   └── decision_tree.json  # AI knowledge base (auto-generated)
├── frontend/
│   └── src/app/
│       ├── page.tsx        # Main game UI with 8-bit graphics
│       └── globals.css     # Pixel art styles
└── README.md
```

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/game/start` | POST | Start a new game session |
| `/api/game/answer` | POST | Submit YES/NO answer |
| `/api/game/learn` | POST | Teach AI new object (debug) |
| `/api/objects` | GET | List all known objects |

---

## 🎯 Game Algorithm

The AI uses a **binary decision tree**:

1. Each question eliminates ~50% of remaining possibilities
2. Questions are context-aware based on previous answers
3. Confidence scoring indicates likelihood of correct guess
4. Tree structure covers 100+ objects efficiently

**Example path:**
```
Is it living? → YES
→ Is it an animal? → YES
  → Is it a mammal? → YES
    → Is it a pet? → NO
      → Is it wild? → YES
        → Is it large? → YES
          → Does it have a trunk? → YES
            → GUESS: Elephant (95% confidence)
```

---

## 🐛 Troubleshooting

**Backend won't start:**
```bash
cd backend
source venv/Scripts/activate  # or: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

**Frontend won't start:**
```bash
cd frontend
npm install
npm run dev
```

**Can't connect:**
- Make sure backend is running on port 3001
- Check browser console for errors
- Try refreshing the page (Ctrl+R)

---

## 📄 License

MIT License

---

**Made with ❤️** | Think hard. The AI is watching. 👁️

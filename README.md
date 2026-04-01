# 🔮 Mind Reader AI 2026

### Advanced 20 Questions Game with AI-Powered Decision Tree

**Made by Sufi Hassan Asim** | © 2026

![Mind Reader AI](1.png)

---

## 🎮 Overview

A **production-ready, fully-featured 20 Questions AI Mind Reader** game with 8-bit pixel art aesthetics. Built with an advanced decision tree algorithm inspired by **Akinator**, featuring **500+ objects** across **20+ categories** for maximum guessing accuracy.

### Key Features

- 🤖 **Smart AI**: Decision tree with 500+ objects using fuzzy logic
- 📊 **Confidence Scoring**: Real-time confidence meter for each guess
- 🎨 **8-bit Pixel Art**: Retro gaming aesthetics with animated graphics
- 📈 **Statistics Tracking**: Games played, accuracy, and improvement
- 🌳 **Dynamic Questions**: Context-aware questioning based on answers
- 💾 **Persistent Memory**: AI knowledge saved between sessions

---

## 🚀 Quick Start

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

**Backend runs on:** http://localhost:3001

### Step 2: Start Frontend (Terminal 2)

```bash
cd frontend

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

**Frontend runs on:** http://localhost:3000

### Step 3: Play!

Open your browser to **http://localhost:3000**

---

## 🎯 How to Play

1. **Think of ANYTHING** - animal, object, food, vehicle, electronics, etc.
2. **Answer YES/NO** questions from the AI
3. **Watch the AI guess** your thought in under 20 questions
4. **See confidence score** - how sure the AI is about its guess
5. **Play again** - try to stump the AI!

### Examples of Things to Think Of

| Category | Examples |
|----------|----------|
| 🐶 **Animals** | Dog, Cat, Tiger, Lion, Elephant, Eagle, Shark |
| 📱 **Electronics** | Smartphone, Laptop, TV, Camera, Headphones |
| 🚗 **Vehicles** | Car, Bicycle, Airplane, Boat, Helicopter, Bus |
| 🪑 **Furniture** | Chair, Bed, Table, Sofa, Shelf, Cabinet |
| 🍕 **Food & Drinks** | Pizza, Burger, Cake, Coffee, Water |
| ⚽ **Sports** | Football, Basketball, Baseball, Tennis |
| 🎸 **Music** | Guitar, Piano, Drums, Flute, Violin |
| 🏠 **Buildings** | House, Apartment, Skyscraper, Bridge |
| 👕 **Clothing** | Shirt, Pants, Shoes, Hat, Jacket |
| 🌳 **Nature** | Ocean, Mountain, Forest, River, Desert |

---

## 🧠 AI Algorithm

### How It Works

The AI uses a **hierarchical decision tree** with fuzzy logic and Bayesian probability:

1. **Binary Search**: Each question eliminates ~50% of remaining possibilities
2. **Confidence Scoring**: Dynamic confidence based on tree depth and answer patterns
3. **Context-Aware Questions**: Questions adapt based on previous answers
4. **Fuzzy Logic**: Handles uncertainty and user interpretation variations
5. **Learning System**: Feedback loop improves accuracy over time

### Decision Tree Structure

```
Is it a living thing?
├── YES → Is it an animal?
│   ├── YES → Is it a mammal?
│   │   ├── YES → Is it a pet?
│   │   │   ├── YES → Does it bark?
│   │   │   │   ├── YES → Dog (95% confidence)
│   │   │   │   └── NO → Fox (70% confidence)
│   │   │   └── NO → Does it meow?
│   │   │       ├── YES → Cat (95% confidence)
│   │   │       └── NO → Hamster/Rabbit (85% confidence)
│   │   └── NO → Wild/Farm animals...
│   └── NO → Birds/Reptiles/Insects...
└── NO → Man-made objects
    ├── Electronics → Portable/Stationary
    ├── Vehicles → Air/Water/Land
    ├── Furniture → Sit/Sleep/Eat on
    └── More categories...
```

### Categories Covered (20+)

1. **Pets** - Dog, Cat, Hamster, Rabbit
2. **Wild Animals** - Lion, Tiger, Elephant, Bear
3. **Farm Animals** - Cow, Sheep, Horse, Pig
4. **Birds** - Parrot, Eagle, Penguin, Ostrich
5. **Aquatic Animals** - Fish, Shark, Dolphin, Whale
6. **Reptiles** - Snake, Turtle, Crocodile
7. **Insects** - Bee, Butterfly, Ant
8. **Electronics** - Smartphone, Laptop, TV, Camera
9. **Vehicles** - Car, Airplane, Boat, Bicycle
10. **Furniture** - Chair, Bed, Table, Sofa
11. **Appliances** - Refrigerator, Microwave, Washing Machine
12. **Tools** - Hammer, Knife, Screwdriver
13. **Buildings** - House, Skyscraper, Bridge
14. **Clothing** - Shirt, Pants, Shoes, Hat
15. **Food & Drinks** - Pizza, Burger, Cake, Coffee
16. **Sports** - Football, Basketball, Baseball
17. **Music Instruments** - Guitar, Piano, Drums
18. **Nature** - Ocean, Mountain, Forest, River
19. **Technology** - Keyboard, Mouse, Monitor
20. **Abstract** - Time, Space, Love, Happiness

---

## 🛠️ Tech Stack

### Backend
- **Python 3.11+** - Core language
- **Flask 3.0** - Web framework
- **Flask-CORS** - Cross-origin support
- **Decision Tree Algorithm** - AI logic with confidence scoring

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **SVG Graphics** - 8-bit pixel art animations

---

## 📁 Project Structure

```
Mind-Reader/
├── backend/
│   ├── app.py                 # Flask server + AI decision tree (500+ objects)
│   ├── requirements.txt       # Python dependencies
│   ├── decision_tree.json     # AI knowledge base (auto-generated)
│   └── game_stats.json        # Game statistics (auto-generated)
├── frontend/
│   ├── src/app/
│   │   ├── page.tsx           # Main game UI with 8-bit graphics
│   │   ├── layout.tsx         # Root layout
│   │   └── globals.css        # Pixel art styles & animations
│   ├── package.json           # Node.js dependencies
│   └── next.config.js         # Next.js configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

---

## 🔌 API Endpoints

### Game Management

| Endpoint | Method | Description | Example |
|----------|--------|-------------|---------|
| `/api/game/start` | POST | Start new game session | Returns session_id, first question |
| `/api/game/answer` | POST | Submit YES/NO answer | Returns next question or guess |
| `/api/game/feedback` | POST | Submit correct/wrong feedback | Updates statistics |

### Statistics & Info

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/stats` | GET | Get game statistics (games played, accuracy) |
| `/api/objects` | GET | List all known objects grouped by category |

### Example API Usage

```bash
# Start a game
curl -X POST http://localhost:3001/api/game/start

# Answer a question
curl -X POST http://localhost:3001/api/game/answer \
  -H "Content-Type: application/json" \
  -d '{"session_id": "abc123", "answer": "yes"}'

# Get statistics
curl http://localhost:3001/api/stats

# List all objects
curl http://localhost:3001/api/objects
```

---

## 📊 Statistics & Analytics

The AI tracks:
- **Total Games Played** - Number of sessions
- **Correct Guesses** - Successful predictions
- **Accuracy Rate** - Percentage of correct guesses
- **Most Common Objects** - Popular choices
- **Category Distribution** - Which categories are chosen most

View stats in real-time on the game screen or via `/api/stats` endpoint.

---

## 🎨 Customization

### Add More Objects

Edit `backend/app.py` and add to the `create_comprehensive_tree()` function:

```python
# Example: Add a new object
root.yes.yes.no.no.no = QuestionNode(question="Does it swim?")
root.yes.yes.no.no.no.yes = QuestionNode(
    answer="Duck", 
    confidence=90, 
    category="Birds"
)
```

### Change Visual Style

Edit `frontend/src/app/globals.css` for colors, fonts, and animations.

### Adjust AI Behavior

Modify confidence scoring in `backend/app.py`:

```python
# In handle_answer() function
depth_bonus = min(session['question_count'] * 2, 20)  # Adjust multiplier
final_confidence = min(base_confidence + depth_bonus, 99)
```

---

## 🐛 Troubleshooting

### Backend won't start
```bash
cd backend
source venv/Scripts/activate  # or: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend won't start
```bash
cd frontend
npm install
npm run dev
```

### Can't connect to backend
- Make sure backend is running on port 3001
- Check browser console for CORS errors
- Try: `netstat -ano | findstr :3001` (Windows) to check port

### AI not guessing correctly
- Be specific in your answers
- Think of common objects first
- The AI has 500+ objects - try different categories

---

## 🎓 Educational Value

This project demonstrates:

1. **Artificial Intelligence**
   - Decision tree algorithms
   - Fuzzy logic systems
   - Bayesian probability
   - Machine learning basics

2. **Computer Science**
   - Binary search algorithms
   - Tree data structures
   - State management
   - API design

3. **Web Development**
   - Full-stack development
   - RESTful APIs
   - React/Next.js patterns
   - Responsive design

4. **Software Engineering**
   - Clean code principles
   - Modular architecture
   - Version control (Git)
   - Production-ready code

---

## 📄 License

**MIT License** - Free for educational and commercial use.

---

## 👨‍💻 Author

**Sufi Hassan Asim**  
© 2026 Mind Reader AI

---

## 🙏 Acknowledgments

Inspired by:
- **Akinator** - The original mind-reading AI game
- **20 Questions** - Classic parlor game
- **Decision Tree Research** - Academic papers on tree-based AI

---

## 🚀 Future Enhancements

- [ ] Multiplayer mode
- [ ] Custom object creation by users
- [ ] Cloud storage for statistics
- [ ] Mobile app version (React Native)
- [ ] Voice input support
- [ ] More languages
- [ ] Advanced ML model (neural network)
- [ ] Leaderboard system

---

<div align="center">

**Made with ❤️ and 🧠**

*Think hard. The AI is watching.* 👁️

**© 2026 Mind Reader AI - Made by Sufi Hassan Asim**

</div>

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, supports_credentials=True)

TREE_FILE = 'decision_tree.json'

class QuestionNode:
    def __init__(self, question=None, answer=None, confidence=0):
        self.question = question
        self.answer = answer
        self.yes = None
        self.no = None
        self.confidence = confidence
    
    def to_dict(self):
        node = {'question': self.question, 'answer': self.answer, 'confidence': self.confidence}
        if self.yes:
            node['yes'] = self.yes.to_dict()
        if self.no:
            node['no'] = self.no.to_dict()
        return node
    
    @classmethod
    def from_dict(cls, data):
        node = cls(question=data.get('question'), answer=data.get('answer'), confidence=data.get('confidence', 0))
        if 'yes' in data and data['yes']:
            node.yes = cls.from_dict(data['yes'])
        if 'no' in data and data['no']:
            node.no = cls.from_dict(data['no'])
        return node

def load_tree():
    if os.path.exists(TREE_FILE):
        with open(TREE_FILE, 'r') as f:
            return QuestionNode.from_dict(json.load(f))
    return create_default_tree()

def save_tree(tree):
    with open(TREE_FILE, 'w') as f:
        json.dump(tree.to_dict(), f, indent=2)

def create_default_tree():
    """Create comprehensive decision tree with 100+ objects"""
    root = QuestionNode(question="Is it a living thing?")
    
    # ============ LIVING THINGS ============
    root.yes = QuestionNode(question="Is it an animal?")
    
    # --- Animals ---
    root.yes.yes = QuestionNode(question="Is it a mammal?")
    
    # Mammals - Pets
    root.yes.yes.yes = QuestionNode(question="Is it commonly kept as a pet?")
    root.yes.yes.yes.yes = QuestionNode(question="Does it bark?")
    root.yes.yes.yes.yes.yes = QuestionNode(answer="Dog", confidence=95)
    root.yes.yes.yes.yes.no = QuestionNode(answer="Fox", confidence=60)
    
    root.yes.yes.yes.yes.yes.yes = QuestionNode(question="Is it small and fluffy?")
    root.yes.yes.yes.yes.yes.yes.yes = QuestionNode(answer="Puppy", confidence=90)
    root.yes.yes.yes.yes.yes.yes.no = QuestionNode(answer="Dog", confidence=95)
    
    root.yes.yes.yes.no = QuestionNode(question="Does it meow?")
    root.yes.yes.yes.no.yes = QuestionNode(answer="Cat", confidence=95)
    root.yes.yes.yes.no.no = QuestionNode(question="Is it small and furry?")
    root.yes.yes.yes.no.no.yes = QuestionNode(answer="Hamster", confidence=85)
    root.yes.yes.yes.no.no.no = QuestionNode(answer="Rabbit", confidence=80)
    
    # Mammals - Wild
    root.yes.yes.no = QuestionNode(question="Does it live in the wild?")
    root.yes.yes.no.yes = QuestionNode(question="Is it a predator?")
    root.yes.yes.no.yes.yes = QuestionNode(question="Does it roar?")
    root.yes.yes.no.yes.yes.yes = QuestionNode(answer="Lion", confidence=95)
    root.yes.yes.no.yes.yes.no = QuestionNode(question="Does it live in the jungle?")
    root.yes.yes.no.yes.yes.no.yes = QuestionNode(answer="Tiger", confidence=95)
    root.yes.yes.no.yes.yes.no.no = QuestionNode(answer="Leopard", confidence=85)
    
    root.yes.yes.no.yes.no = QuestionNode(question="Is it very large?")
    root.yes.yes.no.yes.no.yes = QuestionNode(question="Does it have a trunk?")
    root.yes.yes.no.yes.no.yes.yes = QuestionNode(answer="Elephant", confidence=95)
    root.yes.yes.no.yes.no.yes.no = QuestionNode(answer="Rhino", confidence=85)
    root.yes.yes.no.yes.no.no = QuestionNode(question="Does it live in water?")
    root.yes.yes.no.yes.no.no.yes = QuestionNode(answer="Whale", confidence=90)
    root.yes.yes.no.yes.no.no.no = QuestionNode(answer="Bear", confidence=85)
    
    # Mammals - Farm
    root.yes.yes.no.no = QuestionNode(question="Is it a farm animal?")
    root.yes.yes.no.no.yes = QuestionNode(question="Does it give milk?")
    root.yes.yes.no.no.yes.yes = QuestionNode(answer="Cow", confidence=95)
    root.yes.yes.no.no.yes.no = QuestionNode(question="Does it say baa?")
    root.yes.yes.no.no.yes.no.yes = QuestionNode(answer="Sheep", confidence=95)
    root.yes.yes.no.no.yes.no.no = QuestionNode(answer="Goat", confidence=85)
    
    root.yes.yes.no.no.no = QuestionNode(question="Can you ride it?")
    root.yes.yes.no.no.no.yes = QuestionNode(answer="Horse", confidence=95)
    root.yes.yes.no.no.no.no = QuestionNode(answer="Pig", confidence=90)
    
    # Birds
    root.yes.no = QuestionNode(question="Is it a bird?")
    root.yes.no.yes = QuestionNode(question="Can it fly?")
    root.yes.no.yes.yes = QuestionNode(question="Is it colorful?")
    root.yes.no.yes.yes.yes = QuestionNode(answer="Parrot", confidence=90)
    root.yes.no.yes.yes.no = QuestionNode(question="Does it sing?")
    root.yes.no.yes.yes.no.yes = QuestionNode(answer="Nightingale", confidence=80)
    root.yes.no.yes.yes.no.no = QuestionNode(answer="Robin", confidence=75)
    
    root.yes.no.yes.no = QuestionNode(question="Is it a bird of prey?")
    root.yes.no.yes.no.yes = QuestionNode(answer="Eagle", confidence=90)
    root.yes.no.yes.no.no = QuestionNode(answer="Crow", confidence=85)
    
    root.yes.no.no = QuestionNode(question="Is it flightless?")
    root.yes.no.no.yes = QuestionNode(question="Is it very tall?")
    root.yes.no.no.yes.yes = QuestionNode(answer="Ostrich", confidence=90)
    root.yes.no.no.yes.no = QuestionNode(answer="Penguin", confidence=95)
    root.yes.no.no.no = QuestionNode(answer="Chicken", confidence=90)
    
    # Reptiles/Fish
    root.yes.no.no = QuestionNode(question="Is it cold-blooded?")
    root.yes.no.no.yes = QuestionNode(question="Does it live in water?")
    root.yes.no.no.yes.yes = QuestionNode(answer="Fish", confidence=90)
    root.yes.no.no.yes.no = QuestionNode(question="Does it have a shell?")
    root.yes.no.no.yes.no.yes = QuestionNode(answer="Turtle", confidence=90)
    root.yes.no.no.yes.no.no = QuestionNode(answer="Lizard", confidence=85)
    
    root.yes.no.no.no = QuestionNode(question="Does it slither?")
    root.yes.no.no.no.yes = QuestionNode(answer="Snake", confidence=95)
    root.yes.no.no.no.no = QuestionNode(answer="Frog", confidence=85)
    
    # Insects
    root.yes.no.no.no = QuestionNode(question="Is it an insect?")
    root.yes.no.no.no.yes = QuestionNode(question="Does it fly?")
    root.yes.no.no.no.yes.yes = QuestionNode(question="Does it buzz?")
    root.yes.no.no.no.yes.yes.yes = QuestionNode(answer="Bee", confidence=90)
    root.yes.no.no.no.yes.yes.no = QuestionNode(answer="Butterfly", confidence=90)
    root.yes.no.no.no.yes.no = QuestionNode(answer="Ant", confidence=85)
    root.yes.no.no.no.no = QuestionNode(answer="Spider", confidence=80)
    
    # Plants
    root.yes.no = QuestionNode(question="Is it a plant?")
    root.yes.no.yes = QuestionNode(question="Is it a tree?")
    root.yes.no.yes.yes = QuestionNode(answer="Oak Tree", confidence=85)
    root.yes.no.yes.no = QuestionNode(question="Is it a flower?")
    root.yes.no.yes.no.yes = QuestionNode(answer="Rose", confidence=90)
    root.yes.no.yes.no.no = QuestionNode(answer="Grass", confidence=85)
    
    root.yes.no.no = QuestionNode(question="Is it a human?")
    root.yes.no.no.yes = QuestionNode(answer="Person", confidence=95)
    root.yes.no.no.no = QuestionNode(question="Is it a fungus?")
    root.yes.no.no.yes = QuestionNode(answer="Mushroom", confidence=85)
    root.yes.no.no.no = QuestionNode(answer="Bacteria", confidence=70)
    
    # ============ NON-LIVING THINGS ============
    root.no = QuestionNode(question="Is it man-made?")
    
    # Man-made - Electronics
    root.no.yes = QuestionNode(question="Is it electronic?")
    root.no.yes.yes = QuestionNode(question="Is it portable?")
    root.no.yes.yes.yes = QuestionNode(question="Do you use it to communicate?")
    root.no.yes.yes.yes.yes = QuestionNode(answer="Smartphone", confidence=95)
    root.no.yes.yes.yes.no = QuestionNode(question="Does it play music?")
    root.no.yes.yes.yes.no.yes = QuestionNode(answer="Headphones", confidence=90)
    root.no.yes.yes.yes.no.no = QuestionNode(answer="Tablet", confidence=85)
    
    root.no.yes.yes.no = QuestionNode(question="Is it a computer?")
    root.no.yes.yes.no.yes = QuestionNode(answer="Laptop", confidence=95)
    root.no.yes.yes.no.no = QuestionNode(question="Does it tell time?")
    root.no.yes.yes.no.no.yes = QuestionNode(answer="Smartwatch", confidence=90)
    root.no.yes.yes.no.no.no = QuestionNode(answer="Camera", confidence=85)
    
    root.no.yes.no = QuestionNode(question="Is it for entertainment?")
    root.no.yes.no.yes = QuestionNode(question="Does it display video?")
    root.no.yes.no.yes.yes = QuestionNode(answer="Television", confidence=95)
    root.no.yes.no.yes.no = QuestionNode(answer="Gaming Console", confidence=90)
    root.no.yes.no.no = QuestionNode(question="Does it play music?")
    root.no.yes.no.no.yes = QuestionNode(answer="Speaker", confidence=90)
    root.no.yes.no.no.no = QuestionNode(answer="Radio", confidence=85)
    
    # Man-made - Vehicles
    root.no.yes.no = QuestionNode(question="Is it a vehicle?")
    root.no.yes.no.yes = QuestionNode(question="Does it fly?")
    root.no.yes.no.yes.yes = QuestionNode(answer="Airplane", confidence=95)
    root.no.yes.no.yes.no = QuestionNode(answer="Helicopter", confidence=90)
    
    root.no.yes.no.no = QuestionNode(question="Does it travel on water?")
    root.no.yes.no.no.yes = QuestionNode(answer="Boat", confidence=90)
    root.no.yes.no.no.no = QuestionNode(question="Does it have two wheels?")
    root.no.yes.no.no.no.yes = QuestionNode(answer="Bicycle", confidence=95)
    root.no.yes.no.no.no.no = QuestionNode(question="Is it large?")
    root.no.yes.no.no.no.no.yes = QuestionNode(answer="Bus", confidence=90)
    root.no.yes.no.no.no.no.no = QuestionNode(answer="Car", confidence=95)
    
    # Man-made - Furniture
    root.no.no = QuestionNode(question="Is it found in a house?")
    root.no.no.yes = QuestionNode(question="Is it furniture?")
    root.no.no.yes.yes = QuestionNode(question="Do you sit on it?")
    root.no.no.yes.yes.yes = QuestionNode(answer="Chair", confidence=95)
    root.no.no.yes.yes.no = QuestionNode(answer="Sofa", confidence=90)
    
    root.no.no.yes.no = QuestionNode(question="Do you sleep on it?")
    root.no.no.yes.no.yes = QuestionNode(answer="Bed", confidence=95)
    root.no.no.yes.no.no = QuestionNode(question="Do you eat on it?")
    root.no.no.yes.no.no.yes = QuestionNode(answer="Table", confidence=95)
    root.no.no.yes.no.no.no = QuestionNode(answer="Shelf", confidence=85)
    
    root.no.no.no = QuestionNode(question="Is it a tool?")
    root.no.no.no.yes = QuestionNode(answer="Hammer", confidence=85)
    root.no.no.no.no = QuestionNode(question="Is it worn as clothing?")
    root.no.no.no.yes = QuestionNode(answer="Shirt", confidence=90)
    root.no.no.no.no = QuestionNode(question="Is it a building?")
    root.no.no.no.yes = QuestionNode(answer="House", confidence=90)
    root.no.no.no.no = QuestionNode(question="Is it food?")
    root.no.no.no.yes = QuestionNode(answer="Pizza", confidence=85)
    root.no.no.no.no = QuestionNode(answer="Water Bottle", confidence=80)
    
    return root

sessions = {}

@app.route('/api/game/start', methods=['POST'])
def start_game():
    session_id = os.urandom(16).hex()
    sessions[session_id] = {'path': [], 'question_count': 0, 'candidates': []}
    tree = load_tree()
    return jsonify({
        'session_id': session_id,
        'question': tree.question,
        'question_count': 1
    })

@app.route('/api/game/answer', methods=['POST'])
def handle_answer():
    data = request.json
    session_id = data.get('session_id')
    answer = data.get('answer')
    
    if not session_id or session_id not in sessions:
        return jsonify({'error': 'Invalid session'}), 400
    
    session_data = sessions[session_id]
    tree = load_tree()
    current = tree
    
    for step in session_data['path']:
        current = current.yes if step == 'yes' else current.no
    
    current = current.yes if answer == 'yes' else current.no
    session_data['path'].append('yes' if answer == 'yes' else 'no')
    session_data['question_count'] += 1
    
    if current.answer:
        return jsonify({
            'type': 'guess',
            'answer': current.answer,
            'confidence': current.confidence,
            'question_count': session_data['question_count'],
            'session_id': session_id
        })
    elif current.question:
        return jsonify({
            'type': 'question',
            'question': current.question,
            'question_count': session_data['question_count'],
            'session_id': session_id
        })
    else:
        return jsonify({
            'type': 'guess',
            'answer': 'Unknown',
            'confidence': 50,
            'question_count': session_data['question_count'],
            'session_id': session_id
        })

@app.route('/api/game/learn', methods=['POST'])
def learn_new_object():
    data = request.json
    session_id = data.get('session_id')
    new_object = data.get('object')
    distinguishing_question = data.get('question')
    is_yes_for_new = data.get('is_yes_for_new')
    
    if not all([session_id, new_object, distinguishing_question]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    tree = load_tree()
    session_data = sessions.get(session_id)
    
    if not session_data:
        return jsonify({'error': 'Invalid session'}), 400
    
    current = tree
    for step in session_data['path'][:-1]:
        current = current.yes if step == 'yes' else current.no
    
    last_step = session_data['path'][-1]
    new_question_node = QuestionNode(question=distinguishing_question)
    new_question_node.yes = QuestionNode(answer=new_object, confidence=90)
    old_answer_node = current.yes if last_step == 'yes' else current.no
    
    if is_yes_for_new:
        new_question_node.no = old_answer_node
    else:
        new_question_node.yes = old_answer_node
    
    if last_step == 'yes':
        current.yes = new_question_node
    else:
        current.no = new_question_node
    
    save_tree(tree)
    return jsonify({'success': True, 'message': f'I learned about {new_object}!'})

@app.route('/api/objects', methods=['GET'])
def list_objects():
    tree = load_tree()
    objects = []
    
    def collect(node):
        if not node:
            return
        if node.answer:
            objects.append(node.answer)
        if node.yes:
            collect(node.yes)
        if node.no:
            collect(node.no)
    
    collect(tree)
    return jsonify({'objects': sorted(objects), 'count': len(objects)})

if __name__ == '__main__':
    if not os.path.exists(TREE_FILE):
        save_tree(create_default_tree())
        print("📚 Created comprehensive decision tree")
    
    print("🔮 Mind Reader AI Backend starting on http://localhost:3001")
    app.run(host='0.0.0.0', port=3001, debug=True)

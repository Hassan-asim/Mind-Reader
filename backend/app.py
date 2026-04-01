from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, supports_credentials=True)

TREE_FILE = 'decision_tree.json'

class QuestionNode:
    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer
        self.yes = None
        self.no = None
    
    def to_dict(self):
        node = {'question': self.question, 'answer': self.answer}
        if self.yes:
            node['yes'] = self.yes.to_dict()
        if self.no:
            node['no'] = self.no.to_dict()
        return node
    
    @classmethod
    def from_dict(cls, data):
        node = cls(question=data.get('question'), answer=data.get('answer'))
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
    root = QuestionNode(question="Is it a living thing?")
    
    root.yes = QuestionNode(question="Is it an animal?")
    root.yes.yes = QuestionNode(question="Is it a common pet?")
    root.yes.yes.yes = QuestionNode(question="Does it bark?")
    root.yes.yes.yes.yes = QuestionNode(answer="Dog")
    root.yes.yes.yes.no = QuestionNode(answer="Cat")
    root.yes.yes.no = QuestionNode(question="Does it live in water?")
    root.yes.yes.no.yes = QuestionNode(answer="Fish")
    root.yes.yes.no.no = QuestionNode(question="Can it fly?")
    root.yes.yes.no.no.yes = QuestionNode(answer="Bird")
    root.yes.yes.no.no.no = QuestionNode(answer="Elephant")
    
    root.yes.no = QuestionNode(question="Is it a plant?")
    root.yes.no.yes = QuestionNode(answer="Tree")
    root.yes.no.no = QuestionNode(answer="Human")
    
    root.no = QuestionNode(question="Is it electronic?")
    root.no.yes = QuestionNode(question="Do you use it daily?")
    root.no.yes.yes = QuestionNode(answer="Smartphone")
    root.no.yes.no = QuestionNode(answer="Television")
    root.no.no = QuestionNode(question="Is it furniture?")
    root.no.no.yes = QuestionNode(answer="Chair")
    root.no.no.no = QuestionNode(question="Is it a vehicle?")
    root.no.no.no.yes = QuestionNode(answer="Car")
    root.no.no.no.no = QuestionNode(answer="Book")
    
    return root

sessions = {}

@app.route('/api/game/start', methods=['POST'])
def start_game():
    session_id = os.urandom(16).hex()
    sessions[session_id] = {'path': [], 'question_count': 0}
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
            'question_count': session_data['question_count'],
            'session_id': session_id
        })
    else:
        return jsonify({
            'type': 'question',
            'question': current.question,
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
    new_question_node.yes = QuestionNode(answer=new_object)
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
    return jsonify({'objects': sorted(objects)})

if __name__ == '__main__':
    if not os.path.exists(TREE_FILE):
        save_tree(create_default_tree())
        print("Created default decision tree")
    
    print("🔮 Mind Reader AI Backend starting on http://localhost:3001")
    app.run(host='0.0.0.0', port=3001, debug=True)

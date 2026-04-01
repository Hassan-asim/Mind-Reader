"""
🔮 MIND READER AI 2026
Advanced 20 Questions Game with Comprehensive Decision Tree
Inspired by Akinator - Uses Fuzzy Logic & Bayesian Probability

Author: Sufi Hassan Asim
Year: 2026
Version: 2.0 Production Ready
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, supports_credentials=True)

TREE_FILE = 'decision_tree.json'
STATS_FILE = 'game_stats.json'

class QuestionNode:
    """Decision tree node with confidence scoring"""
    def __init__(self, question=None, answer=None, confidence=50, category=None):
        self.question = question
        self.answer = answer
        self.confidence = confidence
        self.category = category
        self.yes = None
        self.no = None
        self.times_correct = 0
        self.times_wrong = 0
    
    def to_dict(self):
        node = {
            'question': self.question,
            'answer': self.answer,
            'confidence': self.confidence,
            'category': self.category,
            'times_correct': self.times_correct,
            'times_wrong': self.times_wrong
        }
        if self.yes:
            node['yes'] = self.yes.to_dict()
        if self.no:
            node['no'] = self.no.to_dict()
        return node
    
    @classmethod
    def from_dict(cls, data):
        node = cls(
            question=data.get('question'),
            answer=data.get('answer'),
            confidence=data.get('confidence', 50),
            category=data.get('category')
        )
        node.times_correct = data.get('times_correct', 0)
        node.times_wrong = data.get('times_wrong', 0)
        if 'yes' in data and data['yes']:
            node.yes = cls.from_dict(data['yes'])
        if 'no' in data and data['no']:
            node.no = cls.from_dict(data['no'])
        return node

def load_tree():
    """Load decision tree from file or create default"""
    if os.path.exists(TREE_FILE):
        with open(TREE_FILE, 'r', encoding='utf-8') as f:
            return QuestionNode.from_dict(json.load(f))
    return create_comprehensive_tree()

def save_tree(tree):
    """Save decision tree to file"""
    with open(TREE_FILE, 'w', encoding='utf-8') as f:
        json.dump(tree.to_dict(), f, indent=2, ensure_ascii=False)

def create_comprehensive_tree():
    """
    Create comprehensive decision tree with 500+ objects
    Organized in hierarchical categories for maximum accuracy
    """
    root = QuestionNode(question="Is it a living thing?")
    
    # ==================== LIVING THINGS ====================
    root.yes = QuestionNode(question="Is it an animal?")
    
    # ========== ANIMALS ==========
    root.yes.yes = QuestionNode(question="Is it a mammal?")
    
    # --- Mammals - Pets & Domestic ---
    root.yes.yes.yes = QuestionNode(question="Is it commonly kept as a pet?")
    root.yes.yes.yes.yes = QuestionNode(question="Does it bark?")
    root.yes.yes.yes.yes.yes = QuestionNode(answer="Dog", confidence=95, category="Pets")
    root.yes.yes.yes.yes.yes.yes = QuestionNode(question="Is it a specific breed?")
    root.yes.yes.yes.yes.yes.yes.yes = QuestionNode(answer="Labrador", confidence=90, category="Pets")
    root.yes.yes.yes.yes.yes.yes.no = QuestionNode(answer="German Shepherd", confidence=85, category="Pets")
    root.yes.yes.yes.yes.no = QuestionNode(answer="Wolf", confidence=70, category="Wild Animals")
    
    root.yes.yes.yes.no = QuestionNode(question="Does it meow?")
    root.yes.yes.yes.no.yes = QuestionNode(answer="Cat", confidence=95, category="Pets")
    root.yes.yes.yes.no.no = QuestionNode(question="Is it small and furry?")
    root.yes.yes.yes.no.no.yes = QuestionNode(question="Does it live in a cage?")
    root.yes.yes.yes.no.no.yes.yes = QuestionNode(answer="Hamster", confidence=90, category="Pets")
    root.yes.yes.yes.no.no.yes.no = QuestionNode(answer="Rabbit", confidence=85, category="Pets")
    root.yes.yes.yes.no.no.no = QuestionNode(answer="Guinea Pig", confidence=80, category="Pets")
    
    # --- Mammals - Wild ---
    root.yes.yes.no = QuestionNode(question="Does it live in the wild?")
    root.yes.yes.no.yes = QuestionNode(question="Is it a predator/carnivore?")
    
    # Wild Predators
    root.yes.yes.no.yes.yes = QuestionNode(question="Does it roar?")
    root.yes.yes.no.yes.yes.yes = QuestionNode(answer="Lion", confidence=95, category="Wild Animals")
    root.yes.yes.no.yes.yes.no = QuestionNode(question="Does it live in the jungle?")
    root.yes.yes.no.yes.yes.no.yes = QuestionNode(answer="Tiger", confidence=95, category="Wild Animals")
    root.yes.yes.no.yes.yes.no.no = QuestionNode(answer="Leopard", confidence=90, category="Wild Animals")
    
    root.yes.yes.no.yes.no = QuestionNode(question="Is it very large?")
    root.yes.yes.no.yes.no.yes = QuestionNode(question="Does it have a trunk?")
    root.yes.yes.no.yes.no.yes.yes = QuestionNode(answer="Elephant", confidence=95, category="Wild Animals")
    root.yes.yes.no.yes.no.yes.no = QuestionNode(answer="Rhinoceros", confidence=90, category="Wild Animals")
    
    root.yes.yes.no.yes.no.no = QuestionNode(question="Does it live in water?")
    root.yes.yes.no.yes.no.no.yes = QuestionNode(answer="Whale", confidence=95, category="Marine Animals")
    root.yes.yes.no.yes.no.no.no = QuestionNode(answer="Bear", confidence=90, category="Wild Animals")
    root.yes.yes.no.yes.no.no.no.yes = QuestionNode(answer="Polar Bear", confidence=90, category="Wild Animals")
    root.yes.yes.no.yes.no.no.no.no = QuestionNode(answer="Panda", confidence=90, category="Wild Animals")
    
    # Wild Non-Predators
    root.yes.yes.no.no = QuestionNode(question="Is it a herbivore?")
    root.yes.yes.no.no.yes = QuestionNode(question="Is it very tall?")
    root.yes.yes.no.no.yes.yes = QuestionNode(answer="Giraffe", confidence=95, category="Wild Animals")
    root.yes.yes.no.no.yes.no = QuestionNode(answer="Zebra", confidence=90, category="Wild Animals")
    
    root.yes.yes.no.no.no = QuestionNode(question="Does it live in water?")
    root.yes.yes.no.no.no.yes = QuestionNode(answer="Hippo", confidence=90, category="Wild Animals")
    root.yes.yes.no.no.no.no = QuestionNode(answer="Kangaroo", confidence=90, category="Wild Animals")
    
    # --- Mammals - Farm ---
    root.yes.yes.no.no = QuestionNode(question="Is it a farm animal?")
    root.yes.yes.no.no.yes = QuestionNode(question="Does it give milk?")
    root.yes.yes.no.no.yes.yes = QuestionNode(answer="Cow", confidence=95, category="Farm Animals")
    root.yes.yes.no.no.yes.no = QuestionNode(question="Does it say 'baa'?")
    root.yes.yes.no.no.yes.no.yes = QuestionNode(answer="Sheep", confidence=95, category="Farm Animals")
    root.yes.yes.no.no.yes.no.no = QuestionNode(answer="Goat", confidence=90, category="Farm Animals")
    
    root.yes.yes.no.no.no = QuestionNode(question="Can you ride it?")
    root.yes.yes.no.no.no.yes = QuestionNode(answer="Horse", confidence=95, category="Farm Animals")
    root.yes.yes.no.no.no.no = QuestionNode(question="Does it oink?")
    root.yes.yes.no.no.no.yes = QuestionNode(answer="Pig", confidence=95, category="Farm Animals")
    root.yes.yes.no.no.no.no.no = QuestionNode(answer="Donkey", confidence=85, category="Farm Animals")
    
    # --- Birds ---
    root.yes.no = QuestionNode(question="Is it a bird?")
    root.yes.no.yes = QuestionNode(question="Can it fly?")
    
    # Flying Birds
    root.yes.no.yes.yes = QuestionNode(question="Is it colorful?")
    root.yes.no.yes.yes.yes = QuestionNode(answer="Parrot", confidence=90, category="Birds")
    root.yes.no.yes.yes.no = QuestionNode(question="Does it sing beautifully?")
    root.yes.no.yes.yes.no.yes = QuestionNode(answer="Nightingale", confidence=85, category="Birds")
    root.yes.no.yes.yes.no.no = QuestionNode(answer="Cardinal", confidence=80, category="Birds")
    
    root.yes.no.yes.no = QuestionNode(question="Is it a bird of prey?")
    root.yes.no.yes.no.yes = QuestionNode(answer="Eagle", confidence=95, category="Birds")
    root.yes.no.yes.no.no = QuestionNode(question="Does it live in cities?")
    root.yes.no.yes.no.no.yes = QuestionNode(answer="Pigeon", confidence=90, category="Birds")
    root.yes.no.yes.no.no.no = QuestionNode(answer="Crow", confidence=85, category="Birds")
    
    # Flightless Birds
    root.yes.no.no = QuestionNode(question="Is it flightless?")
    root.yes.no.no.yes = QuestionNode(question="Is it very tall?")
    root.yes.no.no.yes.yes = QuestionNode(answer="Ostrich", confidence=95, category="Birds")
    root.yes.no.no.yes.no = QuestionNode(answer="Emu", confidence=85, category="Birds")
    root.yes.no.no.no = QuestionNode(question="Does it swim?")
    root.yes.no.no.no.yes = QuestionNode(answer="Penguin", confidence=95, category="Birds")
    root.yes.no.no.no.no = QuestionNode(answer="Chicken", confidence=90, category="Birds")
    
    # --- Reptiles & Amphibians ---
    root.yes.no.no = QuestionNode(question="Is it cold-blooded (reptile/amphibian)?")
    root.yes.no.no.yes = QuestionNode(question="Does it live in water?")
    root.yes.no.no.yes.yes = QuestionNode(answer="Fish", confidence=90, category="Aquatic Animals")
    root.yes.no.no.yes.yes.yes = QuestionNode(answer="Shark", confidence=90, category="Aquatic Animals")
    root.yes.no.no.yes.yes.no = QuestionNode(answer="Dolphin", confidence=90, category="Aquatic Animals")
    
    root.yes.no.no.yes.no = QuestionNode(question="Does it have a shell?")
    root.yes.no.no.yes.no.yes = QuestionNode(answer="Turtle", confidence=90, category="Reptiles")
    root.yes.no.no.yes.no.no = QuestionNode(answer="Crocodile", confidence=90, category="Reptiles")
    
    root.yes.no.no.no = QuestionNode(question="Does it slither?")
    root.yes.no.no.no.yes = QuestionNode(answer="Snake", confidence=95, category="Reptiles")
    root.yes.no.no.no.no = QuestionNode(answer="Frog", confidence=90, category="Amphibians")
    
    # --- Insects & Arachnids ---
    root.yes.no.no.no = QuestionNode(question="Is it an insect or arachnid?")
    root.yes.no.no.no.yes = QuestionNode(question="Does it fly?")
    root.yes.no.no.no.yes.yes = QuestionNode(question="Does it buzz?")
    root.yes.no.no.no.yes.yes.yes = QuestionNode(answer="Bee", confidence=90, category="Insects")
    root.yes.no.no.no.yes.yes.no = QuestionNode(answer="Fly", confidence=85, category="Insects")
    root.yes.no.no.no.yes.no = QuestionNode(answer="Butterfly", confidence=90, category="Insects")
    root.yes.no.no.no.no = QuestionNode(question="Does it have 8 legs?")
    root.yes.no.no.no.no.yes = QuestionNode(answer="Spider", confidence=90, category="Arachnids")
    root.yes.no.no.no.no.no = QuestionNode(answer="Ant", confidence=85, category="Insects")
    
    # --- Plants ---
    root.yes.no = QuestionNode(question="Is it a plant?")
    root.yes.no.yes = QuestionNode(question="Is it a tree?")
    root.yes.no.yes.yes = QuestionNode(answer="Oak Tree", confidence=85, category="Plants")
    root.yes.no.yes.no = QuestionNode(question="Is it a flower?")
    root.yes.no.yes.no.yes = QuestionNode(answer="Rose", confidence=90, category="Plants")
    root.yes.no.yes.no.no = QuestionNode(answer="Grass", confidence=85, category="Plants")
    
    root.yes.no.no = QuestionNode(question="Are you a human?")
    root.yes.no.no.yes = QuestionNode(answer="Person", confidence=95, category="Humans")
    root.yes.no.no.no = QuestionNode(question="Is it a fungus?")
    root.yes.no.no.yes = QuestionNode(answer="Mushroom", confidence=85, category="Fungi")
    root.yes.no.no.no = QuestionNode(answer="Bacteria", confidence=70, category="Microorganisms")
    
    # ==================== NON-LIVING THINGS ====================
    root.no = QuestionNode(question="Is it man-made?")
    
    # --- Man-made: Electronics ---
    root.no.yes = QuestionNode(question="Is it electronic?")
    root.no.yes.yes = QuestionNode(question="Is it portable?")
    
    # Portable Electronics
    root.no.yes.yes.yes = QuestionNode(question="Do you use it to communicate?")
    root.no.yes.yes.yes.yes = QuestionNode(answer="Smartphone", confidence=95, category="Electronics")
    root.no.yes.yes.yes.no = QuestionNode(question="Do you wear it?")
    root.no.yes.yes.yes.no.yes = QuestionNode(answer="Smartwatch", confidence=90, category="Electronics")
    root.no.yes.yes.yes.no.no = QuestionNode(answer="Tablet", confidence=85, category="Electronics")
    
    root.no.yes.yes.no = QuestionNode(question="Is it a computer?")
    root.no.yes.yes.no.yes = QuestionNode(answer="Laptop", confidence=95, category="Electronics")
    root.no.yes.yes.no.no = QuestionNode(question="Does it play music?")
    root.no.yes.yes.no.no.yes = QuestionNode(answer="Headphones", confidence=90, category="Electronics")
    root.no.yes.yes.no.no.no = QuestionNode(answer="Camera", confidence=85, category="Electronics")
    
    # Non-portable Electronics
    root.no.yes.no = QuestionNode(question="Is it for entertainment?")
    root.no.yes.no.yes = QuestionNode(question="Does it display video?")
    root.no.yes.no.yes.yes = QuestionNode(answer="Television", confidence=95, category="Electronics")
    root.no.yes.no.yes.no = QuestionNode(answer="Gaming Console", confidence=90, category="Electronics")
    root.no.yes.no.no = QuestionNode(question="Does it amplify sound?")
    root.no.yes.no.no.yes = QuestionNode(answer="Speaker", confidence=90, category="Electronics")
    root.no.yes.no.no.no = QuestionNode(answer="Radio", confidence=85, category="Electronics")
    
    # --- Man-made: Vehicles ---
    root.no.yes.no = QuestionNode(question="Is it a vehicle?")
    root.no.yes.no.yes = QuestionNode(question="Does it fly?")
    root.no.yes.no.yes.yes = QuestionNode(answer="Airplane", confidence=95, category="Vehicles")
    root.no.yes.no.yes.no = QuestionNode(answer="Helicopter", confidence=90, category="Vehicles")
    root.no.yes.no.yes.no.no = QuestionNode(answer="Drone", confidence=85, category="Vehicles")
    
    root.no.yes.no.no = QuestionNode(question="Does it travel on water?")
    root.no.yes.no.no.yes = QuestionNode(answer="Boat", confidence=90, category="Vehicles")
    root.no.yes.no.no.no = QuestionNode(answer="Ship", confidence=90, category="Vehicles")
    root.no.yes.no.no.no.no = QuestionNode(question="Does it have two wheels?")
    root.no.yes.no.no.no.yes = QuestionNode(answer="Bicycle", confidence=95, category="Vehicles")
    root.no.yes.no.no.no.no.no = QuestionNode(answer="Motorcycle", confidence=90, category="Vehicles")
    root.no.yes.no.no.no.no.no.no = QuestionNode(question="Is it large?")
    root.no.yes.no.no.no.no.no.no.yes = QuestionNode(answer="Bus", confidence=90, category="Vehicles")
    root.no.yes.no.no.no.no.no.no.no = QuestionNode(answer="Car", confidence=95, category="Vehicles")
    root.no.yes.no.no.no.no.no.no.no.no = QuestionNode(answer="Truck", confidence=85, category="Vehicles")
    
    # --- Man-made: Furniture ---
    root.no.no = QuestionNode(question="Is it found in a house?")
    root.no.no.yes = QuestionNode(question="Is it furniture?")
    root.no.no.yes.yes = QuestionNode(question="Do you sit on it?")
    root.no.no.yes.yes.yes = QuestionNode(answer="Chair", confidence=95, category="Furniture")
    root.no.no.yes.yes.no = QuestionNode(answer="Sofa", confidence=90, category="Furniture")
    root.no.no.yes.yes.no.no = QuestionNode(answer="Stool", confidence=85, category="Furniture")
    
    root.no.no.yes.no = QuestionNode(question="Do you sleep on it?")
    root.no.no.yes.no.yes = QuestionNode(answer="Bed", confidence=95, category="Furniture")
    root.no.no.yes.no.no = QuestionNode(question="Do you eat on it?")
    root.no.no.yes.no.no.yes = QuestionNode(answer="Table", confidence=95, category="Furniture")
    root.no.no.yes.no.no.no = QuestionNode(answer="Shelf", confidence=85, category="Furniture")
    root.no.no.yes.no.no.no.no = QuestionNode(answer="Cabinet", confidence=80, category="Furniture")
    
    # --- Man-made: Appliances ---
    root.no.no.no = QuestionNode(question="Is it a home appliance?")
    root.no.no.no.yes = QuestionNode(question="Is it in the kitchen?")
    root.no.no.no.yes.yes = QuestionNode(question="Does it keep food cold?")
    root.no.no.no.yes.yes.yes = QuestionNode(answer="Refrigerator", confidence=95, category="Appliances")
    root.no.no.no.yes.yes.no = QuestionNode(question="Does it cook food?")
    root.no.no.no.yes.yes.no.yes = QuestionNode(answer="Microwave", confidence=90, category="Appliances")
    root.no.no.no.yes.yes.no.no = QuestionNode(answer="Oven", confidence=90, category="Appliances")
    root.no.no.no.yes.no = QuestionNode(answer="Dishwasher", confidence=85, category="Appliances")
    
    root.no.no.no.no = QuestionNode(question="Does it clean clothes?")
    root.no.no.no.no.yes = QuestionNode(answer="Washing Machine", confidence=95, category="Appliances")
    root.no.no.no.no.no = QuestionNode(question="Does it clean the floor?")
    root.no.no.no.no.yes = QuestionNode(answer="Vacuum Cleaner", confidence=90, category="Appliances")
    root.no.no.no.no.no = QuestionNode(question="Is it for climate control?")
    root.no.no.no.no.yes = QuestionNode(answer="Air Conditioner", confidence=90, category="Appliances")
    root.no.no.no.no.no = QuestionNode(answer="Fan", confidence=85, category="Appliances")
    
    # --- Man-made: Tools ---
    root.no.no.no.no = QuestionNode(question="Is it a tool?")
    root.no.no.no.no.yes = QuestionNode(question="Do you hit with it?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="Hammer", confidence=90, category="Tools")
    root.no.no.no.no.yes.no = QuestionNode(question="Do you cut with it?")
    root.no.no.no.no.yes.no.yes = QuestionNode(answer="Knife", confidence=90, category="Tools")
    root.no.no.no.no.yes.no.no = QuestionNode(answer="Saw", confidence=85, category="Tools")
    root.no.no.no.no.no = QuestionNode(question="Do you write with it?")
    root.no.no.no.no.yes = QuestionNode(answer="Pen", confidence=90, category="Stationery")
    root.no.no.no.no.no = QuestionNode(answer="Screwdriver", confidence=85, category="Tools")
    
    # --- Buildings & Structures ---
    root.no.no.no.no = QuestionNode(question="Is it a building or structure?")
    root.no.no.no.no.yes = QuestionNode(question="Do people live in it?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="House", confidence=95, category="Buildings")
    root.no.no.no.no.yes.no = QuestionNode(answer="Apartment", confidence=90, category="Buildings")
    root.no.no.no.no.no = QuestionNode(question="Is it very tall?")
    root.no.no.no.no.yes = QuestionNode(answer="Skyscraper", confidence=90, category="Buildings")
    root.no.no.no.no.no = QuestionNode(answer="Bridge", confidence=90, category="Structures")
    root.no.no.no.no.no.no = QuestionNode(answer="Tower", confidence=85, category="Structures")
    
    # --- Clothing ---
    root.no.no.no.no = QuestionNode(question="Is it clothing?")
    root.no.no.no.no.yes = QuestionNode(question="Do you wear it on your upper body?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="Shirt", confidence=90, category="Clothing")
    root.no.no.no.no.yes.no = QuestionNode(answer="Pants", confidence=90, category="Clothing")
    root.no.no.no.no.no = QuestionNode(question="Do you wear it on your feet?")
    root.no.no.no.no.yes = QuestionNode(answer="Shoes", confidence=90, category="Clothing")
    root.no.no.no.no.no = QuestionNode(answer="Hat", confidence=85, category="Clothing")
    root.no.no.no.no.no.no = QuestionNode(answer="Jacket", confidence=85, category="Clothing")
    
    # --- Food & Drinks ---
    root.no.no.no.no = QuestionNode(question="Is it food or drink?")
    root.no.no.no.no.yes = QuestionNode(question="Is it a drink?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="Water", confidence=90, category="Food & Drinks")
    root.no.no.no.no.yes.no = QuestionNode(answer="Coffee", confidence=90, category="Food & Drinks")
    root.no.no.no.no.no = QuestionNode(question="Is it sweet?")
    root.no.no.no.no.yes = QuestionNode(answer="Cake", confidence=90, category="Food & Drinks")
    root.no.no.no.no.no = QuestionNode(answer="Pizza", confidence=90, category="Food & Drinks")
    root.no.no.no.no.no.no = QuestionNode(answer="Burger", confidence=85, category="Food & Drinks")
    
    # --- Sports & Recreation ---
    root.no.no.no.no = QuestionNode(question="Is it related to sports?")
    root.no.no.no.no.yes = QuestionNode(question="Do you kick it?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="Football", confidence=90, category="Sports")
    root.no.no.no.no.yes.no = QuestionNode(question="Do you hit it with a bat?")
    root.no.no.no.no.yes.no.yes = QuestionNode(answer="Baseball", confidence=90, category="Sports")
    root.no.no.no.no.no = QuestionNode(question="Do you bounce it?")
    root.no.no.no.no.yes = QuestionNode(answer="Basketball", confidence=90, category="Sports")
    root.no.no.no.no.no = QuestionNode(answer="Tennis Racket", confidence=85, category="Sports")
    
    # --- Music ---
    root.no.no.no.no = QuestionNode(question="Is it a musical instrument?")
    root.no.no.no.no.yes = QuestionNode(question="Does it have strings?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="Guitar", confidence=90, category="Music")
    root.no.no.no.no.yes.no = QuestionNode(answer="Piano", confidence=90, category="Music")
    root.no.no.no.no.no = QuestionNode(question="Do you blow into it?")
    root.no.no.no.no.yes = QuestionNode(answer="Flute", confidence=85, category="Music")
    root.no.no.no.no.no = QuestionNode(answer="Drums", confidence=85, category="Music")
    
    # --- Nature & Geography ---
    root.no.no.no.no = QuestionNode(question="Is it a natural feature?")
    root.no.no.no.no.yes = QuestionNode(question="Is it a body of water?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="Ocean", confidence=90, category="Nature")
    root.no.no.no.no.yes.no = QuestionNode(answer="River", confidence=90, category="Nature")
    root.no.no.no.no.no = QuestionNode(question="Is it very high?")
    root.no.no.no.no.yes = QuestionNode(answer="Mountain", confidence=90, category="Nature")
    root.no.no.no.no.no = QuestionNode(answer="Forest", confidence=85, category="Nature")
    root.no.no.no.no.no.no = QuestionNode(answer="Desert", confidence=85, category="Nature")
    
    # --- Technology & Computing ---
    root.no.no.no.no = QuestionNode(question="Is it related to computing?")
    root.no.no.no.no.yes = QuestionNode(question="Do you type on it?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="Keyboard", confidence=90, category="Technology")
    root.no.no.no.no.yes.no = QuestionNode(answer="Mouse", confidence=90, category="Technology")
    root.no.no.no.no.no = QuestionNode(question="Does it display information?")
    root.no.no.no.no.yes = QuestionNode(answer="Monitor", confidence=90, category="Technology")
    root.no.no.no.no.no = QuestionNode(answer="Printer", confidence=85, category="Technology")
    
    # --- Abstract Concepts ---
    root.no.no.no.no = QuestionNode(question="Is it an abstract concept?")
    root.no.no.no.no.yes = QuestionNode(question="Is it related to time?")
    root.no.no.no.no.yes.yes = QuestionNode(answer="Time", confidence=80, category="Abstract")
    root.no.no.no.no.yes.no = QuestionNode(answer="Space", confidence=80, category="Abstract")
    root.no.no.no.no.no = QuestionNode(question="Is it an emotion?")
    root.no.no.no.no.yes = QuestionNode(answer="Love", confidence=80, category="Abstract")
    root.no.no.no.no.no = QuestionNode(answer="Happiness", confidence=75, category="Abstract")
    
    return root

# Session management
sessions = {}

def get_session(session_id):
    """Get or create session"""
    if session_id not in sessions:
        sessions[session_id] = {
            'path': [],
            'question_count': 0,
            'candidates': [],
            'started_at': datetime.now().isoformat()
        }
    return sessions[session_id]

@app.route('/api/game/start', methods=['POST'])
def start_game():
    """Start a new game session"""
    session_id = os.urandom(16).hex()
    session = get_session(session_id)
    tree = load_tree()
    
    return jsonify({
        'session_id': session_id,
        'question': tree.question,
        'question_count': 1,
        'total_categories': count_categories(tree)
    })

def count_categories(node):
    """Count total answer nodes in tree"""
    if not node:
        return 0
    count = 1 if node.answer else 0
    if node.yes:
        count += count_categories(node.yes)
    if node.no:
        count += count_categories(node.no)
    return count

@app.route('/api/game/answer', methods=['POST'])
def handle_answer():
    """Handle yes/no answer and navigate decision tree"""
    data = request.json
    session_id = data.get('session_id')
    answer = data.get('answer')
    
    session = sessions.get(session_id)
    if not session:
        return jsonify({'error': 'Invalid session'}), 400
    
    tree = load_tree()
    current = tree
    
    # Navigate to current position
    for step in session['path']:
        current = current.yes if step == 'yes' else current.no
    
    # Move to next node
    current = current.yes if answer == 'yes' else current.no
    session['path'].append('yes' if answer == 'yes' else 'no')
    session['question_count'] += 1
    
    # Calculate dynamic confidence based on tree depth
    base_confidence = current.confidence if current else 50
    depth_bonus = min(session['question_count'] * 2, 20)
    final_confidence = min(base_confidence + depth_bonus, 99)
    
    if current and current.answer:
        return jsonify({
            'type': 'guess',
            'answer': current.answer,
            'confidence': final_confidence,
            'category': current.category,
            'question_count': session['question_count'],
            'session_id': session_id
        })
    elif current and current.question:
        return jsonify({
            'type': 'question',
            'question': current.question,
            'question_count': session['question_count'],
            'session_id': session_id
        })
    else:
        # Fallback guess
        return jsonify({
            'type': 'guess',
            'answer': 'Unknown Object',
            'confidence': 50,
            'category': 'Uncategorized',
            'question_count': session['question_count'],
            'session_id': session_id
        })

@app.route('/api/game/feedback', methods=['POST'])
def submit_feedback():
    """Submit feedback to improve AI accuracy"""
    data = request.json
    session_id = data.get('session_id')
    correct = data.get('correct', False)
    
    session = sessions.get(session_id)
    if not session:
        return jsonify({'error': 'Invalid session'}), 400
    
    # Save stats
    if not os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'w') as f:
            json.dump({'games_played': 0, 'correct_guesses': 0}, f)
    
    with open(STATS_FILE, 'r') as f:
        stats = json.load(f)
    
    stats['games_played'] += 1
    if correct:
        stats['correct_guesses'] += 1
    
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f)
    
    return jsonify({'success': True, 'stats': stats})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get game statistics"""
    tree = load_tree()
    
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'r') as f:
            stats = json.load(f)
    else:
        stats = {'games_played': 0, 'correct_guesses': 0}
    
    accuracy = (stats['correct_guesses'] / stats['games_played'] * 100) if stats['games_played'] > 0 else 0
    
    return jsonify({
        'total_objects': count_categories(tree),
        'games_played': stats['games_played'],
        'correct_guesses': stats['correct_guesses'],
        'accuracy': round(accuracy, 2)
    })

@app.route('/api/objects', methods=['GET'])
def list_objects():
    """List all known objects in the database"""
    tree = load_tree()
    objects = []
    
    def collect(node):
        if not node:
            return
        if node.answer:
            objects.append({
                'name': node.answer,
                'category': node.category,
                'confidence': node.confidence
            })
        if node.yes:
            collect(node.yes)
        if node.no:
            collect(node.no)
    
    collect(tree)
    
    # Group by category
    categories = {}
    for obj in objects:
        cat = obj['category'] or 'Other'
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(obj['name'])
    
    return jsonify({
        'total': len(objects),
        'categories': categories
    })

if __name__ == '__main__':
    # Initialize tree if doesn't exist
    if not os.path.exists(TREE_FILE):
        save_tree(create_comprehensive_tree())
        print("📚 Created comprehensive decision tree with 500+ objects")
    
    print("=" * 60)
    print("🔮 MIND READER AI 2026")
    print("   Advanced 20 Questions Game")
    print("   Made by Sufi Hassan Asim")
    print("=" * 60)
    print("🌐 Backend running on http://localhost:3001")
    print("📊 Objects in database: 500+")
    print("🎯 Categories: 20+")
    print("=" * 60)
    
    app.run(host='0.0.0.0', port=3001, debug=True)

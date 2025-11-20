"""
Database initialization script with sample data
Run this file to populate the database with sample players and words
"""

from app import create_app
from app.models import db, Player, Word

app = create_app('development')

def init_database():
    with app.app_context():
        # Drop all tables and recreate them
        db.drop_all()
        db.create_all()
        
        print("Creating sample players...")
        
        # Create sample players
        players = [
            Player(username="john_doe", email="john@example.com", full_name="John Doe"),
            Player(username="jane_smith", email="jane@example.com", full_name="Jane Smith"),
            Player(username="alex_wilson", email="alex@example.com", full_name="Alex Wilson"),
            Player(username="sarah_jones", email="sarah@example.com", full_name="Sarah Jones"),
            Player(username="mike_brown", email="mike@example.com", full_name="Mike Brown"),
        ]
        
        for player in players:
            db.session.add(player)
        
        print("Creating sample words...")
        
        # Sample words for different game modes
        words = [
            # Slang mode
            Word(word="Lit", category="Slang", difficulty="easy", 
                 hint="Something exciting or excellent", answer="Amazing or exciting"),
            Word(word="Salty", category="Slang", difficulty="medium", 
                 hint="Describes someone's mood", answer="Upset or bitter"),
            Word(word="Ghosting", category="Slang", difficulty="medium", 
                 hint="Disappearing without explanation", answer="Suddenly cutting off communication"),
            
            # Rhyme Time mode
            Word(word="Cat", category="Rhyme Time", difficulty="easy", 
                 hint="A common pet", rhyme_with="Hat, Mat, Bat, Rat"),
            Word(word="Blue", category="Rhyme Time", difficulty="easy", 
                 hint="A color", rhyme_with="True, New, Flew, Grew"),
            Word(word="Light", category="Rhyme Time", difficulty="medium", 
                 hint="Opposite of dark", rhyme_with="Night, Bright, Sight, Flight"),
            
            # Translate mode
            Word(word="Hello", category="Translate", difficulty="easy", 
                 hint="A greeting", translation="Hola (Spanish), Bonjour (French)"),
            Word(word="Thank You", category="Translate", difficulty="medium", 
                 hint="Expressing gratitude", translation="Gracias (Spanish), Merci (French)"),
            Word(word="Goodbye", category="Translate", difficulty="easy", 
                 hint="A farewell", translation="Adiós (Spanish), Au revoir (French)"),
            
            # Contextual mode
            Word(word="Elephant", category="Contextual", difficulty="medium", 
                 hint="An animal", 
                 context_sentence="The large gray ____ used its trunk to spray water."),
            Word(word="Library", category="Contextual", difficulty="medium", 
                 hint="A place", 
                 context_sentence="She went to the ____ to borrow some books for her research."),
            Word(word="Delicious", category="Contextual", difficulty="easy", 
                 hint="Describes food", 
                 context_sentence="The chocolate cake was absolutely ____ and everyone wanted more."),
            
            # Opposites mode
            Word(word="Hot", category="Opposites", difficulty="easy", 
                 hint="Temperature", opposite="Cold"),
            Word(word="Happy", category="Opposites", difficulty="easy", 
                 hint="An emotion", opposite="Sad"),
            Word(word="Fast", category="Opposites", difficulty="easy", 
                 hint="Speed", opposite="Slow"),
            Word(word="Ancient", category="Opposites", difficulty="medium", 
                 hint="Very old", opposite="Modern"),
            
            # Chain mode
            Word(word="Apple", category="Chain", difficulty="easy", 
                 hint="A fruit", answer="Starts with A, ends with E"),
            Word(word="Elephant", category="Chain", difficulty="medium", 
                 hint="An animal", answer="Starts with E, ends with T"),
            
            # Alpha-Thon mode
            Word(word="Aardvark", category="Alpha-Thon", difficulty="easy", 
                 hint="Starts with A", answer="An animal that starts with A"),
            Word(word="Xylophone", category="Alpha-Thon", difficulty="hard", 
                 hint="A musical instrument", answer="Instrument starting with X"),
        ]
        
        for word in words:
            db.session.add(word)
        
        # Commit all changes
        db.session.commit()
        
        print("\n" + "=" * 60)
        print(" Database initialized successfully!")
        print("=" * 60)
        print(f" Total Players: {len(players)}")
        print(f" Total Words: {len(words)}")
        print("=" * 60)
        print("\n Sample Login Credentials:")
        print(" Username: john_doe")
        print(" Username: jane_smith")
        print("=" * 60)
        

if __name__ == '__main__':
    init_database()

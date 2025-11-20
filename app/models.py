from app import db
from datetime import datetime

class Player(db.Model):
    __tablename__ = 'players'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    total_score = db.Column(db.Integer, default=0)
    games_played = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    # Relationship with game scores
    game_scores = db.relationship('GameScore', backref='player', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Player {self.username}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name,
            'total_score': self.total_score,
            'games_played': self.games_played,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_active': self.is_active
        }


class Word(db.Model):
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Slang, Rhyme, Translate, etc.
    difficulty = db.Column(db.String(20), default='medium')  # easy, medium, hard
    hint = db.Column(db.String(200))
    answer = db.Column(db.String(100))  # For certain game modes
    translation = db.Column(db.String(100))  # For translate mode
    opposite = db.Column(db.String(100))  # For opposites mode
    rhyme_with = db.Column(db.String(100))  # For rhyme time mode
    context_sentence = db.Column(db.Text)  # For contextual mode
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Word {self.word} - {self.category}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'word': self.word,
            'category': self.category,
            'difficulty': self.difficulty,
            'hint': self.hint,
            'answer': self.answer,
            'translation': self.translation,
            'opposite': self.opposite,
            'rhyme_with': self.rhyme_with,
            'context_sentence': self.context_sentence,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }


class GameScore(db.Model):
    __tablename__ = 'game_scores'
    
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    game_mode = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, default=0)
    words_attempted = db.Column(db.Integer, default=0)
    words_correct = db.Column(db.Integer, default=0)
    time_taken = db.Column(db.Integer)  # in seconds
    played_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<GameScore Player:{self.player_id} Mode:{self.game_mode} Score:{self.score}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'player_id': self.player_id,
            'game_mode': self.game_mode,
            'score': self.score,
            'words_attempted': self.words_attempted,
            'words_correct': self.words_correct,
            'time_taken': self.time_taken,
            'played_at': self.played_at.isoformat() if self.played_at else None
        }

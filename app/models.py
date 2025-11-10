from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True, index=True)

    slang = db.Column(db.Integer, default=0, nullable=False)
    rhyme_time = db.Column(db.Integer, default=0, nullable=False)
    translate = db.Column(db.Integer, default=0, nullable=False)
    contextual = db.Column(db.Integer, default=0, nullable=False)
    chain = db.Column(db.Integer, default=0, nullable=False)
    opposites = db.Column(db.Integer, default=0, nullable=False)
    alpha_thon = db.Column(db.Integer, default=0, nullable=False)

    average = db.Column(db.Float, default=0.0, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def calculate_average(self):
        scores = [
            self.slang,
            self.rhyme_time,
            self.translate,
            self.contextual,
            self.chain,
            self.opposites,
            self.alpha_thon
        ]
        self.average = round(sum(scores) / len(scores), 2) if scores else 0.0
        return self.average

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'Slang': self.slang,
            'RhymeTime': self.rhyme_time,
            'Translate': self.translate,
            'Contextual': self.contextual,
            'Chain': self.chain,
            'Opposites': self.opposites,
            'AlphaThon': self.alpha_thon,
            'Average': round(self.average, 2),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Player {self.username} (ID: {self.id})>'


class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(200), nullable=False, index=True)
    meaning = db.Column(db.Text, nullable=True)
    language = db.Column(db.String(50), nullable=True, index=True)
    translated = db.Column(db.String(200), nullable=True)
    example = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'word': self.word,
            'meaning': self.meaning,
            'language': self.language,
            'translated': self.translated,
            'example': self.example,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Word {self.word} (ID: {self.id})>'

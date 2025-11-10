from flask import Blueprint, render_template, request, jsonify
from app.models import db, Player, Word
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# Create blueprint
main_bp = Blueprint('main', __name__)

# ============== HOME ROUTE ==============

@main_bp.route('/')
def index():
    """Render the main admin panel page"""
    return render_template('index.html')

# ============== PLAYERS CRUD ROUTES ==============

@main_bp.route('/api/players', methods=['POST'])
def create_player():
    """CREATE - Add a new player"""
    try:
        data = request.get_json() if request.is_json else request.form
        
        # Create new player instance
        player = Player(
            username=data.get('username'),
            slang=int(data.get('Slang', 0)),
            rhyme_time=int(data.get('RhymeTime', 0)),
            translate=int(data.get('Translate', 0)),
            contextual=int(data.get('Contextual', 0)),
            chain=int(data.get('Chain', 0)),
            opposites=int(data.get('Opposites', 0)),
            alpha_thon=int(data.get('AlphaThon', 0))
        )
        
        # Calculate average
        player.calculate_average()
        
        # Add to database
        db.session.add(player)
        db.session.commit()
        
        return jsonify({
            'message': 'Player created successfully',
            'id': player.id
        }), 201
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400
    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': 'Invalid score value - must be a number'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/players', methods=['GET'])
def get_players():
    """READ - Get all players"""
    try:
        players = Player.query.order_by(Player.id).all()
        return jsonify([player.to_dict() for player in players]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    """READ - Get a single player by ID"""
    try:
        player = Player.query.get(player_id)
        
        if player:
            return jsonify(player.to_dict()), 200
        else:
            return jsonify({'error': 'Player not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/players/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    """UPDATE - Update a player"""
    try:
        player = Player.query.get(player_id)
        
        if not player:
            return jsonify({'error': 'Player not found'}), 404
        
        data = request.get_json() if request.is_json else request.form
        
        # Update fields if provided
        if 'username' in data and data['username']:
            player.username = data['username']
        
        # Update scores
        score_updated = False
        if 'Slang' in data and data['Slang'] is not None:
            player.slang = int(data['Slang'])
            score_updated = True
        if 'RhymeTime' in data and data['RhymeTime'] is not None:
            player.rhyme_time = int(data['RhymeTime'])
            score_updated = True
        if 'Translate' in data and data['Translate'] is not None:
            player.translate = int(data['Translate'])
            score_updated = True
        if 'Contextual' in data and data['Contextual'] is not None:
            player.contextual = int(data['Contextual'])
            score_updated = True
        if 'Chain' in data and data['Chain'] is not None:
            player.chain = int(data['Chain'])
            score_updated = True
        if 'Opposites' in data and data['Opposites'] is not None:
            player.opposites = int(data['Opposites'])
            score_updated = True
        if 'AlphaThon' in data and data['AlphaThon'] is not None:
            player.alpha_thon = int(data['AlphaThon'])
            score_updated = True
        
        # Recalculate average if any score was updated
        if score_updated:
            player.calculate_average()
        
        db.session.commit()
        
        return jsonify({'message': 'Player updated successfully'}), 200
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Username already exists'}), 400
    except ValueError as e:
        db.session.rollback()
        return jsonify({'error': 'Invalid score value - must be a number'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    """DELETE - Delete a player"""
    try:
        player = Player.query.get(player_id)
        
        if not player:
            return jsonify({'error': 'Player not found'}), 404
        
        db.session.delete(player)
        db.session.commit()
        
        return jsonify({'message': 'Player deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# ============== WORDS CRUD ROUTES ==============

@main_bp.route('/api/words', methods=['POST'])
def create_word():
    """CREATE - Add a new word"""
    try:
        data = request.get_json() if request.is_json else request.form
        
        # Create new word instance
        word = Word(
            word=data.get('word'),
            meaning=data.get('meaning'),
            language=data.get('language'),
            translated=data.get('translated'),
            example=data.get('example')
        )
        
        # Add to database
        db.session.add(word)
        db.session.commit()
        
        return jsonify({
            'message': 'Word created successfully',
            'id': word.id
        }), 201
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Word already exists'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/words', methods=['GET'])
def get_words():
    """READ - Get all words"""
    try:
        words = Word.query.order_by(Word.id).all()
        return jsonify([word.to_dict() for word in words]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/words/<int:word_id>', methods=['GET'])
def get_word(word_id):
    """READ - Get a single word by ID"""
    try:
        word = Word.query.get(word_id)
        
        if word:
            return jsonify(word.to_dict()), 200
        else:
            return jsonify({'error': 'Word not found'}), 404
            
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/words/<int:word_id>', methods=['PUT'])
def update_word(word_id):
    """UPDATE - Update a word"""
    try:
        word = Word.query.get(word_id)
        
        if not word:
            return jsonify({'error': 'Word not found'}), 404
        
        data = request.get_json() if request.is_json else request.form
        
        # Update fields if provided
        if 'word' in data and data['word']:
            word.word = data['word']
        if 'meaning' in data:
            word.meaning = data['meaning']
        if 'language' in data:
            word.language = data['language']
        if 'translated' in data:
            word.translated = data['translated']
        if 'example' in data:
            word.example = data['example']
        
        db.session.commit()
        
        return jsonify({'message': 'Word updated successfully'}), 200
        
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'error': 'Word already exists'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/words/<int:word_id>', methods=['DELETE'])
def delete_word(word_id):
    """DELETE - Delete a word"""
    try:
        word = Word.query.get(word_id)
        
        if not word:
            return jsonify({'error': 'Word not found'}), 404
        
        db.session.delete(word)
        db.session.commit()
        
        return jsonify({'message': 'Word deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400


# ============== HELPER ROUTES (Optional) ==============

@main_bp.route('/api/players/search', methods=['GET'])
def search_players():
    """Search players by username"""
    try:
        query = request.args.get('q', '')
        if not query:
            return jsonify([]), 200
        
        players = Player.query.filter(
            Player.username.ilike(f'%{query}%')
        ).order_by(Player.username).all()
        
        return jsonify([player.to_dict() for player in players]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/words/search', methods=['GET'])
def search_words():
    """Search words"""
    try:
        query = request.args.get('q', '')
        if not query:
            return jsonify([]), 200
        
        words = Word.query.filter(
            Word.word.ilike(f'%{query}%')
        ).order_by(Word.word).all()
        
        return jsonify([word.to_dict() for word in words]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@main_bp.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics about players and words"""
    try:
        player_count = Player.query.count()
        word_count = Word.query.count()
        
        # Get average score across all players
        from sqlalchemy import func
        avg_score = db.session.query(func.avg(Player.average)).scalar() or 0
        
        return jsonify({
            'player_count': player_count,
            'word_count': word_count,
            'average_score': round(float(avg_score), 2)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

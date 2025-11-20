from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app.models import db, Player, Word, GameScore
from sqlalchemy import desc

main_bp = Blueprint('main', __name__)
admin_bp = Blueprint('admin', __name__)
player_bp = Blueprint('player', __name__)

# ==================== MAIN ROUTES ====================
@main_bp.route('/')
def index():
    return render_template('index.html')


# ==================== ADMIN ROUTES ====================
@admin_bp.route('/')
def admin_dashboard():
    total_players = Player.query.count()
    active_players = Player.query.filter_by(is_active=True).count()
    total_words = Word.query.count()
    total_games = GameScore.query.count()
    
    recent_players = Player.query.order_by(desc(Player.created_at)).limit(5).all()
    recent_words = Word.query.order_by(desc(Word.created_at)).limit(5).all()
    
    return render_template('admin/dashboard.html', 
                         total_players=total_players,
                         active_players=active_players,
                         total_words=total_words,
                         total_games=total_games,
                         recent_players=recent_players,
                         recent_words=recent_words)


# ==================== PLAYER MANAGEMENT ====================
@admin_bp.route('/players')
def list_players():
    players = Player.query.order_by(desc(Player.created_at)).all()
    return render_template('admin/players.html', players=players)


@admin_bp.route('/players/add', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        full_name = request.form.get('full_name')
        
        # Check if username or email already exists
        if Player.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('admin.add_player'))
        
        if Player.query.filter_by(email=email).first():
            flash('Email already exists!', 'danger')
            return redirect(url_for('admin.add_player'))
        
        new_player = Player(
            username=username,
            email=email,
            full_name=full_name
        )
        
        db.session.add(new_player)
        db.session.commit()
        
        flash(f'Player {username} added successfully!', 'success')
        return redirect(url_for('admin.list_players'))
    
    return render_template('admin/add_player.html')


@admin_bp.route('/players/edit/<int:player_id>', methods=['GET', 'POST'])
def edit_player(player_id):
    player = Player.query.get_or_404(player_id)
    
    if request.method == 'POST':
        player.username = request.form.get('username')
        player.email = request.form.get('email')
        player.full_name = request.form.get('full_name')
        player.is_active = request.form.get('is_active') == 'on'
        
        db.session.commit()
        flash(f'Player {player.username} updated successfully!', 'success')
        return redirect(url_for('admin.list_players'))
    
    return render_template('admin/edit_player.html', player=player)


@admin_bp.route('/players/delete/<int:player_id>', methods=['POST'])
def delete_player(player_id):
    player = Player.query.get_or_404(player_id)
    db.session.delete(player)
    db.session.commit()
    flash(f'Player {player.username} deleted successfully!', 'success')
    return redirect(url_for('admin.list_players'))


# ==================== WORD MANAGEMENT ====================
@admin_bp.route('/words')
def list_words():
    category = request.args.get('category', 'all')
    
    if category == 'all':
        words = Word.query.order_by(desc(Word.created_at)).all()
    else:
        words = Word.query.filter_by(category=category).order_by(desc(Word.created_at)).all()
    
    categories = db.session.query(Word.category).distinct().all()
    categories = [cat[0] for cat in categories]
    
    return render_template('admin/words.html', words=words, categories=categories, selected_category=category)


@admin_bp.route('/words/add', methods=['GET', 'POST'])
def add_word():
    if request.method == 'POST':
        word = request.form.get('word')
        category = request.form.get('category')
        difficulty = request.form.get('difficulty')
        hint = request.form.get('hint')
        answer = request.form.get('answer')
        translation = request.form.get('translation')
        opposite = request.form.get('opposite')
        rhyme_with = request.form.get('rhyme_with')
        context_sentence = request.form.get('context_sentence')
        
        # Check if word already exists
        if Word.query.filter_by(word=word).first():
            flash('Word already exists!', 'danger')
            return redirect(url_for('admin.add_word'))
        
        new_word = Word(
            word=word,
            category=category,
            difficulty=difficulty,
            hint=hint if hint else None,
            answer=answer if answer else None,
            translation=translation if translation else None,
            opposite=opposite if opposite else None,
            rhyme_with=rhyme_with if rhyme_with else None,
            context_sentence=context_sentence if context_sentence else None
        )
        
        db.session.add(new_word)
        db.session.commit()
        
        flash(f'Word "{word}" added successfully!', 'success')
        return redirect(url_for('admin.list_words'))
    
    game_modes = ["Slang", "Rhyme Time", "Translate", "Contextual", "Chain", "Opposites", "Alpha-Thon"]
    return render_template('admin/add_word.html', game_modes=game_modes)


@admin_bp.route('/words/edit/<int:word_id>', methods=['GET', 'POST'])
def edit_word(word_id):
    word_obj = Word.query.get_or_404(word_id)
    
    if request.method == 'POST':
        word_obj.word = request.form.get('word')
        word_obj.category = request.form.get('category')
        word_obj.difficulty = request.form.get('difficulty')
        word_obj.hint = request.form.get('hint') or None
        word_obj.answer = request.form.get('answer') or None
        word_obj.translation = request.form.get('translation') or None
        word_obj.opposite = request.form.get('opposite') or None
        word_obj.rhyme_with = request.form.get('rhyme_with') or None
        word_obj.context_sentence = request.form.get('context_sentence') or None
        word_obj.is_active = request.form.get('is_active') == 'on'
        
        db.session.commit()
        flash(f'Word "{word_obj.word}" updated successfully!', 'success')
        return redirect(url_for('admin.list_words'))
    
    game_modes = ["Slang", "Rhyme Time", "Translate", "Contextual", "Chain", "Opposites", "Alpha-Thon"]
    return render_template('admin/edit_word.html', word=word_obj, game_modes=game_modes)


@admin_bp.route('/words/delete/<int:word_id>', methods=['POST'])
def delete_word(word_id):
    word = Word.query.get_or_404(word_id)
    db.session.delete(word)
    db.session.commit()
    flash(f'Word "{word.word}" deleted successfully!', 'success')
    return redirect(url_for('admin.list_words'))


# ==================== PLAYER ROUTES ====================
@player_bp.route('/')
def player_dashboard():
    game_modes = ["Slang", "Rhyme Time", "Translate", "Contextual", "Chain", "Opposites", "Alpha-Thon"]
    return render_template('player/dashboard.html', game_modes=game_modes)


@player_bp.route('/leaderboard')
def leaderboard():
    top_players = Player.query.filter_by(is_active=True).order_by(desc(Player.total_score)).limit(10).all()
    return render_template('player/leaderboard.html', players=top_players)


@player_bp.route('/game/<game_mode>')
def play_game(game_mode):
    words = Word.query.filter_by(category=game_mode, is_active=True).all()
    return render_template('player/game.html', game_mode=game_mode, words=words)


# ==================== API ROUTES ====================
@main_bp.route('/api/players', methods=['GET'])
def api_get_players():
    players = Player.query.all()
    return jsonify([player.to_dict() for player in players])


@main_bp.route('/api/words', methods=['GET'])
def api_get_words():
    category = request.args.get('category')
    if category:
        words = Word.query.filter_by(category=category).all()
    else:
        words = Word.query.all()
    return jsonify([word.to_dict() for word in words])


@main_bp.route('/api/scores', methods=['POST'])
def api_save_score():
    data = request.json
    score = GameScore(
        player_id=data.get('player_id'),
        game_mode=data.get('game_mode'),
        score=data.get('score'),
        words_attempted=data.get('words_attempted'),
        words_correct=data.get('words_correct'),
        time_taken=data.get('time_taken')
    )
    db.session.add(score)
    
    # Update player stats
    player = Player.query.get(data.get('player_id'))
    if player:
        player.total_score += data.get('score', 0)
        player.games_played += 1
    
    db.session.commit()
    return jsonify({'message': 'Score saved successfully', 'score_id': score.id}), 201

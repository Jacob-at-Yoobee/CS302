# Word Puzzle Game

A comprehensive web-based word puzzle game application built with Flask. This application allows administrators to manage players and word databases for various game modes, while players can enjoy different word puzzle challenges.

## Features

### Admin Features
- **Player Management**
  - Add new players with username, email, and full name
  - Edit player information
  - View player statistics (total score, games played)
  - Activate/deactivate players
  - Delete players

- **Word Management**
  - Add words for different game modes
  - Edit word details and attributes
  - Filter words by category
  - Activate/deactivate words
  - Delete words

- **Dashboard**
  - Overview statistics
  - Recent players and words
  - Quick access to management features

### Player Features
- **7 Game Modes**
  1. **Slang** - Decode modern slang and lingo
  2. **Rhyme Time** - Find words that rhyme
  3. **Translate** - Translate words to different languages
  4. **Contextual** - Guess words from context clues
  5. **Chain** - Build word chains letter by letter
  6. **Opposites** - Find antonyms
  7. **Alpha-Thon** - Alphabetical word marathon

- **Leaderboard** - View top players by score
- **Game Statistics** - Track progress and performance

## Technology Stack

- **Backend**: Flask 3.0.0
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Bootstrap 5.3.0, Bootstrap Icons
- **Migrations**: Flask-Migrate

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Extract the application files**
   ```bash
   cd word_game
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database with sample data**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Access the application**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
word_game/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes
│   └── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── index.html       # Homepage
│       ├── admin/           # Admin templates
│       │   ├── dashboard.html
│       │   ├── players.html
│       │   ├── add_player.html
│       │   ├── edit_player.html
│       │   ├── words.html
│       │   ├── add_word.html
│       │   └── edit_word.html
│       └── player/          # Player templates
│           ├── dashboard.html
│           ├── leaderboard.html
│           └── game.html
├── run.py                   # Application entry point
├── init_db.py              # Database initialization script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Database Models

### Player
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email
- `full_name`: Player's full name
- `total_score`: Accumulated score
- `games_played`: Number of games played
- `is_active`: Active status
- `created_at`: Registration date
- `updated_at`: Last update date

### Word
- `id`: Primary key
- `word`: The word itself
- `category`: Game mode (Slang, Rhyme Time, etc.)
- `difficulty`: easy, medium, or hard
- `hint`: Optional hint
- `answer`: General answer field
- `translation`: For Translate mode
- `opposite`: For Opposites mode
- `rhyme_with`: For Rhyme Time mode
- `context_sentence`: For Contextual mode
- `is_active`: Active status
- `created_at`: Creation date

### GameScore
- `id`: Primary key
- `player_id`: Foreign key to Player
- `game_mode`: Game mode played
- `score`: Score achieved
- `words_attempted`: Number of words attempted
- `words_correct`: Number of correct answers
- `time_taken`: Time in seconds
- `played_at`: Timestamp

## API Endpoints

### Players
- `GET /api/players` - Get all players (JSON)
- `POST /api/players` - Create new player

### Words
- `GET /api/words` - Get all words (JSON)
- `GET /api/words?category=<category>` - Get words by category

### Scores
- `POST /api/scores` - Save game score

## Usage Guide

### For Administrators

1. **Access Admin Dashboard**
   - Click "Admin" in the navigation bar
   - View statistics and recent activity

2. **Add a New Player**
   - Go to Admin > Players > Add New Player
   - Fill in username, email, and full name
   - Click "Add Player"

3. **Add a New Word**
   - Go to Admin > Words > Add New Word
   - Enter the word and select category
   - Fill in relevant fields based on game mode
   - Click "Add Word"

4. **Edit Existing Data**
   - Navigate to Players or Words list
   - Click "Edit" button on desired entry
   - Modify information
   - Click "Update"

### For Players

1. **Choose a Game Mode**
   - Click "Play" in the navigation
   - Select one of 7 available game modes

2. **Play the Game**
   - View words and challenges
   - Use hints if needed
   - Check answers to learn

3. **View Leaderboard**
   - Click "Leaderboard" in navigation
   - See top players and rankings

## Sample Data

The `init_db.py` script creates sample data including:
- 5 sample players
- 20+ sample words across all game modes

## Development

### Adding New Features
1. Update models in `app/models.py` if needed
2. Add routes in `app/routes.py`
3. Create templates in appropriate folder
4. Run migrations if database schema changed

### Database Migrations
```bash
# Initialize migrations (first time only)
flask db init

# Create a migration
flask db migrate -m "Description of changes"

# Apply migration
flask db upgrade
```

## Configuration

Environment variables can be set in a `.env` file:
```
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///word_game.db
```

## Troubleshooting

### Common Issues

1. **Module not found errors**
   - Make sure virtual environment is activated
   - Run `pip install -r requirements.txt`

2. **Database errors**
   - Delete `word_game.db` file
   - Run `python init_db.py` again

3. **Port already in use**
   - Change port in `run.py`
   - Or kill process using port 5000

## Future Enhancements

- User authentication and authorization
- Real-time gameplay with scoring
- Multiplayer challenges
- More game modes
- Mobile app version
- Advanced statistics and analytics
- Word difficulty ratings
- Time-based challenges
- Achievement system

## Credits

Made by Jacob Rosner
2025

## License

This project is for educational purposes.

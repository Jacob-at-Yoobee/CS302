        // Switch between tabs
        function switchTab(tabName) {
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

            event.target.classList.add('active');
            document.getElementById(tabName + '-tab').classList.add('active');

            if (tabName === 'players') loadPlayers();
            if (tabName === 'words') loadWords();
        }

        // Show message
        function showMessage(text, type) {
            const msg = document.getElementById('message');
            msg.textContent = text;
            msg.className = 'message ' + type;
            msg.style.display = 'block';
            setTimeout(() => msg.style.display = 'none', 4000);
        }

        // ============== PLAYERS ==============

        // Load all players
        async function loadPlayers() {
            try {
                const response = await fetch('/api/players');
                const players = await response.json();
                const tbody = document.getElementById('players-tbody');

                if (players.length === 0) {
                    tbody.innerHTML = '<tr><td colspan="11" style="text-align: center;">No players found</td></tr>';
                    return;
                }

                tbody.innerHTML = players.map(p => `
                    <tr>
                        <td>${p.id}</td>
                        <td>${p.username}</td>
                        <td>${p.Slang}</td>
                        <td>${p.RhymeTime}</td>
                        <td>${p.Translate}</td>
                        <td>${p.Contextual}</td>
                        <td>${p.Chain}</td>
                        <td>${p.Opposites}</td>
                        <td>${p.AlphaThon}</td>
                        <td>${p.Average.toFixed(1)}</td>
                        <td class="action-buttons">
                            <button class="btn btn-warning" onclick="editPlayer(${p.id})">Edit</button>
                            <button class="btn btn-danger" onclick="deletePlayer(${p.id})">Delete</button>
                        </td>
                    </tr>
                `).join('');
            } catch (error) {
                showMessage('Error loading players: ' + error.message, 'error');
            }
        }

        // Add new player
        document.getElementById('player-form').addEventListener('submit', async (e) => {
            e.preventDefault();

            const data = {
                username: document.getElementById('player-username').value,
                Slang: document.getElementById('player-slang').value,
                RhymeTime: document.getElementById('player-rhyme').value,
                Translate: document.getElementById('player-translate').value,
                Contextual: document.getElementById('player-contextual').value,
                Chain: document.getElementById('player-chain').value,
                Opposites: document.getElementById('player-opposites').value,
                AlphaThon: document.getElementById('player-alpha').value
            };

            try {
                const response = await fetch('/api/players', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });

                if (response.ok) {
                    showMessage('Player added successfully!', 'success');
                    e.target.reset();
                    loadPlayers();
                } else {
                    const error = await response.json();
                    showMessage('Error: ' + error.error, 'error');
                }
            } catch (error) {
                showMessage('Error: ' + error.message, 'error');
            }
        });

        // Edit word
        async function editWord(id) {
            const newWord = prompt('Enter new word (or leave blank to keep):');
            if (newWord === null) return;

            const data = {};
            if (newWord) data.word = newWord;

            try {
                const response = await fetch(`/api/words/${id}`, {
                    method: 'PUT',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(data)
                });

                if (response.ok) {
                    showMessage('Word updated successfully!', 'success');
                    loadWords();
                } else {
                    const error = await response.json();
                    showMessage('Error: ' + error.error, 'error');
                }
            } catch (error) {
                showMessage('Error: ' + error.message, 'error');
            }
        }

        // Delete word
        async function deleteWord(id) {
            if (!confirm('Are you sure you want to delete this word?')) return;

            try {
                const response = await fetch(`/api/words/${id}`, {
                    method: 'DELETE'
                });

                if (response.ok) {
                    showMessage('Word deleted successfully!', 'success');
                    loadWords();
                } else {
                    const error = await response.json();
                    showMessage('Error: ' + error.error, 'error');
                }
            } catch (error) {
                showMessage('Error: ' + error.message, 'error');
            }
        }

        // Load players on page load
        loadPlayers();
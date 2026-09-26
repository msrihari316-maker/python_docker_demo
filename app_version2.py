from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Couple Games Hub 💕</title>
    <style>
        :root {
            --bg-color: #faf7f8;
            --card-bg: #ffffff;
            --accent-color: #e85a71;
            --text-color: #2b2b2b;
            --subtext-color: #7d7d7d;
            --border-color: #f0e6e8;
            --radius: 16px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            width: 100%;
            max-width: 500px;
            background: var(--card-bg);
            border-radius: var(--radius);
            box-shadow: 0 10px 30px rgba(0,0,0,0.04);
            border: 1px solid var(--border-color);
            padding: 24px;
        }

        header {
            text-align: center;
            margin-bottom: 24px;
        }

        header h1 {
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--accent-color);
        }

        header p {
            font-size: 0.875rem;
            color: var(--subtext-color);
            margin-top: 4px;
        }

        /* Navigation / Menu Tabs */
        .game-menu {
            display: flex;
            gap: 8px;
            background: var(--bg-color);
            padding: 4px;
            border-radius: 12px;
            margin-bottom: 24px;
        }

        .menu-btn {
            flex: 1;
            border: none;
            background: transparent;
            padding: 8px 12px;
            font-size: 0.85rem;
            font-weight: 500;
            color: var(--subtext-color);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .menu-btn.active {
            background: var(--card-bg);
            color: var(--accent-color);
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        /* Game Sections */
        .game-section {
            display: none;
            animation: fadeIn 0.3s ease-in-out;
        }

        .game-section.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Common Button Styles */
        .btn {
            display: inline-block;
            width: 100%;
            background: var(--accent-color);
            color: white;
            border: none;
            padding: 12px;
            border-radius: 10px;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            transition: opacity 0.2s ease;
            text-align: center;
            margin-top: 12px;
        }

        .btn:hover {
            opacity: 0.9;
        }

        .btn-outline {
            background: transparent;
            color: var(--text-color);
            border: 1px solid var(--border-color);
        }

        /* Game 1: Tic-Tac-Toe */
        .board {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-top: 16px;
        }

        .cell {
            aspect-ratio: 1;
            background: var(--bg-color);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            cursor: pointer;
            user-select: none;
        }

        .status {
            text-align: center;
            font-size: 0.95rem;
            font-weight: 500;
            margin-bottom: 8px;
        }

        /* Game 2: Would You Rather */
        .option-card {
            background: var(--bg-color);
            border: 1px solid var(--border-color);
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 12px;
            text-align: center;
            font-weight: 500;
            font-size: 0.95rem;
            cursor: pointer;
            transition: border-color 0.2s ease;
        }

        .option-card:hover {
            border-color: var(--accent-color);
        }

        /* Game 3: Compliment Generator */
        .card-display {
            background: var(--bg-color);
            border: 1px dashed var(--accent-color);
            border-radius: 12px;
            padding: 32px 16px;
            text-align: center;
            font-size: 1rem;
            font-weight: 500;
            min-height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 12px;
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>Couple Games</h1>
            <p>Pick a game and play together 💕</p>
        </header>

        <nav class="game-menu">
            <button class="menu-btn active" onclick="switchGame('tictactoe')">Tic-Tac-Toe</button>
            <button class="menu-btn" onclick="switchGame('wyr')">Would You Rather</button>
            <button class="menu-btn" onclick="switchGame('deck')">Love Deck</button>
        </nav>

        <!-- GAME 1: TIC TAC TOE -->
        <section id="tictactoe" class="game-section active">
            <div id="ttt-status" class="status">Turn: ❤️ Player 1</div>
            <div class="board">
                <div class="cell" onclick="makeMove(this, 0)"></div>
                <div class="cell" onclick="makeMove(this, 1)"></div>
                <div class="cell" onclick="makeMove(this, 2)"></div>
                <div class="cell" onclick="makeMove(this, 3)"></div>
                <div class="cell" onclick="makeMove(this, 4)"></div>
                <div class="cell" onclick="makeMove(this, 5)"></div>
                <div class="cell" onclick="makeMove(this, 6)"></div>
                <div class="cell" onclick="makeMove(this, 7)"></div>
                <div class="cell" onclick="makeMove(this, 8)"></div>
            </div>
            <button class="btn btn-outline" onclick="resetTTT()">Restart Game</button>
        </section>

        <!-- GAME 2: WOULD YOU RATHER -->
        <section id="wyr" class="game-section">
            <div class="status">Would You Rather...</div>
            <div id="wyr-opt1" class="option-card" onclick="nextWYR()">Option 1</div>
            <div style="text-align: center; margin-bottom: 12px; font-size: 0.8rem; color: var(--subtext-color);">OR</div>
            <div id="wyr-opt2" class="option-card" onclick="nextWYR()">Option 2</div>
            <button class="btn btn-outline" onclick="nextWYR()">Next Question ➔</button>
        </section>

        <!-- GAME 3: LOVE DECK -->
        <section id="deck" class="game-section">
            <div id="deck-display" class="card-display">Click below to draw a card ✨</div>
            <button class="btn" onclick="drawCard()">Draw a Card 💖</button>
        </section>
    </div>

    <script>
        // Tab Navigation
        function switchGame(gameId) {
            document.querySelectorAll('.game-section').forEach(sec => sec.classList.remove('active'));
            document.querySelectorAll('.menu-btn').forEach(btn => btn.classList.remove('active'));
            
            document.getElementById(gameId).classList.add('active');
            event.target.classList.add('active');
        }

        // --- Game 1: Tic-Tac-Toe Logic ---
        let board = ["", "", "", "", "", "", "", "", ""];
        let currentPlayer = "❤️";
        let gameActive = true;

        const winPatterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ];

        function makeMove(cell, index) {
            if (board[index] !== "" || !gameActive) return;

            board[index] = currentPlayer;
            cell.innerText = currentPlayer;

            if (checkWin()) {
                document.getElementById('ttt-status').innerText = `Winner: ${currentPlayer} 🎉`;
                gameActive = false;
                return;
            }

            if (!board.includes("")) {
                document.getElementById('ttt-status').innerText = "It's a draw! 🤝";
                gameActive = false;
                return;
            }

            currentPlayer = currentPlayer === "❤️" ? "🌹" : "❤️";
            document.getElementById('ttt-status').innerText = `Turn: ${currentPlayer}`;
        }

        function checkWin() {
            return winPatterns.some(pattern => {
                return pattern.every(index => board[index] === currentPlayer);
            });
        }

        function resetTTT() {
            board = ["", "", "", "", "", "", "", "", ""];
            currentPlayer = "❤️";
            gameActive = true;
            document.getElementById('ttt-status').innerText = "Turn: ❤️ Player 1";
            document.querySelectorAll('.cell').forEach(cell => cell.innerText = "");
        }

        // --- Game 2: Would You Rather Logic ---
        const wyrQuestions = [
            ["Go on a spontaneous road trip", "Stay in with takeout and movies"],
            ["Always have to cook together", "Always have to do the dishes together"],
            ["Explore a new city together", "Relax on a quiet beach together"],
            ["Relive our very first date", "Fast forward to a dream vacation in 5 years"],
            ["Cook a 3-course meal from scratch", "Order from 3 different restaurants"]
        ];
        let wyrIndex = 0;

        function renderWYR() {
            const pair = wyrQuestions[wyrIndex];
            document.getElementById('wyr-opt1').innerText = pair[0];
            document.getElementById('wyr-opt2').innerText = pair[1];
        }

        function nextWYR() {
            wyrIndex = (wyrIndex + 1) % wyrQuestions.length;
            renderWYR();
        }

        renderWYR();

        // --- Game 3: Love Deck Logic ---
        const deckCards = [
            "Tell me about a moment when you realized you liked me.",
            "What is your favorite memory of us together?",
            "Compliment one thing you love about my personality.",
            "What is one small thing I do that makes you smile?",
            "Name a song that reminds you of us.",
            "What is a dream trip you want us to take together?"
        ];

        function drawCard() {
            const randomIndex = Math.floor(Math.random() * deckCards.length);
            document.getElementById('deck-display').innerText = deckCards[randomIndex];
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

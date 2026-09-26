from flask import Flask, render_template_string

app = Flask(__name__)

# Single HTML template with CSS/JS built-in
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Special Surprise ❤️</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
            color: #333;
        }

        .card {
            background: rgba(255, 255, 255, 0.9);
            padding: 40px 30px;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
            text-align: center;
            max-width: 400px;
            width: 90%;
            z-index: 10;
            position: relative;
        }

        h1 {
            color: #ff4b2b;
            font-size: 2rem;
            margin-bottom: 10px;
        }

        p {
            font-size: 1.1rem;
            color: #555;
            line-height: 1.5;
        }

        .btn {
            background: linear-gradient(to right, #ff416c, #ff4b2b);
            color: white;
            border: none;
            padding: 12px 28px;
            font-size: 1rem;
            font-weight: bold;
            border-radius: 25px;
            cursor: pointer;
            margin-top: 20px;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 5px 15px rgba(255, 75, 43, 0.4);
        }

        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 20px rgba(255, 75, 43, 0.6);
        }

        .hidden-message {
            display: none;
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            animation: fadeIn 1s ease-in-out forwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Floating Hearts Animation */
        .heart {
            position: absolute;
            color: #ff4b2b;
            font-size: 20px;
            animation: floatUp 4s linear infinite;
            bottom: -50px;
            z-index: 1;
        }

        @keyframes floatUp {
            0% { transform: translateY(0) rotate(0deg); opacity: 1; }
            100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
        }
    </style>
</head>
<body>

    <div class="card">
        <h1>Hey Beautiful 💕</h1>
        <p>I built this little app just to remind you how extra special you are to me!</p>

        <button class="btn" onclick="revealSurprise()">Click For Your Surprise ✨</button>

        <div id="surprise" class="hidden-message">
            <h2>💖 I Love You! 💖</h2>
            <p>Thank you for bringing so much joy into my life. Every single day with you is a gift!</p>
        </div>
    </div>

    <script>
        function revealSurprise() {
            document.getElementById('surprise').style.display = 'block';
            createHearts();
        }

        function createHearts() {
            for(let i = 0; i < 30; i++) {
                setTimeout(() => {
                    const heart = document.createElement('div');
                    heart.classList.add('heart');
                    heart.innerHTML = '❤️';
                    heart.style.left = Math.random() * 100 + 'vw';
                    heart.style.animationDuration = (Math.random() * 2 + 3) + 's';
                    heart.style.fontSize = (Math.random() * 20 + 15) + 'px';
                    document.body.appendChild(heart);

                    setTimeout(() => heart.remove(), 4000);
                }, i * 150);
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

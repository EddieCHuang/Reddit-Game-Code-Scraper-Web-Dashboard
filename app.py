from flask import Flask, render_template, json
from markupsafe import Markup
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "multi_game_codes.json")


app = Flask(__name__)

# Optional filter to convert newlines to <br>
@app.template_filter('nl2br')
def nl2br_filter(s):
    if not s:
        return ""
    return Markup(s.replace('\n', '<br>\n'))

@app.route("/")
def index():
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            results_list = json.load(f)
            print("Loaded results:", results_list)  # Debug print
    except FileNotFoundError:
        results_list = []
        print("JSON file not found")

    # Group list entries by 'game'
    grouped_results = {}
    for entry in results_list:
        game = entry.get("game", "Unknown Game")
        grouped_results.setdefault(game, []).append(entry)

    return render_template("index.html", results=grouped_results)




if __name__ == "__main__":
    app.run(debug=True)

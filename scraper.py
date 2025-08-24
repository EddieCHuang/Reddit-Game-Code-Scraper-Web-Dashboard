import praw
import re
import json
from dateutil import parser as date_parser
from datetime import datetime
from dotenv import load_dotenv
import os

# SET YOUR REDDIT API CREDENTIALS HERE
reddit = praw.Reddit(
    client_id="*****", 
    client_secret="****",
    user_agent="****"

)


script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "multi_game_codes.json")

expiration_patterns = [
    r'expires?\s+on\s+([A-Za-z0-9,/\- ]+)',
    r'valid\s+until\s+([A-Za-z0-9,/\- ]+)',
    r'expires?\s+([A-Za-z0-9,/\- ]+)',  
]

games = [
    {
        "name": "Genshin Impact",
        "reddit_user": "GenshinImpact",
        "keywords": ["redeem", "redemption code", "gift code"],
        "logo_url": "https://upload.wikimedia.org/wikipedia/en/1/1e/Genshin_Impact_logo.svg"
    },
    {
        "name": "Honkai Star Rail",
        "reddit_user": "HonkaiStarRail",
        "keywords": ["redeem", "redemption code", "winner"],
        "logo_url": "https://upload.wikimedia.org/wikipedia/en/1/1e/Genshin_Impact_logo.svg"
    },

    # Add more games here
]



all_matches = []

# Loop through each game
for game in games:
    user = reddit.redditor(game["reddit_user"])
    comments = user.comments.new(limit=50)

    for comment in comments:
        if not hasattr(comment, "body"):
            continue

        body = comment.body
        body_lower = body.lower()

        # seach for keywords
        if any(keyword in body_lower for keyword in game["keywords"]):
            expire_date = None

            # extract expiration date
            for pattern in expiration_patterns:
                match = re.search(pattern, body_lower)
                if match:
                    try:
                        expire_date = date_parser.parse(match.group(1), fuzzy=True)
                        break
                    except:
                        continue

            # Save only if a valid (and unexpired)
            if expire_date and expire_date <= datetime.now():
                all_matches.append({
                    "game": game["name"],
                    "full_comment": body,
                    "source": f"https://reddit.com{comment.permalink}",
                    "expire_date": expire_date.strftime('%Y-%m-%d'),
                    "logo_url": game["logo_url"]
                })



# Save all matach result
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_matches, f, indent=2, ensure_ascii=False)


print(" Done! Found", len(all_matches), "matching comments.")
for entry in all_matches:
    print(f"[{entry['game']}] {entry['source']}")

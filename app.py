import os
from flask import Flask, jsonify
from tweety import Twitter
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://petertechdev.github.io/"}})

twitter_session_id = os.getenv("TWITTER_SESSION_ID")

# Check if the session ID is properly loaded
if not twitter_session_id:
    raise ValueError("TWITTER_SESSION_ID is not set. Please check your environment variables.")

twitter_app = Twitter(twitter_session_id)

@app.route('/api/tweets/<username>', methods=['GET'])
def get_tweets(username):
    try:
        all_tweets = twitter_app.get_tweets(username, pages=1)
        tweet_ids = [tweet.id for tweet in all_tweets[:5]]
        return jsonify(tweet_ids)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

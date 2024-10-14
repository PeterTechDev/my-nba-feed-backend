from flask import Flask, jsonify
from tweety import Twitter
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Get the Twitter session ID from the environment variable
twitter_session_id = os.getenv("TWITTER_SESSION_ID")
twitter_app = Twitter(twitter_session_id)

@app.route('/api/tweets/<username>', methods=['GET'])
def get_tweets(username):
    try:
        # Get tweets from the user's account (e.g., 'celtics')
        all_tweets = twitter_app.get_tweets(username, pages=1)
        tweet_ids = [tweet.id for tweet in all_tweets[:5]]  # Get the last 5 tweet IDs
        return jsonify(tweet_ids)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

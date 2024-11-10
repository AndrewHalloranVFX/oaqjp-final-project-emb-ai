"""
Server for Emotion Detection
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_detector():

    """
    Endpoint for detecting emotions in text.
    Takes a text input from user and returns a JSON response
    with emotion scores and the dominant emotion
    """

    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze:
        return jsonify({"error": "Invalid Text! Please Try Again"}), 400

    emotions = emotion_detector(text_to_analyze)
    return jsonify(emotions)

@app.route("/")
def render_index_page():

    """
    Renders Index Page
    """

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

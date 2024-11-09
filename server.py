from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_detector():
    
    text_to_analyze = request.args.get("textToAnalyze", "")

    emotions = emotion_detector(text_to_analyze)

    return jsonify(emotions)

    if not text_to_analyze:
        return jsonify({"error": "Invalid Text! Please Try Again"}), 400

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""
Flask application for emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("My Emotion")

@app.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    """
    Handle emotion detection for the given text.
    """
    txt = request.args.get('textToAnalyze')
    response = emotion_detector(txt)

    # Handle API failure case
    if response['anger'] is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement,the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is"
        f"{response['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

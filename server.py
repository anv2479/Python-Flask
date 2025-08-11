import json
from flask import Flask, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def show_emotion_detector():
    statement = request.args.get("textToAnalyze")
    resp = emotion_detector(statement)

    if resp['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return_string = "For the given statement, the system response is" \
     f" 'anger': {resp['anger']}, 'disgust': {resp['disgust']}, " \
     f"'fear': {resp['fear']}, 'joy': {resp['joy']} and 'sadness': {resp['sadness']}." \
     f" The dominant emotion is {resp['dominant_emotion']}."
    return return_string

@app.route("/") 
def render_index_page(): 
    return render_template('index.html') 

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000) 

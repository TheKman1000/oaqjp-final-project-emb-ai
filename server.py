from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emote_detector():
    # Retrieve text to analyze from the query parameter
    textToAnalyze = request.args.get('textToAnalyze')

    # Call the emotion detector
    response = emotion_detector(textToAnalyze)

    # If the detector returned None values (e.g., blank / invalid text),
    # dominant_emotion will be None based on our error handling.
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract values from response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Return formatted string
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )
    
@app.route('/')
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
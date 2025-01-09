from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def get_emotion_detector():
    text_to_analyse = request.args.get('textToAnalyze')

    if text_to_analyse is None or text_to_analyse == '':
        return "Invalid input"

    result = emotion_detector(text_to_analyse)

    if result is None:
        return "Invalid input"

    response = (f"For the given statement, the system response is \'anger\': {result['anger']}, "
                f"\'disgust\': {result['disgust']}, \'fear\': {result['fear']}, "
                f"\'joy\': {result['joy']}, and \'sadness\': {result['sadness']}. "
                f"The dominant emotion is <b>{result['dominant_emotion']}</b>.")

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

"""
This is the server module for the Flask application that handles emotion detection.

This module contains the Flask routes and views for the web application. It exposes 
a route to render the home page and a route for detecting emotions from text input 
using the Watson emotion detection API.

Routes:
    - /: Displays the home page (index.html)
    - /emotionDetector: Accepts a GET request with a text query parameter and 
      returns the detected emotions as a JSON response.

Dependencies:
    - Flask: A lightweight web framework for Python
    - EmotionDetection.emotion_detection: A custom module for emotion analysis
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Route for the home page of the web application.
    
    This function renders the 'index.html' template when the home page is accessed.
    
    Returns:
        str: The rendered HTML page of the home route.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def get_emotion_detector():
    """
    Route that handles GET requests to detect emotions in a given text.
    
    This function takes a text input via the query parameter 'textToAnalyze', passes
    it to the `emotion_detector` function, and returns a JSON response with the detected
    emotions and the dominant emotion.
    
    Args:
        None (retrieves text from the query string using 'textToAnalyze' parameter)
    
    Returns:
        Response: A JSON response containing the emotion analysis results or an error message.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (f"For the given statement, the system response is \'anger\': {result['anger']}, "
                f"\'disgust\': {result['disgust']}, \'fear\': {result['fear']}, "
                f"\'joy\': {result['joy']}, and \'sadness\': {result['sadness']}. "
                f"The dominant emotion is <b>{result['dominant_emotion']}</b>.")

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

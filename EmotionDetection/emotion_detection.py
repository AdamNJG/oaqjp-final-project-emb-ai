import requests
import json

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotional tone of a given text using IBM Watson's Emotion API.

    This function sends a POST request to the Watson Emotion service to get 
    emotion predictions for the provided text. It returns a dictionary containing
    the intensity scores for different emotions (anger, disgust, fear, joy, sadness)
    and identifies the dominant emotion with the highest score.

    Args:
        text_to_analyse (str): The text that you want to analyze for emotional tone.

    Returns:
        dict or None: A dictionary containing the emotional scores for 'anger', 'disgust', 
        'fear', 'joy', 'sadness', and the 'dominant_emotion' (the emotion with the highest 
        score), or None if no emotion predictions are found in the response.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = body, headers=headers)

    if response.status_code == 400:
        return {
                'anger' : None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

    jsonResponse = json.loads(response.text)
    emotion = jsonResponse['emotionPredictions'][0]['emotion']
    return {
        'anger' : emotion['anger'],
        'disgust': emotion['disgust'],
        'fear': emotion['fear'],
        'joy': emotion['joy'],
        'sadness': emotion['sadness'],
        'dominant_emotion': max(emotion, key=emotion.get)
    }

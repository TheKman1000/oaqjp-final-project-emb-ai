import requests
import json

def emotion_detector(textToAnalyze):
        # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = { "raw_document": { "text": textToAnalyze } }                            # Create a dictionary with the text to be analysed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}     # Set the headers required for the API request
    response = requests.post(url, json=input_json, headers=header)                          # Send a POST request to the API with text and headers
    
        # --- Error handling for blank/invalid input ---
    if response.status_code == 400:
        # Return the same keys, but all values are None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)                                          # Parse the JSON response from the API
        # Extract sentiment scores separately from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    joy_score = emotions['joy']
    fear_score = emotions['fear']
    sadness_score = emotions['sadness']
    disgust_score = emotions['disgust']
    dict_emotion = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score}
    dom_emotion = max(dict_emotion, key=dict_emotion.get)
        # Return dictionary of responses from the API
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dom_emotion}
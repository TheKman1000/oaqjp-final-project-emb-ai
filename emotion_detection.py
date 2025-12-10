import requests

def emotion_detector(text_to_analyse):
        # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        # Create a dictionary with the text to be analysed
    input_json = { "raw_document": { "text": text_to_analyse } }
        # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        # Send a POST request to the API with text and headers
    response = requests.post(url, json=input_json, headers=header)
        # Return the response text from the API
    return response.text
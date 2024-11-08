import requests
import json

def emotion_detector(text_to_analyse):
   
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=input_json)

    return response.text

    response.dict = response.json()

    emotions = {}
    if "emotion_scores" in response_dict:
        emotions_data = response_dict["emotion_scores"]
        emotions = {
            "anger": emotions_data.get("anger", 0),
            "disgust": emotions_data.get("disgust", 0),
            "fear": emotions_data.get("fear", 0),
            "joy": emotions_data.get("joy", 0),
            "sadness": emotions_data.get("sadness", 0),
            "dominant_emotion": "joy"
        }
    return emotions


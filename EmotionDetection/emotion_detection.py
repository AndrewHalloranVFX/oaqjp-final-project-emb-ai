import requests
import json

def emotion_detector(text_to_analyse):
   
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
   
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
   
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=input_json)

    #return response.text

    response_dict = response.json()

        # Ensure the expected structure is present
    if ("emotionPredictions" in response_dict and
            len(response_dict["emotionPredictions"]) > 0 and
            "emotion" in response_dict["emotionPredictions"][0]):
        
        # Extract emotion scores
        emotion_scores = response_dict["emotionPredictions"][0]["emotion"]

        # Find the dominant emotion by the highest score
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the formatted dictionary
        return {
            'anger': emotion_scores.get('anger', 0),
            'disgust': emotion_scores.get('disgust', 0),
            'fear': emotion_scores.get('fear', 0),
            'joy': emotion_scores.get('joy', 0),
            'sadness': emotion_scores.get('sadness', 0),
            'dominant_emotion': dominant_emotion
        }
    else:
        # If the expected structure is missing, return an error or empty response
        return {
            'anger': 0,
            'disgust': 0,
            'fear': 0,
            'joy': 0,
            'sadness': 0,
            'dominant_emotion': 'unknown'
        }

    """emotions = {}
    if "emotion_scores" in response_dict:
        emotions_data = response_dict["emotion_scores"]
        emotions = {
            "anger": emotions_data.get("anger", 0),
            "disgust": emotions_data.get("disgust", 0),
            "fear": emotions_data.get("fear", 0),
            "joy": emotions_data.get("joy", 0),
            "sadness": emotions_data.get("sadness", 0),
            "dominant_emotion": dominant_emotion
        }
    return emotions"""

    """
    #Extracting emotion score
    if "emotionPredictions" in response_dict:
        emotions = response_dict["emotionPredictions"][0]["emotion"]

        #Find emotion with highest score
        dominant_emotion = max(emotions, key=emotions.get)

        return dominant_emotion #Return only the dominant emotion as a string

    #Fallback if expected structure is not present
    return None
    """


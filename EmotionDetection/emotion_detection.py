import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 400:
        # Return dictionary with None values for blank entries or bad request
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}: {response.text}")

    # Extract the emotions
    response_json = response.json()
    emotion_scores = response_json['emotionPredictions'][0]['emotion']

    # Extract only the required emotions
    anger = emotion_scores.get('anger', 0)
    disgust = emotion_scores.get('disgust', 0)
    fear = emotion_scores.get('fear', 0)
    joy = emotion_scores.get('joy', 0)
    sadness = emotion_scores.get('sadness', 0)

    # Determine dominant emotion
    emotion_dict = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    # Return result in required format
    emotion_dict['dominant_emotion'] = dominant_emotion
    return emotion_dict
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
import os

authenticator = IAMAuthenticator(os.getenv('WATSON_API_KEY'))
nlu = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)
nlu.set_service_url(os.getenv('WATSON_URL'))

def detect_emotion(text: str) -> dict:
    try:
        response = nlu.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        return response['emotion']['document']['emotion']
    except Exception as e:
        return {"error": str(e)}

def format_emotion_output(emotion_dict: dict) -> str:
    if "error" in emotion_dict:
        return f"Error: {emotion_dict['error']}"
    return "\n".join([f"{emotion.capitalize()}: {score:.2f}" for emotion, score in emotion_dict.items()])

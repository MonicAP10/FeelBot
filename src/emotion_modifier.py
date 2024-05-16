import random
from lambda_handler import modify_emotions_in_lambda

def modify_emotions(emotions):
    """
    Modifica las emociones utilizando un servicio Lambda.
    """
    data = {
        "function": "increase_emotion_and_find_extremes(",
        "positive_emotions": {k: v for k, v in emotions.items() if v > 0},
        "negative_emotions": {k: v for k, v in emotions.items() if v < 0},
        "to_modify": list(emotions.keys()),
        "percentage": random.randint(1, 100)
    }
    modify_emotions_in_lambda(data)

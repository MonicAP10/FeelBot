import random
from lambda_handler import modify_emotions_in_lambda

def modify_emotions(emotions):

    emotions = {emotion: value for emotion, value in emotions.items()}
    positive_emotions = {emotion: value for emotion, value in emotions.items() if value > 0}
    negative_emotions = {emotion: value for emotion, value in emotions.items() if value < 0}
    """
    Modifica las emociones utilizando un servicio Lambda.
    """
    data = {
        "function": "increase_emotion",
        "positive_emotions": positive_emotions,
        "negative_emotions": negative_emotions,
        "to_modify": list(emotions.keys()),
        "percentage": random.randint(1, 100)
    }

    modify_emotions_in_lambda(data)

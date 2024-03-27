import re

def extract_emotions(response_content):
    """
    Extrae las emociones del texto de respuesta.
    """
    pattern = r"- (\w+): (-?\d+\.\d+)"
    matches = re.findall(pattern, response_content)
    return {emotion: float(num) for emotion, num in matches}

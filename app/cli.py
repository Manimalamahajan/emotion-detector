import sys
from app.emotion_detector import detect_emotion, format_emotion_output

def main():
    text = " ".join(sys.argv[1:])
    emotions = detect_emotion(text)
    print(format_emotion_output(emotions))

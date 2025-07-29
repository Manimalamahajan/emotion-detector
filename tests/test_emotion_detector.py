from app.emotion_detector import format_emotion_output

def test_format_output():
    sample = {"joy": 0.7, "sadness": 0.1, "anger": 0.05, "disgust": 0.05, "fear": 0.1}
    output = format_emotion_output(sample)
    assert "Joy: 0.70" in output

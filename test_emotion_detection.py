import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        r1=emotion_detector("I am glad this happened")
        self.assertEqual(r1['dominant_emotion'], "joy")

        r1=emotion_detector("I am really mad about this")
        self.assertEqual(r1['dominant_emotion'], "anger")

        r1=emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(r1['dominant_emotion'], "disgust")

        r1=emotion_detector("I am so sad about this	")
        self.assertEqual(r1['dominant_emotion'], "sadness")

        r1=emotion_detector("I am really afraid that this will happen")
        self.assertEqual(r1['dominant_emotion'], "fear")

unittest.main()
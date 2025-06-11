import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def setUp(self):
        # This can be used if you want to set up any common data before tests
        pass

    def test_emotions(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected_dominant in test_cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                dominant = result.get('dominant_emotion')
                self.assertEqual(dominant, expected_dominant, 
                    f"For input '{text}', expected dominant emotion '{expected_dominant}' but got '{dominant}'")

if __name__ == '__main__':
    unittest.main()

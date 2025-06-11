import os
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'oaqjp-final-project-emb-ai', 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'oaqjp-final-project-emb-ai', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/', methods=['GET'])
def home():
    # render the index.html template
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    # Get the text from form
    user_text = request.form.get('text')

    if not user_text:
        # Return error message and 400 status code as a tuple
        return "Please provide text to analyze", 400

    try:
        result = emotion_detector(user_text)
    except Exception as err:  # Broad exception caught to handle unexpected errors
        return f"Error processing emotion detection: {str(err)}", 500

    # result might be a tuple (message, status_code) when error occurs,
    # so check if it's a dict before proceeding
    if not isinstance(result, dict):
        # Assume invalid input case, just return result as is
        return result

    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!", 400

    emotions = {k: v for k, v in result.items() if k != 'dominant_emotion'}
    dominant = result.get('dominant_emotion')

    emotions_str = ', '.join([f"'{k}': {v}" for k, v in emotions.items()])

    response_text = (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is {dominant}."
    )

    return response_text


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
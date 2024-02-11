
# Python script for sentiment analysis using NLTK or other NLP libraries
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer
def analyze_sentiment(text):
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    return sentiment_score

print(analyze_sentiment("i hate you"))

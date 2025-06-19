import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def get_news_sentiment(query, api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&pageSize=10&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])

    sentiments = []
    for article in articles:
        score = analyzer.polarity_scores(article["title"])
        sentiments.append(score["compound"])

    if sentiments:
        avg_score = sum(sentiments) / len(sentiments)
        return avg_score
    return 0

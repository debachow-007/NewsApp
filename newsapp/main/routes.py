from flask import Blueprint, render_template, request, current_app
import requests


main = Blueprint('main', __name__)

@main.route('/')
def index():
    query = request.args.get("query", "latest")
    NEWS_API_KEY = current_app.config["NEWS_API_KEY"]
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news = response.json()
    
    articles = news.get("articles", [])
    
    filtered_articles = [article for article in articles if "Yahoo" not in article["source"]["name"] and "removed" not in article["title"].lower()]
    
    return render_template("index.html", articles=filtered_articles, query=query)

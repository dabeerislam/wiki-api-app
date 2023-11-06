from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Wikipedia API URL
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

# Define your endpoint
@app.route('/pageview')
def get_pageview_count():
    article_title = request.args.get('article_title')
    year = request.args.get('year')
    month = request.args.get('month')

    if not article_title or not year or not month:
        return jsonify({"error": "Please provide article_title, year, and month."})

    # Define parameters for the Wikipedia API request
    params = {
        "action": "query",
        "format": "json",
        "prop": "pageviews",
        "titles": article_title,
        "pvipdays": month,
        "pvipmetric": "unique-devices",
        "pvipdays": 1,
        "pviprange": f"{year}{month}01-{year}{month}31"
    }

    # Make a request to Wikipedia API
    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()
    
    # Extract view count
    page_id = list(data['query']['pages'].keys())[0]
    view_count = data['query']['pages'][page_id]['pageviews'].get(f"{year}{month}01", 0)

    return jsonify({"article_title": article_title, "year": year, "month": month, "view_count": view_count})

if __name__ == '__main__':
    app.run(debug=True)

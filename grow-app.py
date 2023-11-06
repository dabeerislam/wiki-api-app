from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Wikipedia API URL
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

# Define your endpoint
@app.route('/view_count', methods=['GET'])
def view_count():
    article_title = request.args.get('article_title')
    year = request.args.get('year')
    month = request.args.get('month')

    if not article_title or not year or not month:
        return jsonify({"error": "Please provide article_title, year, and month."})

    try:
        year = int(year)
        month = int(month)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid year or month format"})

    params = {
        "action": "query",
        "format": "json",
        "prop": "pageviews",
        "titles": article_title,
        "pvipmetric": "unique-devices",
        "pvipdays": f"{year}{month:02}01-{year}{month:02}31"
    }

    response = requests.get(WIKIPEDIA_API_URL, params=params)
    data = response.json()

    if 'query' in data:
        page_id = list(data['query']['pages'].keys())[0]
        page_views = data['query']['pages'][page_id]['pageviews']
        view_count = page_views.get(f"{year}{month:02}01", 0)

        response_data = {
            "article_title": article_title,
            "year": year,
            "month": month,
            "view_count": view_count
        }
        return jsonify(response_data)
    else:
        return jsonify({"error": "Failed to retrieve view count"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

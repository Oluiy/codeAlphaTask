from flask import Flask, request, redirect, jsonify
from models import create_table, insert_url, get_long_url
import string, random

app = Flask(__name__)
create_table()

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.hexdigits, k=9))

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    long_url = data['url']
    short = generate_short_url()
    insert_url(short, long_url)
    return jsonify({'short_url': f'http://localhost:5000/{short}'})

@app.route('/<short>')
def redirect_url(short):
    long_url = get_long_url(short)
    if long_url:
        return redirect(long_url)
    return 'URL not found', 404

@app.route('/')
def home():
    return "Welcome to the URL Shortener API. Use POST /shorten to shorten URLs."

if __name__ == '__main__':
    app.run(debug=True)

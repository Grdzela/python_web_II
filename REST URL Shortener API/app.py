from flask import Flask, render_template, request, redirect
import string
import random
import validators
import time

app = Flask(__name__)

urls = {}


def shorten_url():
    """Generate a random short URL"""
    while True:
        letters = string.ascii_letters + string.digits
        code = ''.join(random.choice(letters) for i in range(8))
        if code not in urls:
            return code


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/shorten", methods=["POST"])
def shorten():
    url = request.form["url"]
    custom_code = request.form.get("custom_code", "")

    # Validate URL
    if not validators.url(url) or len(url) > 250:
        return render_template('index.html', error="Invalid URL")

    # Check custom code
    if custom_code != "" and custom_code in urls:
        return render_template('index.html', error="Custom code already taken")

    # Generate a random short code
    if custom_code == "":
        short_code = shorten_url()
    else:
        short_code = custom_code

    # Add the URL
    urls[short_code] = {"url": url, "count": 0, "timestamp": time.time()}

    return render_template('success.html', short_url=request.host_url + short_code)


@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirect the short URL to the original URL"""
    if short_code in urls:
        urls[short_code]['count'] += 1
        return redirect(urls[short_code]['url'])
    else:
        return render_template('error.html')


if __name__ == "__main__":
    app.run(debug=True)

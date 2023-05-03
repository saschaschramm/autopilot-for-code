from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the Google Maps API key from the environment variable
    google_maps_api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    
    # Render the HTML template and pass the API key to it
    return render_template('index.html', google_maps_api_key=google_maps_api_key)

if __name__ == '__main__':
    # Start the Flask webserver on 0.0.0.0:8888
    app.run(host='0.0.0.0', port=8888)
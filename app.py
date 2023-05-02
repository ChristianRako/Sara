from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

# Define your asset bundles here
css_bundle = Bundle('css/style.scss', output='gen/main.css')

# Register your asset bundles with the environment
assets.register('css_all', css_bundle)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True, port=5002)
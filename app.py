from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route('/static/<path:filename>')
def serve_static(filename):
    """
    Serves static files from the 'static' folder.
    """
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
from flask import Flask, request
import logging
import os

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.route('/print', methods=['POST'])
def print_post_body():
    data = request.get_json()  # Get the JSON data from the request
    app.logger.info(f"Received data: {data}")  # Log the data
    return "Data printed successfully!", 200

@app.route('/logs', methods=['GET'])
def get_logs():
    if os.path.exists('app.log'):
        with open('app.log', 'r') as file:
            logs = file.read()
        return logs, 200
    else:
        return "No logs available.", 200

@app.route('/view-logs', methods=['GET'])
def view_logs():
    return app.send_static_file('logs.html')

if __name__ == '__main__':
    app.run(debug=True)

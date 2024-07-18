from flask import Flask, request

app = Flask(__name__)

@app.route('/print', methods=['POST'])
def print_post_body():
    data = request.get_json()  # Get the JSON data from the request
    print(data)  # Print the data to the console
    return "Data printed successfully!", 200

if __name__ == '__main__':
    app.run(debug=True)

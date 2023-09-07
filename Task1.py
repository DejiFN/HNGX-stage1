from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get the slack_name and track from the GET parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    
    # Get the current day of the week and UTC time
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    
    # Create the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/DejiFN/HNGX-stage1/blob/main/Task1.py",
        "github_repo_url": "https://github.com/DejiFN/HNGX-stage1",
        "status_code": 200
    }
    
    # Return the JSON response with a status code of 200
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)

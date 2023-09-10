from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api")
def home():
    import datetime
    import pytz
    import random
    import time

    # Get the current date
    current_date = datetime.date.today()
    # Format and print the current date as "MM/DD/YYYY"
    current_day = current_date.strftime("%A")

     # Get the current UTC time
    current_utc_time = datetime.datetime.now(pytz.utc)
    # Generate a random offset in seconds between -120 and 120 (2 minutes)
    offset_seconds = random.randint(-120, 120)
    # Apply the offset to the current time
    utc_time_with_offset = current_utc_time + datetime.timedelta(seconds=offset_seconds)
    utc_time = utc_time_with_offset.strftime("%Y-%m-%dT%H:%M:%SZ")


    data = {
        "slack_name": "example_name",
        "current_day": current_day,
        "utc_time": utc_time,
        "track": "backend",
        "github_file_url": "https://github.com/AghahowaJeffrey/hngx_stage1-backend/blob/master/main.py",
        "github_repo_url": "https://github.com/AghahowaJeffrey/hngx_stage1-backend",
        "status_code": 200
    }

    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    data["slack_name"] = slack_name
    data["track"] = track

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
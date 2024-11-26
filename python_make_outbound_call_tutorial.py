import freeclimb
from freeclimb.api import default_api
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
import json

load_dotenv()
account_id = os.environ.get("ACCOUNT_ID")
api_key = os.environ.get("API_KEY")
api_server = os.environ.get("API_SERVER", "https://www.freeclimb.com/apiserver")

YOUR_FREECLIMB_NUMBER = ""
YOUR_VERIFIED_NUMBER = ""
YOUR_APP_ID = ""

configuration = freeclimb.Configuration(
    host = api_server,
    username = account_id,
    password = api_key
)

api_instance = default_api.DefaultApi(freeclimb.ApiClient(configuration))

app = Flask(__name__)

# Make a request to this endpoint to trigger an outbound call
@app.route('/sendCall', methods=['POST'])
def sendCall():
    if request.method == 'POST':
        call_request = freeclimb.MakeCallRequest(
            _from=YOUR_FREECLIMB_NUMBER, to=YOUR_VERIFIED_NUMBER, application_id=YOUR_APP_ID)
        api_instance.make_a_call(make_call_request=call_request)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Specify this route with 'CALL CONNECT URL' in App Config
@app.route('/callConnect', methods=['POST'])
def callConnect():
    if request.method == 'POST':
        script = freeclimb.PerclScript(commands=[
            freeclimb.Say(text="Hello. Welcome to FreeClimb's outbound call tutorial."),
            freeclimb.Pause(length=1000),
            freeclimb.Say(text="Goodbye.")
        ])

        return script.to_json(), 200, {'ContentType': 'application/json'}

# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
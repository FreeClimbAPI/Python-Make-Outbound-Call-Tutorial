from __future__ import print_function
import time
import freeclimb
import os
import json
from flask import Flask, request
from freeclimb import percl_to_json

configuration = freeclimb.Configuration()
# Configure HTTP basic authorization: fc
configuration.username = os.environ['ACCOUNT_ID']
configuration.password = os.environ['AUTH_TOKEN']

# Defining host is optional and default to https://www.freeclimb.com/apiserver
configuration.host = "https://www.freeclimb.com/apiserver"
# Create an instance of the API class
api_instance = freeclimb.DefaultApi(freeclimb.ApiClient(configuration))

app = Flask(__name__)

# Triggered locally for convenience
@app.route('/sendCall', methods=['POST'])
def sendCall():
    if request.method == 'POST':
        call_request = freeclimb.MakeCallRequest(
            _from='+19193468860', to='+17733133558', application_id='AP5991fbadecfdcd227d326b23a3d498efca14d387')
        api_instance.make_a_call(make_call_request=call_request)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

# Specify this route with 'CALL CONNECT URL' in App Config
@app.route('/callConnect', methods=['POST'])
def callConnect():
    if request.method == 'POST':
        script = freeclimb.PerclScript(commands=[])

        script.commands.append(freeclimb.Say(
            text="Hello. Welcome to FreeClimb's outbound call tutorial."))
        script.commands.append(freeclimb.Pause(length=1000))
        script.commands.append(freeclimb.Say(text="Goodbye."))
        return percl_to_json(script)

# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

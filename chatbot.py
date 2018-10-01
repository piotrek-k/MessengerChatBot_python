"""
Based on: https://developers.facebook.com/docs/messenger-platform/getting-started/webhook-setup
"""

from flask import Flask, request, jsonify, abort
import json
app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook_post():
    """
    This endpoint is where the Messenger Platform will send all webhook events
    E.g. when someone send message to Page, it will be redirected here.
    """
    data = request.data
    dataDict = json.loads(data)

    fb_object = dataDict['object']
    entries = dataDict['entry']

    if fb_object == 'page':
        for e in entries:
            print(e["messaging"][0])

        resp = jsonify(success=True)
        return resp
    else:
        return abort(404)


@app.route("/webhook", methods=["GET"])
def webhook_get():
    """
    This code adds support for the Messenger Platform's webhook verification to your webhook.
    This is required to ensure your webhook is authentic and working.
    """
    verify_token = "some random token"

    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if mode is not None and token is not None:
        if mode == "subscribe" and token == verify_token:
            print("webhook verified")
            return challenge
        else:
            return "", 403

"""
Based on: https://developers.facebook.com/docs/messenger-platform/getting-started/webhook-setup
"""

import json
import secrets

import requests
from flask import Flask, request, jsonify, abort

# secrets.py need to contain:
# secrets.PAGE_ACCESS_TOKEN

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
            # Body of webhook event
            webhook_event = e["messaging"][0]
            # print(e["messaging"][0])

            # Sender PSID
            sender_psid = webhook_event["sender"]["id"]
            print("Sender id: ", sender_psid)

            # Check if the event is a message or postback and
            # pass the event to the appropriate handler function
            if "message" in webhook_event:
                handle_message(sender_psid, webhook_event["message"])
            elif "postback" in webhook_event:
                handle_postback(sender_psid, webhook_event["postback"])

        resp = jsonify(success=True)
        return resp
    else:
        return abort(404)


@app.route("/webhook", methods=["GET"])
def webhook_verfication():
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
            return abort(403, "Token incorrect or mode unknown")

    abort(400, "Webhook verification failed")

def handle_message(sender_psid, received_message):
    """
    Handles messages events
    Responses with text if user send text
    Sends 'structured image' if user send image
    """
    response = {}

    if "text" in received_message:
        response["text"] = "You sent the message: " + received_message["text"] + ". Now send me an image!"
    elif "attachments" in received_message:
        attachment_url = received_message["attachments"][0]["payload"]["url"]
        print("URL of attachment: ", attachment_url)
        response = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": "Is this the right picture?",
                        "subtitle": "Tap a button to answer.",
                        "image_url": attachment_url,
                        "buttons": [
                            {
                                "type": "postback",
                                "title": "Yes!",
                                "payload": "yes",
                            },
                            {
                                "type": "postback",
                                "title": "No!",
                                "payload": "no",
                            }
                        ],
                    }]
                }
            }
        }

    call_send_api(sender_psid, response)


def handle_postback(sender_psid, received_postback):
    """
    Handles messaging_postbacks events
    It's when user taps "Yes!" or "No!" after sending image
    """
    response = ""
    payload = received_postback["payload"]

    if payload == 'yes':
        response = {"text": "Thanks!"}
    elif payload == 'no':
        response = {"text": "Oops, try sending another image."}

    call_send_api(sender_psid, response)


def call_send_api(sender_psid, response):
    """
    Sends response messages via the Send API
    """
    request_body = {
        "recipient": {
            "id": sender_psid
        },
        "message": response
    }
    headers = {'content-type': 'application/json'}

    print("called send api")

    requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + secrets.PAGE_ACCESS_TOKEN,
                  data=json.dumps(request_body), headers=headers)

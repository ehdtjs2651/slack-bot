from flask import Flask, request, Response
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = Flask(__name__)


@app.route('/db', methods=['POST'])
def db():
    client.chat_postMessage(channel="#test", text="db")
    return Response(), 200


if __name__ == '__main__':
    client = WebClient(token="")
    port = 10300
    app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

app = Flask(__name__)


@app.route('/db', methods=['GET, POST'])
def db():
    return "db"


if __name__ == '__main__':
    client = WebClient(token="xoxb-2637151350448-2663729429670-1BATBYkj6fEhgiLkAPRPCetF")
    port = 10300
    try:
        response = client.chat_postMessage(channel='#test', text="Hello world!")
        assert response["message"]["text"] == "Hello world!"
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
    app.run(host='0.0.0.0', port=port, debug=True)

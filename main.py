from flask import Flask, request, Response
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl

app = Flask(__name__)


@app.route('/db', methods=['POST'])
def db():
    client.chat_postMessage(channel="#test", text="db")
    return Response(), 200


if __name__ == '__main__':
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='/etc/letsencrypt/live/cyberclass.ga/cert.pem', keyfile='/etc/letsencrypt/live/cyberclass.ga/privkey.pem')
    client = WebClient(token="")
    port = 10300
    app.run(host='0.0.0.0', port=port, debug=True)

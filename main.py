from flask import Flask, request, Response
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl
from db_check import db_ls

app = Flask(__name__)
client = WebClient(token="")


@app.route('/db', methods=["POST"])
def db():
    db_ls()
    client.chat_postMessage(channel="#test")
    return Response(status=200, mimetype="application/json")


if __name__ == '__main__':
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='/etc/letsencrypt/live/cyberclass.ga/fullchain.pem', keyfile='/etc/letsencrypt/live/cyberclass.ga/privkey.pem')
    port = 10300
    app.run(host='0.0.0.0', port=port, ssl_context=ssl_context, debug=True)

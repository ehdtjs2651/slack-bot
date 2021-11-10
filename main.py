from flask import Flask, request, Response
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl

app = Flask(__name__)
client = WebClient(token="xoxb-2637151350448-2663729429670-m5KXVsn4DAhF4OMw1dSUAOnn")

@app.route('/db', methods=["POST"])
def db():
    client.chat_postMessage(channel="#test", text="db")
    return Response(status=200, mimetype="application/json")


if __name__ == '__main__':
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='/etc/letsencrypt/live/cyberclass.ga/fullchain.pem', keyfile='/etc/letsencrypt/live/cyberclass.ga/privkey.pem')
    port = 10300
    app.run(host='0.0.0.0', port=port, ssl_context=ssl_context, debug=True)

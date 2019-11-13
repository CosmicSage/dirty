import sys, os, logging
from flask import Flask, jsonify, abort, request
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def email():
    print("s")
    message = request.args.get("message")
    name = request.args.get("email")
    subject = request.args.get("subject")
    email = request.args.get("email")
    print(message, email, name, subject)
    from mailjet_rest import Client
    api_key = 'c499ffc2f4c768c55e226cf86ac2e893'
    api_secret = '6f3be8c0fef4b49743f9fbfb8171276e'
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": "profuu77@gmail.com",
            "Name": "Cold"
          },
          "To": [
            {
              "Email": f"{email}",
              "Name": f"{name}"
            }
          ],
          "Subject": f"{subject}",
          "TextPart": f" {message}",
          "HTMLPart": f"<h3>Hello This a dynamically generated bot message</a>!</h3><br />May the delivery force be with you! {message}",
          "CustomID": "AppGettingStartedTest"
        }
      ]
    }
    result = mailjet.send.create(data=data)
    print( result.status_code)
    return result.json()


if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.run(host="0.0.0.0", port=5000)

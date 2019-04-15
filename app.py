from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from joke import joke
import requests
from cleverwrap import CleverWrap
from dialog import fetch_replay

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello I'm Bot and i'm alive"

@app.route("/sms", methods=['POST'])
def sms_reply():
    resp = MessagingResponse()
    msg = request.form.get("Body")
    phone_number = request.form.get("From")
    replay = fetch_replay(msg, phone_number)
    resp.message(replay)

    return str(resp)

    # url = "https://icanhazdadjoke.com/search"
    # res = requests.get(
    #     url,
    #     # we want json respons
    #     headers={"Accept": "application/json"},
    #     params={"term": msg}
    # ).json()
    # if(msg == 'היי' or msg == "מה קורה?"):
    #     resp.message(f"היי מה קורה? תשלח לי נושא בדיחה באנגלית ואשלח לך בדיחה!!!")
    # else:
    #     resp.message(joke(msg, res))

if __name__ == "__main__":
    app.run(debug=True)

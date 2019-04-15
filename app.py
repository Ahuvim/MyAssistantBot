from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from joke import joke
import requests
# from cleverwrap import CleverWrap

app = Flask(__name__)

# cleverbot_API = CleverWrap("INSERT YOUR API KEY")

@app.route("/")
def hello():
    return "Hello I'm Bot and i'm alive"

@app.route("/sms", methods=['POST'])
def sms_reply():
    resp = MessagingResponse()
    msg = request.form.get("Body")
    # cleverbot_response = cleverbot_API.say(msg)

    url = "https://icanhazdadjoke.com/search"

    res = requests.get(
        url,
        # we want json respons
        headers={"Accept": "application/json"},
        params={"term": msg}
    ).json()

    if(msg == 'היי' or msg == "מה קורה?"):
        resp.message(f"היי מה קורה? תשלח לי נושא בדיחה באנגלית ואשלח לך בדיחה!!!")
    else:
        resp.message(joke(msg, res))
    return str(resp)
    # resp.message(cleverbot_response)
    # return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

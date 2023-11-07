from flask import Flask, render_template, request
import vlak
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


# def index():
#    if request.method == 'POST':
#        if request.form.get('action1') == 'faks':
#            return vlak.run("faks")
#        elif request.form.get('action2') == 'doma':
#            return vlak.run("doma")
#        else:
#            return "<p>Handleat cu kasnije</p>"
#    elif request.method == 'GET':
#        return render_template('index.html')


@app.route("/", methods=['POST'])
def index():

    # user input
    user_msg = request.values.get('Body', '').lower()

    # creating object of MessagingResponse
    response = MessagingResponse()
    msg = response.message()

    # User Query
    if user_msg == 'faks':
        msg.body(vlak.run('faks'))
    elif user_msg == 'doma':
        msg.body(vlak.run('doma'))
    else:
        msg.body("upomoc")

    return str(response)


if __name__ == "__main__":
    app.run()

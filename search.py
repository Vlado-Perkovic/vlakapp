from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/", methods=["POST"])

# chatbot logic
def bot():

	# user input
	user_msg = request.values.get('Body', '').lower()

	# creating object of MessagingResponse
	response = MessagingResponse()

	# displaying result
	msg = response.message(f"--- Results for '{user_msg}' ---")

	return str(response)


if __name__ == "__main__":
	app.run()


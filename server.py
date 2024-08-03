#####################################################################
# This code connects (binds) to port 5555 on your local
# machine, it then waits for a message from the client
# when the server gets a message it performs some action
# and sends a message back to the client.

# This code was largely based on the example found on
# zguide titled hwserver: https://zguide.zeromq.org/docs/chapter1/
# (c) 2010-2012 Pieter Hintjens
#####################################################################

import requests
import zmq # For ZeroMQ





context = zmq.Context()
socket = context.socket(zmq.REP)

port = 5555
protocol = "tcp"
socket.bind(f"{protocol}://*:{port}")


api_url = 'https://zenquotes.io/api/random'


print("Server established")
print(f"Running on port {port} using protocol {protocol}")
while True:
    # @recv(flags=0, copy: bool = True, track: bool = False): will
    # receive a message from the client.
    message = socket.recv()

    print(f"Received request from the client: {message.decode()}")

    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        print(response.text)
        socket.send_string(response.text)
    else:
        print("Error:", response.status_code, response.text)
        socket.send_string("Error: ", response.status_code)


#######################################################################
# Client for ZeroMQ request-reply program. This will connect to
# a server via a request socket. Once connected to the localhost
# sends a string message and waits for reply from the server.

# This code was heavily based on the example found on
# zguide titled hwclient: https://zguide.zeromq.org/docs/chapter1/
#######################################################################


import zmq # For ZeroMQ

# @Context(): sets up the environment so that we are able to begin
# creating sockets.
context = zmq.Context()

# Connect to the server to send a message.
print("Client attempting to connect to server...")

# @socket(socket_type): This is the type of socket we
# will be working with. In this case REQ is the request socket.
socket = context.socket(zmq.REQ)

# @connect(addr): This will connect to a remote socket
# The format for this is: protocol://interface:port
print("Connecting to ")
socket.connect("tcp://localhost:5555")

# Request a value from the server. Sending a
# user specified string.
print(f"Sending a request...")
sending_message = "This is a message from CS361."
print("Out bound message: ", sending_message)

#@send_string will send the user specified string.
socket.send_string(sending_message)

# Get the reply.
#recv(flags=0, copy: bool = True, track: bool = False): will
# receive a message from the client.
# Parameter will be blank for simplicity.
message = socket.recv()

# Print our message!
print(f"Server sent back: {message.decode()}")

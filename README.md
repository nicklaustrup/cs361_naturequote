# About
This microservice uses ZeroMQ to receive and send messages. The incoming message is intended to come from a client and this nature quote service will return a response containing a randomly polled quote.

## Starting the Server
- Start the server by opening a terminal to the current directory and typing the following commands:
  ```
  pip install -r requirements.txt
  python server.py
  ```
- Once the server is running, send any message to the socket.
- To start the example client, open another terminal and type ```python example_client.py```

server.py will listen on port 5555 for any incoming messages. When it receives a message, it will poll the zenquotes API and return the quote to the socket.
To receive data, keep the socket open and allow incoming json messages.

## Example call
The client will connect to the socket on port 5555 and send a message.
```
socket.connect("tcp://localhost:5555")
sending_message = "Quote"
socket.send_string(sending_message)
```
The server will respond with this JSON format:
```
[
  {
    "q":"What you get by achieving your goals is not as important as what you become by achieving your goals.",
    "a":"Henry David Thoreau",
    "h":"<blockquote>&ldquo;What you get by achieving your goals is not as important as what you become by achieving your goals.&rdquo; &mdash; <footer>Henry David Thoreau</footer></blockquote>"
  }
]
```
## Return format
![Quote Response](img.png)

## UML Diagram
![Sequence diagram of making a request](https://github.com/user-attachments/assets/4f596d9d-59f0-4302-a6af-3bf05f14c546)

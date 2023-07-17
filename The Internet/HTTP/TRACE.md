#web 
[Source](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/TRACE)
The [[HTTP]] TRACE method performs a message loop-back test along the path to the target resource, providing a useful debugging mechanism.

The final recipient of the request should reflect the message received, excluding some fields described below, back to the client as the message body of a [[200]] (OK) response with a Content-Type of `message/http`. The final recipient is either the origin server or the first server to receive a Max-Forwards value of 0 in the request.
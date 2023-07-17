#web 
[Source](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/CONNECT)
The [[HTTP]] CONNECT method starts two-way communications with the requested resource. It can be used to open a tunnel.

For example, the CONNECT method can be used to access websites that use [[SSL]] ([[HTTPS]]). The client asks an HTTP Proxy server to tunnel the [[TCP]] connection to the desired destination. The server then proceeds to make the connection on behalf of the client. Once the connection has been established by the [[server]], the [[Proxy]] server continues to proxy the TCP stream to and from the [[client]].

CONNECT is a hop-by-hop method.
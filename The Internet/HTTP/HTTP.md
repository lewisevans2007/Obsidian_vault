#web
[Source](https://www.cloudflare.com/en-gb/learning/ddos/glossary/hypertext-transfer-protocol-http/)
The Hypertext Transfer Protocol (HTTP) is the foundation of the World Wide Web, and is used to load webpages using hypertext links. HTTP is an application layer protocol designed to transfer information between networked devices and runs on top of other layers of the network protocol stack. A typical flow over HTTP involves a client machine making a request to a server, which then sends a response message.

> [!warning]
> HTTP is not considered secure use [[HTTPS]] instead

## What is in an HTTP request?

An HTTP request is the way Internet communications platforms such as web browsers ask for the information they need to load a website.

Each HTTP request made across the Internet carries with it a series of encoded data that carries different types of information. A typical HTTP request contains:

1. HTTP version type
2. a [[URL]]
3. an HTTP method
4. HTTP request headers
5. Optional HTTP body.

Let’s explore in greater depth how these requests work, and how the contents of a request can be used to share information.

## What is an HTTP method?

An HTTP method, sometimes referred to as an HTTP verb, indicates the action that the HTTP request expects from the queried server. For example, two of the most common HTTP methods are [[GET]] and [[POST]].
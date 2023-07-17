#web 
[Source](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)
The [[HTTP]] POST method sends data to the server. The type of the body of the request is indicated by the Content-Type header.

The difference between [[PUT]] and POST is that PUT is idempotent: calling it once or several times successively has the same effect (that is no side effect), where successive identical POST may have additional effects, like passing an order several times.

A POST request is typically sent via an [[HTML]] form and results in a change on the server. In this case, the content type is selected by putting the adequate string in the `enctype` attribute of the `<form>` element or the `formenctype` attribute of the `<input>` or `<button>` elements:

- `application/x-www-form-urlencoded`: the keys and values are encoded in key-value tuples separated by `&`, with a `=` between the key and the value. Non-alphanumeric characters in both keys and values are URL encoded: this is the reason why this type is not suitable to use with binary data (use multipart/form-data instead)
- `multipart/form-data`: each value is sent as a block of data ("body part"), with a user agent-defined delimiter ("boundary") separating each part. The keys are given in the Content-Disposition header of each part.
- `text/plain`
When the POST request is sent via a method other than an HTML form — like via an `XMLHttpRequest` — the body can take any type. As described in the HTTP 1.1 specification, POST is designed to allow a uniform method to cover the following functions:

Annotation of existing resources
Posting a message to a bulletin board, newsgroup, mailing list, or similar group of articles;
Adding a new user through a signup modal;
Providing a block of data, such as the result of submitting a form, to a data-handling process;
Extending a database through an append operation.
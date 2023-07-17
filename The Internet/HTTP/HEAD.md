#web 
[Source](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD)
The [[HTTP]] HEAD method requests the headers that would be returned if the HEAD request's [[URL]] was instead requested with the [[HTTP]] [[GET]] method. For example, if a URL might produce a large download, a HEAD request could read its Content-Length header to check the file size without actually downloading the file.

>[!warning] 
> A response to a HEAD method should not have a body. If it has one anyway, that body must be ignored: any representation headers that might describe the erroneous body are instead assumed to describe the response which a similar [[GET]] request would have received.

If the response to a HEAD request shows that a cached [[URL]] response is now outdated, the cached copy is invalidated even if no [[GET]] request was made.

#web 
[Source](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH)
The [[HTTP]] PATCH request method applies partial modifications to a resource.

PATCH is somewhat analogous to the "update" concept found in CRUD (in general, HTTP is different than CRUD, and the two should not be confused).

A PATCH request is considered a set of instructions on how to modify a resource. Contrast this with [[PUT]]; which is a complete representation of a resource.

A PATCH is not necessarily idempotent, although it can be. Contrast this with [[PUT]]; which is always idempotent. The word "idempotent" means that any number of repeated, identical requests will leave the resource in the same state. For example if an auto-incrementing counter field is an integral part of the resource, then a PUT will naturally overwrite it (since it overwrites everything), but not necessarily so for PATCH.
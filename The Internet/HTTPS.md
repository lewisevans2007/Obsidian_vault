#web
## What is HTTPS?
Any website, especially those that require login credentials, should use HTTPS. In modern web browsers such as Chrome, websites that do not use HTTPS are marked differently than those that are. Look for a padlock in the [[URL]] bar to signify the webpage is secure.

## How does HTTPS work?
HTTPS uses an encryption protocol to encrypt communications. The protocol is called Transport Layer Security ([[TLS]]), although formerly it was known as Secure Sockets Layer ([[SSL]]). This protocol secures communications by using what’s known as an asymmetric public key infrastructure. This type of security system uses two different keys to encrypt communications between two parties:

The private key - this key is controlled by the owner of a website and it’s kept, as the reader may have speculated, private. This key lives on a web server and is used to decrypt information encrypted by the public key.
The public key - this key is available to everyone who wants to interact with the server in a way that’s secure. Information that’s encrypted by the public key can only be decrypted by the private key.
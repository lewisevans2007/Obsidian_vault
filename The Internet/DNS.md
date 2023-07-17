DNS stands for Domain Name System, and it is a fundamental protocol used on the internet to translate human-readable domain names into [[IP]] addresses. It serves as a distributed directory that maps domain names, such as "example.com," to the corresponding [[IP]] addresses, such as "192.0.2.1." This translation allows computers to communicate with each other using easily recognizable domain names rather than numerical [[IP]] addresses.

## Key parts of DNS

### DNS Hierarchy
The DNS system is organized in a hierarchical structure. At the top level, there are the root domain servers, which maintain information about the top-level domains (TLDs) such as .com, .org, .net, etc. Beneath the TLDs, there are authoritative name servers that handle specific domains, such as example.com.

### DNS Query
When you enter a domain name in a web browser or any other application, your device sends a DNS query to a DNS resolver (also known as a recursive resolver) provided by your internet service provider (ISP) or a third-party DNS resolver like Google DNS or Cloudflare DNS.

### Recursive Resolution
The DNS resolver doesn't have the requested IP address in its cache, so it starts the resolution process. It contacts the root domain servers to obtain the [[IP]] address of the [[TLD]] nameserver responsible for the requested domain (e.g., the .com nameserver for example.com).

### TLD Resolution
The resolver then sends a query to the [[TLD]] nameserver to obtain the [[IP]] address of the authoritative nameserver responsible for the specific domain (e.g., the nameserver for example.com).

### Authoritative Resolution
The resolver sends a query to the authoritative nameserver for the domain. This nameserver is typically managed by the domain owner or their DNS provider. The authoritative nameserver responds with the requested [[IP]] address if it has the mapping in its records.

### Caching
The resolver receives the [[IP]] address from the authoritative nameserver and stores it in its cache for future use, reducing the need for repeated queries for the same domain name.

### Response to the Application
The resolver sends the [[IP]] address back to the application that initiated the DNS query, such as a web browser. The application can then use the [[IP]] address to establish a connection with the desired web server.

### TTL and DNS Cache
DNS records have a Time to Live ([[TTL]]) value that specifies how long the resolver can keep the record in its cache before it expires. Once the [[TTL]] expires, the resolver needs to perform a fresh query to obtain the updated [[IP]] address.
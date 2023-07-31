Improper Limitation of a Pathname to a Restricted Directory - This CWE relates to path traversal vulnerabilities, where a file or directory path is not properly restricted, potentially allowing unauthorized access.
## Example (PHP)
```php
$file = $_GET['file'];
$restrictedDir = "/var/www/data/";
$path = $restrictedDir . $file; // Vulnerability: The 'file' parameter could contain '../' to traverse to other directories.
include($path);
```

---
#### Links:
- [Mitre CWE](https://cwe.mitre.org/data/definitions/22.html)

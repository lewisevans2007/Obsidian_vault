Improper Neutralization of Special Elements used in an [[SQL]] Command - This CWE refers to [[SQL]] injection [[Vulnerability|vulnerabilities]] where untrusted data is used in constructing [[SQL]] queries, allowing attackers to manipulate [[database]] queries.
## Example (PHP/MySQL)
```php
$username = $_POST['username'];
$password = $_POST['password'];
$query = "SELECT * FROM users WHERE username='" . $username . "' AND password='" . $password . "';";
// Vulnerability: If an attacker submits ' OR '1'='1 to the 'username' field, the query will return all users.
```

---
#### Links:
- [Mitre CWE](https://cwe.mitre.org/data/definitions/89.html)

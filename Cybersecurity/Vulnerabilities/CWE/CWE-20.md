Improper Input Validation - This weakness involves not properly validating input data, leading to potential security issues like injection attacks or [[privilege escalation]].

## Example (Java)
```java
public void loadUserData(String username) {
    String query = "SELECT * FROM users WHERE username='" + username + "';";
    // Vulnerability: The 'username' parameter is not sanitized, making it vulnerable to SQL injection.
    // Execute the query...
}
```

---
#### Links:
- [Mitre CWE](https://cwe.mitre.org/data/definitions/20.html)

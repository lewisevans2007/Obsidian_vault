Improper Neutralization of Input During Web Page Generation ([[XSS]]) - This weakness involves not properly sanitizing user input, leading to the injection of malicious scripts into web pages viewed by other users.
## Example (HTML/JavaScript)
```html
<input type="text" id="username" value="">
<script>
    var username = document.getElementById('username').value;
    document.write("Welcome, " + username); // Vulnerability: If a user inputs malicious scripts, they will be executed in other users' browsers.
</script>
```

---
#### Links:
- [Mitre CWE](https://cwe.mitre.org/data/definitions/79.html)

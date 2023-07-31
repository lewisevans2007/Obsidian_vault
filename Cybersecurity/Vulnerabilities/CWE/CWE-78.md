Improper Neutralization of Special Elements used in an [[Operating system|OS]] Command - This CWE refers to command injection [[Vulnerability|vulnerabilities]] when input data is not properly sanitized and executed as part of a command in an [[operating system]] shell.
## Example (Ruby)
```ruby
def process_user_input(input)
    command = "echo #{input}"
    system(command) # Vulnerability: If 'input' contains a malicious command, it will be executed.
end
```

---
#### Links:
- [Mitre CWE](https://cwe.mitre.org/data/definitions/78.html)

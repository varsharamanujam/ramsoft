---
# Offensive Security Intern – Round 2 Submission

## Exercise 3: Automating a Security Task with AI & Scripting
---

### 1. Objective
The goal of this exercise is to create a simple security automation script using Python, with the assistance of AI tools like ChatGPT. The script scans common ports on a given target domain or IP address and reports whether they are open or closed. This mimics how attackers or defenders might check for available services.

---

### 2. Tools Used
- **Programming Language:** Python 3.x  
- **AI Tool:** ChatGPT (for code generation and learning support)  
- **Libraries:** `socket` (Python standard library)  
- **System:** [e.g., Windows 10 / Ubuntu 22.04]

---

### 3. Script
```python
import socket

target = "scanme.nmap.org"  

ports = [21, 22, 80, 443, 3306]

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

        sock.close()  

    except Exception as e:
        print(f"Error scanning port {port}: {e}")
```

---

### 4. Explanation (Line-by-Line)
| Line | Explanation |
|------|-------------|
| `import socket` | Imports a Python module that lets you open network connections. |
| `target = "scanme.nmap.org"` | Sets the domain/IP you want to scan. This one is safe to test on. |
| `ports = [21, 22, 80, 443, 3306]` | List of ports (common services like FTP, SSH, HTTP, HTTPS, MySQL). |
| `for port in ports:` | Start a loop to scan each port one by one. |
| `socket.socket(...)` | Create a connection using IPv4 (AF_INET) and TCP (SOCK_STREAM). |
| `settimeout(1)` | Only wait 1 second before moving on to avoid delays. |
| `connect_ex(...)` | Try to connect — result 0 means success, anything else means failure. |
| `if result == 0:` | If the connection was successful... |
| `print(...)` | Show whether the port is open or closed. |
| `sock.close()` | Clean up — always close the socket. |
| `except` block | Catch and print any error that occurs (e.g., network issues). |

---

### 5. AI's Contribution
I used ChatGPT to:
- Generate the basic structure of the script
- Explain what each function does
- Help me add debug errors like timeouts and connection failures for safe practices.
- Suggest adding error handling and timeout for smoother performance

---

### 6. Conclusion
AI helped speed up the scripting process, especially as a beginner. It explained difficult parts and helped debug the code efficiently. This exercise showed how AI can make cybersecurity tasks easier and faster to learn.

---

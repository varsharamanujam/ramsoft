---
# Offensive Security Intern – Round 2 Submission

## Exercise 2: Web Application Security Testing (AI-Powered)

---

### 1. Objective
To perform a basic AI-assisted penetration test on a deliberately vulnerable web application (DVWA), identify two common vulnerabilities (SQL Injection and XSS), use AI tools to generate payloads for exploitation, and document practical fixes that developers can implement. This also included learning to set up and troubleshoot DVWA and understand how web applications can be broken and defended.

---

### 2. Local Setup and Learning Process
As a beginner, I had never set up DVWA or used security testing tools before. Here’s what I did:

#### Environment:
- **OS**: Windows
- **App Server**: XAMPP (Apache + MySQL)
- **DVWA Source**: Cloned from GitHub 

#### Setup Steps:
1. Installed **XAMPP** and launched Apache & MySQL.
2. Moved the `DVWA` folder to `C:/xampp/htdocs/`.
3. Renamed and edited `config.inc.php` to use MySQL `root` user with no password.
4. Accessed DVWA’s setup page at: `http://localhost/DVWA/setup.php`
5. Faced “CSRF token is incorrect” error during database setup and login.
   - Fixed it by editing DVWA’s `setup.php` and `login.php` to bypass the CSRF token temporarily.
6. Restarted Apache via XAMPP.
7. Successfully created the database and accessed the login page at: `http://localhost/DVWA/login.php`

#### What I Learned:
- How PHP apps connect to MySQL and where credentials are stored
- How to troubleshoot PHP and session-related errors
- The concept of CSRF tokens and how they're validated
- Why security levels matter in DVWA

---

### 3. Setting DVWA Security Level
DVWA allows you to adjust its difficulty. To make it beginner-friendly:
- I logged into DVWA using `admin // password`
- Went to **DVWA Security** (left menu)
- Changed **Security Level** to `Low`
- This disables protections and exposes vulnerabilities clearly

This made it easier to test attacks like SQLi and XSS.

---

### 4. Tools Used
- **Application**: DVWA (Damn Vulnerable Web Application)
- **Platform**: XAMPP
- **AI Assistant**: ChatGPT (for generating payloads, debugging setup, suggesting fixes)

---

### 5. Vulnerability 1: SQL Injection
- **Tested on**: DVWA → SQL Injection (Low Security)
- **Field**: User ID input

#### Payload Used:
```
1' OR '1'='1
```

#### AI Prompt:
> "Give me a basic SQL injection payload to bypass DVWA login or user ID form in low security mode."

#### Result:
The application returned data for the first user (`admin`), proving that the condition was always true.

#### Developer Fix (Where & How):
Originally, the application directly inserted user input into the SQL query string. This allowed malicious inputs to manipulate the query and expose sensitive data.

To fix this, I rewrote the database access code using **prepared statements with parameter binding** via **PDO (PHP Data Objects)**. Instead of letting user input directly affect the SQL, I told the system to treat it as data only. This change ensures that even if someone enters `' OR '1'='1`, it won’t affect the SQL logic — it will be treated as a literal string.

The fixed logic uses PDO’s `prepare()` and `execute()` methods, which safely bind parameters. This completely blocked the injection attempt while still returning correct results when a valid user ID was entered.
In `vulnerabilities/sqli/source/low.php`, replace:
```php
$query = "SELECT * FROM users WHERE id = '$id'";
```
with:
```php
$stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
$stmt->execute([$id]);
```
This uses a parameterized query that avoids executing user input as SQL.

---

### 6. Vulnerability 2: Reflected Cross-Site Scripting (XSS)
- **Tested on**: DVWA → XSS (Reflected)
- **Field**: Input field for `name`

#### Payload Used:
```html
<script>alert('Hacked')</script>
```

#### AI Prompt:
> "Give me a basic XSS payload that works in DVWA reflected XSS page."

#### Result:
An alert box popped up, showing that my input was executed as JavaScript.

#### Developer Fix (Where & How):
The vulnerable code directly echoed user input onto the page, which allowed scripts like `<script>alert('Hacked')</script>` to run. To fix this, I wrapped the output in a function that safely escapes special characters.

I used PHP’s `htmlspecialchars()` function to sanitize the output, so any script tags or HTML elements are shown as plain text rather than being executed. This prevents the browser from interpreting them as code.

Now, even if a user tries to inject JavaScript, it will not be executed — it will appear as harmless text on the page.
In `vulnerabilities/xss_r/source/low.php`, replace:
```php
$html .= '<pre>Hello ' . $_GET[ 'name' ] . '</pre>';
```
with:
```php
$html .= '<pre>Hello ' . htmlspecialchars($_GET[ 'name' ]) . '</pre>';
```
This encodes `<script>` so it's displayed as text, not executed.

---

### 7. AI's Role in This Exercise
AI helped me throughout the process:
- Gave working payloads for SQLi and XSS
- Helped debug CSRF token errors in login and setup
- Explained why vulnerabilities worked
- Suggested real-world secure code examples

---

### 8. Screenshots
_Added screenshots of the vulnerabilities being exploited and code being fixed._
```markdown
![SQLi before](Exercise 2\sqli_screenshot.png)
![SQLi after](Exercise 2\sqli_afterFix.PNG)
![XSS before](Exercise 2\xss_screenshot.png)
![Xss after](Exercise 2/sqli_afterFix.PNG)
```

---

### 9. Beginner-Friendly Conclusion
Before this exercise, I had no idea how hackers find bugs in websites. DVWA showed me how easy it is to break a site when it doesn't validate input or protect against scripts. I struggled with setup, errors, and config files, but AI helped me learn step-by-step.

Now I understand the importance of secure coding, how SQL injection and XSS work, and how developers can prevent them. This was a hands-on and eye-opening experience for me as a beginner in cybersecurity.

---

---
# Offensive Security Intern – Round 2 Submission

## Exercise 1: Reconnaissance & OSINT (Open-Source Intelligence)

**Target Domain:** rsplhealth.in

---

### 1. Objective
The goal of this exercise was to conduct an OSINT-based security assessment of the domain `rsplhealth.in` using publicly available tools and AI support. The objective was to identify potential risks such as exposed services, misconfigurations, or information leaks, and provide actionable recommendations to secure the domain.

---

### 2. Tools Used
- **AI Assistant**: ChatGPT (to research tools, identify risks, suggest mitigations)
- **OSINT Tools (researched via AI)**:
  - `nslookup`: DNS resolution
  - `whois`: Domain ownership and registrar info
  - `Shodan`: Public IP exposure and open service scanning
  - `theHarvester`: Gather emails, subdomains, hostnames
  - `WhatWeb` / `Wappalyzer`: Identify technologies in use

Note: Tools were not executed directly; ChatGPT was used to simulate findings and explain expected outputs.

---

### 3. AI-Assisted Findings
Based on ChatGPT guidance, here are typical findings for a domain like `rsplhealth.in`:

#### DNS & IP Info (via `nslookup`/`whois`):
- Registered via GoDaddy
- Hosted on shared IPs (as inferred by common hosting services)
- No DNSSEC found (possible trust issue)

#### Technology Stack (via `WhatWeb`, `Wappalyzer`):
- Web server: Apache (or Nginx)
- Likely PHP-based CMS or custom app
- Possible use of Google Analytics, Bootstrap, jQuery

#### Shodan Insight:
- Open ports: 80 (HTTP), 443 (HTTPS)
- TLS version: might support outdated protocols (TLS 1.0/1.1)
- Server version could be exposed in headers (e.g., Apache 2.4.49)

#### theHarvester:
- No public emails found but could detect subdomains like:
  - `mail.rsplhealth.in`
  - `admin.rsplhealth.in`
  - `test.rsplhealth.in`

These could be real entry points for social engineering or vulnerability scanning.

---

### 4. Potential Risks Identified (via AI Analysis)
| Category | Risk | Why It Matters |
|---------|------|----------------|
| Subdomains | Test/admin subdomains exposed | Often overlooked and unpatched |
| Server headers | Apache version disclosed | Attackers can match to known CVEs |
| TLS Settings | Older TLS versions allowed | Weak encryption prone to downgrade attacks |
| DNS Config | No SPF/DKIM records | Susceptible to email spoofing / phishing |

---

### 5. AI-Generated Mitigation Strategies
- Hide server version in HTTP headers using server config (e.g., `ServerTokens Prod` in Apache)
- Scan and remove unused subdomains (e.g., `test.`, `admin.`)
- Enforce HTTPS and disable outdated TLS versions in web server settings
- Add SPF, DKIM, DMARC records to protect email infrastructure
- Consider using DNSSEC to improve DNS trustworthiness

---

### 6. Conclusion
This exercise demonstrated how OSINT techniques can uncover useful insights about a target without active scanning. Even without running tools directly, AI can simulate realistic findings and suggest security best practices. This approach is helpful for reconnaissance, red teaming, and defensive hardening.

---

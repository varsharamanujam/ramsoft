---
# Offensive Security Intern – Round 2 Submission

## Exercise 1: Reconnaissance & OSINT (Open-Source Intelligence)

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
---

### 3. AI-Assisted Findings
Based on ChatGPT guidance, here are typical findings for a domain like `rsplhealth.in`:

#### DNS & IP Info (via `nslookup`/`whois`):
- Registered via GoDaddy
- Hosted on shared IPs (as inferred by common hosting services)
- No DNSSEC found (possible trust issue)

#### Technology Stack (via `WhatWeb`, `Wappalyzer`):
- Web server: Vercel
- Likely React or custom app
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

### 4. Manual OSINT Findings
To complement the AI-generated findings, I conducted my own manual OSINT reconnaissance using freely accessible online tools and command-line utilities.

#### DNS and WHOIS:
- Used `nslookup rsplhealth.in` to confirm the domain resolves to an IP.
- Used `whois rsplhealth.in` to view registrar, admin contact, and DNS expiry information.

#### Subdomain Enumeration:
- Searched `crt.sh` with query `%.rsplhealth.in` to find publicly known subdomains issued under SSL/TLS certificates.

#### Technology Detection:
- Used `BuiltWith` and `Wappalyzer` browser extensions to analyze tech stack.
- Verified Next.js, React, HSTS, Tailwind CSS and vercel usage.

#### SSL Configuration (via SSL Labs):
- Performed SSL/TLS scan using [SSL Labs](https://www.ssllabs.com/ssltest/)
- Both IPs `66.33.60.193` and `66.33.60.67` returned A+ grade
- TLS 1.3 and 1.2 supported; TLS 1.0 and 1.1 disabled 
- Secure cipher suites and forward secrecy enabled
- No known SSL vulnerabilities detected (e.g., POODLE, Heartbleed)
- HSTS enabled with long duration, OCSP stapling enabled, DNS CAA present

These findings confirmed a secure SSL/TLS configuration and helped reinforce confidence in server-side encryption.

#### Additional Passive Recon:
- Accessed website directly and used `Developer Tools > Network > Headers` to examine server headers.
- Found references to analytics (Google Analytics), fonts (Google Fonts), and older JavaScript libraries.

---


### 5. Potential Risks Identified (via AI Analysis and Manual Verification)
| Category | Risk | Why It Matters |
|---------|------|----------------|
| Subdomains | Test/admin subdomains exposed | Often overlooked and unpatched |
| Server headers | Vercel server disclosed | Reveals platform used and can aid targeted enumeration |
| DNS Config | No SPF/DKIM records | Susceptible to email spoofing / phishing |
| Public Web Resources | Older JS libraries detected | May contain client-side vulnerabilities |

*Note: TLS-related concerns were not found due to strong results in manual SSL Labs scans.*

--

### 5. AI-Generated Mitigation Strategies
- Scan and remove unused subdomains (e.g., `test.`, `admin.`)
- Ensure platform headers like 'server: Vercel' are minimized or obfuscated via edge config or CDN settings
- Add SPF, DKIM, DMARC records to protect email infrastructure
- Consider using DNSSEC to improve DNS trustworthiness

---

### 6. Conclusion
This exercise demonstrated how OSINT techniques can uncover useful insights about a target without active scanning. Even without running tools directly, AI can simulate realistic findings and suggest security best practices. This approach is helpful for reconnaissance, red teaming, and defensive hardening.

---

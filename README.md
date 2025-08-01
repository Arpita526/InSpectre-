#🛡️ Web Sentinel – A Lightweight Website Vulnerability Scanner


# 1. Introduction

Web Sentinel is a simple yet powerful web-based tool that helps users scan any website for common security issues. Whether you're a developer, student, or website owner, 
you can use Web Sentinel to check if a site is secure and safe from basic threats.

Goal:

To identify common website vulnerabilities such as:

* Missing security headers
* SSL/TLS support issues
* Directory listing exposure
* XSS vulnerabilities (basic)
* Clickjacking possibilities
* Open ports (using optional Nmap scan)

# 2. How It Works (Behind the Scene)

Here’s how Web Sentinel operates in a step-by-step flow:

Step 1: User Inputs a Website URL

* You enter the **website link** (like `https://example.com`) into the Web Sentinel web interface.

Step 2: Flask Backend Receives the URL

* The Flask backend takes this URL and starts scanning using different modules.

Step 3: Vulnerability Scanning Begins

Security Header Check:

* Uses `requests` to send a GET request to the site.
* Checks if important **HTTP security headers** are present (like `Content-Security-Policy`, `X-Frame-Options`, etc.).

SSL/TLS Check:

* Tries to connect via HTTPS.
* Checks if the SSL certificate is valid and not expired.
* Looks for HTTPS redirection.

Directory Listing Check:

* Sends a request to some common folders (`/uploads`, `/admin`, `/images`) and looks for index pages or file lists.

Clickjacking Check:

* Looks for missing `X-Frame-Options` header.
* If missing, the website can be embedded into a malicious frame.

XSS Basic Check:

* Uses basic payload injection like `<script>alert(1)</script>` in URL parameters to see how the site responds.

Port Scanning (Optional):

* Uses Nmap, a powerful network scanning tool, to find open ports on the website server.

# 3. How It Works (On-Site/Front-End View)

User Interface:

* Built with **HTML**, **CSS**, and **JavaScript**.
* Easy-to-use form for inputting the target website.
* Visual output showing:

  * Safe items in green
  * Warnings in yellow
  * Vulnerabilities in red

Output:

* Each security check displays:

  * What was tested
  * Result (Pass / Fail / Warning)
  * A simple explanation
  * Suggestion to fix the issue


# 4. Technologies Used & Why

 Python Flask                    Backend Web Framework                                                     
 HTML/CSS/JavaScript             Frontend Web Interface                                                    
 Requests (Python library)       For sending HTTP requests                                                  
 BeautifulSoup4                  For HTML parsing (e.g., checking script injection or form vulnerabilities) 
 Nmap                            Port scanning (optional)                                                  
 Kali Linux Live USB (Test Lab)  To test the scanner on purposely vulnerable websites                       


# 5. Test Environment

Test Setup:

* Use Linux for testing tools and demo scans.
* Include **DVWA (Damn Vulnerable Web App)** or any basic web app with security misconfigurations.
* Ensures **no harm to real websites** and full control over tests.

# 6. Objectives

* Help students, developers, and small website owners to quickly check site security.
* Be an educational tool to understand web vulnerabilities.
* Build a foundation for more advanced scanners.


Web Sentinel is a user-friendly security tool that acts as the first line of defense in identifying website vulnerabilities. It’s designed to be simple enough for beginners, 
yet functional enough to highlight real-world security issues.

"You can’t fix what you don’t know is broken. Web Sentinel helps you find it."

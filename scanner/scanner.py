import subprocess

def run_command(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        result = e.output
    return result

def check_clickjacking(url):
    headers = run_command(f"curl -I {url}")
    result = "\n--- Clickjacking Protection Check ---\n"
    if "X-Frame-Options" in headers or "Content-Security-Policy" in headers:
        result += " Clickjacking protection header found.\n"
        if "X-Frame-Options" in headers:
            result += "X-Frame-Options: Present\n"
        if "Content-Security-Policy" in headers and "frame-ancestors" in headers:
            result += "Content-Security-Policy: frame-ancestors directive found\n"
    else:
        result += "No Clickjacking protection headers found!"
    return result

def run_scans(url):
    output = "\n--- Nmap Scan ---\n"
    output += run_command(f"nmap -Pn {url}")

    output += "\n\n--- Curl Headers ---\n"
    headers = run_command(f"curl -I {url}")
    output += headers

    output += "\n\n--- SSL Check ---\n"
    output += run_command(f"sslscan {url} || echo 'sslscan not found'")

    output += "\n\n--- XSS Check (Simple) ---\n"
    xss_payload = "<script>alert('XSS')</script>"
    output += run_command(f"curl -G --data-urlencode \"q={xss_payload}\" {url}")

    output += "\n\n--- Directory Listing Check ---\n"
    output += run_command(f"curl -s {url} | grep -i 'index of' || echo 'No directory listing detected'")

    output += check_clickjacking(url)

    return output

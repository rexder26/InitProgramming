# 📌 Day-4: OWASP Top-10 Web Vulnerabilities.

## What is OWASP?
    
    OWASP/Open Web Application Security Project/ is A Project That lists a Vulnerability that have been 
    Happened or Got a high Attacking level in a 3 years.
    Example: ...,OWASP top 10 of 2017,OWASP top 10 of 2021,...

> ## 1. **Broken Access Control**

    Broken access control means that attackers can gain access to user accounts and act as users or administrators, and that regular users can gain unintended privileged functions. Strong access mechanisms ensure that each role has clear and isolated privileges.

> ## 2.  **Cryptographic Failures**

    Cryptographic Failures, previously known as 
    [Sensitive Data Exposure], covers the protection of data in transit and at rest. This includes passwords, credit card numbers, health records, personal information and other sensitive information.

> ## 3.  **Injection**

    An injection vulnerability in a web application allows attackers to send hostile data to an interpreter, causing that data to be compiled and executed on the server. A common form of injection is SQL injection.

> ## 4.  **Insecure Design**
    Insecure Design is a category of weaknesses that originate from missing or ineffective security controls. Some applications are built without security in mind. Others do have a secure design, but have implementation flaws that can lead to exploitable vulnerabilities.
> ## 5.  **Security Misconfiguration**
    Security Misconfiguration is a lack of security hardening across the application stack. This can include improper configuration of cloud service permissions, enabling or installing features that are not required, and default admin accounts or passwords. This now also includes XML External Entities (XXE), previously a separate OWASP category.
> ## 6.  **Vulnerable and Outdated Components**
    Vulnerable and Outdated Components, previously known as “Using Components with Known Vulnerabilities,” includes vulnerabilities resulting from unsupported or outdated software. Anyone who builds or uses an application without knowing its internal components, their versions, and whether they are updated, is exposed to this category of vulnerabilities.
> ## 7.  **Identification and Authentication Failures**
    Identification and Authentication Failures, previously known as Broken Authentication, this category now also includes security problems related to user identities. Confirming and verifying user identities, and establishing secure session management, is critical to protect against many types of exploits and attacks.
> ## 8.  **Software and Data Integrity Failures**
    Software and Data Integrity Failures involve code and infrastructure that are vulnerable to integrity violations. This includes software updates, modification of sensitive data, and CI/CD pipeline changes performed without validation. An insecure CI/CD pipeline can lead to unauthorized access, introduction of malware, and other severe vulnerabilities.
> ## 9.  **Security Logging and Monitoring Failures**
    Security Logging and Monitoring Failures, previously named “Insufficient Logging and Monitoring”, involves weaknesses in an application’s ability to detect security risks and respond to them. Breaches cannot be detected without logging and monitoring. Failures in this cateogry affect visibility, alerting, and forensics.
> ## 10.  **Server-Side Request Forgery**
    A Server-Side Request Forgery (SSRF) vulnerability occurs when a web application pulls data from a remote resource based on a user-specified URL, without validating the URL. Even servers protected by a firewall, VPN, or network access control list (ACL) can be vulnerable to this attack, if they accept unvalidated URLs as user inputs.
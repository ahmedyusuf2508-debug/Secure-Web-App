\# Secure Flask Web Application



A cybersecurity and application security project I built using Python and Flask.



The goal of this project was to build a working web application and apply security controls to protect user accounts, passwords, sessions, and data.



\## Features



\- User registration

\- User login

\- Password hashing

\- Secure authentication

\- Protected dashboard

\- User sessions

\- Logout functionality

\- CSRF protection

\- SQL injection protection

\- XSS protection

\- HTTP security headers

\- Input validation

\- SQLite database



\## Security Controls



\### Password Hashing



Passwords are not stored as plain text. The application uses Werkzeug password hashing before passwords are saved in the database.



\### SQL Injection Protection



The application uses parameterized SQL queries instead of placing user input directly into SQL statements.



\### CSRF Protection



Flask-WTF is used to protect forms against Cross-Site Request Forgery (CSRF) attacks.



I also tested the application by sending a request without a CSRF token. The application rejected the request because the CSRF token was missing.



\### XSS Protection



User-controlled data is displayed through Jinja templates, which escape HTML by default.



I tested the application using an XSS test string:



`<script>alert('XSS')</script>`



The application displayed the script as text instead of executing the JavaScript.



\### Secure Sessions



Flask sessions are used to keep track of authenticated users. Protected pages check the session before allowing access.



\### Security Headers



The application uses HTTP security headers including:



\- Content-Security-Policy

\- X-Content-Type-Options

\- X-Frame-Options

\- Referrer-Policy



\## Security Testing



\### Semgrep



I used Semgrep to perform static application security testing on the Python code.



The first scan detected Flask debug mode as a security issue.



I fixed the issue by disabling debug mode and ran the scan again.



\*\*Final result: 0 findings\*\*



\### pip-audit



I used pip-audit to scan the Python dependencies for known vulnerabilities.



The original scan identified vulnerable dependencies. I updated the affected package and ran the scan again.



\*\*Final result: No known vulnerabilities found\*\*



\## Technologies Used



\- Python

\- Flask

\- Flask-WTF

\- SQLite

\- HTML

\- Werkzeug

\- Git

\- GitHub

\- Semgrep

\- pip-audit



\## What I Learned



This project helped me understand how security can be built into a web application instead of only being added after development.



I practiced secure authentication, password storage, session management, input validation, database security, CSRF protection, XSS protection, security headers, static code scanning, and dependency vulnerability scanning.



I also practiced using Git and GitHub to manage and document a security project.



\## Project Screenshots



\### Application Security Testing



The screenshots below show examples of the application and security testing performed during the project.



!\[Application Security Test](screenshots/Screenshot%202026-09-19%20121450.png)



!\[XSS Protection Test](screenshots/Screenshot%202026-09-19%20123236.png)



\### Security Scanning



!\[Semgrep Security Scan](screenshots/Screenshot%202026-09-19%20173137.png)



!\[Dependency Vulnerability Scan](screenshots/Screenshot%202026-09-19%20174056.png)



!\[GitHub Project](screenshots/Screenshot%202026-09-19%20174450.png)



\## Author



\*\*Ahmed Yusuf\*\*



Cybersecurity


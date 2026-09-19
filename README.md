\# Secure Flask Web Application



This is a cybersecurity and application security project I built using Python and Flask. The goal of this project was to build a working web application and add security controls to protect user accounts and data.



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



Flask-WTF is used to help protect forms against Cross-Site Request Forgery attacks.



\### XSS Protection



User-controlled data is displayed through Jinja templates, which escape HTML by default. I tested the application using an XSS test string to verify that it was displayed as text instead of being executed as JavaScript.



\### Secure Sessions



Flask sessions are used to keep track of authenticated users. Protected pages check the session before allowing access.



\### Security Headers



The application adds HTTP security headers including:



\- Content-Security-Policy

\- X-Content-Type-Options

\- X-Frame-Options

\- Referrer-Policy



\## Security Testing



I used Semgrep to perform static application security testing on the Python code.



The first scan detected Flask debug mode as a security issue.



I changed the application to disable debug mode and ran the scan again.



Final Semgrep result:



\*\*0 findings\*\*



I also used pip-audit to scan the Python dependencies for known vulnerabilities.



Final pip-audit result:



\*\*No known vulnerabilities found\*\*



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



This project helped me understand how security can be built into a web application instead of being added only after development. I practiced secure authentication, password storage, session management, input validation, database security, CSRF protection, XSS protection, security headers, static code scanning, and dependency vulnerability scanning.



\## Project Screenshots



\### Application Security Testing



The screenshots below show examples of the application and security testing performed during the project.



!\[Security Test](screenshots/Screenshot%202026-09-19%20121450.png)



!\[Security Test](screenshots/Screenshot%202026-09-19%20123236.png)



\### Security Scanning



!\[Security Scan](screenshots/Screenshot%202026-09-19%20173137.png)



!\[Dependency Scan](screenshots/Screenshot%202026-09-19%20174056.png)



!\[GitHub Project](screenshots/Screenshot%202026-09-19%20174450.png)



\## Author



Ahmed Yusuf



Cybersecurity


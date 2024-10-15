import smtplib
from email.mime.text import MIMEText


def send_repair_ticket(ip, error_message):
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_email@example.com'
    smtp_password = 'your_password'
    recipient = 'support@example.com'

    subject = f"Ticket de réparation pour {ip}"
    body = f"Erreur détectée sur {ip}: {error_message}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = recipient

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, recipient, msg.as_string())

from gpt4all import GPT4All
from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

FROM_EMAIL = os.getenv("FROM_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
TO_EMAILS = os.getenv("TO_EMAILS").split(",") 
PHISHING_LINK = os.getenv("PHISHING_LINK")

# === Step 1: Generate phishing email using local LLM ===
def generate_phishing_email(context):
    model_name = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"
    model = GPT4All(model_name)

    prompt = f"""Write a realistic phishing email with subject and body based on the following context:
    Phishing email from HR asking employees to update bank account details to avoid salary delays.

    Make sure:
    - The greeting is 'Dear Employee'
    - Replace any URL with this link: {PHISHING_LINK}
    - Do NOT include any placeholder email addresses or names or for anything else.
    - The email should look like it is from a legitimate company.
    - The email should be convincing and realistic.
    
    Format:
    Subject: <subject line>

    <email body>
    """

    with model.chat_session():
        print("[*] Generating phishing email using local LLM...\n")
        response = model.generate(prompt, max_tokens=400)

    # Parse output to separate subject and body
    if "Subject:" in response:
        parts = response.split("Subject:", 1)[1].strip().split("\n", 1)
        subject = parts[0].strip()
        body = parts[1].strip() if len(parts) > 1 else "Body could not be extracted."
    else:
        subject = "Generated Phishing Email"
        body = response.strip()

    return subject, body

# === Step 2: Send the email using SMTP ===
def send_email(subject, body, to_emails, from_email, app_password):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg.set_content(body)

    try:
        print("[*] Sending phishing email...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(from_email, app_password)
            smtp.send_message(msg)
        print("[+] Email sent successfully!")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")

if __name__ == "__main__":
    context = "Phishing email from HR asking employees to update bank account details to avoid salary delays."
    subject, body = generate_phishing_email(context)
    
    print("\n--- Generated Email ---\n")
    print(f"Subject: {subject}\n\n{body}\n")

    send_email(subject, body, TO_EMAILS, FROM_EMAIL, APP_PASSWORD)

import smtplib
import getpass
from base_code.security_info import passwords ,emails

def send_email_forgot_password(username,password, code, to_email):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = emails["outlook"]

    MESSAGE = f"""Subject: Send email from Nhom13

    Hello {username} are you forgot password .

    Here are your code :

    {code}

    Remember your code is only valid for 3 minutes
    """

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, password)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, to_email, MESSAGE)
    smtp.quit()

    print("Email sent successfully")
    return "Email sent successfully"

# Sử dụng hàm
# if __name__ == "__main__":
# password = passwords["outlook"]
# # # print(password)
# #     # password = getpass.getpass("Enter password: ")
# code = "000000"  # Thay bằng code bạn muốn gửi đi
# to_email = emails["email_test_to_send"]  # Địa chỉ email của người nhận
# result = send_email_forgot_password(password, code, to_email)

# if result == "Email sent successfully":
#     print("ok")
# else:
#     print("something wrong to send email , please check your email again")

# reminder admin about contact
def send_email_reminder_admin_about_contact_customer(username,password, to_email , created_time):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = emails["outlook"]

    MESSAGE = f"""Subject: Reminder email for Admin about contact customer

    Hello Admin you have an contact from {username} .

    This contact send at {created_time}

    Remember to give feedback to customers.
    """

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, password)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, to_email, MESSAGE)
    smtp.quit()

    print("Email sent successfully")
    return "Email sent successfully"

# confirm email registeration
def send_email_confirm_registration(username,password, code, to_email):
    HOST = "smtp-mail.outlook.com"
    PORT = 587

    FROM_EMAIL = emails["outlook1"]

    MESSAGE = f"""Subject: Send email from Nhom13

    Hello {username} are you register new acc .

    Here are your code :

    {code}

    Remember your code is only valid for 3 minutes
    """

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, password)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(FROM_EMAIL, to_email, MESSAGE)
    smtp.quit()

    print("Email sent successfully")
    return "Email sent successfully"
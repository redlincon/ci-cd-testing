import requests
import email_template


def PaymentHubMonitor_handler(event, context):
    response = requests.get("https://dev.simusolar.lamt.app/payments/")

    if response.status_code == 200:
        output = "REQUEST HAS BEEN SENT SUCCESSFULLY"
        return output

    else:
        output = "REQUEST FAILED"
        email_template.send_email()
        return output

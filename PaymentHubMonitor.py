import requests
import email_template


def PaymentHubMonitor_handler(event, context):
    response = requests.get("https://dev.simusolar.lamt.app/payments/")

    if response.status_code == 200:
        email_template.send_email()
        output = "REQUEST HAS BEEN SENT SUCCESSFULY"
        return output

    else:
        output = "REQUEST FAILED"
        return output

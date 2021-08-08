import boto3

def send_email():
    SENDER = "PAYMENT HUB LAMBDA FUNCTION <redlincon@gmail.com>"

    RECIPIENT = "redlincon@gmail.com"

    AWS_REGION = "us-east-2"

    SUBJECT = "PAYMENT HANDLER IS OFF"

    BODY_TEXT = ("PAYMENT HANDLER IS DOWN\r\n"
                 "PLEASE CLICK <a href='https://app.datadoghq.com/logs?from_ts=1626523613058&index=&live=true&query=&to_ts=1626524513058'>HERE</a> TO VIEW THE LOGS SO THAT YOU CAN TRACK AND SOLVE THE ISSUE\r\n"
                 "From the Payment Hub Lambda Function"
                 )

    BODY_HTML = """<html>
        <head></head>
            <body>
                <h1>PAYMENT HANDLER IS DOWN</h1>
                    <p>THE PAYMENT HANDLER IS DOWN. PLEASE CLICK
                    <a href='https://app.datadoghq.com/logs?from_ts=1626523613058&index=&live=true&query=&to_ts=1626524513058'>HERE</a> TO VIEW THE LOGS SO THAT YOU CAN TRACK AND SOLVE THE ISSUE\r\n
                    </p>
                    <p>From the Payment Hub Lambda Function me</p>
            </body>
        </html>
            """

    CHARSET = "UTF-8"

    client = boto3.client('ses',region_name=AWS_REGION)

    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER

    )

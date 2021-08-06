import unittest
import httpretty
import requests


class PaymentHubTest(unittest.TestCase):
    def test_ifTheConnectionIsAlive(self):
        httpretty.enable()
        httpretty.register_uri(
            method=httpretty.GET,
            uri='https://dev.simusolar.lamt.app/payments/',
            status=200,
            body="HTTPretty"
        )

        response = requests.get("https://dev.simusolar.lamt.app/payments/")
        self.assertEqual(response.status_code, 200)

        httpretty.disable()
        httpretty.reset()

    def test_ifTheConnectionIsBroken(self):
        httpretty.enable()
        httpretty.register_uri(
            method=httpretty.GET,
            uri='https://dev.simusolar.lamt.app/payments/',
            status=400,
            body="HTTPretty"
        )

        response = requests.get("https://dev.simusolar.lamt.app/payments/")
        self.assertEqual(response.status_code, 400)

        httpretty.disable()
        httpretty.reset()


if __name__ == '__main__':
    unittest.main()

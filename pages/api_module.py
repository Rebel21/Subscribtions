import requests


class ApiClient:

    def __init__(self):
        return

    def create_subscription(self, email, name, time):
        body = {
            "email": email,
            "name": name,
            "time": time
        }
        req = requests.post("http://127.0.0.1:4000/subscriptions", json=body)
        assert req.status_code == 200
        return req

    def get_subscriptions(self):
        req = requests.get("http://127.0.0.1:4000/subscriptions")
        assert req.status_code == 200
        return req

    def delete_subscriptions(self):
        req = requests.delete("http://127.0.0.1:4000/subscriptions")
        assert req.status_code == 200
        return req

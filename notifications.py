class Notifications:

    def send(self, message):
        raise NotImplementedError

class Email:

    def send(self, message):
        print(f"Message : {message}\nsent via Email")

class SMS:

    def send(self, message):
        print(f"Message :{message}\nsent via SMS")

class PushNotification:

    def send(self, message):
        print(f"Message :{message}\nsent via Push Notifications")

class WhatsApp:

    def send(self, message):
        print(f"Message : {message}\nsent via WhatsApp")

notifications = [Email(), SMS(), PushNotification()]

for notification in notifications:
    notification.send("This is notification design")
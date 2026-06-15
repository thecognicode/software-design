class Notifications:

    def send(self, message):
        raise NotImplementedError

class Email:

    def send(self, message):
        print(f"Message : {message}\nsent via Email")

class SMS:

    def send(self, message):
        print(f"Message :{message}\nsent via SMS")
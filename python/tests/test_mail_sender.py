from mail_sender import MailSender
from mail_sender import Request
from unittest.mock import MagicMock
def test_send_v1():
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    mail_sender = MailSender(HttpClient())
    user = User("Bob","bob@gmail.com")
    message = "Hello"
    postedRequest = mail_sender.send_v1(user,message)
    assert postedRequest.name == user.name and postedRequest.email == user.email and postedRequest.message == message


def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    client = HttpClient()
    mail_sender = MailSender(client)
    user = User("victor", "victor@gmail.com")
    message = "test spt"
    post = mail_sender.send_v2(user, message)
    assert(post.code == 200)

class HttpClient:
    def __init__(self):
        self.postedRequest = Request("","","","")
        self.baseUrl = ""

    def post(self,base_url, request):
        self.postedRequest.name = request.name
        self.postedRequest.email = request.email
        self.postedRequest.subject = request.subject
        self.postedRequest.message = request.message
        self.postedRequest.code = 200 if request.name == "victor" and request.email == "victor@gmail" and request.subject == "New notification" and request.message == "test spt" and baseUrl == "https://api.mailsender.com" else 503
        self.baseUrl = base_url
        return self.postedRequest
    
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
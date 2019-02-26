
def authenticate(user, password):
    print(f'user {user} has been authenticated')

def get_page_content(url):
    return '<html>Page content</html>'

def log(url):
    print(f'user requested Url = {url}')

def return_response(content):
    print(f'Response: {content}')

class Request:
    def __init__(self, user, password, url):
        self.user = user
        self.password = password
        self.url = url

class FrontController:
    def process(self, request):
        log(request.url)
        authenticate(request.user, request.password)
        content = get_page_content(request.url)
        return_response(content)

if __name__=='__main__':
    controller = FrontController()
    request = Request(url='http://example.com', user='user', password='12345')
    controller.process(request)

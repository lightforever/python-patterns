class WebBrowser:
    def get(self, url: str)->str:
        return '<html>Page text</html>'

class Parser:
    def parse(self, text:str)->str:
        text = text.replace('<html>', '').replace('</html>', '')
        return text

class Db:
    def __init__(self):
        self.records = []

    def save(self, text):
        self.records.append(text)
        print(f'Text = "{text}" saved in db')

class Crowler:
    def __init__(self):
        self.browser = WebBrowser()
        self.parse = Parser()
        self.db = Db()

    def process(self, url: str)->None:
        text = self.browser.get(url)
        text = self.parse.parse(text)
        self.db.save(text)

if __name__=='__main__':
    crowler = Crowler()
    crowler.process('http://ya.ru')
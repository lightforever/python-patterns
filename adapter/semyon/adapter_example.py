

class AmericanPlayer:

    location = 'Dallas'

    def play_soccer(self):
        print('we play by legs 11 on 11')

class EnglishPlayer:

    location = 'Liverpool'

    def play_football(self):
        print('we play by legs 11 on 11')

class ItalianPlayer:

    location = 'Turin'

    def giocare_calcio(self):
        print('we play by legs 11 on 11')

class Adapter:

    def __init__(self, obj, method):
        self.obj = obj
        self.obj.__dict__['adapted'] = method

    def adapted(self, **kwargs):
        self.obj.adapted(**kwargs)



if __name__ == '__main__':
    ap = AmericanPlayer()
    ep = EnglishPlayer()
    ip = ItalianPlayer()

    adapter_usa = Adapter(ap, ap.play_soccer)
    adapter_eng = Adapter(ep, ep.play_football)
    adapter_ita = Adapter(ip, ip.giocare_calcio)

    for p in [adapter_eng, adapter_ita, adapter_usa]:
        print(f'In {p.obj.location} ...')
        p.adapted()
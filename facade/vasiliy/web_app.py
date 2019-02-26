class DataBase:
    def create_infrastructure(self):
        print('schemas created')

    def run(self):
        print('db started')

    def stop(self):
        print('db stopped')


class DjangoApp:
    def start(self):
        print('django app started')

    def stop(self):
        print('django app stopped')


class CeleryWorker:
    def start(self):
        print('celery worker started')

    def stop(self):
        print('celery worker stopped')


class WebApp:
    def __init__(self):
        self.db = DataBase()
        self.celery = CeleryWorker()
        self.django_app = DjangoApp()

    def run(self):
        self.db.run()
        self.db.create_infrastructure()

        self.celery.start()
        self.django_app.start()

    def stop(self):
        self.django_app.stop()
        self.celery.stop()
        self.db.stop()


if __name__ == '__main__':
    app = WebApp()
    app.run()
    print('---')
    app.stop()

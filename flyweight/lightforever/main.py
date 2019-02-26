from datetime import datetime, timedelta
from copy import copy

class FileChange:
    def __init__(self, folder:str, name:str, date_created: datetime, date_modified: datetime):
        self.folder = folder
        self.name = name
        self.date_created = copy(date_created)
        self.date_created2 = copy(date_created)
        self.date_modified = copy(date_modified)

class File:
    def __init__(self, folder: str, name: str, date_created: datetime, date_created2: datetime):
        self.folder = folder
        self.name = name
        self.date_created = date_created
        self.date_created2 = date_created2

    def key(self):
        return hash(f'folder={self.folder},name={self.name},date_created={self.date_created},date_created2={self.date_created2}')

class FileChangeFlyweight:
    _files = dict()

    def __init__(self, folder: str, name: str, date_created: datetime, date_modified: datetime):
        file = File(folder, name, copy(date_created), copy(date_created))
        if file.key() not in FileChangeFlyweight._files:
            FileChangeFlyweight._files[file.key()] = file
        else:
            file = FileChangeFlyweight._files[file.key()]

        self.file = file
        self.date_modified = date_modified

if __name__=='__main__':
    objects = []
    dt = datetime.now()
    modified = datetime.now()+ timedelta(days=10)
    folder = '/home'
    name = 'log.txt'
    for i in range(10**6):
        objects.append(FileChange(folder, name, dt, modified))

    objects = []
    for i in range(10**6):
        objects.append(FileChangeFlyweight(folder, name, dt, modified))



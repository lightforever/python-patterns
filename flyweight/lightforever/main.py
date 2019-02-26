from datetime import datetime

class FileChange:
    def __init__(self, folder:str, name:str, date_created: datetime, date_modified: datetime):
        self.folder = folder
        self.name = name
        self.date_created = date_created
        self.date_modified = date_modified

class File:
    def __init__(self, folder: str, name: str, date_created: datetime):
        self.folder = folder
        self.name = name
        self.date_created = date_created

    def key(self):
        return hash(f'folder={self.folder},name={self.name},date_created={self.date_created}')

class FileChangeFlyweight:
    _files = dict()

    def __init__(self, folder: str, name: str, date_created: datetime, date_modified: datetime):
        file = File(folder, name, date_created)
        if file.key() not in FileChangeFlyweight._files:
            FileChangeFlyweight._files[file.key()] = file
        else:
            file = FileChangeFlyweight._files[file.key()]

        self.file = file
        self.date_modified = date_modified

if __name__=='__main__':
    objects = []
    dt = datetime.now()
    folder = '/home'
    name = 'log.txt'
    for i in range(10**2):
        objects.append(FileChange(folder, name, dt, dt))

    objects = []
    for i in range(10**2):
        objects.append(FileChangeFlyweight(folder, name, dt, dt))


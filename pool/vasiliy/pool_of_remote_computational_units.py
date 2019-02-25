from contextlib import AbstractContextManager
from time import sleep


class Server:
    def __init__(self):
        self.busy = False

    def do(self, task):
        print(f'do task: {task}')
        return 'done'


class ServersPool(AbstractContextManager):
    def __init__(self, max_servers=15):
        self.__pool = []
        self.__current_server = None
        self.max_servers = max_servers

    def __get_available_server(self):
        try:
            return next(filter(lambda s: not s.busy, self.__pool))
        except StopIteration:
            return None

    def __wait_for_free_server(self):
        sleep(2)
        self.__pool[0].busy = False

    def __enter__(self):
        server = self.__get_available_server()

        if server is None:
            if len(self.__pool) < self.max_servers:
                print('---create new server---')
                new_server = Server()
                new_server.busy = True
                self.__pool.append(new_server)
                self.__current_server = new_server
                return new_server

            else:
                print('---wait for server---')
                self.__wait_for_free_server()
                server = self.__get_available_server()
                server.busy = True
                self.__current_server = server
                return server

        else:
            print('---return available server---')
            server.busy = True
            self.__current_server = server
            return server

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__current_server is not None:
            self.__current_server.busy = False
            self.__current_server = None


if __name__ == '__main__':
    server_getter = ServersPool(3)

    for work in [f'work {i}' for i in range(10)]:
        with server_getter as server:
            print(server.do(work))  # it does not work because of lack of parallelism






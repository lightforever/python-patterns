class Robot:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Android:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


def robot_factory(type='robot', name='Mr. Robot'):
    if type == 'robot':
        return Robot(name)
    else:
        return Android(name, 'Android')


if __name__ == '__main__':
    print(robot_factory('robot', 'Chicken'))
    print(robot_factory('android', 'Jery'))

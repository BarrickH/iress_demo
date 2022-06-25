from app.coordinate import Coordinate


def place_validator(fn):
    def wrapper(self, *args, **kwargs):
        if self.cmd.strip().startswith('PLACE'):
            Coordinate().place_robot(self.cmd)
            self.placed = True
        if not self.placed:
            raise Exception(str('CMD place is missing'))
        return fn(self, *args, **kwargs)

    return wrapper


def move_validator(fn):
    def wrapper(self, *args, **kwargs):
        if self.cmd.strip() in {'RIGHT', 'LEFT', 'MOVE', 'REPORT'}:
            return fn(self, *args, **kwargs)
    return wrapper

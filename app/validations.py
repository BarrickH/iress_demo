from app.exceoptions import IncorrectPlaceException, IncorrectCoordinateCommand
import re

valid_cmd = {'PLACE','RIGHT', 'LEFT', 'MOVE', 'REPORT'}
face_directions = {'NORTH', 'EAST', 'SOUTH', 'WEST'}
square_coordinate_range = {0, 1, 2, 3, 4}


class CoordinateValidations:
    @staticmethod
    def position_destruction(position: list) -> tuple:
        x = int(position[0])
        y = int(position[1])
        new_face_direction = position[2]
        return x, y, new_face_direction

    @staticmethod
    def place_cmd_validation(place:str):
        place = place.strip()
        if not place.startswith('PLACE'):
            raise IncorrectPlaceException
        result = re.search(r"PLACE\s[0-4],[0-4],(NORTH+|SOUTH+|EAST+|WEST+)", place)
        if not result:
            raise IncorrectPlaceException
        return place

    @staticmethod
    def face_validate(face:str):
        if face not in face_directions:
            raise IncorrectCoordinateCommand

    @staticmethod
    def coordinate_validation_decorator(simulate_first=False):
        def coordinate_validation_decorator_inner(fn):
            def wrapper(self,*args,**kwargs):
                x = kwargs['x']
                y = kwargs['y']
                if simulate_first:
                    x += self._x
                    y += self._y
                if x not in square_coordinate_range or y not in square_coordinate_range:
                    raise IncorrectPlaceException
                return fn(self,*args, **kwargs)
            return wrapper
        return coordinate_validation_decorator_inner


def place_validator_decorator(fn):
    def wrapper(self, *args, **kwargs):
        if not self.placed:
            raise IncorrectPlaceException
        return fn(self, *args, **kwargs)

    return wrapper


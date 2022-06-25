from app.exceoptions import IncorrectPlaceException, IncorrectCoordinateCommand
import re

face_directions = {'NORTH', 'EAST', 'SOUTH', 'WEST'}
square_coordinate_range = {0, 1, 2, 3, 4}


class CoordinateValidations:
    @staticmethod
    def position_destruction(position):
        x = int(position[0])
        y = int(position[1])
        new_face_direction = position[2]
        return x, y, new_face_direction

    @staticmethod
    def place_cmd_validation(place):
        place = place.strip()
        if not place.startswith('PLACE'):
            raise IncorrectPlaceException
        result = re.search(r"PLACE\s[0-4],[0-4],(NORTH+|SOUTH+|EAST+|WEST+)", place)
        if not result:
            raise IncorrectPlaceException
        return place

    @staticmethod
    def face_validate(face):
        if face not in face_directions:
            raise IncorrectCoordinateCommand

    @staticmethod
    def coordinate_validation_decorator(fn):
        def wrapper(**kwargs):
            x = kwargs['x']
            y = kwargs['y']
            if x not in square_coordinate_range or y not in square_coordinate_range:
                raise IncorrectPlaceException
            return fn(x, y)
        return wrapper

    # def coordinate_validation(self, coordinate):
    #
    #     x, y, face = self.position_destruction(coordinate)
    #
    #     if x not in square_coordinate_range or y not in square_coordinate_range:
    #         raise IncorrectPlaceException
    #     if face not in face_directions:
    #         raise IncorrectCoordinateCommand

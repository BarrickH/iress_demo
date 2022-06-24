from app.exceoptions import IncorrectPlaceException

current_position = []
current_face_direction = ''
new_face_direction = ''
simulated_position = []
face_directions = {'NORTH', 'EAST', 'SOUTH', 'WEST'}


def coordinate_range():
    return {
        "square": {0, 1, 2, 3, 4}
    }


class Coordinate:

    def coordinate_validation(self, place):
        if not place.strip().startswith('PLACE'):
            raise IncorrectPlaceException
        raise IncorrectPlaceException

    def place_robort(self, cmd):
        if self.coordinate_validation(cmd):
            return
        print(cmd)
        pass



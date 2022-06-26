from app.validations import CoordinateValidations as cv


class Coordinate:
    current_face_direction = ''
    _x = 0
    _y = 0

    def __str__(self):
        return f'{self._x},{self._y},{self.current_face_direction}'

    def get_coordinate(self, place_cmd: str) -> tuple:
        place_list = place_cmd.split(' ')[1].split(',')
        return cv.position_destruction(place_list)

    @cv.coordinate_validation_decorator()
    def place_to_coordinate(self, x: int, y: int, face: str) -> None:
        cv.face_validate(face)
        self._x = x
        self._y = y
        self.current_face_direction = face

    @cv.coordinate_validation_decorator(simulate_first=True)
    def move_in_coordinate(self, x: int, y: int) -> None:
        self._x += x
        self._y += y

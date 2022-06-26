from app.command import Command
from app.exceoptions import IncorrectPlaceException
from app.coordinate import Coordinate


class Robot(Coordinate):
    def __init__(self):
        pass

    def go(self, cmd: str,r) -> None:
        new_command = Command(cmd)
        try:
            new_command.execute_command()
        except IncorrectPlaceException:
            return
        else:
            return
        finally:
            return

    def set_placed(self):
        self.placed=True

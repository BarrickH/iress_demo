from app.command import Command
from app.exceoptions import IncorrectPlaceException


class Robot:
    def __init__(self):
        pass

    def go(self, cmd: str) -> None:
        new_command = Command(cmd)
        try:
            new_command.execute_command()
        except IncorrectPlaceException:
            pass
        else:
            pass
        finally:
            pass

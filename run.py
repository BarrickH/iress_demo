from app.command import Command


def main():
    command = Command('')
    while True:
        cmd = input()
        command.go(cmd)


if __name__ == '__main__':
    main()

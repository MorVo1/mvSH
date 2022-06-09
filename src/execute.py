import sys
import errors

def execute(command, args):
    try:
        match command:
            case 'exit':
                sys.exit()
            case 'echo':
                print(' '.join(args))
            case _:
                raise errors.CommandNotFound(command)
    except errors.CommandNotFound as e:
        print(e.message)

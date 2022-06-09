import sys
import errors
import os

def execute(command, args):
    try:
        match command:
            case 'exit':
                sys.exit()

            case 'echo':
                print(' '.join(args))

            case 'cd':
                if len(args) < 1:
                    raise errors.NotEnoughArgs(command)
                os.chdir(args[0])

            case 'pwd':
                print(os.getcwd())

            case 'ls':
                for i in os.listdir():
                    if os.path.isdir(i):
                        print(f'\u001b[34m{i}/\u001b[0m')
                    else:
                        print(i)

            case _:
                raise errors.CommandNotFound(command)

    except errors.CommandNotFound as e:
        print(e.message)

    except errors.NotEnoughArgs as e:
        print(e.message)
        
    except FileNotFoundError as e:
        print('File not found.')

import sys

def execute(command, args):
    match command:
        case 'exit':
            sys.exit()
        case 'echo':
            print(' '.join(args))
        case _:
            print('Command not found')

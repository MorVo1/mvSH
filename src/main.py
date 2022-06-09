import parser as _parser
import json
import sys
import execute

config = json.load(open('config.json'))
parser = _parser.Parser()
constants = {
    'name': 'MVShell',
    'version': '0.0.1',
}

def main():
    raw = input(config['profiles'][0]['prompt'])
    cmd = parser.parse(raw)[0]
    args = parser.parse(raw)[1]
    print(cmd)
    execute.execute(cmd, args)

if __name__ == '__main__':
    main()

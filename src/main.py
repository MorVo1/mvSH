from asyncio import constants
import parser as _parser
import json
import execute

config = json.load(open('config.json'))
parser = _parser.Parser()
constants = {
    'sh_name': 'MVShell',
    'version': '0.0.1'
}

def prompt_formater(prompt:str):
    return prompt.replace('.u', config['profiles'][0]['user_name']).replace('.h', config['profiles'][0]['host_name'])
    
vars = {
    'prompt': prompt_formater(config['profiles'][0]['prompt'])
}

def main():
    while True:
        raw = input(vars['prompt'])
        cmd = parser.parse(raw)[0]
        args = parser.parse(raw)[1]
        execute.execute(cmd, args)


if __name__ == '__main__':
    main()

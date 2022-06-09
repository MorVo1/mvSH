import parser as _parser
import sys
import json
import execute
import os

config = json.load(open('..\config.json'))
parser = _parser.Parser()
constants = {
    'sh_name': 'MVShell',
    'version': '0.1.0'
}

current_profile = 0

if len(sys.argv) < 2:
    print('I see you are running MVShell without any arguments so i set up a default profile for you.')
    print('If you want to change profile: mvshell.py <profile (int)>\n Example: mvshell.py 1\n Tip: you can modify config.json to add more profiles.')
else:
    current_profile = int(sys.argv[1])

def prompt_formater(prompt:str):
    return prompt.replace('.u', config['profiles'][current_profile]['user_name'])\
    .replace('.h', config['profiles'][current_profile]['host_name'])\
    .replace('.d', os.getcwd())

vars = {
    'prompt': prompt_formater(config['profiles'][current_profile]['prompt'])
}

def update_prompt():
    vars['prompt'] = prompt_formater(config['profiles'][current_profile]['prompt'])

def main():
    while True:
        raw = input(vars['prompt'])
        cmd = parser.parse(raw)[0]
        args = parser.parse(raw)[1]
        execute.execute(cmd, args)
        update_prompt()

if __name__ == '__main__':
    main()

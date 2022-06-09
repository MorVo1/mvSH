from curses import raw
import shlex

class Parser:
    def __init__(self):
        self.raw = None
        self.command = None
        self.args = None
    def parse(self, raw):
        self.raw = raw
        self.command = shlex.split(raw)[0]
        self.args = shlex.split(raw)[1:]
        return self.command, self.args
    
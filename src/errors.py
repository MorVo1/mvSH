class CommandNotFound(Exception):
    def __init__(self, command):
        self.message = f"Command '{command}' not found."
        super().__init__(self.message)

class NotEnoughArgs(Exception):
    def __init__(self, command):
        self.message = f"Command '{command}' needs more arguments."
        super().__init__(self.message)
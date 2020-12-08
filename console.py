from enum import Enum

class ProgramStatus(Enum):
    READY = 1
    RUNNING = 2
    EXIT_NORMALLY = 3

class ConsoleExecutor:

    def __init__(self, program = []):
        self.accum = 0
        self.pos = 0
        self.program = program
        self.status = ProgramStatus.READY

    def nop(self, arg):
        self.pos += 1

    def jmp(self, arg):
        offset = int(arg)
        self.pos += offset

    def acc(self, arg):
        self.accum += int(arg)
        self.pos += 1

    def run_next(self):
        self.status = ProgramStatus.RUNNING
        if self.pos >= len(self.program):
            self.status = ProgramStatus.EXIT_NORMALLY
            return
        line = self.program[self.pos]
        command, args = line.split(' ')
        getattr(self, command)(args)

    def run(self):
        # maybe later to run  commands in batch
        pass
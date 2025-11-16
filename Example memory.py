class Memory:
    def __init__(self, size):
        self.data = bytearray(size)
    
    def load_program(self, program):
        self.data[:len(program)] = program

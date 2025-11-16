class CPU:
    def __init__(self, memory):
        self.memory = memory
        self.register = 0
    
    def step(self):
        # Example instruction: increment register
        self.register += 1
        print(f"CPU register: {self.register}")

from src.cpu import CPU
from src.memory import Memory
from src.display import Display

def main():
    memory = Memory(size=0xFFFF)
    cpu = CPU(memory)
    display = Display()
    
    # Load a demo program (legal, example binary)
    with open("examples/demo.bin", "rb") as f:
        program = f.read()
        memory.load_program(program)
    
    print("Starting emulator...")
    for _ in range(10):  # Run 10 cycles for demo
        cpu.step()
        display.render(cpu)

if __name__ == "__main__":
    main()

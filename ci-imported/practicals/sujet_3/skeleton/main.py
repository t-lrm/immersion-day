from skeleton.chip8 import Chip8

chip = Chip8(None)
chip.memory.load_rom("../other/examples/brick.ch8")
chip.run_program()

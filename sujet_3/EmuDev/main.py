from sujet_3.EmuDev.chip8 import Chip8

chip = Chip8(None)
chip.memory.load_rom('../Roms/brick.ch8')
chip.run_program()
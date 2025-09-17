import os
from pathlib import Path
from EmuDev.custom_types import UShort, Byte


class Memory:
    def __init__(self):
        self.registers = [Byte(0)] * 16
        self.ram = [Byte(0)] * 4096

        font = [
            0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
            0x20, 0x60, 0x20, 0x20, 0x70,  # 1
            0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
            0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
            0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
            0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
            0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
            0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
            0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
            0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
            0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
            0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
            0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
            0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
            0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
            0xF0, 0x80, 0xF0, 0x80, 0x80,  # F
        ]

        # Load font into RAM
        for i, byte in enumerate(font):
            self.ram[i] = byte

    def read_short(self, i: UShort) -> UShort:
        """Reads a 16-bit value from RAM (big-endian)."""
        return UShort((self.ram[i] << 8) | self.ram[i + 1])

    def load_rom(self, file_path: str) -> None:
        """Loads a ROM file into RAM at address 0x200."""
        rom_path = Path(file_path)
        if not rom_path.is_absolute():
            rom_path = Path(__file__).parent / file_path

        rom_path = rom_path.resolve()
        if not rom_path.exists():
            raise FileNotFoundError(f"Cannot find the file at location {rom_path}")

        # Read the file as a list of bytes (r = read, b = binary)
        with open(rom_path, "rb") as f:
            file_bytes = list(f.read())

        if len(file_bytes) > len(self.ram) - 0x200:
            raise ValueError("ROM is too big.")

        # Load ROM into RAM starting at 0x200
        self.ram[0x200:0x200 + len(file_bytes)] = file_bytes
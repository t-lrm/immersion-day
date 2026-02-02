import time


class Display:

    def __init__(self):
        self._memory = [False] * (32 * 64)
        self.CPF = 10  # cycles per frame
        self.DISPLAY_W = 2 * 64 + 2 + 1  # 2 per pixel, 2 for borders, one for '\n'
        self.DISPLAY_H = 34
        self.str = [" "] * (self.DISPLAY_W * self.DISPLAY_H)
        self._cycle = 0

        # Horizontal lines
        for i in range(1, self.DISPLAY_W - 2):
            self.str[i] = "-"
            self.str[(self.DISPLAY_H - 1) * self.DISPLAY_W + i] = "-"

        # Vertical lines
        for i in range(self.DISPLAY_H):
            self.str[i * self.DISPLAY_W] = "|"
            self.str[(i + 1) * self.DISPLAY_W - 2] = "|"
            self.str[(i + 1) * self.DISPLAY_W - 1] = "\n"

    def __getitem__(self, i):
        return self._memory[i]

    def __setitem__(self, i, value):
        if self._memory[i] == value:
            return

        self._memory[i] = value

        c = "█" if value else " "
        x = i % 64
        y = i // 64
        idx = (y + 1) * self.DISPLAY_W + 2 * x + 1

        self.str[idx] = c
        self.str[idx + 1] = c

    def draw(self):
        self._cycle += 1
        if self._cycle < self.CPF:
            return
        self._cycle = 0
        print("".join(self.str))
        time.sleep(0.06)

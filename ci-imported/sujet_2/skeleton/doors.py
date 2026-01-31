class Door:
    def __init__(self, message, decoding):
        self.message = message
        self.decoding = decoding

    def read(self, key):
        return self.decoding(self.message, key)

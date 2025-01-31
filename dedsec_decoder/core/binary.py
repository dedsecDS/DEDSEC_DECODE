class BinaryConverter:
    @staticmethod
    def encode(message: str) -> str:
        return ' '.join(format(ord(char), '08b') for char in message)
    
    @staticmethod
    def decode(binary: str) -> str:
        try:
            return ''.join(chr(int(bits, 2)) for bits in binary.split())
        except ValueError:
            raise ValueError("Invalid binary message format")
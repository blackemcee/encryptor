import string

MORSE = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..'
        }


class YP100:
    """
    Кодировщик для преобразования строки в азбуку Морзе. Для кодирования
    принимает строку, выдает список, для раскодирования - необорот
    """
    def encrypt(self, text: str) -> list:
        new_text = []
        for char in text.lower():
            if char in MORSE:
                new_text.append(MORSE[char])
            else:
                new_text.append(char)
        return new_text

    def decrypt(self, text: list) -> str:
        new_text = ''
        for let in text:
            if let in MORSE.values():
                for key, value in MORSE.items():
                    if value == let:
                        new_text += key
            else:
                new_text += let
        return new_text

class YP200(YP100):
    """
    Кодировщик смещает каждую букву на n позиций вправо, после чего
    переводит строку в азбуку Морзе и разворачивает ее задом наперед
    """
    def encrypt(self, text: str, n) -> list:
        indexed_text = [string.ascii_lowercase.index(char) if
                        char in MORSE else char for char in text.lower()]
        moved_text = []
        for ind in indexed_text:
            if isinstance(ind, int):
                if ind + n > 25:
                    moved_text.append(ind + n - 26)
                else:
                    moved_text.append(ind + n)
            else:
                moved_text.append(ind)
        moved_string = ''
        for ind in moved_text:
            if isinstance(ind, int):
                moved_string += string.ascii_lowercase[ind]
            else:
                moved_string += ind
        return super().encrypt(moved_string)[::-1]

    def decrypt(self, text: list, n) -> str:
        dec_text = super().decrypt(text)
        indexed_text = [string.ascii_lowercase.index(char) if
                        char in MORSE else char for char in dec_text.lower()]
        moved_text = []
        for ind in indexed_text:
            if isinstance(ind, int):
                if ind - n < 0:
                    moved_text.append(26 - ind + n)
                else:
                    moved_text.append(ind - n)
            else:
                moved_text.append(ind)
        moved_string = ''
        for ind in moved_text:
            if isinstance(ind, int):
                moved_string += string.ascii_lowercase[ind]
            else:
                moved_string += ind
        return moved_string[::-1]
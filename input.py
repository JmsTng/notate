class Modifiers:
    """Data container for modifier keys."""
    
    LCTRL = 1073742048
    LSHIFT = 1073742049
    LALT = 1073742050
    WIN = 1073742051
    RCTRL = 1073742051
    RSHIFT = 1073742051
    RALT = 1073742051
    
    keys = [LCTRL, LSHIFT, LALT, WIN, RCTRL, RSHIFT, RALT]

class Specials:
    """Data container for special keys."""

    BACKSPACE = 8
    DELETE = 127
    ENTER = 13
    UP = 1073741906
    DOWN = 1073741905
    LEFT = 1073741904
    RIGHT = 1073741903

    keys = [BACKSPACE, DELETE, ENTER, UP, DOWN, LEFT, RIGHT]


class Input:
    """Handle and categorize input events."""

    EDITING = 0
    COMMAND = 1

    MODIFIERS = Modifiers()
    SPECIALS = Specials()

    def __init__(self):
        self.mode = self.EDITING
        self.text = []
        self.pos_offset = 0

    def handle_char(self, key: int):
        if key in Specials.keys:
            match key:
                case Specials.BACKSPACE:
                    if len(self.text) > 0:
                        self.text.pop(len(self.text) - self.pos_offset - 1)
                case Specials.DELETE:
                    if self.pos_offset > 0:
                        self.text.pop(len(self.text) - self.pos_offset)
                        self.pos_offset -= 1  # shift caret pointer instead of moving with delete
                case Specials.LEFT:
                    if self.pos_offset < len(self.text):
                        self.pos_offset += 1
                case Specials.RIGHT:
                    if self.pos_offset > 0:
                        self.pos_offset -= 1

        if key not in (Modifiers.keys + Specials.keys):
            self.append(chr(key))

    def append(self, key: str):
        if self.pos_offset:
            self.text.insert(-self.pos_offset, key)
        else:
            self.text.append(key)

    def get_text(self):
        return "".join(self.text)

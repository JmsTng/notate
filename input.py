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


class Input:
    """Handle and categorize input events."""

    EDITING = 0
    COMMAND = 1

    MODIFIERS = Modifiers()

    def __init__(self):
        self.mode = self.EDITING
        self.text = ""

    def append(self, key: int):
        if key == 8:  # if key is a backspace character, delete last character
            self.text = self.text[:-1]
        elif key not in self.MODIFIERS.keys:  # ignore modifier keys
            self.text += chr(key)

from pynput.keyboard import Controller


ROLL_THRESHHOLD = 3


class KeyboardManager:
    def __init__(self) -> None:
        self.lean_left = False
        self.lean_right = False
        self.keyboard = Controller()

    def update(self, data: dict) -> None:
        roll = data['roll']
        if roll > ROLL_THRESHHOLD and not self.lean_left:
            self.lean_left = True
            self.keyboard.press('q')
            print('q pressed')

        elif roll < -ROLL_THRESHHOLD and not self.lean_right:
            self.lean_right = True
            self.keyboard.press('e')
            print('e pressed')

        if -ROLL_THRESHHOLD < roll < ROLL_THRESHHOLD:
            if self.lean_left:
                self.keyboard.release('q')
                self.lean_left = False
                print('q released')
            elif self.lean_right:
                self.keyboard.release('e')
                self.lean_right = False
                print('e released')

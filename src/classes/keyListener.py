from pynput import keyboard

class KeyListener:
    def __init__(self, target) -> None:
        self.target = keyboard.KeyCode.from_vk(target).vk
        self.target_state = False

        self.registerListener(self.on_press, self.on_release)

    def registerListener(self, press, release):
        listener = keyboard.Listener(on_press=press, on_release=release)
        listener.start()

    def on_press(self, key):
        try:
            if key.vk == self.target:
                self.target_state = True
        except AttributeError:
            if key.value.vk == self.target:
                self.target_state = True

    def on_release(self, key):
        try:
            if key.vk == self.target:
                self.target_state = False
        except AttributeError:
            if key.value.vk == self.target:
                self.target_state = False
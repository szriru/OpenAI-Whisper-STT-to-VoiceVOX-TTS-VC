from pynput import mouse

class MouseListener:
    def __init__(self, target) -> None:
        self.target = self.get_target_button(target)
        self.target_state = False
        self.register_listener(self.on_click)

    def get_target_button(self, target):
        if target == 'mouse1':
            return mouse.Button.left
        elif target == 'mouse2':
            return mouse.Button.right
        elif target == 'mouse3':
            return mouse.Button.x1
        elif target == 'mouse4':
            return mouse.Button.x2
        else:
            raise ValueError("Invalid mouse target")

    def register_listener(self, click):
        listener = mouse.Listener(on_click=click)
        listener.start()

    def on_click(self, x, y, button, pressed):
        if button == self.target:
            if pressed:
                self.target_state = True
            else:
                self.target_state = False
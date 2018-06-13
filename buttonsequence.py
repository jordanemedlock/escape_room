from gpiozero import Button

class ButtonSequence(object):
    def __init__(self, tags, delegate, history_size=10, on_up=True):
        self.tags = tags
        self.buttons = [Button(k) for k, v in tags.iteritems()]
        self.delegate = delegate
        self.history = []
        self.history_size = history_size
        def button_up(dev):
            self.button_up(dev)
        for button in self.buttons:
            if on_up:
                button.when_released = button_up
            else:
                button.when_pressed = button_up
    def button_up(self, dev):
        tag = self.tags[dev.pin]
        if self.history_size == len(self.history):
            self.history = self.history[1:] + [tag]
        self.delegate(tag, self.history)
        return tag

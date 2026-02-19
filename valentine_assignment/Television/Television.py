class Television:
    def __init__(self):
        self.is_on = False
        self.volume = 5
        self.min_volume = 0
        self.max_volume = 100
        self.channel = 1
        self.min_channel = 1
        self.max_channel = 50

    def power(self):
        self.is_on = not self.is_on
        return self.is_on

    def turn_tv_on(self):
        self.is_on = True

    def turn_tv_off(self):
        self.is_on = False

    def increase_volume(self):
        if not self.is_on:
            return None
        if self.volume < self.max_volume:
            self.volume += 1
        return self.volume

    def get_volume(self):
        return self.volume

    def reduce_volume(self):
        if not self.is_on:
            return None
        if self.volume > self.min_volume:
            self.volume -= 1
        return self.volume

    def channel_up(self):
        if not self.is_on:
            return None
        if self.channel < self.max_channel:
            self.channel += 1
        return self.channel

    def get_channel(self):
        return self.channel

    def channel_down(self):
        if not self.is_on:
            return None
        if self.channel > self.min_channel:
            self.channel -= 1
        return self.channel






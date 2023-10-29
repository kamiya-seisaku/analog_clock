def update_class(self):
    print("Updating class...")
    now = time.localtime()
    hour = int(time.strftime("%I", time.strptime(str(now.tm_hour), "%H"))) * 5
    now = (hour + now.tm_min / 12, now.tm_min, now.tm_sec)
    len = [.7, 1, 1]

    for n, i in enumerate(now):
        x, y = self.canvas.coords(self.hands[n])[0:2]
        cr = [x, y]
        cr.append(len[n] * self.hand_length * math.cos(math.radians(i * 6) - math.radians(90)) + self.x)
        cr.append(len[n] * self.hand_length * math.sin(math.radians(i * 6) - math.radians(90)) + self.y)
        self.canvas.coords(self.hands[n], tuple(cr))

    if hasattr(self, '_job'):
        self.after_cancel(self._job)
    self._job = self.after(1000, self.update_class)
    print("Class updated.")

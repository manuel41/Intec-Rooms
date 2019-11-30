class Room(object):
    def __init__(self):
        self.name = ''
        self.monday = []
        self.tuesday = []
        self.wednesday = []
        self.thursday = []
        self.friday = []
        self.saturday = []

    def ParseTime(self, time, day):
        if day == 'monday':
            if time[0] != '0':
                self.monday.append(int(time[0]))
            else:
                self.monday.append(int(time[0:-3]))
            if time[2] != '0':
                self.monday.append(int(time[2]))
            else:
                self.monday.append(int(time[2:]))

        if day == 'tuesday':
            if time[0] != '0':
                self.tuesday.append(int(time[0]))
            else:
                self.tuesday.append(int(time[0:-3]))
            if time[2] != '0':
                self.tuesday.append(int(time[2]))
            else:
                self.tuesday.append(int(time[2:]))

        if day == 'wednesday':
            if time[0] != '0':
                self.wednesday.append(int(time[0]))
            else:
                self.wednesday.append(int(time[0:-3]))
            if time[2] != '0':
                self.wednesday.append(int(time[2]))
            else:
                self.wednesday.append(int(time[2:]))

        if day == 'thursday':
            if time[0] != '0':
                self.thursday.append(int(time[0]))
            else:
                self.thursday.append(int(time[0:-3]))
            if time[2] != '0':
                self.thursday.append(int(time[2]))
            else:
                self.thursday.append(int(time[2:]))

        if day == 'friday':
            if time[0] != '0':
                self.friday.append(int(time[0]))
            else:
                self.friday.append(int(time[0:-3]))
            if time[2] != '0':
                self.friday.append(int(time[2]))
            else:
                self.friday.append(int(time[2:]))

        if day == 'saturday':
            if time[0] != '0':
                self.saturday.append(int(time[0]))
            else:
                self.saturday.append(int(time[0:-3]))
            if time[2] != '0':
                self.saturday.append(int(time[2]))
            else:
                self.saturday.append(int(time[2:]))
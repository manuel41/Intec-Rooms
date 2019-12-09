class Room(object):
    def __init__(self):
        self.name = ''
        self.monday = []
        self.tuesday = []
        self.wednesday = []
        self.thursday = []
        self.friday = []
        self.saturday = []

    def ParseTime(self, time):
        ini, fin = 0, 0
        if time[1] == '/':
            ini = int(time[0])
            fin = int(time[2:])
            return [ini, fin]
        else:
            ini = int(time[0:2])
            fin = int(time[3:])
            return [ini, fin]

    def AddTime(self, time, tag):
        class_time = self.ParseTime(time)
        hours = class_time[1] - class_time[0]
        for x in range(hours):
            if tag == 3:
                if class_time[0] + x in self.monday:
                    continue
                self.monday.append(class_time[0] + x)
                self.monday.sort()
            if tag == 4:
                if class_time[0] + x in self.tuesday:
                    continue
                self.tuesday.append(class_time[0] + x)
                self.tuesday.sort()
            if tag == 5:
                if class_time[0] + x in self.wednesday:
                    continue
                self.wednesday.append(class_time[0] + x)
                self.wednesday.sort()
            if tag == 6:
                if class_time[0] + x in self.thursday:
                    continue
                self.thursday.append(class_time[0] + x)
                self.thursday.sort()
            if tag == 7:
                if class_time[0] + x in self.friday:
                    continue
                self.friday.append(class_time[0] + x)
                self.friday.sort()
            if tag == 8:
                if class_time[0] + x in self.saturday:
                    continue
                self.saturday.append(class_time[0] + x)
                self.saturday.sort()
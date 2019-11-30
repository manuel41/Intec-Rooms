class Room(object):
    def __init__(self):
        self.name = ''
        self.monday = []
        self.tuesday = []
        self.wednesday = []
        self.thursday = []
        self.friday = []
        self.saturday = []

    def ParseTime(time):
        ini, fin = 0, 0
        if time[1] == '/':
            ini = int(time[0])
            fin = int(time[2:])
            return [ini, fin]
        else:
            ini = int(time[0:2])
            fin = int(time[3:])
            return [ini, fin]
    def AddTime(self, time, day):
        class_time = self.ParseTime(time)
        hours = class_time[1] - class_time[0]
        for x in range(hours + 1):
            if day == 'monday':
                if class_time[0] + x in self.monday:
                    continue
                self.monday.append(class_time[0] + x)
                self.monday.sort()
            if day == 'tuesday':
                if class_time[0] + x in self.tuesday:
                    continue
                self.tuesday.append(class_time[0] + x)
                self.tuesday.sort()
            if day == 'wednesday':
                if class_time[0] + x in self.wednesday:
                    continue
                self.wednesday.append(class_time[0] + x)
                self.wednesday.sort()
            if day == 'thursday':
                if class_time[0] + x in self.thursday:
                    continue
                self.thursday.append(class_time[0] + x)
                self.thursday.sort()
            if day == 'friday':
                if class_time[0] + x in self.friday:
                    continue
                self.friday.append(class_time[0] + x)
                self.friday.sort()
            if day == 'saturday':
                if class_time[0] + x in self.saturday:
                    continue
                self.saturday.append(class_time[0] + x)
                self.saturday.sort()



if __name__ == '__main__':
    # room = Room()
    # print(room.ParseTime('18/20', 'monday'))
    # print(room.ParseTime('7/9', 'monday'))
    # print(room.ParseTime('9/11', 'monday'))
    # time = '18/20'
    # print(time[3:])
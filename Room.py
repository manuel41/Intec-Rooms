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



if __name__ == '__main__':
    # room = Room()
    # print(room.ParseTime('18/20', 'monday'))
    # print(room.ParseTime('7/9', 'monday'))
    # print(room.ParseTime('9/11', 'monday'))
    # time = '18/20'
    # print(time[3:])
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("등번호 변경:From %d to %d"%(self.back_number, new_number))

        self.back_number = new_number
    def __str__(self):
        return "Hello, My name is %s. I play in %s in center."%(self.name, self.position)
    
jinhyeon = SoccerPlayer("Jinhyeon", "MF",10)

print("현재, 선수의 등번호는:", jinhyeon.back_number)
jinhyeon.change_back_number(5)
print("현재, 선수의 등번호는:", jinhyeon.back_number)

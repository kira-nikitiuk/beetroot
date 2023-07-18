# Task 3
# TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.


CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.index = 0


    def first_channel(self):
        self.index = 0
        return self.channels[0]  


    def last_channel(self):
        self.index = len(CHANNELS) - 1
        return self.channels[-1]
    

    def turn_channel(self, N):
        if N > len(CHANNELS):
            self.index = 0
            return self.channels[0]
        else:
            self.index = N - 1
            return self.channels[N-1] 


    def next_channel(self):
        if self.index < len(CHANNELS) - 1: 
            self.index += 1
        else:
            self.index = 0
        return self.channels[self.index]


    def previous_channel(self):
        if self.index == 0: 
            self.index = len(self.channels) - 1
        else:
            self.index -=1
        return self.channels[self.index]


    def current_channel(self):
        return self.channels[self.index]


    def is_exist(self):
        print("if you want to know if there is a channel with this name press 1, if you want to know if there is a channel with this number press 2: ")
        self.choice  = int(input("input your choice: "))
        if self.choice == 1:
            self.name_ch = input("input name of the channel: ")
            if self.name_ch in CHANNELS:
                return "YES"
            else:
                return "NO"
        else:
            self.num_ch = int(input("input number of the channel: "))
            if self.num_ch in range(len(CHANNELS)):
                return "YES"
            else:
                return "NO"



pr1 = TVController(CHANNELS)
print(pr1.first_channel(),"\n")

print(pr1.last_channel(), "\n")

print(pr1.turn_channel(1))
print(pr1.turn_channel(3), "\n")

print(pr1.next_channel(), "\n")

print(pr1.previous_channel(), "\n")

print(pr1.current_channel(), "\n")

print(pr1.is_exist(), "\n")
       



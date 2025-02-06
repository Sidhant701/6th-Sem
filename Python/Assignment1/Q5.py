'''5. . Write a Python program using a Time class to input a given time in 24-hour format and convert it
to a 12-hour format with AM/PM. The program should also validate time strings to ensure they are
in the correct HH:MM:SS format. Implement a method to check if the time is valid and return an
appropriate message.'''

print('''Name: Sidhanta Barik, RegNo: 2241002049
-----------------------------------------''')
class Time:
    def __init__(self, timeStr):
        self.timeStr = timeStr
        self.validateTime()
        self.convertTo12Hour()

    def validateTime(self):
        try:
            hours, minutes, seconds = map(int, self.timeStr.split(':'))
            if hours < 0 or hours > 23 or minutes < 0 or minutes > 59 or seconds < 0 or seconds > 59:
                raise ValueError
            else:
                self.hours = hours
                self.minutes = minutes
                self.seconds = seconds
        except ValueError:
            print("Invalid time. Please enter valid time in HH:MM:SS format.")
            exit()
        
    def convertTo12Hour(self):
        if self.hours == 0:
            self.hours = 12
            self.period = "AM"
        elif self.hours < 12:
            self.period = "AM"
        elif self.hours == 12:
            self.period = "PM"
        else:
            self.hours -= 12
            self.period = "PM"
        self.timeStr = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {self.period}"

timeStr = input("Enter time in 24-hour format (HH:MM:SS): ")
time = Time(timeStr)
print(f"Time in 12-hour format: {time.timeStr}")

# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Enter time in 24-hour format (HH:MM:SS): 16:45:10
# Time in 12-hour format: 04:45:10 PM


# Name: Sidhanta Barik, RegNo: 2241002049
# -----------------------------------------
# Enter time in 24-hour format (HH:MM:SS): 29:45:65
# Invalid time. Please enter valid time in HH:MM:SS format.
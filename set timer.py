import time
import winsound   # For sound 

def set_timer():

    hours = int(input("Enter hours: "))
    mins = int(input("Enter minutes: "))
    secs = int(input("Enter seconds: "))

    total_seconds = hours * 3600 + mins * 60 + secs

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        hours, mins = divmod(mins, 60)

        timer_display = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print(timer_display,end="\r")

        time.sleep(1)
        total_seconds -= 1

    print("00:00:00")
    print("Time's up!")

    #Play beepsound until user press ctrl+c or stopped it.
    while True:
        winsound.Beep(1100,400)  # (frency, duration(in_minieconds))

        

set_timer()
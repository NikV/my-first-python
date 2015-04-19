import platform
import calendar
import time;


raw_input("\n\nPress the enter key to continue.")
print platform.machine()
print platform.version()
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks
cal = calandar.month(2015, 1)
print cal;

str = raw_input("Are you cool? ");

words = str.split() #split the sentence into individual words

if str in ['y', 'Y', 'yes', 'Yes', 'YES']:
    print("Cool!")
else:
    print("TROLOLOLO")



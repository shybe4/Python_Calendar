count = 0
dates = list()
events = list()
command = input("Enter What You Want to Do: ")
if command == "set":
    date = int(input("Enter Date: "))
    while command != set:
        if date == 0:
            break
        count = count + 1
        event = input("Enter Event: ")
        dates.insert(1, date)
        events.insert(1, event)
        for n in range(1, count):
            print("\n", n, "\t", dates[n], "\t", events[n])
#            print (events[n])
        date = int(input("Enter Date: "))

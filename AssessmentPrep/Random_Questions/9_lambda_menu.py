n = int(input("enter the number of events: "))

if n > 0:
    print("enter the details in CSV(Event Name, Event Type, Organizer Name)")

    event_list = []

    for i in range(n):
        event_list.append(list(map(str, input().split(","))))

    print(event_list)
    print("Filer:\n1)Using Event name\n2)Using Event type\n3)Using Organizer name")

    choice = int(input("choice: "))

    if choice == 1:
        event_name = input("Enter event name: ")
        ans = list(filter(lambda x: x[0] == event_name, event_list))
        for i in ans:
            print("|".join(i))

    elif choice == 2:
        event_type = input("enter event type: ")
        ans = list(filter(lambda x: x[1] == event_type, event_list))
        for i in ans:
            print("|".join(i))

    elif choice == 3:
        org_name = input("enter organiser name: ")
        ans = list(filter(lambda x: x[2] == org_name, event_list))
        for i in ans:
            print("|".join(i))

    else:
        print("invalid choice")


else:
    print("invalid input")
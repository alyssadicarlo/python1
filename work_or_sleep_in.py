day = int(input('Day (0-6)? '))

if day in [1,2,3,4,5]:
    print("Go to work")
elif day == 0 or day == 6:
    print("Sleep in")
else:
    print("Please enter a number between 0 and 6")
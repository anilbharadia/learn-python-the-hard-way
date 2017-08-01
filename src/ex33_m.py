def create_list(size, increament_by = 1):
    i = 0
    numbers = []

    while i < size:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increament_by
        print "Numbers now: ", numbers

        print "At the bottom i is %d" % i
    return numbers

size = int(raw_input("Enter the size: "))

print "The numbers: "

for num in create_list(size, 2):
    print num
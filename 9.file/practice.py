fruitList = []
while True:
    command = int(input("1 to insert fruit \n2 to list all fruits\n3 to load from file \n4 to save \n5 to exit\n"))
    if command == 1:
        fruitName = input("Fruit Name : ")
        fruitList.append(fruitName)
    elif command == 2:
        print(fruitList)
    elif command == 3:
        fileName = input("File Path :")
        file = open(fileName, 'r')
        tempList = []
        while True:
            fruit = file.readline()
            if len(fruit) == 0:
                break
            fruit = fruit.rstrip()
            tempList.append(fruit)
        fruitList = tempList
        print(fruitList)
    elif command == 4:
        fileName = input("File Path : ")
        file = open(fileName, 'w')
        for item in fruitList:
            file.write(item + "\n")
        file.close()
    elif command == 5:
        break


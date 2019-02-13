fruitList = []
while True:
    command = int(input("1 to insert fruit \n2 to list all fruits\n3 to load from file \n4 to save \n5 to exit\n"))
    if command == 1: # 1 입력시
        fruitName = input("Fruit Name : ")
        fruitList.append(fruitName)
    elif command == 2: # 2 입력시
        print(fruitList)
    elif command == 3: # 3 입력시
        fileName = input("File Path :") # 파일 경로 받기
        file = open(fileName, 'r')
        tempList = []
        while True:
            fruit = file.readline()
            if len(fruit) == 0:
                break
            fruit = fruit.rstrip() # \n과 같은 이스케이프 문자 없애기
            tempList.append(fruit) # 리스트에 더하기
        file.close()
        fruitList = tempList # 기존 리스트를 파일에서 읽어온 리스트도 바꿔치기
        print(fruitList)
    elif command == 4:
        fileName = input("File Path : ")
        file = open(fileName, 'w')
        for item in fruitList:
            file.write(item + "\n") # 3과 마찬가지인데 이번엔 줄바꿈 문자를 붙여서 저장해야함
        file.close()
    elif command == 5:
        break


def insert_fruit_name(list):
    fruit_name = input("Fruit Name : ")
    list.append(fruit_name)


def read_file():
    file_name = input("File Path :")  # 파일 경로 받기
    file = open(file_name, 'r')
    tmp_list = []
    while True:
        fruit = file.readline()
        if len(fruit) == 0:
            break
        fruit = fruit.rstrip()  # \n과 같은 이스케이프 문자 없애기
        tmp_list.append(fruit)  # 리스트에 더하기
    file.close()
    return tmp_list


def write_file(list):
    fruit_name = input("File Path : ")
    file = open(fruit_name, 'w')
    for item in list:
        file.write(item + "\n")  # 3과 마찬가지인데 이번엔 줄바꿈 문자를 붙여서 저장해야함
    file.close()


fruitList = []
while True:
    command = int(input("1 to insert fruit \n2 to list all fruits\n3 to load from file \n4 to save \n5 to exit\n"))
    if command == 1:  # 1 입력시
        insert_fruit_name(fruitList)
    elif command == 2:  # 2 입력시
        print(fruitList)
    elif command == 3:  # 3 입력시
        fruitList = read_file()  # 기존 리스트를 파일에서 읽어온 리스트도 바꿔치기
        print(fruitList)
    elif command == 4:
        write_file(fruitList)
    elif command == 5:
        break


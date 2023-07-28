if __name__ == "__main__":
    # numb_arr = []
    # for i in range(int(input("start value")), int(input("end value"))+ 1):
    #     if i %3 == 0 and i%5 ==0:
    #         numb_arr.append(i)
    #         print(numb_arr)


    start_value = int(input("Start:"))
    end_value = int(input("Final"))

    simple_num = []
    for i in range(start_value, end_value):
        flag = True
        for j in range(start_value, end_value):
            if i != 1 and i !=j:
                result = i%j
                if result == 0:
                    break

        if flag:
            simple_num.append(i)
            print(simple_num)



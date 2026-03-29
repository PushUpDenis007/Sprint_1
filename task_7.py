#num = int(input("Введите целое натуральное число: "))
def digit_root(num):
        answer = 0
        while num//10>0: # пока делится на 10
            for i in range(len(str(num))): #для каждой цифры
                answer += (num % 10) #добавить последнюю цифру
                num = num // 10 #удалить посленюю цифру
            num, answer = answer, 0  #переназначить для следующей итерации  
        print (num)

digit_root(123)   
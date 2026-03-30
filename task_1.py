#Строка содержит пять временных значений. Они записаны через запятую:
stroka = '1h 45m,360s,25m,30m 120s,2h 60s'
answer=0
#Напиши цикл, который посчитает общее количество минут. 
#Используй в решении методы split(), replace() и оператор in.
for i in stroka.split(","):
    for j in i.split():
        if "s" in j:
            answer+=(int(j.replace("s","")))/60
        elif "h" in j:
            answer+=(int(j.replace("h","")))*60
        else: answer+=(int(j.replace("m","")))

#Результат сохрани в переменную и выведи на экран. 
print(answer)
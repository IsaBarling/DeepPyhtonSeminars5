# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

cont = (" "*(2-len(str(i))) + str(i) + " X " + " "*(2-len(str(k))) + str(k) + " = " + " "*(2-len(str(i*k))) + str(i*k) for i in range (2, 10, 1) for k in range(2, 11, 1))
cont = list(cont)
cont2 = ((cont[i + 9*n + 36*y]) for y in range((len(cont)//50)+1) for i in range(0, 9) for n in range(4))
cont2 = list(cont2)
n = 0
c = True
print("\t\t\tТаблица умножения")
while(n < len(cont2)):
    print(cont2[n] + "\t" + cont2[n+1] + "\t" + cont2[n+2] + "\t" + cont2[n+3])
    n +=4
    if(n == 36):
        print()
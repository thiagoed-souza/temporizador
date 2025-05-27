import time

t = input("Digite o tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida!")
    quit()

# 120 / 60 = 2
# 150 / 60 = 2 | 30

while t: # 0 ---> False | 1, 2, ... --> True
    minutos, segundos = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutos, segundos) # Dessa forma podemos definir o formato dos minutos e segundos
    print(timer, end="\r")
    time.sleep(1)  # Dar lentidão ao timer
    t = t - 1



# 70 / 60 -> 1 | 10 -> TIMER: "1:10"
# 69 / 60 -> 1 | 9 -> TIMER: "1:90"

print("Tempo acabou!")


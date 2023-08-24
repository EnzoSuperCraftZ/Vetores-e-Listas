#Enzo Kail Vizalli
#IFRO Calama 1°B INFO
q0=0

#Questão 1

q1 = '''
q1l = []
for q1a in range(5):
    q1i = int(input("Mim dê um número: "))
    q1l.append(q1i)
print(q1l)
exit()'''


#Questão 2

q2 = '''
q2l = []
for q2a in range(4):
    q2i = int(input("Mim dê um número: "))
    q2l.append(q2i)
print(sorted(q2l))
print(sorted(q2l, reverse=True))
print(max(q2l))
exit()'''


#Questão 3

q3 = '''
q3l = [0]
for q3a in range(5):
    q3i = str(input("Mim dê um nome: "))
    q3l.append(q3i)
for q3a, q3b in enumerate(q3l[1:6], start = 1):
    print(q3a, q3b)'''



q4 = 0
q5 = 0
q6 = 0
q7 = 0
q8 = 0

q = int(input("Escolha qual questão quer fazer: "))
questões = [q0, q1, q2, q3, q4, q5, q6, q7, q8]
exec(questões[q])


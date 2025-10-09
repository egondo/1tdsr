from faker import Faker

obj = Faker('pt_BR')

arq = open('nomes.txt', mode='w')

for i in range(500000):
    arq.write(obj.name())
    arq.write("\n")

arq.close()
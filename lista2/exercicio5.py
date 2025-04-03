#entrada de dados
dias_uteis = int(input("Dias úteis: "))
horas_trabalhadas = int(input("Horas trabalhadas no mês: "))
salario_hora = float(input("Salário-hora: "))

jornada_obrigatoria = dias_uteis * 8

if horas_trabalhadas <= jornada_obrigatoria:
    salario_mensal = horas_trabalhadas * salario_hora
else:
    horas_extra = horas_trabalhadas - jornada_obrigatoria
    valor_hora_extra = horas_extra * salario_hora * 1.5
    print(f"valor hora extra: {valor_hora_extra}")
    salario_mensal = jornada_obrigatoria * salario_hora + valor_hora_extra

print(f"Salario mensal {salario_mensal}")
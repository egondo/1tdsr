distancia = float(input("Dist em metros: "))
tempo = float(input("Tempo em segundos: "))

velocidade = distancia / tempo
print(f"Velocidade: {velocidade} m/s")

dist_km = distancia / 1000
tempo_h = tempo / 3600

velo_kmh = dist_km / tempo_h
print(f"ou {velo_kmh} km/h")



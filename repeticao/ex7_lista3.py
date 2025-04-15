print(f"°F \t °C")

gf = 50.0

while gf <= 150.0:
    gc = 5 * (gf - 32) / 9
    print(f"{gf} \t {gc:.1f}")
    gf = gf + 1

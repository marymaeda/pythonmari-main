def celsius_para_fahrenheit(celsius):
    return (9 * celsius / 5) + 32

# Programa principal
temperatura_c = float(input("Digite a temperatura em graus Celsius: "))
temperatura_f = celsius_para_fahrenheit(temperatura_c)

print(f"{temperatura_c}°C correspondem a {temperatura_f:.2f}°F")
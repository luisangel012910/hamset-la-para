

balance_inicial = float(input("Ingrese el balance inicial de la cuenta: "))


interes = 0.055  # 5.5%


for i in range(1, 4):  
    balance_final = balance_inicial * (1 + interes) ** i
    print(f"Balance al final del año {i}: ${balance_final:.2f}")
interes= 0.04
capital= int(input("Introduce el dinero que tienes en el banco : "))
calculo_interes= capital*(1+interes)
calculo_interes2= calculo_interes*(1+interes)
calculo_interes3= calculo_interes2*(1+interes)

print(f"ahorros tras el primer {calculo_interes :.2f}")
print(f"ahorros tras el segundo {calculo_interes2 :.2f}")
print(f"ahorros tras el tercer {calculo_interes3 :.2f}")
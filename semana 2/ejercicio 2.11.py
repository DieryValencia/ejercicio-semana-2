
L = float(input("Ingrese el largo de la piscina:  "))
A = float(input("Ingrese el ancho de la piscina:  "))
H = float(input("Ingrese la altura de la piscina: "))
    
   
precio_por_metro_cubico = float(input("Ingrese el precio por metro cúbico de agua: "))
    
   
V = L * A * H
    
    
costo_total = V * precio_por_metro_cubico
    
    
print(f'{costo_total}$ El costo total por llenar la piscina ')



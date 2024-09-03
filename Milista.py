# ejemplos de uso de listas
Misnovias=["Agripina","Anastacia","Maria"]   
Misnumeros=[666, 77, 10]
# Mostrando mis novias
print(Misnovias)
# mostrando mis numeros raros
print(Misnumeros)
print("---accediendo a los elementos de la lista---")
print(Misnovias[-2])
if "Ana" in Misnovias:
  print("Si, 'Maria' esta en la lista de mis novias")
else:
  print("Chale no eres mi novia")
print("Numero de novias")
Nnovias=len(Misnovias)
print(f"Numero de novias = {Nnovias}")
print("ciclo for en listas")
posicion=0
for medianaranja in Misnovias:
  print(posicion," ",medianaranja)
  posicion=posicion+1
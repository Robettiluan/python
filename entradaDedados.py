salario01:float;salario02:float
nome01:str;nome02:str
idade01:int;idade02:int
sexo01:str; sexo02:str

nome01 = input ("digite o nome da primeira pessoa : ")
salario01 = float(input("digite o salario da primeira pessoa:"))
idade01 = int(input("digite a idade da primeira pessoa:"))
sexo01 = input("digite o sexo da primeira pessoa :")

nome02 = input("digite o nome da segunda pessoa :")
salario02 = float(input("digite o salario a segunda pessoa :"))
idade02 = int(input("digite da idade da segunda pessoa :"))
sexo02 = input(" digite o sexo da segunda pessoa :")

print("--------------------------------------------------")

print(f"nome da primeira pessoa : {nome01}")
print(f"salario da primeira pessoa :{salario01 :.2f}")
print(f"idade da primeira pessoa :{idade01}")
print(f"sexo da primeira pessoa : {sexo01}")
print("----------------------------------------")
print(f"nome da segunda pessoa : {nome02} ")
print (f"salario da segunda pessoa :{salario02:.2f}")
print(f"idade da segunda pessoa :{idade02}")    
print(f"sexo da segunda pessoa : {sexo02}")
print("---------------------------------------------")

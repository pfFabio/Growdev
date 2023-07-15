


#o python retira os elementos repetidos, usando set e {}
conjunto = ["maçã", "pera", "maçã"]
print(conjunto)
print(set(conjunto))
conjunto1 = {"maçã", "pera", "maçã"}
print(conjunto1)
conjunto2 = ["banana", "melancia"]
#update junta 2 conjuntos mas mistura a ordem
conjunto1.update(conjunto2)
print(conjunto1)
print(conjunto1.issubset()
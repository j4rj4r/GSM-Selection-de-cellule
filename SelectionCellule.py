print("Calcul automatique des paramètres A et B puis de possibilité d'association à une BTS")
RxLev = int(input("RxLev : "))
RxLev_Access_min = int(input("RxLev_Access_min : "))
A = RxLev - RxLev_Access_min
Ms_Tx_Pwr_Max_CCH = int(input("Ms_Tx_Pwr_Max_CCH : "))
Pmax = int(input("Pmax :"))
B = Ms_Tx_Pwr_Max_CCH - Pmax
print("[*]Qualité de la liaison descendante : " + str(A) + " dBm")
if A >= 0 :
	print("Liaison descendante assurée !")
else :
	print("Liaison descendante non assurée !")
print("[*]Qualité de la liaison montante : " + str(B) + " dBm")
if B <= 0 :
	print("Liaison montante assurée !")
else :
	print("Liaison montrant non assurée !")
if B > 0 :
	C1 = A - B
else :
	C1 = A - 0
print("[*]Critère d'affaiblissement C1 : " + str(C1) + " dBm")
if C1 >= 0 :
	print("Le mobile sera associé à cette cellule !")
else :
	print("Le mobile ne sera pas associé à cette cellule !")

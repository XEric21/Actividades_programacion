import time
from colorama import Fore, Back, Style, init
def menu_bienvenida():
	centro = "CIPFP LUIS SUÑER"
	print(Fore.BLUE+"|------ Control de Promoción del " +  centro + "------|") 
	print("|-----------------------------------------------------|"+Style.RESET_ALL)
	print(Fore.YELLOW+"|--------------- Entrando al sistema... --------------|")
	print("|-----------------------------------------------------|"+Style.RESET_ALL)
	time.sleep(3)
	print(Fore.GREEN +"|--------------------- Cargando... -------------------|"+ Style.RESET_ALL)
	time.sleep(5)
	print(Fore.BLUE+"|----------------------------------------------------------|")
	print("|--------------- Hola, Bienvenido/a al sistema ------------|"+Style.RESET_ALL)
	print(Fore.YELLOW+"|========= Registro del alumnado del " +  centro +"========|")
	print("|----------------------------------------------------------|"+Style.RESET_ALL)
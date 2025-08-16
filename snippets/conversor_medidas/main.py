import Modulos.convert

print("Bem vindo(a) ao conversor de Metros, Pés e Jardas!")

print("\n\n(1) - Converter Pes para Metros.")
print("\n(2) - Converter Metros para Pes.")
print("\n(3) - Converter Jardas para Metros.")
print("\n(4) - Converter Jardas para Pes.")

optionUser = int(input("\nSelecione uma opção: "))

if optionUser == 1:
    numberUser = int(input("\nInforme a quantidade de pes: "))
    convertedMeters = Modulos.convert.feet_to_meters(numberUser)
    print("\n" + str(numberUser) + " pés em metros são: " + str(convertedMeters) + " metros")
elif optionUser == 2:
    numberUser = int(input("\nInforme a quantidade de metros: "))
    convertedFeets = Modulos.convert.meters_to_feet(numberUser)
    print("\n" + str(numberUser) + " metros em pés são: " + str(convertedFeets) + " pés")
elif optionUser == 3:
    numberUser = int(input("\nInforme a quantidade de jardas: "))
    convertedFeets = Modulos.convert.yard_to_meters(numberUser)
    print("\n" + str(numberUser) + " jardas em metros são: " + str(convertedFeets) + " metros")
elif optionUser == 4:
    numberUser = int(input("\nInforme a quantidade de jardas: "))
    convertedFeets = Modulos.convert.yard_to_feet(numberUser)
    print("\n" + str(numberUser) + " jardas em pés são: " + str(convertedFeets) + " pés")
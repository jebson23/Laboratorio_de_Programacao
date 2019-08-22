command = input().upper()

distance = command.count('F') - command.count('T')

if distance < 0:
	print("O robo percorreu {} metros para tras.".format(distance * (-1)))

elif distance == 0:
	print('O robo esta na mesma posicao.')

else:
	print('O robo percorreu {} metros para frente.'.format(distance))
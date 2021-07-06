listaLogs = 'ListaDeOrdemDos200Logs.txt'
verificaPlagio = 'EhPlagio200.txt'
ConcatenacaoLogsEhPlagio = 'Lista200LogsEhPlagio.txt'

manipulador = open(listaLogs,'r')
logs_list = manipulador.readlines()

manipulador2 = open(verificaPlagio, 'r')
ehPlagio_list =  manipulador2.readlines()

print(logs_list)
print(ehPlagio_list)

concat_list = []

for i in range(len(logs_list)):
    logs = logs_list[i].rstrip()
    ehPlagio = ehPlagio_list[i].rstrip()

    concat = "{},{}\n".format(logs,ehPlagio)

    concat_list.append(concat)

print(concat_list)

manipulador3 = open(ConcatenacaoLogsEhPlagio,'w')
manipulador3.writelines(concat_list)

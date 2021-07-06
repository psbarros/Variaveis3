hoje = int(input())
diasPraFrente = int(input())

if(hoje < 0 or hoje > 6):
  print("A entrada",hoje, "eh invalida")

else:
  if(hoje == 0):
    diaAtual = "domingo"
  elif(hoje == 1):
    diaAtual = "segunda"
  elif(hoje == 2):
    diaAtual = "terca"
  elif(hoje == 3):
    diaAtual = "quarta"
  elif(hoje == 4):
    diaAtual = "quinta"
  elif(hoje == 5):
    diaAtual = "sexta"
  elif(hoje == 6):
    diaAtual = "sabado"
  
  futuro = (hoje+diasPraFrente) % 7
  if(futuro == 0):
    diaFuturo = "domingo"
  elif(futuro == 1):
    diaFuturo = "segunda"
  elif(futuro == 2):
    diaFuturo = "terca"
  elif(futuro == 3):
    diaFuturo = "quarta"
  elif(futuro == 4):
    diaFuturo = "quinta"
  elif(futuro == 5):
    diaFuturo = "sexta"
  elif(futuro == 6):
    diaFuturo = "sabado"

  print("Hoje eh",diaAtual,"e o dia futuro eh",diaFuturo)
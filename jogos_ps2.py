import csv
import datetime 
jogos = []

with open("playstation2_games_merge.csv", mode="r", encoding="utf-8-sig") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    jogos.append(linha)

def titulo(texto):
  print()
  print(texto)
  print("-"*40)

def informacoes_gerais(): 
  titulo("Total de Jogos e Desenvolvedoras/Publicadoras Distintas")
  
  dev = {}
  pub = {}

  for jogo in jogos:
    desenvolvedora = jogo['Developer']
    publicadora = jogo['Publisher']

    dev[desenvolvedora] = dev.get(desenvolvedora, 0) + 1
    
    pub[publicadora] = pub.get(publicadora, 0) + 1

  print(f"Total de jogos na lista: {len(jogos)}")
  print(f"Total de desenvolvedoras distintas: {len(dev)}")
  print(f"Total de publicadoras distintas: {len(pub)}")
  print("-" * 40)

while True:
  titulo("Análise de Dados: Jogos Lançados para PlayStation 2")
  print("1. Total de Jogos e Desenvolvedoras/Publicadoras Distintas")
  print("2. Os Primeiros 10 Jogos Lançados")
  print("3. Jogos Lançados na Europa porém não nos EUA")
  print("4. Comparar Top 10 de um ano com Geral")
  print("5. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    informacoes_gerais()
  elif opcao == 2:
    primeiros_10_jogos()
  elif opcao == 3:
    jogos_europa_nao_eua()
  elif opcao == 4:
    informacoes_gerais()
  else:
    break
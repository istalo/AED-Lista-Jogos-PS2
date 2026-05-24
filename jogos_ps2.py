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

def primeiros_jogos():
    titulo("Os Primeiros 20 Jogos Lançados")

    def arruma_data(data):
        ano = data[:4]
        try:
            return datetime.datetime.strptime(data[:10], "%Y-%m-%d")
        except:
            return datetime.datetime.strptime(f"{ano}-01-01", "%Y-%m-%d")

    jogos_ordenados = sorted(jogos, key=lambda x: arruma_data(x['First released']))

    for i in range(20):
        jogo = jogos_ordenados[i]
        print(f"{i+1}. {jogo['Title']} - Lançado em: {jogo['First released']}")

while True:
  titulo("Análise de Dados: Jogos Lançados para PlayStation 2")
  print("1. Total de Jogos e Desenvolvedoras/Publicadoras Distintas")
  print("2. Os Primeiros 20 Jogos Lançados")
  print("3. Jogos Lançados na Europa porém não nos EUA")
  print("4. Comparar Top 10 de um ano com Geral")
  print("5. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    informacoes_gerais()
  elif opcao == 2:
    primeiros_jogos()
  elif opcao == 3:
    jogos_europa_nao_eua()
  elif opcao == 4:
    informacoes_gerais()
  else:
    break
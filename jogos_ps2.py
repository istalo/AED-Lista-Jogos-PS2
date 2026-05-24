import csv
import datetime
import plotly.express as px
import webbrowser
jogos = []

with open("playstation2_games_merge.csv", mode="r", encoding="utf-8-sig") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    jogos.append(linha)

def titulo(texto):
  print()
  print(texto)
  print("-"*60)

def informacoes_gerais(): 
  titulo("Total de Jogos, Desenvolvedoras e Publicadoras Únicas")
  
  dev = {}
  pub = {}

  for jogo in jogos:
    desenvolvedora = jogo['Developer']
    publicadora = jogo['Publisher']

    dev[desenvolvedora] = dev.get(desenvolvedora, 0) + 1
    
    pub[publicadora] = pub.get(publicadora, 0) + 1

  print(f"Jogos Lançados: {len(jogos)}")
  print(f"Desenvolvedoras Únicas: {len(dev)}")
  print(f"Publicadoras Únicas: {len(pub)}")
  print("-" * 60)

  resposta = input("Deseja gerar um gráfico com esses dados? (S/N): ").strip().upper()

  if resposta == 'S':
    valores = [len(jogos), len(dev), len(pub)]
    
    fig = px.bar(
        x=['Jogos', 'Desenvolvedoras', 'Publicadoras'],
        y=valores,
        title="Visão Geral das Informações",
        text=valores
    )

    fig.update_traces(textposition='outside') 

    fig.show()

def primeiros_jogos():
    titulo("Primeiros 20 Lançamentos")

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
    print("-"*60)

def jogos_todas_regioes():
  titulo("Jogos Lançados Mundialmente")

  count = 0
  for jogo in jogos:
    if jogo['JP'] == 'Released' and jogo['EU/PAL'] == 'Released' and jogo['NA'] == 'Released':
      count += 1

  print(f"Total de Lançamentos Mundiais: {count}")
  print("-"*60)

def jogos_regiao():
  titulo("Número de Exclusivos por Região")

  set_jp = set()
  set_eu = set()
  set_na = set()
  for jogo in jogos:
    if jogo['JP'] == 'Released':
      set_jp.add(jogo['Title'])
    if jogo['EU/PAL'] == 'Released':
      set_eu.add(jogo['Title'])
    if jogo['NA'] == 'Released':
      set_na.add(jogo['Title'])

  apenas_jp = set_jp - (set_eu | set_na)
  apenas_eu = set_eu - (set_jp | set_na)
  apenas_na = set_na - (set_jp | set_eu)

  print(f"Exclusivos do Japão: {len(apenas_jp)}")
  print(f"Exclusivos da Europa: {len(apenas_eu)}")
  print(f"Exclusivos da América do Norte: {len(apenas_na)}")
  print("-"*60)

  resposta = input("Deseja gerar um gráfico com esses dados? (S/N): ").strip().upper()

  if resposta == 'S':
    fig = px.pie(
        names=['Japão', 'Europa', 'América do Norte'],
        values=[len(apenas_jp), len(apenas_eu), len(apenas_na)],
        title="Distribuição de Exclusivos por Região"
    )
    
    fig.show()

while True:
  titulo("Análise de Dados: Jogos Lançados para PlayStation 2")
  print("1. Total de Jogos, Desenvolvedoras e Publicadoras Únicas")
  print("2. Primeiros 20 Lançamentos")
  print("3. Jogos Lançados Mundialmente")
  print("4. Número de Exclusivos por Região")
  print("5. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    informacoes_gerais()
  elif opcao == 2:
    primeiros_jogos()
  elif opcao == 3:
    jogos_todas_regioes()
  elif opcao == 4:
    jogos_regiao()
  elif opcao == 5:
    break
  elif opcao == 2000:
    webbrowser.open("https://www.youtube.com/watch?v=Cxk1gI2sg3w")
  else:
    print("Opção inválida. Tente novamente...\n(Psst... Tem um easter egg nas opções!).")

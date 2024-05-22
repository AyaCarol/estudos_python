import random

# ● ┌ ─ ┐ │ └  ┘ ♥

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dados_variacao = {
    1: ("┌─────────┐",
        "│         │",
        "│    ♥    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ♥      │",
        "│         │",
        "│      ♥  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ♥      │",
        "│    ♥    │",
        "│      ♥  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ♥   ♥  │",
        "│         │",
        "│  ♥   ♥  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ♥   ♥  │",
        "│    ♥    │",
        "│  ♥   ♥  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ♥   ♥  │",
        "│  ♥   ♥  │",
        "│  ♥   ♥  │",
        "└─────────┘"),
}

dados = []
total = 0
numero_dados = int(input("Quantos dados?: "))

for dado in range(numero_dados):
    dados.append(random.randint(1, 6))

#for die in range(num_of_dice):
#   for line in dados_variacao.get(dice[die]):
#       print(line)

for line in range(5):
    for dado in dados:
        print(dados_variacao.get(dado)[line], end="")
    print()

for dado in dados:
    total += dado
print(f"total: {total}")
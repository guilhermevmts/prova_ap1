# 1- Faca um for loop no dicionario e exiba os valores de cada tipo: 
tipos_cores = {
    'primaria': ['vermelho', 'azul', 'amarelo'],
    'secundaria': ['verde', 'laranja', 'roxo'],
    }

for tipo, cores in tipos_cores.items():
    print(f"Cores {tipo}:")
    for cor in cores:
        print(f" - {cor}")

# 2 - Faca um for loop na lista e mostre qual tipo ela é
lst_cores = ['vermelho', 'roxo', 'preto'] 
for cor in lst_cores:
    for tipo, cores in tipos_cores.items():
        if cor in cores:
            print(f"A cor {cor} é {tipo}.")
            encontrado = True
            break
    if not encontrado:
        print(f"A cor {cor} não pertence a nenhum tipo conhecido.")




# 3 – Verifique o total da compra baseado no preco
precos = {
    'camiseta': 100.00,
    'tenis': 900.00,
    'meia': 45.00,
    'blusa': 245.00,
    'calça': 145.00,
    'luva': 18.00,
    }

compra = ['luva', 'blusa', 'tenis']

total_compra = 0
for item in compra:
    if item in precos:
        total_compra += precos[item]

print(f"O total da compra é: R$ {total_compra:.2f}")

# 4 – Faca uma funcao que entre 3 notas e calcule a media
#  final de acordo com o crirterio de nota do ibmec
# Crie uma pasta meu_pacote e grava essa funcao la dentro
# Importe a funcao, e chame ela, calculando a media final
p1 = 8.5
p2 = 9.0
ac = 1.0

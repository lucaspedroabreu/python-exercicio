# -*- coding: utf-8 -*-

# Lista inicial de candidatos e seus resultados
lista_de_candidatos = [
    {'id': 1, 'nome_completo': 'Luana', 'resultado': 'e5_t10_p8_s8'},
    {'id': 2, 'nome_completo': 'Wash', 'resultado': 'e10_t7_p7_s8'},
    {'id': 3, 'nome_completo': 'Nicholas', 'resultado': 'e8_t5_p4_s9'},
    {'id': 4, 'nome_completo': 'Guilherme', 'resultado': 'e2_t2_p2_s1'},
    {'id': 5, 'nome_completo': 'Marlon', 'resultado': 'e10_t10_p8_s9'},
    {'id': 6, 'nome_completo': 'Lucas Pedro', 'resultado': 'e9_t9_p8_s9'},
    {'id': 7, 'nome_completo': 'Francisco', 'resultado': 'e10_t10_p6_s9'}
]

# Notas de corte padrão que serão atualizadas pelo usuário, caso queira
notas_de_corte = {
    "e": 6,
    "t": 6,
    "p": 6,
    "s": 6
}

# Entrada de novos candidatos
while True:
    comando = input("Deseja cadastrar um novo candidato? (s/n): ").lower()
    if comando == 's' or comando == 'sim':
        id_cadastro = len(lista_de_candidatos) + 1
        nome_completo_cadastro = input("Qual o nome completo do novo candidato?")
        resultado_cadastro = input("Digite o resultado do candidato no formato 'eX_tX_pX_sX': ")
        lista_de_candidatos.append({'id': id_cadastro, 'nome_completo': nome_completo_cadastro, 'resultado': resultado_cadastro})

    elif comando == 'n' or comando == 'não' or comando == 'nao':
        break
    else:
        print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")

# Busca por candidatos que atendem aos critérios
while True:
    comando = input("\nA nota padrão é 6 para todas as avaliações.\nDeseja definir os critérios de corte dos candidatos? (s/n):").lower()
    if comando == 's' or comando == 'sim':
        notas_de_corte['e'] = int(input("Digite a nota mínima para a entrevista: "))
        notas_de_corte['t'] = int(input("Digite a nota mínima para o teste teórico: "))
        notas_de_corte['p'] = int(input("Digite a nota mínima para o teste prático: "))
        notas_de_corte['s'] = int(input("Digite a nota mínima para a avaliação de soft skills: "))
    elif comando == 'n' or comando == 'não' or comando == 'nao':
        break
    else:
        print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")


# Função para extrair as notas do resultado de um candidato
def extrair_notas(resultado):
    notas_com_prefixo = resultado.split('_')
    notas_sem_prefixo = [int(nota[1:]) for nota in notas_com_prefixo]
    
    return notas_sem_prefixo

# Função para selecionar candidatos com base nas notas de corte
def selecionar_candidatos(notas_de_corte, lista_de_candidatos):
    candidatos_selecionados = []
    for candidato in lista_de_candidatos:
        e, t, p, s = extrair_notas(candidato['resultado'])
        if e >= notas_de_corte['e'] and t >= notas_de_corte['t'] and p >= notas_de_corte['p'] and s >= notas_de_corte['s']:
            candidatos_selecionados.append(candidato['nome_completo'])
    return candidatos_selecionados

selecionados = selecionar_candidatos(notas_de_corte, lista_de_candidatos)
print(f'Candidatos que atendem os critérios: {selecionados}')

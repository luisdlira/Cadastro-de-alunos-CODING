alunos = []

def adicionar_aluno(alunos):
    while True:
        nome_aluno = input('\nQual o nome do aluno que deseja cadastrar?\nR:').strip()
        while True:
            try:
                idade_aluno = int(input('\nQual a idade do aluno?\nR: '))
                if idade_aluno <= 0 or idade_aluno > 100:
                    print('Idade Inválida! Coloque uma idade existente!')
                else:
                    break
            except ValueError:
                print('Idade inválida! Tente novamente colocando uma idade válida.')
        while True:
            try:
                nota_aluno = float(input('Qual a nota do aluno?\nR: '))
                if nota_aluno < 0 or nota_aluno > 10:
                    print('\nNota inválida! A nota deve estar entre 0 e 10. Tente novamente.')
                else:
                    break
            except ValueError:
                print('\nEntrada inválida! Por favor, insira um número válido para a nota.')
        alunos.append({'nome': nome_aluno, 'idade': idade_aluno, 'nota':nota_aluno})
        while True:
            mais_adicao = input('\nVocê deseja cadastrar mais algum aluno? [Y/N]\nR:').upper()
            if mais_adicao not in ['Y', 'N']:
                print('\nResposta Inválida! tente novamente, apenas utilizando "Y" para sim e "N" para não.')
            elif mais_adicao == 'N':
                print('\n---------------------------------------------')
                print('Aluno(s) adicionado(s)! Voltando para o início!')
                print('-----------------------------------------------')
                return
            else:
                break

def listar_alunos(alunos):
    if len(alunos) == 0:
        print('\n\nNão temos nenhum estudante cadastrado no sistema ainda! Voltando para o menu!')
    else:
        print('\nListando todos os alunos encontrados no banco de dados...\n')
        print('====================================================')
        for aluno in alunos:
            print(f"\n4Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")
            print('====================================================')

def aluno_pelo_nome(alunos):
    if len(alunos) == 0:
        print('\n\nNão temos nenhum estudante cadastrado no sistema ainda! Voltando para o menu!')
    else:
        while True:
            aluno_nome = input('\nDigite o nome do aluno que deseja buscar\nOu digite "Voltar" se quiser ir de volta para o menu!:\nR: ').strip().lower()
            if aluno_nome == 'voltar':
                return
            encontrado = False
            for aluno in alunos:
                if aluno['nome'].lower() == aluno_nome:
                    print(f"\nNome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")
                    encontrado = True
                    return
            if not encontrado:
                print('\nAluno não encontrado!')        

def remover_aluno(alunos):
    if len(alunos) == 0:
        print('\n\nNão existem alunos cadastrados no sistema ainda!')
    else:
        while True:
            aluno_removido = input('\nQual o aluno que você deseja remover?\nR:').strip().lower()
            encontrado = False
            for aluno in alunos:
                if aluno_removido == aluno['nome'].strip().lower():
                    alunos.remove(aluno)
                    print('\nAluno removido!\n')
                    encontrado = True
                    break
            if not encontrado:
                    print('\nAluno não encontrado! Tente novamente!')
                    continue
            if len(alunos) == 0:
                print('\nNão há mais alunos cadastrados!')
                return
            while True:
                mais_remocao = str(input('Você deseja remover mais algum aluno? [Y/N]\nR:')).strip().upper()
                if mais_remocao not in ['Y', 'N']:
                    print('Resposta inválida! Tente novamente utilizando "Y" para SIM e "N" para não')
                elif mais_remocao == 'N':
                    return
                else:
                    print('Removendo outro aluno')
                    break

def media_notas(alunos):
    if len(alunos) == 0:
        print('\nAinda não temos alunos para fazer a média das notas! Volte novamente quando existir mais alunos registrados!')
    else:
        nota_geral = 0
        for nota in alunos:
            nota_geral += nota['nota']
        media_geral = nota_geral / len(alunos)
        print(f'\nA média geral das notas dos alunos registrados é: {media_geral:.2f}\n')
        
def menu():
    while True:
        print('''\n
===============================
 SISTEMA DE CADASTRO DE ALUNO
===============================

1.) Adicionar um aluno
2.) Listar todos os alunos
3.) Buscar aluno pelo nome
4.) Remover Aluno
5.) Mostrar média geral das notas
6.) Sair
''')
        opcao = ''
        while opcao not in ['1','2','3','4','5','6']:
            opcao = input('\nQual opção você deseja escolher? ').strip()
            if opcao not in ['1','2','3','4','5','6']:
                print('\nOpção inválida. Tente novamente escolhendo as opções de 1 a 6!')
        if opcao == '1':
            adicionar_aluno(alunos)
        elif opcao == '2':
            listar_alunos(alunos)
        elif opcao == '3':
            aluno_pelo_nome(alunos)
        elif opcao == '4':
            remover_aluno(alunos)
        elif opcao == '5':
            media_notas(alunos)
        else:
            print('\nSaindo...\n\n')
            break

menu()
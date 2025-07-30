import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False}, 
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo':True},
                {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    '''Essa função exibe o titulo do programa'''
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    '''Essa função exibe as opções do programa'''
    print('1. Cadastrar Resturante')
    print('2. Listar Resturante')
    print('3. Alternar estado do Resturante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função é responsavel por exibir a frase "Encerrando o app" ao finalizar o programa'''
    exibir_subtitulo('Encerrando o App')

def voltar_ao_menu_principal():
    '''solicita uma tecla para voltar oa menu principal
    
    Outputs:
    - retorna ao menu principal
    '''
    input('Aperte qualquer tecla para retornar ao menu')
    main()

def opcao_invalida():
    '''Essa função mostra ao usurario que a opção escolhida não é valida
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função limpa a tela e exibe o subtitulo da opção escolhida

    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()



def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos retaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsavel por listar os restaurantes existentes
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listar Restaurantes')

    print({'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'})
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''Essa função alterna o status do restaurante
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')


    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsavel por permitir ao usuario escolher uma das opções
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

import requests

def testar_conexao():
    try:
        requests.get('https://www.pudim.com.br', timeout=5)
        print('✅ Conexão com a internet funcionando!')
    except requests.ConnectionError:
        print('❌ Sem conexão com a internet!')
    except requests.Timeout:
        print('⏱️ A conexão demorou demais e foi encerrada.')
    except Exception as erro:
        print(f'⚠️ Ocorreu um erro inesperado: {erro}')

testar_conexao()

#Programa para criar um servidor simpls TCP IPV4.
#Envio de arquivos através de um browser como cliente.
#Basta acessar em seu navegador localhost:9999 (ou Host e Porta especificados)
#E solicitar algum arquivo da pasta "/data"

#Trabalho de Rede de Computadores - UFRB

import socket

#Definição de Host e Porta
host, port = '', 9999

#Criação do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Tipo: IPV4 e TCP
servidor.bind((host, port))

#Confirmação
print("Servidor criado na porta: {}:{}".format(host,port))

#Escutar a porta.
servidor.listen(1)

#Aguardando conexão do usuario:
while True:
        print('Aguardando conexão do cliente... ')

        coneccao, endereco = servidor.accept()
        print("Conexão em: {}".format(endereco))

        #Recebendo mensagem do navegador
        mensagem = coneccao.recv(1024).decode('utf-8')
        #Divindo a mensagem
        mensagemString = mensagem.split(' ')
        #Separando apenas o caminho
        requisicao = mensagemString[1]

        print('Solicitação do cliente: ', requisicao)

        #Separando o nome do arquivo
        nomearquivo = requisicao.split('?')[0]
        nomearquivo = nomearquivo.lstrip('/')

        #Arquivo caso seja a homepage.
        if (nomearquivo == ''):
                nomearquivo = 'homepage.html'  # Pagina inicial

        try:
                arquivo = open('data/'+nomearquivo,'rb') # acescenta a pasta do caminho e le o arquivo em bytes
                resposta = arquivo.read()
                arquivo.close()

        except Exception as e: #caso não encontre o arquivo, abra o arquivo de erro 404
                nomearquivo = '404.html'
                arquivo = open('data/'+nomearquivo, 'rb')
                response = arquivo.read()
                arquivo.close()

        if (nomearquivo.endswith(".jpg")):
                mimetype = 'image/jpg'
        elif (nomearquivo.endswith(".png")):
                mimetype = 'image/png'
        elif (nomearquivo.endswith(".mp4")):
                mimetype = 'video/mpeg'
        elif (nomearquivo.endswith(".mp3")):
                mimetype = 'audio/mpeg'
        elif (nomearquivo.endswith(".ico")):
                mimetype = 'image/x-ico'
        else:
                mimetype = 'text/html'  #diversos tipos disponiveis de arquivo

        header ='HTTP/1.1 200 OK\nContent-Type: ' + str(mimetype) + '\n\n' #padrão http

        respostaEnvio = header.encode('utf-8') + resposta #junta cabeçalho e mensagem
        try:
                coneccao.send(respostaEnvio) #envia
                print('Enviado com sucesso.')
        except:
                print('Erro ao envio')
        coneccao.close() #fecha conexão
        print('Conexão encerrada')
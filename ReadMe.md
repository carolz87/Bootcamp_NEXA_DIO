# Desafio Prático: Extração de Texto de Imagens com AWS Textract e Python

## Descrição do Projeto

Este projeto tem como objetivo criar uma aplicação para extrair texto de imagens utilizando o serviço AWS Textract e a linguagem de programação Python. A aplicação será demonstrada utilizando a CLI da AWS e o AWS SAM (Serverless Application Model).

## Passo a Passo

### Pré-requisitos

1. **Conta AWS**: É possível utilizar serviços sem custo, maiores detalhes podem ser encotrados no [Site oficial](https://aws.amazon.com/pt/free) 
2. **AWS CLI**: Para instalação do AWS CLI em sua máquina. [Guia de instalação](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
3. **AWS SAM CLI**: Para instalação do AWS SAM CLI. [Guia de instalação](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
4. **Python**: Para instalação do Python (deve ser 3.6 ou superior). [Guia de instalação](https://www.python.org/downloads/)

### Configuração do Ambiente

1. **Configurar AWS CLI**:
    ```sh
    aws configure
    ```
    Insira suas credenciais da AWS (Access Key ID e Secret Access Key) e a região padrão.

2. **Criar um novo diretório para o projeto**:
    ```sh
    mkdir aws-textract-project
    cd aws-textract-project
    ```

    Isso também pode ser feito pelo seu explorador de arquivos ou por sua IDE de preferência, caso ela tenha suporte

3. **Inicializar um novo projeto SAM**:
    ```sh
    sam init
    ```
    Selecione a opção para criar um novo projeto com Python.

### Desenvolvimento da Aplicação

  A aplicação foi desenvolvida como demonstração básica da funcionalidade de extração de texto a partir de uma imagem pelo serviço TextExtract da AWS, está contida no arquivo `app.py` e depende da configuração disposta em `config.yaml`


### Implantação e Teste

1. **Construir o projeto SAM**:
    ```sh
    sam build
    ```

2. **Implantar o projeto SAM**:
    ```sh
    sam deploy --guided
    ```
    Siga as instruções para configurar a implantação.

3. **Testar a função Lambda**:
    ```sh
    aws lambda invoke --function-name TextExtractFunction --payload '{"bucket": "nome-do-bucket", "name": "nome-da-imagem.jpg"}' response.json
    cat response.json
    ```


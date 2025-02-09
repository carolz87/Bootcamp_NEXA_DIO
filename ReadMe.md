# AWS Rekognition

Este projeto é um exercício do Bootcamp Nexa IA da DIO. O objetivo do código é utilizar o serviço AWS Rekognition para detectar celebridades em imagens e desenhar uma `bounding-box` em volta das celebridades detectadas.


## Funcionalidade do Código

O código em `main.py` realiza as seguintes etapas:

1. **Carregar Imagens**: As imagens são carregadas a partir do diretório `Img/`.
2. **Reconhecimento de Celebridades**: Utiliza o serviço AWS Rekognition para reconhecer celebridades nas imagens.
3. **Desenhar Bounding-Box**: Desenha uma bounding-box em volta das celebridades detectadas e salva a imagem resultante.

### Funções Principais

- `caminho(arquivo: str) -> str`: Retorna o caminho completo de um arquivo no diretório `Img/`.
- `reconhecimento(foto: str) -> RecognizeCelebritiesResponseTypeDef`: Realiza o reconhecimento de celebridades utilizando o AWS Rekognition.
- `faz_caixa(image_path: str, output_path: str, face_details: list[CelebrityTypeDef])`: Desenha uma bounding-box em volta das celebridades detectadas e salva a imagem resultante.

### Como Executar

1. **Variáveis de Ambiente**: Edite o arquivo `.env.example` com suas respectivas chaves de acesso da AWS. Após salvar o arquivo altere o nome para `.env`

2. **Dependências**: Certifique-se de ter as dependências instaladas:
    ```bash
    pip install -r requirements.txt
    ```

3. **Executar o Script**: Execute o script `main.py`:
    ```sh
    python main.py
    ```


from pathlib import Path
import boto3
from mypy_boto3_rekognition.type_defs import (CelebrityTypeDef,RecognizeCelebritiesResponseTypeDef)
from PIL import Image, ImageDraw, ImageFont
import dotenv
import os

dotenv.load_dotenv()

def conecta():
    session = boto3.Session(
        aws_access_key_id= os.getenv('ACESS_KEY'),
        aws_secret_access_key= os.getenv('SECRET_ACCESS_KEY'),
        region_name=os.getenv('REGION')
    )

    client = session.client("rekognition")
    
    return client

def desconecta(conn):
    conn.close()


def caminho(arquivo: str) -> str:
    return str(Path(__file__).parent / "img" / arquivo)


def reconhecimento(foto: str) -> RecognizeCelebritiesResponseTypeDef:
    with open(foto, "rb") as image:
        return conn.recognize_celebrities(Image={"Bytes": image.read()})


def faz_caixa(image_path: str, output_path: str, face_details: list[CelebrityTypeDef]):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Ubuntu-R.ttf", 20)

    width, height = image.size

    for face in face_details:
        box = face["Face"]["BoundingBox"]  
        left = int(box["Left"] * width)  
        top = int(box["Top"] * height)  
        right = int((box["Left"] + box["Width"]) * width)  
        bottom = int((box["Top"] + box["Height"]) * height)  

        confidence = face.get("MatchConfidence", 0)
        if confidence > 80:
            draw.rectangle([left, top, right, bottom], outline="red", width=3)

            text = face.get("Name", "")
            position = (left, top - 20)
            bbox = draw.textbbox(position, text, font=font)
            draw.rectangle(bbox, fill="red")
            draw.text(position, text, font=font, fill="white")

    image.save(output_path)
    print(f"Imagem salva com resultados em : {output_path}")


if __name__ == "__main__":
    
    conn = conecta()

    caminho_foto = [
        caminho("001.jpg"),
        caminho("002.jpg"),
        caminho("003.jpg"),
       
    ]

    for endereco in caminho_foto:
        response = reconhecimento(endereco)
        faces = response["CelebrityFaces"]
        if not faces:
            print(f"Não foram encontrados famosos para a imagem: {endereco}")
            continue
        output_path = caminho(f"{Path(endereco).stem}-resultado.jpg")
        faz_caixa(endereco, output_path, faces)
    
    desconecta(conn)
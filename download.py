import xml.etree.ElementTree as ET
import subprocess
from pathlib import Path

PASTA_XML = "xmls"
PASTA_VIDEOS = "videos"

# Cria a pasta de saída se não existir
Path(PASTA_VIDEOS).mkdir(exist_ok=True)

for arquivo_xml in Path(PASTA_XML).glob("*.xml"):
  try:
    tree = ET.parse(arquivo_xml)
    root = tree.getroot()

    # Obtém o id do vídeo
    video_id = root.attrib.get("id", arquivo_xml.stem)

    # Obtém a URL
    url = root.find("url")

    if url is not None and url.text:
      print(f"Baixando {video_id}: {url.text}")

      subprocess.run([
        "yt-dlp",
        "-o",
        f"{PASTA_VIDEOS}/{video_id}.%(ext)s",
        url.text
      ])

  except Exception as e:
    print(f"Erro em {arquivo_xml}: {e}")
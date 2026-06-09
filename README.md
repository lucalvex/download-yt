# Download Automático de Vídeos a partir de Arquivos XML

Este projeto automatiza o download de vídeos do YouTube a partir de arquivos XML que contêm metadados dos vídeos. O script percorre uma pasta contendo arquivos XML, extrai as URLs dos vídeos e realiza o download utilizando o `yt-dlp`.

Os vídeos são salvos automaticamente utilizando o identificador (`id`) definido em cada arquivo XML.

## Requisitos

### Software

- Python 3.11.9
- yt-dlp
- FFmpeg (recomendado)

### Bibliotecas Python

O projeto utiliza apenas bibliotecas nativas do Python:

- `xml.etree.ElementTree`
- `subprocess`
- `pathlib`

Não é necessário instalar dependências adicionais além do `yt-dlp`.

## Instalação

### 1. Instalar o Python

Verifique a instalação:

```bash
python --version
```

Saída esperada:

```text
Python 3.11.9
```

### 2. Instalar o yt-dlp

```bash
pip install -U yt-dlp
```

Verificar instalação:

```bash
yt-dlp --version
```

### 3. Instalar o FFmpeg

O FFmpeg é utilizado pelo `yt-dlp` para combinar fluxos de áudio e vídeo e realizar conversões quando necessário.

Baixe uma versão compilada:

https://www.gyan.dev/ffmpeg/builds/

Após a instalação, verifique:

```bash
ffmpeg -version
```

## Estrutura do Projeto

```text
projeto/
│
├── download.py
├── xmls/
│   ├── video1.xml
│   ├── video2.xml
│   └── video3.xml
│
└── videos/
```

### Pasta `xmls`

Contém os arquivos XML com os metadados dos vídeos.

Exemplo:

```xml
<?xml version="1.0" encoding="utf-8"?>
<video id="v_ArmFlapping_01" keyword="10_yr_severe_autistic">
   <url>http://www.youtube.com/watch?v=I7fdv1q9-m8</url>
   <height>360</height>
   <width>480</width>
</video>
```

## Funcionamento

O script executa as seguintes etapas:

1. Percorre todos os arquivos XML da pasta `xmls`.
2. Lê o conteúdo de cada arquivo.
3. Extrai o atributo `id` da tag `<video>`.
4. Extrai a URL da tag `<url>`.
5. Executa o `yt-dlp`.
6. Salva o vídeo na pasta `videos`.
7. Utiliza o valor do atributo `id` como nome do arquivo.

### Exemplo

Para o XML:

```xml
<video id="v_ArmFlapping_01">
    <url>http://www.youtube.com/watch?v=I7fdv1q9-m8</url>
</video>
```

O vídeo será salvo como:

```text
videos/v_ArmFlapping_01.mp4
```

## Executando o Projeto

Abra um terminal na pasta do projeto e execute:

```bash
python baixar_videos.py
```

Durante a execução será exibido:

```text
Baixando v_ArmFlapping_01: http://www.youtube.com/watch?v=I7fdv1q9-m8
```

## Observações

- Alguns vídeos podem não estar mais disponíveis no YouTube.
- Vídeos privados ou removidos não poderão ser baixados.
- O script continuará processando os demais arquivos mesmo que ocorra erro em algum XML.
- O FFmpeg é recomendado para garantir compatibilidade com diferentes formatos de mídia.

## Versões Utilizadas

| Ferramenta | Versão |
|------------|---------|
| Python | 3.11.9 |
| yt-dlp | Última versão disponível no momento da instalação |
| FFmpeg | Release Essentials |

## Autor

Lucas Alves
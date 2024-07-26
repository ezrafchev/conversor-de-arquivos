

# Conversor de Arquivos


Este é um conversor de arquivos simples que converte arquivos de texto (.txt) para PDF (.pdf) usando Python. Além disso, permite o download de vídeos/arquivos do YouTube e TikTok em todas as resoluções possíveis. O download de vídeos do Instagram requer autenticação.

## Requisitos

- Python 3.x
- fpdf

- yt-dlp
- requests
- PyInstaller (opcional, para criar o executável)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/ezrafchev/conversor-de-arquivos.git
    cd conversor-de-arquivos
    ```

2. Instale as dependências:
    ```bash

    pip install fpdf yt-dlp requests
    ```

## Uso


### Executar o script Python

Para converter um arquivo de texto para PDF, execute o seguinte comando:
```bash
python convert_txt_to_pdf.py input.txt output.pdf
```
Substitua `input.txt` pelo caminho do seu arquivo de texto e `output.pdf` pelo nome desejado para o arquivo PDF de saída.

Para converter todos os arquivos de texto em um diretório para PDF, execute o seguinte comando:
```bash
python convert_all_txt_to_pdf.py /caminho/do/diretorio
```
Substitua `/caminho/do/diretorio` pelo caminho do diretório contendo os arquivos de texto.


Para baixar vídeos do YouTube, execute o seguinte comando:
```bash

python youtube_downloader.py URL OUTPUT_DIR
```

Substitua `URL` pelo link do vídeo do YouTube e `OUTPUT_DIR` pelo diretório onde deseja salvar o vídeo.


Para baixar vídeos do Instagram, forneça cookies ou credenciais de login. Execute o seguinte comando:
```bash

python instagram_downloader.py
```

O download de vídeos do Instagram requer autenticação. Por favor, forneça cookies ou credenciais de login.


Para baixar vídeos do TikTok, execute o seguinte comando:
```bash

python tiktok_downloader.py URL OUTPUT_DIR
```

Substitua `URL` pelo link do vídeo do TikTok e `OUTPUT_DIR` pelo diretório onde deseja salvar o vídeo.

### Usar os Arquivos de Configuração

Você também pode usar os arquivos de configuração pré-configurados para executar as funções. Basta colar os novos parâmetros nos arquivos de configuração e executar os comandos abaixo:

Para converter um arquivo de texto para PDF:
```bash
python convert_txt_to_pdf.py $(cat config_convert_txt_to_pdf.txt)
```

Para converter todos os arquivos de texto em um diretório para PDF:
```bash
python convert_all_txt_to_pdf.py $(cat config_convert_all_txt_to_pdf.txt)
```

Para baixar um vídeo do YouTube:
```bash
python download_youtube_video.py $(cat config_download_youtube_video.txt)
```

Para baixar um post do Instagram:
```bash
python download_instagram_post.py $(cat config_download_instagram_post.txt)
```

Para baixar um vídeo do TikTok:
```bash
python download_tiktok_video.py $(cat config_download_tiktok_video.txt)
```

### Criar o Executável (Opcional)

Se você deseja criar um executável para Windows, siga os passos abaixo:

1. Instale o PyInstaller:
    ```bash
    pip install pyinstaller
    ```

2. Crie o executável:
    ```bash
    pyinstaller --onefile converter.py
    ```

O executável será gerado no diretório `dist`.

### Executar o Executável

Para converter um arquivo de texto para PDF usando o executável, execute o seguinte comando:
```bash
./dist/converter --convert input.txt output.pdf
```
Substitua `input.txt` pelo caminho do seu arquivo de texto e `output.pdf` pelo nome desejado para o arquivo PDF de saída.

## Créditos

Este projeto foi desenvolvido por [ezrafchev](https://github.com/ezrafchev).



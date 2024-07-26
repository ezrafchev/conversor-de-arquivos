

# Conversor de Arquivos

Este é um conversor de arquivos simples que converte arquivos de texto (.txt) para PDF (.pdf) usando Python. Além disso, permite o download de vídeos/arquivos do Instagram, YouTube e TikTok em todas as resoluções possíveis.

## Requisitos

- Python 3.x
- fpdf
- pytube
- instaloader
- TikTokApi
- PyInstaller (opcional, para criar o executável)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/ezrafchev/conversor-de-arquivos.git
    cd conversor-de-arquivos
    ```

2. Instale as dependências:
    ```bash
    pip install fpdf pytube instaloader TikTokApi
    ```

## Uso

### Executar o script Python

Para converter um arquivo de texto para PDF, execute o seguinte comando:
```bash
python converter.py --convert input.txt output.pdf
```
Substitua `input.txt` pelo caminho do seu arquivo de texto e `output.pdf` pelo nome desejado para o arquivo PDF de saída.

Para converter todos os arquivos de texto em um diretório para PDF, execute o seguinte comando:
```bash
python converter.py --convert-all /caminho/do/diretorio
```
Substitua `/caminho/do/diretorio` pelo caminho do diretório contendo os arquivos de texto.

Para baixar um vídeo do YouTube, execute o seguinte comando:
```bash
python converter.py --download-youtube URL RESOLUCAO
```
Substitua `URL` pelo link do vídeo do YouTube e `RESOLUCAO` pela resolução desejada (por exemplo, `720p`).

Para baixar um post do Instagram, execute o seguinte comando:
```bash
python converter.py --download-instagram URL
```
Substitua `URL` pelo link do post do Instagram.

Para baixar um vídeo do TikTok, execute o seguinte comando:
```bash
python converter.py --download-tiktok URL
```
Substitua `URL` pelo link do vídeo do TikTok.

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



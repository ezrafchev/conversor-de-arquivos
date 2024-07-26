
# Conversor de Arquivos

Este é um conversor de arquivos simples que converte arquivos de texto (.txt) para PDF (.pdf) usando Python.

## Requisitos

- Python 3.x
- fpdf
- PyInstaller (opcional, para criar o executável)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/ezrafchev/conversor-de-arquivos.git
    cd conversor-de-arquivos
    ```

2. Instale as dependências:
    ```bash
    pip install fpdf
    ```

## Uso

### Executar o script Python

Para converter um arquivo de texto para PDF, execute o seguinte comando:
```bash
python converter.py input.txt output.pdf
```
Substitua `input.txt` pelo caminho do seu arquivo de texto e `output.pdf` pelo nome desejado para o arquivo PDF de saída.

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
./dist/converter input.txt output.pdf
```
Substitua `input.txt` pelo caminho do seu arquivo de texto e `output.pdf` pelo nome desejado para o arquivo PDF de saída.

## Créditos

Este projeto foi desenvolvido por [ezrafchev](https://github.com/ezrafchev).



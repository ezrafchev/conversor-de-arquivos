# -*- coding: utf-8 -*-
import pyktok as pyk
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import sqlite3
import json
import os
from moviepy.editor import VideoFileClip
import cv2
import numpy as np

def get_edge_cookies():
    # Caminho para o arquivo de cookies copiado manualmente
    cookie_file = 'C:\\Users\\esdra\\OneDrive\\Documentos\\Cookies'
    
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(cookie_file)
    cursor = conn.cursor()
    
    # Selecionar todos os cookies
    cursor.execute("SELECT host_key, name, value, path, expires_utc FROM cookies")
    cookies = cursor.fetchall()
    
    # Fechar a conexão
    conn.close()
    
    # Converter os cookies para o formato esperado pelo Selenium
    selenium_cookies = []
    for cookie in cookies:
        if 'tiktok.com' in cookie[0]:  # Filtrar apenas cookies do domínio tiktok.com
            expiry = None
            if cookie[4] != 0:
                expiry = cookie[4] / 1000000 - 11644473600  # Converter o tempo de expiração
            selenium_cookies.append({
                'domain': cookie[0],
                'name': cookie[1],
                'value': cookie[2],
                'path': cookie[3],
                'expiry': expiry
            })
    
    return selenium_cookies

def remove_watermark(input_video_path, output_video_path):
    """
    Remove a marca d'água do vídeo usando técnicas de processamento de imagem.

    Args:
        input_video_path (str): Caminho do vídeo de entrada.
        output_video_path (str): Caminho do vídeo de saída.
    """
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo: {input_video_path}")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detectar e remover a marca d'água (ajuste conforme necessário)
        # Aqui estamos usando uma máscara para cobrir a área onde a marca d'água geralmente aparece
        mask = np.zeros(frame.shape, dtype=np.uint8)
        cv2.rectangle(mask, (frame.shape[1] - 150, frame.shape[0] - 50), (frame.shape[1], frame.shape[0]), (255, 255, 255), -1)
        frame = cv2.inpaint(frame, cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY), 3, cv2.INPAINT_TELEA)

        out.write(frame)

    cap.release()
    out.release()

def download_tiktok_video(url, output_file, output_dir):
    """
    Baixa vídeos do TikTok e salva os metadados.

    Args:
        url (str): URL do vídeo do TikTok.
        output_file (str): Arquivo de saída para salvar os metadados.
        output_dir (str): Diretório de saída para salvar o vídeo.
    """
    cookies = get_edge_cookies()
    
    options = EdgeOptions()
    options.add_argument("--headless")  # Executar o navegador em modo headless
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    driver.get("https://www.tiktok.com")
    
    # Adicionar cookies ao navegador
    for cookie in cookies:
        if cookie['expiry'] is not None:
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)
    
    # Navegar para a URL do vídeo
    driver.get(url)
    
    # Especificar o navegador Edge para pyktok
    pyk.specify_browser('edge')
    video_path = os.path.join(output_dir, "video.mp4")
    pyk.save_tiktok(url, True, video_path)
    
    # Verificar se o vídeo foi baixado corretamente
    if not os.path.exists(video_path) or os.path.getsize(video_path) == 0:
        print(f"Erro ao baixar o vídeo: {url}")
        driver.quit()
        return
    
    # Verificar se o arquivo de vídeo é válido
    try:
        with VideoFileClip(video_path) as video:
            video.duration  # Tentar acessar a duração do vídeo para verificar se é válido
    except Exception as e:
        print(f"Erro ao processar o vídeo baixado: {e}")
        driver.quit()
        return
    
    # Remover a marca d'água
    output_video_path = os.path.join(output_dir, "video_no_watermark.mp4")
    remove_watermark(video_path, output_video_path)
    
    # Salvar os metadados
    with open(output_file, 'w') as f:
        json.dump({"url": url, "output": output_video_path}, f)
    
    driver.quit()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Download TikTok videos.')
    parser.add_argument('url', help='TikTok video URL')
    parser.add_argument('output', help='Output file for metadata')
    parser.add_argument('output_dir', help='Output directory for video')

    try:
        args = parser.parse_args()
    except SystemExit as e:
        print(f"Erro: {e}")
        parser.print_help()
        exit(1)

    download_tiktok_video(args.url, args.output, args.output_dir)

import requests
import re
import os

def download_tiktok_video(url, output_path='.', resolution='1080p'):
    """
    Baixa vídeos do TikTok.

    Args:
        url (str): URL do vídeo do TikTok.
        output_path (str): Diretório de saída para salvar o vídeo.
        resolution (str): Resolução desejada do vídeo.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    video_url = re.search(r'playAddr":"(.*?)"', response.text).group(1).encode('utf-8').decode('unicode_escape').replace('\u0026', '&')
    
    # Adiciona a resolução ao URL do vídeo se suportado
    if resolution in ['144p', '360p', '720p', '1080p', '1440p', '2160p', '4320p']:
        video_url = video_url.replace('playwm', f'playwm_{resolution}')
    
    video_content = requests.get(video_url, headers=headers).content
    video_name = os.path.join(output_path, f'tiktok_video_{resolution}.mp4')
    with open(video_name, 'wb') as video_file:
        video_file.write(video_content)
    print(f'Download complete: {video_name}')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Download TikTok videos.')
    parser.add_argument('url', help='TikTok video URL')
    parser.add_argument('output', help='Output directory')
    parser.add_argument('--resolution', default='1080p', help='Video resolution (default: 1080p)')
    args = parser.parse_args()

    download_tiktok_video(args.url, args.output, args.resolution)



import requests
import re
import os

def download_tiktok_video(url, output_path='.'):
    """
    Baixa vídeos do TikTok.

    Args:
        url (str): URL do vídeo do TikTok.
        output_path (str): Diretório de saída para salvar o vídeo.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    video_url = re.search(r'playAddr":"(.*?)"', response.text).group(1).encode('utf-8').decode('unicode_escape').replace('\u0026', '&')
    video_content = requests.get(video_url, headers=headers).content
    video_name = os.path.join(output_path, 'tiktok_video.mp4')
    with open(video_name, 'wb') as video_file:
        video_file.write(video_content)
    print('Download complete.')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Download TikTok videos.')
    parser.add_argument('url', help='TikTok video URL')
    parser.add_argument('output', help='Output directory')
    args = parser.parse_args()

    download_tiktok_video(args.url, args.output)




import yt_dlp

def download_youtube_video(url, output_path='.'):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print('Download complete.')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Download YouTube videos in all resolutions.')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('output', help='Output directory')
    args = parser.parse_args()

    download_youtube_video(args.url, args.output)


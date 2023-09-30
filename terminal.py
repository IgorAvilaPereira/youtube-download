
from pytube import YouTube, Playlist
import os
import os
import platform
import subprocess
from os import path
# import time
from time import sleep
# import flet as ft

vet = ['https://www.youtube.com/watch?v=N66_ydbVCBU&list=RDmPmoojB54xI&index=6',
    'https://www.youtube.com/watch?v=z3mzvJiUZao&list=RDmPmoojB54xI&index=3',
    'https://www.youtube.com/watch?v=jIoEaTN7GGo&list=RDEMWC3Rlu-jDs42cJpMIrG07w&index=2',
    'https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=RDQM4bdEoBr6r2c&index=3',
    'https://www.youtube.com/watch?v=zABLecsR5UE&list=RDQM4bdEoBr6r2c&index=10',
    'https://www.youtube.com/watch?v=ofHfsrzEOsk',
    'https://www.youtube.com/watch?v=_ZLh7mYdj8s&list=RDEM1n6Puyuo1xUMaeicc_eMBQ&index=4',
    'https://www.youtube.com/watch?v=b3U_CSaJHuI&list=RDEM1n6Puyuo1xUMaeicc_eMBQ&index=23',
    'https://www.youtube.com/watch?v=1pfImX0MkHk',
    'https://www.youtube.com/watch?v=o7jVqtVgd2U',
    'https://www.youtube.com/watch?v=cQ-48rr6Wfo&list=RDEMbXVCUlMLsZ97rZoEH8tJ8A&start_radio=1&rv=o7jVqtVgd2U',
    'https://www.youtube.com/watch?v=4Zrx5VnLb3U',
    'https://www.youtube.com/watch?v=5cMHTStBrt0',
    'https://www.youtube.com/watch?v=ftJGzhQsLgM',
    'https://www.youtube.com/watch?v=At3RMbGo-HQ',
    'https://www.youtube.com/watch?v=ITiuDJRO5wc',
    'https://www.youtube.com/watch?v=9zpZ4NYBrvU',
    'https://www.youtube.com/watch?v=oTf5qi2J6PM',
    'https://www.youtube.com/watch?v=QOm1-PFsLv0',
    'https://www.youtube.com/watch?v=L-JQ1q-13Ek&list=RDEMj7ObS6TgJ5zSOH9DUcVq8Q&start_radio=1&rv=QOm1-PFsLv0',
    'https://www.youtube.com/watch?v=xvueaanmx4Q',
    'https://www.youtube.com/watch?v=gXAw3-UIQRY',
    'https://www.youtube.com/watch?v=fbu26aP_KG0',
    'https://www.youtube.com/watch?v=q5G0VQ9_S_Y']
for url in vet:
    yt = YouTube(url)      
    audio = yt.streams.filter(only_audio=True).first()
    out_file = audio.download(output_path='audio')        
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
from Download import *
import flet as ft
import os
import platform
import subprocess
from os import path
# import time
from time import sleep

# pip install pydub
# apt-get install ffmpeg      
# from pydub import AudioSegment                                                           
# src = "transcript.mp3"
# dst = "test.wav"
# convert wav to mp3                                                            
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")

# pip install SpeechRecognition
# import speech_recognition as sr

# class AudioToText: 
#     def __init__(self, audio):      
#         r = sr.Recognizer()
#         with sr.AudioFile(audio) as source:  
#             audio_text = r.listen(source)        
#             try:           
#                 text = r.recognize_google(audio_text, language = "pt-BR")
#                 print('convertendo audio para texto ...')
#                 # print(text)            
#                 self.text = text
#             except:
#                 print('Desculpe.. execute novamente...')

def main(page):
    # page.window_title = "Youtube Downloader"
    page.title = "My Youtube Downloader"    
    # page.window_width = 800        
    # page.window_height = 700     
    page.window_resizable = False  # window is not resizable
    pb = ft.ProgressBar(width=200)
    pb.value = 0
    page.update()

    def open_video_folder(e):                
        path = "./video"    
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def open_audio_folder(e):
        path = "./audio"
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def open_playlist_folder(e):
        path = "./playlist"
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def add_new_video(e):
        url_video = new_video.value
        download = Download()        
        # text.value = "Progress..."        
        pb.value = 0 
        page.update()
        # download.text = text
        download.page = page
        download.pb = pb
        download.baixarVideo(url_video)
        # page.add(ft.Checkbox(label=new_video.value))
        new_video.value  = "Download Completed"
        new_video.focus()
        new_video.update()
        # except:
        #   print("incorrect url!")
    
    def add_new_playlist(e):
        url_playlist = new_playlist.value       
        # try: 
            # if (not url_playlist and len(url_playlist) > 0):
        download = Download()
        # text.value = "Progress..."        
        pb.value = 0 
        page.update()
        # download.text = text
        download.page = page
        download.pb = pb
        download.baixarPlaylist(url_playlist)
        # page.add(ft.Checkbox(label=new_playlist.value))
        new_playlist.value =  "Download Completed"
        new_playlist.focus()
        new_playlist.update()
        # except:
        # print("incorrect url!")

    def export_playlist(e):
        url_playlist = new_playlist.value
        # try: 
            # if (not url_playlist and len(url_playlist) > 0):
        download = Download()
        # text.value = "Progress..."        
        pb.value = 0 
        page.update()
        # download.text = text
        download.page = page
        download.pb = pb
        download.gerarLinksMarkdown(url_playlist)
        new_playlist.value = "Download Completed"
        new_playlist.focus()
        new_playlist.update()
        # except:
        #   print("incorrect url!")


    def add_new_audio(e):
        url_audio = new_video.value
        # text.value = "Progress..."        
        download = Download()
        pb.value = 0 
        page.update()
        # download.text = text
        download.page = page
        download.pb = pb
        download.baixarAudio(url_audio)
        # page.add(ft.Checkbox(label=new_video.value))
        new_video.value = "Download Completed"
        new_video.focus()
        new_video.update()

    # bug
    # def export_to_text(e):
    #     url_audio = new_audio.value
    #     # if (not url_audio and len(url_audio) > 0):
    #     download = Download()
    #     file = download.baixarAudio(url_audio)
    #     page.add(ft.Checkbox(label=new_video.value))
    #     new_audio.value = ""
    #     new_audio.focus()
    #     new_audio.update()            
    #     # src = file
    #     # print(src)
    #     # dst = file.replace(".mp3", ".wav")
    #     # print(dst)
    #     # sound = AudioSegment.from_mp3(src)
    #     # sound.export(dst, format="wav")    
    #     print(file)
    #     time.sleep(30)
    #     audioToText = AudioToText(file)
    #     print(audioToText.text)

    # dlg = ft.AlertDialog(
    #     title=ft.Text("Download Completed"), on_dismiss=lambda e: print("Dialog dismissed!")
    # )

    # def open_dlg(e):
    #     page.dialog = dlg
    #     dlg.open = True
    #     page.update()

    text = ft.Text("Progress...")    

    page.add(        
        ft.Column([text, pb])        
    )

    new_video = ft.TextField(hint_text="Youtube Video URL?", width=400)
    page.add(ft.Row([new_video, ft.ElevatedButton("Download Video", on_click=add_new_video), ft.FilledButton(text="Open Video Folder", on_click=open_video_folder), ft.ElevatedButton("Download Audio", on_click=add_new_audio), ft.FilledButton(text="Open Audio Folder", on_click=open_audio_folder)]))

    new_playlist = ft.TextField(hint_text="Youtube Playlist URL?", width=400)
    page.add(ft.Row([new_playlist, ft.ElevatedButton("Download Playlist", on_click=add_new_playlist), ft.ElevatedButton("Export Playlist to Markdown", on_click=export_playlist), ft.FilledButton(text="Open Playlist Folder", on_click=open_playlist_folder)]))

    # new_audio = ft.TextField(hint_text="Youtube Video URL?", width=400)
    # page.add(ft.Row([new_audio, ft.ElevatedButton("Download Audio", on_click=add_new_audio), ft.ElevatedButton("Export Video to Text (Pt-br)", on_click=export_to_text)]))
    # page.add(ft.Row([new_audio, ft.ElevatedButton("Download Audio", on_click=add_new_audio), ft.FilledButton(text="Open Audio Folder", on_click=open_audio_folder)]))
    
    
    

ft.app(target=main)
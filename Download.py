from pytube import YouTube, Playlist
import os
import flet as ft
import os
import platform
import subprocess
from os import path
# import time
from time import sleep

# pytube.request.default_range_size = 1048576 

class Download:

    def progress_callback(self, stream, chunk, bytes_remaining):
        try:
            size = self.video.filesize        
        except:
            size = self.audio.filesize
        self.pb.value = (size - bytes_remaining) / size        
        self.page.update()
        progress = int(((size - bytes_remaining) / size) * 100)        
        print(str(progress) + "%") 
        return str(progress) + "%"        

    def complete_callback(self, stream, file_handle):
        print("Download Completed")
        self.pb.value = 1        
        self.page.update()
        # self.page.add(ft.Text("Download Completed", size=10))
        # self.page.update()
        return "100%"

    def baixarVideo(self, url_video):
        yt = YouTube(url_video)                
        yt.register_on_progress_callback(self.progress_callback)
        yt.register_on_complete_callback(self.complete_callback)    
        self.video = yt.streams.get_highest_resolution()        
        self.video.download(output_path='video')

    def baixarPlaylist(self, url_playlist) :                
        playlist = Playlist(url_playlist)        
        # playlist.register_on_progress_callback(self.progress_callback)
        # playlist.register_on_complete_callback(self.complete_callback)    
        caixaTexto = ft.Text("", size=10)
        self.page.add(caixaTexto)
        for url_video in playlist:
            yt = YouTube(url_video)
            caixaTexto.value = url_video
            self.page.update()
            self.pb.value = 0 
            self.page.update()
            yt.register_on_progress_callback(self.progress_callback)
            yt.register_on_complete_callback(self.complete_callback)    
            self.video = yt.streams.get_highest_resolution()
            self.video.download(output_path='playlist')

    def baixarAudio(self, url_video):                
        yt = YouTube(url_video)        
        yt.register_on_progress_callback(self.progress_callback)
        yt.register_on_complete_callback(self.complete_callback)    
        self.audio = yt.streams.filter(only_audio=True).first()
        out_file = self.audio.download(output_path='audio')        
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return new_file

    def gerarLinksMarkdown(self, url_playlist):
        f = open("playlist.md", "w")
        conteudo = ""     
        playlist = Playlist(url_playlist)
        conteudo = "# Videos - "+playlist.title+"\n\n"
        conteudo = conteudo + "* [Playlist]("+url_playlist+")\n\n"
        for url_video in playlist:
            yt = YouTube(url_video)
            conteudo = conteudo + "* ["+url_video+"] \n\n"
        f.write(conteudo)      
        f.close()
    
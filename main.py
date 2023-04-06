from Download import *
import flet as ft
import os
import platform
import subprocess

# def open_file(path):
#     if platform.system() == "Windows":
#         os.startfile(path)
#     elif platform.system() == "Darwin":
#         subprocess.Popen(["open", path])
#     else:
#         subprocess.Popen(["xdg-open", path])

def main(page):
    # page.window_title = "Youtube Downloader "
    page.window_width = 600        # window's width is 200 px
    page.window_height = 400       # window's height is 200 px
    page.window_resizable = False  # window is not resizable

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
        download.baixarVideo(url_video)
        page.add(ft.Checkbox(label=new_video.value))
        new_video.value = ""
        new_video.focus()
        new_video.update()
    
    def add_new_playlist(e):
        url_playlist = new_playlist.value
        download = Download()
        download.baixarPlaylist(url_playlist)
        page.add(ft.Checkbox(label=new_playlist.value))
        new_playlist.value = ""
        new_playlist.focus()
        new_playlist.update()

    def export_playlist(e):
        url_playlist = new_playlist.value
        download = Download()
        download.gerarLinksMarkdown(url_playlist)
        new_playlist.value = ""
        new_playlist.focus()
        new_playlist.update()


    def add_new_audio(e):
        url_audio = new_audio.value
        download = Download()
        download.baixarAudio(url_audio)
        page.add(ft.Checkbox(label=new_video.value))
        new_audio.value = ""
        new_audio.focus()
        new_audio.update()

    new_video = ft.TextField(hint_text="Youtube Video URL?", width=200)
    page.add(ft.Row([new_video, ft.ElevatedButton("Download Video", on_click=add_new_video)]))

    new_playlist = ft.TextField(hint_text="Youtube Playlist URL?", width=200)
    page.add(ft.Row([new_playlist, ft.ElevatedButton("Download Playlist", on_click=add_new_playlist), ft.ElevatedButton("Export Playlist to Markdown", on_click=export_playlist)]))

    new_audio = ft.TextField(hint_text="Youtube Video URL?", width=200)
    page.add(ft.Row([new_audio, ft.ElevatedButton("Download Audio", on_click=add_new_audio)]))

    page.add(ft.FilledButton(text="Open Video Folder", on_click=open_video_folder), 
        ft.FilledButton(text="Open Playlist Folder", on_click=open_playlist_folder),
        ft.FilledButton(text="Open Audio Folder", on_click=open_audio_folder)
    )

ft.app(target=main)
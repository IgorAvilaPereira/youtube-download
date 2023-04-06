from pytube import YouTube, Playlist
import os

class Download:

    # def on_progress(stream, data_chunk, bytes_remaining):
    #     #print('bytes_remaining:', bytes_remaining)
    #     downloaded = max_file_size - bytes_remaining
    #     percent = downloaded/max_file_size
    #     print(f'Downloaded: {percent:.0%}', end='\r')

    # def on_complete(self, stream, path):
    #     return True
        

    def baixarVideo(self, url_video):
        # yt = YouTube(url_video, on_complete_callback=self.on_complete)
        yt = YouTube(url_video)
        video = yt.streams.get_highest_resolution()        
        video.download(output_path='video')
    def baixarPlaylist(self, url_playlist) :
        # playlist = Playlist(url_playlist, on_complete_callback=self.on_complete)
        playlist = Playlist(url_playlist)
        for url_video in playlist:
            yt = YouTube(url_video)
            video = yt.streams.get_highest_resolution()
            video.download(output_path='playlist')
    def baixarAudio(self, url_video):
        # yt = YouTube(url_video, on_complete_callback=self.on_complete)
        yt = YouTube(url_video)
        # audio = yt.streams.filter(only_audio=True)[0]
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path='audio')        
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(new_file)
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

# if __name__ == '__main__':    
#     download = Download()
#     url_playlist = "https://youtube.com/playlist?list=PLvT8P1q6jMWfsGSRD3MP8cuR_gnsDD59F"
#     download.gerarLinksMarkdown(url_playlist)
#     # download.baixarPlaylist(url_playlist)
#     # url_playlist = "https://youtube.com/playlist?list=PLvT8P1q6jMWfdK6v25Sjhq3qwxLIAnvtk"
#     # download.baixarPlaylist(url_playlist)

    
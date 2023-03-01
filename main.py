from pytube import YouTube, Playlist

VIDEO_URL = 'https://www.youtube.com/watch?v=8EJ3zbKTWQ8&list=PLyORnIW1xT6waC0PNjAMj33FdK2ngL_ik'
PLAYLIST_URL = 'https://www.youtube.com/playlist?list=PLyORnIW1xT6waC0PNjAMj33FdK2ngL_ik'

def download_video(video_url):
	yt = YouTube(video_url)
	video = yt.streams.get_highest_resolution()
	video.download()

def download_playlist(playlist_url):
	playlist = Playlist(playlist_url)
	for url in playlist:
		yt = YouTube(url)
		video = yt.streams.get_highest_resolution()
		video.download(output_path='playlist')

def download_audio(video_url):
	yt = YouTube(video_url)
	audio = yt.streams.filter(only_audio=True)[0]
	audio.download()

if __name__ == '__main__':
	download_video(VIDEO_URL)
	download_playlist(PLAYLIST_URL)
	download_audio(VIDEO_URL)
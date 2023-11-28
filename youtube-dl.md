# Youtube dl download music
- youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" <Playlist/Video URL>

# Youtube dl download best quality video
- youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' <Playlist/Video URL>

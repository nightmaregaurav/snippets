# Youtube dl download best quality audio
- youtube-dl -f 'bestaudio/bestaudio' "<PlaylistURL/IndividualURL>"

# Youtube dl download music as mp3
- youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" "<PlaylistURL/IndividualURL>"

# Youtube dl download best quality video
- youtube-dl -f 'bestvideo+bestaudio/bestvideo+bestaudio' "<PlaylistURL/IndividualURL>"

# Youtube dl download video as mp4
- youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' "<Playlist/Video URL>"

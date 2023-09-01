import vlc,time
#media = vlc.MediaPlayer('Kanye.mp3')
#media.play()
#media_player_new()

#Criando um arquivo
vlc_instance = vlc.Instance()

media = vlc_instance.media_new('Rossum.mp4')

player = vlc_instance.media_player_new()

player.set_media(media)

player.play()


player.get_state()
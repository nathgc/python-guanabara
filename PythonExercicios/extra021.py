#Importando módulo VLC para execução de arquivos vídeo e audio e módulo time paraconseguir um delay na execução delay
import time

import vlc

media_player = vlc.MediaPlayer()

#Criando um objeto 
video = vlc.Media("Rossum.mp4")

media_player.set_media(video)

media_player.play()

time.sleep(5)


duracao = media_player.get_length()

print(duracao)
time.sleep(duracao/1000)




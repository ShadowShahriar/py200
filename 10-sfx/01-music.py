from hdef import path, __script_dir as __dir
import pygame

pygame.init()
pygame.mixer.init()

audio = path.join(__dir, "assets", "the-range.mp3")
pygame.mixer.music.load(audio)
pygame.mixer.music.play(loops=-1, fade_ms=500)  # === -1 to loop forever
pygame.mixer.music.set_volume(0.8)  # =============== range [0.0, 1.0]

while 1:
    pass

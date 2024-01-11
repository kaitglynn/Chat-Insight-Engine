```python
import pygame

class SoundEffects:
    def __init__(self):
        pygame.mixer.init()

    def play_sound(self, sound_file):
        pygame.mixer.Sound(sound_file).play()

    def stop_sound(self):
        pygame.mixer.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

sound_effects = SoundEffects()

def playSoundEffects(sound_file):
    sound_effects.play_sound(sound_file)

def stopSoundEffects():
    sound_effects.stop_sound()

def setSoundEffectsVolume(volume):
    sound_effects.set_volume(volume)
```
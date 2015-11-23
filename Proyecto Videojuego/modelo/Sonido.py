import pygame

pygame.init()

class Sonido(object):
    _instance=None
    def __new__ (self):
      if not self._instance:
         self._instance=super(Sonido,self).__new__(self)
         self.tema=['sound/dog.mp3','sound/Yet Another Movie.mp3','sound/bomb.wav']
      return self._instance


    def playSonido(self,i):
        pygame.mixer.music.load(self.tema[i])
        pygame.mixer.music.play(-1)

    def stopSonido(self):
        pygame.mixer.music.stop()

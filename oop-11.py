# oop
# Polymorphism  

from pathlib import Path


class AudioFile:
    ext: str 

    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError('Invalid file format')
        self.filepath = filepath


class MP3File(AudioFile):
    ext = '.mp3'

    def play(self) -> None:
        print(f'playing {self.filepath} as mp3')


class WaveFile(AudioFile):
    ext = '.wav'

    def play(self) -> None:
        print(f'playing {self.filepath} as wave')


class OggFile(AudioFile):
    ext = '.ogg'

    def play(self) -> None:
        print(f'playing {self.filepath} as ogg')



'''
Duck typing in Python allows us to use any object
that provides the required behavior without forcing 
it to be a subclass.
'''
class FlasFile:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == '.flac':
            raise ValueError('Not a .flac file')
        self.filepath = filepath

    def play(self) -> None:
        print(f'playing {self.filepath} as flac')


# driver code
p1 = MP3File(Path('Alright.mp3'))
p1.play()

# p1 = MP3File(Path('Alright.mov'))
# p1.play()
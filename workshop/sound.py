from core.modules import SoundModule
from core.compiler import sound_compile

s = SoundModule()

def sounds():
    s.generate_sound_dict(1,108,"a",1.0)
    s.generate_sound_dict(1,45,"c",1.0)
    s.generate_sound_dict(1,94,"p",0.8)
    s.music("rain_ambience")
    s.music("haggstrom")
    s.music("mice")
    s.voice("footstep")
    s.voice("teleport")
    return s.soundDict


def main():sound_compile(sounds= sounds()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 
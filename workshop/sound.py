from core.modules import SoundModule
from core.compiler import sound_compile

s = SoundModule()

def sounds():
    s.generate_sound_dict(1,52,"a",1)
    return s.soundDict


def main():sound_compile(sounds= sounds()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 
from core.modules import SoundModule
from core.compiler import sound_compile

s = SoundModule()

def sounds():
    s.music("revenge")
    s.generate_sound_dict(1,53,"a",0.8)
    s.generate_sound_dict(1,34,"c",0.8)

    return s.soundDict


def main():sound_compile(sounds= sounds()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 
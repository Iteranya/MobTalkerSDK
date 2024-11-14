from core.modules import SoundModule
from core.compiler import sound_compile

s = SoundModule()

def sounds():
    s.music("revenge")
    s.music("fish")

    return s.soundDict


def main():sound_compile(sounds= sounds()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 
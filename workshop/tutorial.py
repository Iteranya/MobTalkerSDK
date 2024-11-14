from core.modules import VisualNovelModule
from core.compiler import compile
# -------------------------------------------------------
# This is the Example Multiple File Script
# -------------------------------------------------------

# If you're into organization, this is how you go about it.
# This file is the 'core' file

vn = VisualNovelModule() # Your Module~ Always need this~
storyName = "andr" # This will be the name of the Json File


# Import your scripts (all the .py file inside the script folder)

from tutorial_script import s1_introduction_installation,s2_sdk_installation,s3_basic_usage,s4_resource_packing
scripts = [
    s1_introduction_installation.story(),
    s2_sdk_installation.story(),
    s3_basic_usage.story(),
    s4_resource_packing.story()
]

# This is Only Required if your VN contains sound effect or voice or music etc
# It's a bit weird, but Minecraft needs you to compile everything into sounds.json
# Trust me, I would NOT put this in if Minecraft can load a sound file as easily as images.


def compileMultiStory():
    for script in scripts:
        vn.dialogueDict+=script
    return vn.dialogueDict


def main():compile(storyname=storyName,script=compileMultiStory()) 

# Run the file, if you're in VS Code, top right play button.

if __name__ == "__main__":
    main() 
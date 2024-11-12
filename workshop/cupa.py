from core.modules import VisualNovelModule
from core.compiler import compile
# -------------------------------------------------------
# This is the Example Multiple File Script
# -------------------------------------------------------

# If you're into organization, this is how you go about it.
# This file is the 'core' file

vn = VisualNovelModule() # Your Module~ Always need this~
storyName = "cupa" # This will be the name of the Json File


# Import your scripts (all the .py file inside the script folder)

from tutorial_script import s1_5_cupa_showcase
scripts = [
    s1_5_cupa_showcase.story()
]

# Yes, it's that simple
# No need to change anything below.


def compileMultiStory():
    for script in scripts:
        vn.dialogueDict+=script
    return vn.dialogueDict


def main():compile(storyname=storyName,script=compileMultiStory()) 

# Run the file, if you're in VS Code, top right play button.

if __name__ == "__main__":
    main() 
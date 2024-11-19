# =======================================

# This is where you define the resource pack name, description, and  trigger words
# No need to scroll down
# Just press play, top right corner of the screen
# And it will create the resource pack zip for you

# Have fun then!

RESOURCE_PACK_NAME = "episode_one"
RESOURCE_PACK_DESCRIPTION = "1. The Basics of Script Writing"
TRIGGER_WORDS = "Andr"

# =======================================

# Oh you want to know how it works???
# ...
# Yeah, good luck with that


import json
import os
import shutil

ASSETS_DIR = "mediafile" 
PACK_IMAGE = ASSETS_DIR+"/images/pack.png"
IMAGE_DIR =  ASSETS_DIR + "/images" 
SOUNDS_DIR = ASSETS_DIR + "/sounds"
SCRIPT_DIR = ASSETS_DIR + "/scripts" 

def create_resource_pack():
    """
    Creates a Minecraft resource pack with the specified parameters.
    Copies all contents from IMAGE_DIR and SOUNDS_DIR including subdirectories.
    
    Args:
        description (str): Resource pack description
        trigger_word (str): Trigger word for the pack
        resource_pack_name (str): Name of the output resource pack
    
    Returns:
        str: Path to the created zip file
    """
    output = RESOURCE_PACK_NAME + ".zip"
    
    # Create pack.mcmeta content
    pack_meta_content = {
        "pack": {
            "description": RESOURCE_PACK_DESCRIPTION + "\nTrigger Word: " + TRIGGER_WORDS,
            "pack_format": 15
        }
    }
    
    # Create a temporary directory for building the zip
    temp_dir = "temp_build_dir"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    try:
        # Create the required directory structure
        assets_path = os.path.join(temp_dir, "assets", "mobtalkerredux")
        os.makedirs(assets_path)
        
        # Copy pack.png
        if os.path.exists(PACK_IMAGE):
            shutil.copy2(PACK_IMAGE, os.path.join(temp_dir, "pack.png"))
        
        # Create and write pack.mcmeta
        with open(os.path.join(temp_dir, "pack.mcmeta"), 'w', encoding='utf-8') as f:
            json.dump(pack_meta_content, f, indent=4)
        
        # Copy entire image directory
        if os.path.exists(IMAGE_DIR):
            shutil.copytree(
                IMAGE_DIR, 
                os.path.join(assets_path, "textures"),
                dirs_exist_ok=True
            )
        
        # Copy entire sounds directory
        if os.path.exists(SOUNDS_DIR):
            shutil.copytree(
                SOUNDS_DIR, 
                os.path.join(assets_path, "sounds"),
                dirs_exist_ok=True
            )
        
        # Copy scripts if they exist
        if os.path.exists(SCRIPT_DIR):
            for script_file in os.listdir(SCRIPT_DIR):
                if script_file.endswith('.json'):
                    shutil.copy2(
                        os.path.join(SCRIPT_DIR, script_file),
                        os.path.join(assets_path, script_file)
                    )
        
        # Create the zip file
        if os.path.exists(output):
            os.remove(output)
            
        shutil.make_archive(RESOURCE_PACK_NAME, 'zip', temp_dir)
        
        return output
        
    finally:
        # Clean up temporary directory
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

def main():create_resource_pack() # Yeah, just run this file :v

if __name__ == "__main__":
    main() 

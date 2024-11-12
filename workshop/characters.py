from core.model import Character
# Yep, go ahead, make a new character here~

# This is where you make characters~
# The most important part is the outfit and id
# Both are used to handle character sprite location you see???

# In minecraft, character sprite will be located in
# textures/character.id/character.outfit/emotion.png

# Emotion is defined in the dialogue file.
# Like uhh... show(cupa,"happy")

# It will translate to 
# textures/cupa/default/happy.png

# Currently the Minecraft mod still hasn't have Character Outfit Swapping, yet
# But it's a good groundwork to have
# Just to make your script futureproof~

Cupa = Character(
        id="cupa", # The Id is for folder structure and such, make it unique pls, lower case
        name = "Cupa", # This shows up on the dialogue box
        description = "A creeper girl???", # Unused for now, but nice to have around~
        thoughts= "Unknown", # Same as above
        outfit = "default", # This is the outfit folder
        states = None, # Unused for now
        traits = None
        )

Andr = Character(
        id="andr", # The Id is for folder structure and such, make it unique pls, lower case
        name = "Andr",
        description = "An endergirl???",
        thoughts= "Unknown",
        outfit = "default",
        states = None,
        traits = None,
)


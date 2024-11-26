from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
# By the way, if you're wondering how it works
# It's just gonna combine all of the script into one big script
# So jumpTo and label works across file
# Because everything will be in one big file
def story():
    vn.label("yes")
    vn.say(c,"I was being rhetoric")
    vn.say(p,"I mean... I can lend you some...")
    vn.jumpTo("engarde")

    vn.label("no")
    vn.say(c,"I was being rhetoric")
    vn.say(p,"I mean...")
    vn.jumpTo("engarde")

    vn.label("engarde")
    vn.show(c,"normal")
    vn.say(c,"Since you're asking for a fight, why don't we?")
    vn.say(c,"You're not on hardcore, right?")
    vn.modVar("gamemode",vn.getGamemode())# modvar just changes the variable
    vn.condSame("gamemode","hardcore",[ # conditional to check if "gamemode" is "hardcore"
        vn.show(c,"scared",True), # Fuck, I hate this part...
        vn.say(c,"What the hell?!",True), # So basically, you have to add 'True' for nested stuff
        vn.say(c,"You're not supposed to play this mod on Hardcore!",True), # Don't ask what it is
        vn.show(c,"angry",True), # You just have to add it, okay?
        vn.say(c,"Screw it, I'm sending you back to World Creation, the hard way!",True) # Nothing I can do about it
    ]) # For now
    vn.say(p,"What does that have anything to do with us fighting?")
    vn.say(c,"It means I respawn after death")
    vn.say(c, "Anyway, let's duke it out! I think I got a few gunpowders in my pocket~")
    vn.finish()

    vn.label("gunpowder")
    vn.say(c,"Hmm... You know what? You're not that bad a person")
    vn.givePlayer("minecraft:gunpowder",6) # Minecraft specific command (might put this in another class)
    vn.say(c,"You know what to do with it~")
    vn.show(c,"happy")
    vn.say(c,"Pop off stranger!")
    vn.finish() # This ends the game
    return vn.dialogueDict
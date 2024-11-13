from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
a = Andr

def story():
    
    vn.start()
    vn.show(c,"normal") # show function will automatically create a path. "normal" is the sprite name, normal.png
    vn.say(c,"Oh hi! Is it my turn?")
    vn.show(c,"happy")
    vn.say(c,"Anyway, hi Internet! Long time no see!!!")
    vn.say(c,"How long has  it been? Ten years? More? Ahaha~")
    vn.show(c,"normal")
    vn.say(c,"Never thought this day would come, but yeah, Mob Talker mod is officially revived!!!")
    vn.say(c,"Ahem... so, as you can see just now, the new mod uses Name Tag to tag a character.")
    vn.say(c,"My uhh character as it appears in the Overworld doesn't come from this mod. This mod doesn't create any new mob nor is it dependent of any other mob")
    vn.show_custom(c,"normal",16,9,4,8,2,1)
    vn.say(c,"Basically, any entity that's named with the trigger word can trigger the mod.")
    vn.say(c,"The mod itself doesn't care about the type of entity it is.")
    vn.show_custom("asset","cupa1",16,9,4,8,5,1)
    vn.say(c,"For example, this is a Touhou Little Maid mod entity and it can trigger Cupa's script because the name is cupa")
    vn.show_custom("asset","cupa2",16,9,4,8,9,1)
    vn.say(c,"This, on the other hand, is a vanilla creeper with a CMM Resource  Pack on top of it, it will not trigger because the name is 'Cupa-chan' not 'Cupa'")
    vn.show_custom("asset","cupa3",16,9,4,8,13,1)
    vn.say(c,"And this is a vanilla villager with the CMM Resource Pack on top of it, it will trigger because the name is Cupa")
    vn.say(c,"So, if you, for example, name a chicken Cupa, it will uhh... Trigger too...")
    vn.show_custom(c,"angry",16,9,4,8,2,1)
    vn.say(c,"But don't actually do that,  there's a lot of mods out there  you can install for extra  immersion")
    vn.show_custom(c,"normal",16,9,4,8,2,1)
    vn.say(c,"But hey! This means that this mod isn't limited by the vanilla mobs like the old Mob Talker mod")
    vn.say(c,"As you can see, mods like Touhou Little Maid mod or Cute Mob Models Resource Pack can leverage this mod to create an immersive custom VN-like experience")
    vn.show_custom(c,"happy",16,9,4,8,2,1)
    vn.say(c,"You can theoretically have any characters in this mod, including other game, anime, movie, or any other characters you can think of")
    vn.say(c,"Imagine the possibilities!")
    vn.remove("asset","cupa1")
    vn.remove("asset","cupa2")
    vn.remove("asset","cupa3")
    vn.show(c,"normal")
    vn.say(c,"But yeah, that's what the mod's capable of~")
    vn.show(c,"happy")
    vn.say(c,"Thanks for listening!")
    vn.finish()
    return vn.dialogueDict
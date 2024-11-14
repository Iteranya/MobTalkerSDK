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
    vn.say(c,"How long has it been? Weeks? Months? Years?")
    vn.say(c,"normal")
    vn.say(c,"What was the last version anyway? 1.8? And the current version?")
    vn.show(c,"scared")
    vn.say(c,"What the hell! I've been dead for a whole decade!?")
    vn.show(c,"angry")
    vn.say(c,"Geez, can't believe this mod was abandoned for this long...")
    vn.show(c,"sad")
    vn.say(c,"But still though, Andr said it was nothing sort of miracle and dumb luck that Ars figured it out. So yeah...")
    vn.show(c,"angry")
    vn.say(c,"...")
    vn.say(c,"Still think it's a bummer...")
    vn.show(c, "normal")
    vn.say(c,"Ahem... anyway, as you can see just now, the new mod uses Name Tag to tag a character.")
    vn.say(c,"My uhh character as it appears in the Game doesn't come from this mod. This mod doesn't create any new mob nor is it dependent of any other mob")
    vn.say(c,"Basically, any entity that's named with the trigger word can trigger the mod.")
    vn.say(c,"The mod itself doesn't care about the type of entity it is.")
    vn.show_custom(c,"normal",16,9,4,8,2,1)
    vn.show_custom("asset","cupa1",16,9,4,8,5,1)
    vn.say(c,"For example, this is a Touhou Little Maid mod entity and it can trigger my (Cupa's) script because the name is Cupa")
    vn.show_custom("asset","cupa2",16,9,4,8,9,1)
    vn.say(c,"This, on the other hand, is a vanilla creeper with a CMM Resource  Pack on top of it. Though it looked a lot like me, it will not trigger because the name is 'Cupa-chan' not 'Cupa'")
    vn.show_custom("asset","cupa3",16,9,4,8,13,1)
    vn.say(c,"And this is a vanilla villager with the CMM Resource Pack on top of it, it will trigger because the name is Cupa")
    vn.say(c,"So, if you, for example, name a chicken Cupa, it will uhh... Trigger too...")
    vn.show_custom(c,"angry",16,9,4,8,2,1)
    vn.say(c,"But don't actually do that,  there's a lot of mods out there  you can install for extra  immersion")
    vn.show_custom(c,"normal",16,9,4,8,2,1)
    vn.say(c,"But hey! This means that this mod isn't limited by the vanilla mobs like the old Mob Talker mod")
    vn.say(c,"As you can see, mods like Touhou Little Maid mod or Cute Mob Models Resource Pack can leverage this mod to create an immersive custom VN-like experience")
    vn.show_custom(c,"happy",16,9,4,8,2,1)
    vn.say(c,"You can have any characters in this mod, including other game, anime, or even movies!")
    vn.say(c,"Imagine the possibilities!")
    vn.remove("asset","cupa1")
    vn.remove("asset","cupa2")
    vn.remove("asset","cupa3")
    vn.show(c,"normal")
    vn.say(c,"But someone still gotta write the script and draw the sprites...")
    vn.show(c,"happy")
    vn.say(c,"Thanks for listening!")
    vn.finish()
    return vn.dialogueDict
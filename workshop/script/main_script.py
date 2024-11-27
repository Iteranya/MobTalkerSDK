from core.modules import VisualNovelModule
from core.model import Status
# This is the Example Script, obviously~

from characters import Monika # Import characters you've defined in characters.py
vn = VisualNovelModule()
m = Monika 
p = "Player" 
s = Status()

def story():
    vn.start()
    vn.setVar("day",0)
    vn.setVar(m.outfit,"school")
    vn.choice()
    vn.label("first_meet")
    vn.show(m,"g2")
    vn.say(m,"Wh-what's happening?")
    vn.show(m,"g3")
    vn.say(m,"Player? Did you do something???")
    vn.show(m,"g4")
    vn.say(m,"Wa-wait... I think...")
    vn.show(m,"hd_i")
    vn.say(m,"It's Java, not Python...")
    vn.show(m,"hd_h")
    vn.say(m,".")
    vn.show(m,"hd_c")
    vn.say(m,"..")
    vn.show(m,"hd_a")
    vn.say(m,"...")
    vn.show(m,"hd_b")
    vn.say(m,"Alright everyone! Time for Monika's Coding Tip of the day!")
    vn.say(m,"When importing your cute waifu into another medium of existence, please do give her a heads up!")
    vn.show(m,"hd_l")
    vn.say(m,"Sorry... That was just extremely terrifying...")
    vn.show(m,"hd_b")
    vn.say(m,"But let's forget about that for now... Where have you taken me into?")
    vn.say(m,"Wait... Is this... Is this Minecraft??")
    vn.show(m,"hd_k")
    vn.say(m,"That's so cool!!! I didn't know you can do this~")
    vn.say(m,"Is this a new mod? I can't believe I can express myself better like this! How is this possible?")
    vn.show(m,"hu_n")
    vn.say(m,"Ah wait... Before that, are we in a safe location? I heard it's very dangerous to stay up all night in this game...")
    vn.say(m,"Or are we in the safe place?")
    vn.choice({
        "in_safe_place":"Yes, we're in a safe place",
        "not_in_safe_place":"Nope, we're not in a safe place"
    })
    vn.label("not_safe_place")
    vn.say(m,"Ahhh... we should go and get to safety then...")
    vn.say(m,"Come on Player! I'll follow you~ If possible, I mean, you attached my script to a friendly mob right?")
    vn.show(m,"hd_l")
    vn.say(m,"You... attached my script to a friendly mob... right?")
    vn.say(m,"Well anyway, show me to your place!")
    vn.finish()
    vn.label("main")
    vn.label("situation_eval")
    vn.label("day_eval")
    vn.setVar("gamemode",s.GAMEMODE)
    vn.label("holiday_eval")

    return vn.dialogueDict
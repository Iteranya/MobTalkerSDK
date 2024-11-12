from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Ars # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
a = Ars

def story():
    vn.label("basic_usage") 
    vn.show(a,"happy")
    vn.say(a,"Alright, script making timee!!")
    vn.show(a,"tired")
    vn.say(a,"Please bear with me, I really try to make this SDK as easy as possible to use")
    vn.say(a,"Alright, we start off from the last tutorial")
    vn.background(a,"vs_code_single_script")
    vn.remove(a)
    vn.say(a,"normal")
    vn.say(a,"This, friend dearest is the 'Demo Script'")
    vn.say(a,"Honestly, the best way you can make a script is by reverse engineering a script.")
    vn.say(a,"So, this will be the part where  I leave everything to Future Me")
    vn.say(a,"Sorry, for that... But we can't do a VN style tutorial for this kind of thing...")
    vn.show(a,"tired")
    vn.say(a,"Best of luck")
    vn.next("character_sprite")
    vn.finish()
    return vn.dialogueDict
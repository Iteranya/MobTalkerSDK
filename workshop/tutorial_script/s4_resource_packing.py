from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Ars # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
a = Ars

def story():
    vn.label("resource_packing") 
    vn.show(a,"happy")
    vn.say(a,"Welcome back viewers!")
    vn.show(a,"normal")
    vn.say(a,"Today we'll talk about resource packing")
    vn.say(a,"We've talked about this, but resource packing is how you publish your assets and scripts so that other people can play it")
    vn.say(a,"Let me give a little bit of a theory on how this mod works.")
    vn.show_left(a,"normal")
    vn.finish()
    return vn.dialogueDict
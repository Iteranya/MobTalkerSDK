from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Ars # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
a = Ars

def story():
    vn.label("basic_usage") 
    vn.show(a,"normal")
    vn.say(a,"Alright, script making time")
    vn.show(a,"happy")
    vn.say(a,"This is because I don't have to do anything!")
    vn.show(a,"normal")
    vn.say(a,"Ars will take it from here")
    vn.show(a,"happy")
    vn.say(a,"Best of luck")
    vn.next("finish_basic")
    vn.finish()

    vn.label("finish_basic")
    vn.show(a,"happy")
    vn.say(a,"Welcome back!")
    vn.show(a,"normal")
    vn.say(a,"I hope it wasn't too overwhelming...")
    vn.say(a,"Ah, wait, before we end this, let me show you how some of those commands look like")
    vn.show(a,"normal")
    vn.say(a,"This is what the choice command look like")
    vn.label("choice_showcase")
    vn.choice({
        "andr_left":"Move Left",
        "andr_right":"Move Right",
        "andr_middle":"Andr Middle"
    })
    vn.label("andr_left")
    vn.show_left(a,"normal")
    vn.say(a,"this is the `show_left(a,\"normal\")")
    vn.jumpTo("choice_showcase")
    
    vn.label("andr_right")
    vn.show_right(a,"tired")
    vn.say(a,"this is the `show_right(a,\"tired\")")
    vn.jumpTo("choice_showcase")

    vn.label("andr_middle")
    vn.show(a,"happy")
    vn.say(a,"this is the `show(a,\"happy\")")
    vn.show(a,"normal")
    vn.say(a,"But that's all about it, in the next part, we'll talk about how to deploy your script into a resourcepack.")
    vn.say(a,"Yes, you can just add script into config to test it, but if you wish to load in all the necessary assets such as the images and such, you still need to make a resource pack")
    vn.show(a,"happy")
    vn.say(a,"In any case, I will see you in the next video, take care now!")
    vn.next("resource_packing")
    vn.finish()
    return vn.dialogueDict
from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
a = Andr
p = "Player" 
n = "Narrator"

def story():
    vn.start()
    vn.label("day2") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(c, "normal")
    vn.say(c,"Ahh... Finally, it's morning time~")
    vn.show(c,"happy")
    vn.say(c,"Good Morning Player!")
    vn.choice({
        "chiper":"You're an early bird then?",
        "drowsy":"Mmm? Ngh? *yawn*"
    })

    vn.label("chiper")
    vn.show(c,"normal")
    vn.say(c,"Well, unlike a certain Bookmite, I am an early riser!")
    vn.say(c,"Starting your day right can make all the difference, ya know?")
    vn.say(c,"So go on then, do  your morning routine, get yourself prep up, I'll be here~")
    vn.next("mission")
    vn.finish()

    vn.label("drowsy")
    vn.show(c,"normal")
    vn.say(c,"Aww, come on player, you can do better than that!")
    vn.say(c,"Get a move on! Chop chop~ It's time to face the day")
    vn.say(c,"Or you can just... sleep in, it's whatever, I'll be waiting until you're ready")
    vn.next("mission")
    vn.finish()

    vn.label("mission")
    vn.say(c,"So... Player, what do you do, exactly?")
    vn.say(c,"Sorry if it sounds like a weird question... but like... Yknow...")
    vn.say(c,"I know... next to nothing about you, you see?")
    


    vn.label("day2idle")
    vn.show(c,"angry")
    vn.say(c,"Right... I'm still stuck with you here...")
    
    vn.condNight([
        vn.say("Narrator","The day have come to an end. Are you at home and ready to end the day?",True),
        vn.choice({
            "night2": "Yes",
            "chat_idles": "No"
        },True)
    ])    
    vn.jumpTo("chat_idles")
    vn.finish()
    return vn.dialogueDict
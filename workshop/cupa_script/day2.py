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
    vn.show(c,"happy")
    vn.say(c,"Get a move on! Chop chop~ It's time to face the day")
    vn.show(c,"normal")
    vn.say(c,"Or you can just... sleep in, it's whatever, I'll be waiting until you're ready")
    vn.next("about_player")
    vn.finish()

    vn.label("about_player")
    vn.show(c,"normal")
    vn.say(c,"So... Player, what do you do, exactly?")
    vn.say(c,"Sorry if it sounds like a weird question... but like... Yknow...")
    vn.say(c,"I know... next to nothing about you, you see?")
    vn.say(c,"Like, I've heard rumours of how over powered Players are compared to everything else,  including boss mobs.")
    vn.show_custom(c,"normal",16,9,6,12,6,1)
    vn.say(c,"But like... What do you do exactly?")
    vn.choice({
        "i_mine":"Mining/Exploring",
        "i_craft":"Crafting/Building",
        "i_do_whatever":"Anything Fun"
    })
    
    vn.label("i_mine")
    vn.show(c,"normal")
    vn.say(c,"Hmm, unearthing treasures deep in the depths I see?")
    vn.say(c,"Interesting~")
    vn.jumpTo("cupa_request")

    vn.label("i_craft")
    vn.show(c,"normal")
    vn.say(c,"Hmm, creating wonders beyond anyone's imagination huh?")
    vn.say(c,"Interesting~")
    vn.jumpTo("cupa_request")

    vn.label("i_do_whatever")
    vn.show(c,"happy")
    vn.say(c,"Ahaha! I feel you! Sometimes you just wanna enjoy life, right?")
    vn.say(c,"There's loads of fun things you can do in this world~")
    vn.jumpTo("cupa_request")

    vn.label("cupa_request")
    vn.say(c,"...")
    vn.show(c,"sad")
    vn.say(c,"...")
    vn.show(c,"normal")
    vn.say(c,"Can you do me a favor?")
    vn.say(c,"I... I might need your help with, returning...")
    vn.show(c,"sad")
    vn.say(c,"I... I honestly don't know where to start...")
    vn.choice({
        "memories":"What do you remember?",
        "memories":"When did all this started?"
    })

    vn.label("memories")
    vn.say(c,"Last thing I remembered huh???")
    vn.say(c,"Hmm...")
    vn.show(c,"angry")
    vn.say(c,"HMMMMMMMMMMMM...")
    vn.show(c,"normal")
    vn.say(c,"Nope! Nothing came to mind!")
    vn.say(c,"Guess I'll leave it to you to figure it out~")
    vn.unlock_dialogue(["about_cats"])
    vn.next("day2idle")
    vn.finish()

    vn.label("day2idle")
    vn.show(c,"normal")
    vn.say(c,"Hmm? Something on your mind?")
    
    vn.condNight([
        vn.say("Narrator","The day have come to an end. Are you at home and ready to end the day?",True),
        vn.choice({
            "night2": "Yes",
            "chat_idles": "No"
        },True)
    ])    # Commented because not available yet
    vn.jumpTo("chat_idles")
    vn.finish()
    return vn.dialogueDict
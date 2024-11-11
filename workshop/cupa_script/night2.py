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
    vn.label("night2")
    vn.show(c,"normal")
    vn.say(c,"Say, player...")
    vn.say(c,"Do you have the ability to see how to create item just by looking at it?")
    vn.choice({
        "jei_installed":"Yes, actually, there's a mod that lets me do that",
        "jei_not_installed":"Uhh... No, actually, why?"
    })

    vn.label("jei_installed")
    vn.show(c,"happy")
    vn.say(c,"Ha! I knew it!")
    vn.show(c,"normal")
    vn.say(c,"Here, I think this is broken, like really broken...")
    vn.say(c,"Can you figure out how to make a new one? Or what to do with it?")
    vn.givePlayer("mobtalkerredux:creeper_gate_broken_key_item",1)
    vn.say(n,"The creeper handed you a strange item, it felt cold your hand.")
    vn.show(c,"happy")
    vn.say(c,"Do your magic, player!")
    vn.next("creeper_gatekey")
    vn.finish()

    vn.label("creeper_gatekey")
    vn.say(c,"So, how was it?")
    vn.say(n,"Unfortunately for you and Cupa, the item requires materials with no known crafting recipe.")
    vn.jumpTo("jei_not_installed")

    vn.label("jei_not_installed")
    vn.show(c,"sad")
    vn.say(c,"Hmmm... Guess that'll be too easy huh???")
    vn.show(c,"tired")
    vn.say(c,"I can't believe I'm saying this... But... Can you ask Andr for help?")
    vn.show(c,"sad")
    vn.say(c,"I'm not on good terms with her, but... I think you're the only one that can help me here...")

    vn.next("night2idles")
    vn.finish()

    vn.label("night2idles")
    vn.show(c,"normal")
    vn.say(c,"Good evening")
    
    vn.condDay([
        vn.say("Narrator","The sun has risen, ready to start your day?",True),
        vn.choice({
            "day3": "Yes",
            "chat_idles": "No"
        },True)
    ])    
    vn.jumpTo("chat_idles")
    vn.finish()
    return vn.dialogueDict
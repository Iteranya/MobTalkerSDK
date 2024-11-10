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
    vn.label("night1")
    vn.say(c,"So... This is your place huh...")
    vn.show(c,"angry")
    vn.say(c,"Anyway, you haven't really told me... Who Are You?")
    vn.choice({
        "i_am_steve":"I... Am Steve!",
        "i_am_player":"You can call me 'Player'"
    })
    
    vn.label("i_am_steve")
    vn.say(c,"Okay... 'Steve'...")
    vn.say(c,"I'm just gonna call you player, how about it?")
    vn.say(n,"You nodded, realizing how cringe that introduction was")

    vn.label("i_am_player")
    vn.say(c,"Great, I kinda already know that you are Player")
    vn.show(c,"normal")
    vn.say(c,"You're certainly not a normal human. For one, you're gonna revive after death.")
    vn.say(n,"It is important for the person behind the screen to know that neither this mod nor the script will take account to all the madlads who decided to play this mod in Hardcore mode.")
    vn.say(c,"I'm just like you, you know? If I die, I will probably revive. But now...")
    vn.show(c,"sad")
    vn.say(c,"Ahh... I don't think that's the case anymore... It's like... If I die, I'll die for real, but you...")
    vn.show(c,"angry")
    vn.say(c,"There is... a way... that I can stay alive...")
    vn.show(c,"sad")
    vn.say(c,"And... Ahhh... I don't like it either...")
    vn.condSame("kiss",True,[
        vn.say(c,"I mean YOU probably like it",True),
        vn.say(c,"You creep...",True)
    ])
    vn.say(c,"But umm... close your eyes...")
    vn.say(c,"Just... Just do it!!!")
    vn.show_custom("asset","black_screen",16,9,16,9,1,1)
    vn.say(n,"Something wet and soft met your lips.")
    vn.say(n,"The sensation lingered for a long while")
    vn.say(n,"You tried opening your eyes")
    vn.remove("asset","black_screen")
    vn.show(c,"shy")
    vn.say(c,"...")
    vn.show(c,"sad")
    vn.say(c,"D-don't take this the wrong way! There's a perfectly logical reason why that was required. I did not want to do it, I just had to mark you with an NBT data of me.")
    vn.say(c,"Ba-basically, if anything happen to me... you can bring me back, just... I dunno, I'm sure  you know exactly how it works!!!")
    vn.show(c,"angry")
    vn.say(c,"Again! No funny thoughts! Hmmph!")
    vn.unlock_dialogue(["realms"])
    vn.next("night1idles")
    vn.finish()

    vn.label("night1idles")
    vn.show(c,"angry")
    vn.say(c,"Hmm...?")
    
    vn.condDay([
        vn.say("Narrator","The sun has risen, ready to start your day?",True),
        vn.choice({
            "day2": "Yes",
            "chat_idles": "No"
        },True)
    ])    
    vn.jumpTo("chat_idles")
    vn.finish()
    return vn.dialogueDict
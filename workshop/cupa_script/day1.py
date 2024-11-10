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
    vn.label("start") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(c, "sad")
    vn.say("???","Ho?")
    vn.label("face_off")
    vn.show(c, "angry")
    vn.say("???", "*squints*")
    vn.choice({
        "squint":"Squint back",
        "who":"Uhh... who are you?"
    })
    
    vn.label("squint")
    vn.say(n,"You squinted back at her")
    vn.say(n,"Though the sprite doesn't show it, she squints back harder at you")
    vn.show_left(c,"angry")
    vn.say("???","...")
    vn.show_right(c,"angry")
    vn.say("???","...")
    vn.show(c, "angry")
    vn.say("???","...")
    vn.condSame("kiss",True,[
        vn.say(n,"Perhaps learning from her mistake, the girl kept her distance this time...",True),
        vn.choice({
        "who":"Uhh... Who are you?",
        "step_closer":"Take a step closer"
        },True)
    ])
    vn.show_custom(c,"angry",16,9,6,12,5,1)
    vn.say("???","...")
    vn.choice({
        "squint_harder":"Squint Harder At Her",
        "step_back":"Take a step back",
    })
    
    vn.label("squint_harder")
    vn.show_custom(c, "angry",16,9,8,16,4,1)
    vn.say(n,"The girl stepped closer towards you, squinting even harder")
    vn.say("???","...")
    vn.choice({
        "squint_harder":"Squint Harder At Her",
        "lean_in":"Lean in for a kiss",
        "who":"Ummm... Who are you?"
    })

    vn.label("lean_in")
    vn.say(n,"Perhaps in a spur of the moment, you lean in to kiss her.")
    vn.show_custom(c, "sad",16,9,8,16,4,1)
    vn.say(n,"Your lips met hers and perhaps it didn't register to her immediately")
    vn.say(n,"But the girl simply froze...")
    vn.say("???",".")
    vn.say("???",". .")
    vn.say("???",". . .")
    vn.show_custom(c, "scared",16,9,8,16,4,1)
    vn.show(c, "scared")
    vn.say("???", "What the hell?!")
    vn.say(n,"The girl is blushing despite the sprite not showing it")
    vn.say(n,"See, this is why I'm very important for the narrative, it lets you know what's happening when the visual representation fails...")
    vn.say("???","You creep!")
    vn.show(c,"angry")
    vn.say(c,"Stay away from me!")
    vn.setVar("kiss",True)
    vn.next("face_off")
    vn.finish()

    vn.label("step_back")
    vn.show(c,"angry")
    vn.say(c,"It's... Cupa... What do you want?")
    vn.jumpTo("first_ask")

    vn.label("step_closer")
    vn.say("???","Hey! Back off!")
    vn.show_custom(c,"angry",16,9,3,6,7,1)
    vn.say("???","Stay away from me!")
    vn.finish()

    vn.label("who")
    vn.say(c,"It's... Cupa")
    vn.show(c,"angry")
    vn.condSame("kiss",True,[
        vn.say(c,"You creep...",True)
    ])
    vn.say(c,"What do you want?")
    
    vn.label("first_ask")
    vn.choice({
        "gunpowder":"Can I have Gunpowder?",
        "about_you":"I want to know more about you!"
    })

    vn.label("gunpowder")
    vn.show(c,"tired")
    vn.say(c,"Ugh... I knew it...")
    vn.finish

    vn.label("about_you")
    vn.show(c,"sad")
    vn.say(c,"Eh?")
    vn.say(c,"You want to know about me?")
    vn.say(n,"The girl looks confused at first, though, a smile slowly formed on her face")
    vn.show(c,"normal")
    vn.say(c,"Oh, I see, I guess you can tell that I'm not just a villager huh?")
    vn.say(c,"Hmm... Something about me, I guess my hoodie could be a hint of who I am~")
    vn.choice({
        "you_creeper": "You're a creeper?",
        "you_cactus":"You're a cactus?",
    })
    
    vn.label("you_creeper")
    vn.show(c,"happy")
    vn.say(c,"Mmm~ You're pretty close there")
    vn.show(c,"normal")
    vn.say(c,"Is it the green? The pattern? All that sass?")
    vn.jumpTo("creeper_boss")

    vn.label("you_cactus")
    vn.show(c,"angry")
    vn.say(c,"Did Andr put you up to this?")
    vn.show_custom(c,"angry",16,9,6,12,5,1)
    vn.say(c,"Tell that Pearl Glazing Bookmite that I don't give the slightest fuck about the theories. I'm not a bloody plant or a mushroom.")
    vn.show(c,"tired")
    vn.say(c,"I'm a creeper and I can damn well show you what a plant can't do.")
    vn.jumpTo("creeper_boss")

    vn.label("creeper_boss")
    vn.say(c,"But to be more specific, I'm a creeper boss mob.")
    vn.say(c,"You've heard of Boss Mob before, right? I wouldn't be surprised if you've never seen one.")
    vn.say(c,"We don't usually stick around in this realm...")
    vn.show(c,"normal")
    vn.say(c,"Anyway, I gotta go now, catch ya later, try not to follow me.")
    vn.unlock_dialogue(["cactus_theory","boss_mob"])
    vn.next("stuck")
    vn.finish()

    vn.label("stuck")
    vn.show(c,"tired")
    vn.say(c,"It has come to my attention that I am stuck here...")
    vn.say(n,"The girl before you is blushing, as if too embarrassed to articulate her true thoughts.")
    vn.say(c,"You got... room to spare...?")
    vn.choice({
        "what_happened":"What Happened?",
        "too_fast":"Aren't you taking this too fast?"
    })

    vn.label("too_fast")
    vn.show(c,"angry")
    vn.say(c,"Ugh... Knew you'd say that...")
    vn.condSame("kiss",True,[
        vn.say(c,"And remembering what you did, I'm getting second thoughts now...",True),
        vn.say(c,"But, Ahh, screw it...",True)
    ])
    vn.show_right(c,"Look, no funny business, it's...")
    vn.jumpTo("what_happened")

    vn.label("what_happened")
    vn.show(c,"sad")
    vn.say(c,"I'm actually stuck here, in the Overworld")
    vn.say(c,"It's... dammit, it's pissing me off")
    vn.say(c,"But I can't access my realm anymore, I don't know what happened.")
    vn.next("day1idle")
    vn.say(c,"So... yeah...  Just... I'll follow along for now, aight?")
    vn.finish()


    vn.label("day1idle")
    vn.show(c,"angry")
    vn.say(c,"Right... I'm still stuck with you here...")
    
    vn.condNight([
        vn.say("Narrator","The day have come to an end. Are you at home and ready to end the day?",True),
        vn.choice({
            "night1": "Yes",
            "chat_idles": "No"
        },True)
    ])    
    vn.jumpTo("chat_idles")
    vn.finish()
    return vn.dialogueDict
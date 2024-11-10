from core.modules import VisualNovelModule
# This is the Example Script, obviously~
from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
a = Andr
p = "Player" 
n = "Narrator"
def story():
    
    vn.label("chat_idles")
    vn.idle_chats()

    vn.label("cactus_theory")
    vn.show(c,"angry")
    vn.say(c,"But for real, you don't think I look like a cactus do you?")
    vn.choice({
        "not_cactus":"No, not really",
        "is_cactus":"I mean, you're green and..."
    })

    vn.label("not_cactus")
    vn.show(c,"happy")
    vn.say(c,"Haha! I know right? Andr's just being silly, that's all")
    vn.show(c,"normal")
    vn.say(c,"Creepers are not cactus! I mean, cactus don't blow up in your face now, do they???")
    vn.say(c,"Just because we got the green and all, doesn't mean we're plants!!!")
    vn.jumpTo("just_a_theory")
    
    vn.label("is_cactus")
    vn.show(c,"angry")
    vn.say(c,"Ugh... Not you too!")
    vn.say(c,"Hmph...")
    vn.say(c,"I'd like to hear your thoughts once I blow you up to the Nether!")
    vn.jumpTo("just_a_theory")

    vn.label("just_a_theory")
    vn.show(c,"tired")
    vn.say(c,"But for real though...")
    vn.say(c,"There's this weird dude Andr really likes who made a theory that I'm some sort of a mushroom.")
    vn.say(c,"The rumour spreads, because  it's Andr and now everyone's comparing me to a cactus!")
    vn.show(c,"scared")
    vn.say(c,"Cacti aren't even a Mushroom!!!")
    vn.show(c,"sad")
    vn.say(c,"They even went to an elaborate length about how Creepers are exploding as a way to spread their spores, do you know that?! It's so weird!!!")
    vn.say(c,"I mean, it's just a theory, but you know what? As a  Creeper, I'm going to debunk this theory right here, right now")
    vn.show(c,"angry")
    vn.say(c,"Creepers aren't plants! We're mobs! Powerful mobs!!! The kind that should be feared and heralded as the argent of destruction!!!")
    vn.jumpTo("incoming_call")
    vn.finish()

    vn.label("boss_mob")
    vn.show(c,"normal")
    vn.say(c,"Say, how come you don't know what boss mobs are?")
    vn.say(c,"I mean, yeah, sure we're rare, but like... you're one too, no?")
    vn.say(c,"Right?")
    vn.choice({
        "am_i":"Am I?",
        "am_i":"Guess I am"
    })

    vn.label("am_i")
    vn.say(c,"Yeah! How do I know this? Well you respawn after death!!!")
    vn.say(c,"Only boss mob can pull that off")
    vn.choice({
        "responsible":"What do Boss Mob do?",
        "responsiblent":"Does that mean I do anything?"
    })
    
    vn.label("responsible")
    vn.say(c,"What do boss mob do?")
    vn.show(c,"sad")
    vn.say(c,"...")
    vn.show(c,"happy")
    vn.say(c,"We do whatever we want!")
    vn.say(c,"We are above consequences!")
    vn.choice({
        "responsiblent":"Really?",
        "responsiblent":"Above consequences???"
    })
    
    vn.label("responsiblent")
    vn.show(c,"happy")
    vn.say(c,"Hell yeah! We boss mobs can do anything we want!")
    vn.show(c,"normal")
    vn.say(c,"That includes you by the way! You're 'The Player', you have the power to rewrite the very rules that governs this universe!")
    vn.show(c,"happy")
    vn.say(c,"This world is yours, don't think about responsibility, you're above all that boring stuff!")
    vn.jumpTo("incoming_call")
    vn.finish()

    vn.label("realms")
    vn.show(c,"normal")
    vn.say(c,"Ahhh... I gotta admit, this place is way better than my home...")
    vn.say(c,"No, not the house you built, but like... The Overworld")
    vn.choice({
        "creeper_dimension":"You're not from the Overworld?",
        "creeper_dimension":"You're from different dimension?"
    })
    vn.label("creeper_dimension")
    vn.show(c,"happy")
    vn.say(c,"Yep!  I'm from the creeper dimension!!!")
    vn.show(c,"normal")
    vn.say(c,"...")
    vn.show(c,"angry")
    vn.say(c,"What are you looking at me like that? Bet you think it's a terrible place to live, huh!?")
    vn.say(c,"Well... No! It's a... It's umm...")
    vn.show_left(c,"sad")
    vn.say(c,"It's... It looks like the moon...")
    vn.say(c,"I don't stay there often...")
    vn.show(c,"tired")
    vn.say(c,"But it's still my realm, you hear? And I would prefer that than this... place... you got...")
    vn.show(c,"sad")
    vn.say(c,"And... even though your home, I mean, the Overworld looks way prettier than my realm...")
    vn.say(c,"Ahhh... What am I thinking, of course I want to go back.")
    vn.jumpTo("incoming_call")

    vn.label("incoming_call")
    vn.say(n,"There's an incoming call from an unknown number...")
    vn.say(n,"Pick Up?")
    vn.choice({
        "tutorial":"Sure",
        "end":"No Thanks"
    })
    
    vn.label("end")
    vn.finish()

    vn.label("tutorial")
    vn.show(a,"normal")
    vn.say(a,"Excuse Me")
    vn.show_left(c,"scared")
    vn.say(c,"What the fuck, Andr? What are you doing here?!")
    vn.say(a,"Sorry for the 4th wall break. This is a 'random conversation' that triggers when the 'current day' conversation has been exhausted. I'm here to bring some informations.")
    vn.show_left(c,"angry")
    vn.say(c,"Look, just keep it quick...")
    vn.say(a,"Mm, So here's the thing... Due to 'technical', limitation, the Developer Ars Iteranya have decided not to add a 'real' time or day mechanic. Instead, they cheated, well, not cheated, but rather mark it as a feature.")
    vn.say(a,"The point of day feature is to stop people from speedrunning through the game, yes? That and points of immersion. Iteranya saw this and they decided to just... Skip the entire minecraft handling part of things.")
    vn.say(a, "So, let me explain how... This works, ahem...")
    vn.say(a, "In a nutshell, time progression can only happen at night when you go to sleep.")
    vn.show(a,"shy")
    vn.say(a, "And... well... in a sense... A script maker has to write a 'good night' scene between the mob and player. Since this can only be triggered at night, they have to wait until nighttime.")
    vn.show_left(c,"tired")
    vn.say(c, "Wouldn't the player just speedrun through the night?")
    vn.show(a,"tired")
    vn.say(a,"Good point, Cupa, yes, the player can just speedrun through the night. Due to this, script maker has to make both day and night scenes. Let me explain a bit more.")
    vn.show_custom(a,"normal",16,9,4,8,13,1)
    vn.show_custom("asset","event_handling",16,9,9,6,2,1)
    vn.say(a,"There should be a graph on your left")
    vn.say(a,"If the texture is broken, go to the resourcepack menu and load the generated resourcepack")
    vn.say(a,"Apologies, in advance... But the dev's having trouble loading generated resourcepack automatically")
    vn.show(c,"tired")
    vn.say(c,"Why did you cover me up?")
    vn.show_custom(a,"tired",16,9,4,8,13,1)
    vn.say(a,"/vn.remove(c)")
    vn.show(c,"scared")
    vn.say(c,"Wait, did you just...")
    vn.remove(c)
    vn.say(a,"Ahem, now where was I...")
    vn.show_custom(a,"normal",16,9,4,8,13,1)
    vn.say(a,"Right, event handling. On your left is how the developer designed the event system of this Mob Talker Framework.")
    vn.say(a,"The vanilla one I mean, mod maker is free to implement their own system. This is for 'script making' without Java or Mod development")
    vn.say(a,"As you can see, there are 2 types of scene... Idle Event and Main Event")
    vn.say(a,"When you talk with Cupa for the first time, you are playing the main event. In a single day, usually there are one or two or even three main event")
    vn.say(a,"At some point, you will exhaust all the event for that 'day'. When that happens, a random event will trigger. The conversation you had with Cupa before this one is an example of random event.")
    vn.say(a,"You have to wait until nighttime for a new event. Hence  you cannot simply 'speedrun' through this game.")
    vn.say(a,"Doing main event will also lets you 'unlock' new idle scenes")
    vn.say(a,"Increasing love/affection will give you unique versions of idle events, actually depends on how the Script Maker write it, but that's how the developer intended for the affection system to be designed.")
    vn.say(a,"That would be all...")
    vn.say(a,"You can skip this scene next time by selecting 'Decline' when I called you. Don't  worry, I will  assume you already seen this scene.")
    vn.show(a,"happy")
    vn.remove("event_handling")
    vn.say(a,"Thank you for helping the dev test out this mod!")
    vn.finish()
    
    return vn.dialogueDict
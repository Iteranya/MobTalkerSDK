from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 

def story():
    vn.start()
    vn.label("day5")
    vn.show(c,"sad")
    vn.say(p,"Hey, Cupa. Geez, the storm is still pouring very harshly, huh?")
    vn.say(c,"...")
    vn.say(p,"(I'm not liking this bit...) Cupa? What's the matter?")
    vn.say(c,"Player... Sorry if this is very sudden, but I have to get going...")
    vn.say(p,"Wha-- Hold on! You're just gonna up and leave? What's going on, Cupa?")
    vn.say(c,"...")
    vn.say(p,"Cupa, I'm your friend. You can tell me what's wrong and I'll do what I can to help you. Isn't that what friends are for?")
    vn.show(c,"sad")
    vn.say(c,"... I remember everything... About who I am and what happened to me. I was foraging along with my mother until a bunch of male Creepers approached us. They were being weird and creepy towards us. As they came closer, my mother and I ran. We ran for a good while, but I fell into a hole. Those Creepers split up to get us and that's how my mother and I got separated. Then it started storming, like how it is now. I ran as long and as far as I could trying to get away from those creeps. After a while, I wasn't looking where I was going and fell off a cliff. I hit my head on the way down and I lost consciousness. When I woke up, I couldn't remember a single thing about me.")
    vn.show(c,"tired")
    vn.say(c,"That was when I patched myself up and tried to stay with the villagers. And that was when I met you and the rest was history. To top it all off, that woman in black I've been talking about multiple times... All this time, she was my mother. And if she's out there somewhere, I'm worried those male creepers might have gotten to her, and I need to get out there and find her!")
    vn.say(p,"Let me go with you.")
    vn.show(c,"sad")
    vn.say(c,"... Player, thank you... Thank you so much for taking good care of me. You're the best friend I could ever ask for. I don't know how I could ever repay you. But this is a family matter, something I have to do myself.")
    vn.show(c,"shy")
    vn.say(c,"I appreciate everything you've done for me. If I have the chance, I'll come back to see you again. I'll introduce you to my mother too.")
    vn.show(c,"sad")
    vn.say(c,"So... ... Goodbye.")
    vn.say(p,"Wait! Dammit! ... Cupa... Be careful out there... Because if something happens to you, I wouldn't be able to forgive myself... So please, come back so I can see you again...")
    vn.show("Cupa's voice","shy")
    vn.say("Cupa's voice","Player, thank you...")
    vn.addVar("aff",93)
    vn.finish()
    
    return vn.dialogueDict
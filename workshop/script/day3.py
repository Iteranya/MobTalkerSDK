from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 

def story():
    vn.start()
    vn.label("day3")
    vn.show(c,"sad")
    vn.say(p,"Good morning, Cupa.")
    vn.say(c,"...")
    vn.say(p,"Cupa? Are you all right?")
    vn.show(c,"tired")
    vn.say(c,"Oh! Good morning, Player. You're up early.")
    vn.say(p,"Cupa, it's bright as day right now.")
    vn.show(c,"sad")
    vn.say(c,"Oh. Really? How long have I been here?")
    vn.say(p,"Cupa, were you not able to sleep last night because of the storm?")
    vn.say(c,"Y-Yeah... I had a nightmare. When I woke up, I was sitting here thinking about my memories and that nightmare... I must've been sitting here for a long time and I didn't realize it...")
    vn.say(p,"Is that so? If you don't mind me asking, what happened in your nightmare?")
    vn.say(c,"Um... It's hard to remember since it's fuzzy now... But I remember... it was storming, just like last night. I was running away from something, but I'm not sure what I was running from. And then suddenly, I was struck by lightning.")
    vn.show(c,"tired")
    vn.say(c,"It should've killed me, but somehow, I changed to a completely different person. The next thing I knew, I was destroying a village... The very same village that I was kicked out of... The villagers... I... I...")
    vn.say(p,"Cupa...")
    vn.say(c,"...I'm scared... That's not the kind of person I was, right? Or who I'm going to be? I'm not some crazed Creeper bent on killing villagers, am I?")
    vn.say(p,"Cupa.")
    vn.say(c,"Huh? W-What are you...")
    vn.say(p,"It's going to be all right. That's not who you are now. You haven't hurt anyone, not even me.")
    vn.show(c,"sad")
    vn.say(c,"H-How do you know if I'm not going to turn into some sort of monster one day and hurt you?")
    vn.say(p,"Dreams are a reflection of one's real-life experience and memories, but sometimes they can be a little outrageous. I had dreams where I died in various ways, like falling to my death or getting eaten by zombies. Even though I had those dreams, it didn't actually happen.")
    vn.say(p,"And I believe that you wouldn't turn into some charged Creeper monstrosity and go on a killing spree.")
    vn.say(c,"But... it's still possible to become a charged Creeper, isn't it?")
    vn.say(p,"Yes, but you are not a monster. You're still you right now. I believe you'll come to your senses. That's the Cupa I know.")
    vn.show(c,"shy")
    vn.say(c,"...(playername). Thank you. I'm glad to have you with me.")
    vn.say(p,"Anything for a friend.")
    vn.show(c,"happy")
    vn.say(c,"Ehehe~ Ahh~ You're so warm~")
    vn.say(p,"Are you feeling better now?")
    vn.show(c,"shy")
    vn.say(c,"Yes, I feel much better. Thank you.")
    vn.show(c,"sad")
    vn.say(c,"I'm a little tired, though.")
    vn.show(c,"normal")
    vn.say(p,"Get some rest then. You've been here for hours, and you haven't had any sleep since.")
    vn.say(c,"Yeah, you're right. I'll see you later then.")
    vn.say(p,"See you later, Cupa.")
    vn.addVar("aff",1)
    vn.next("day4")
    vn.finish()
    
    return vn.dialogueDict
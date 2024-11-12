from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Ars # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
a = Ars

def story():
    
    vn.start()
    vn.label("beginning") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(a,"normal") # show function will automatically create a path. "normal" is the sprite name, normal.png
    vn.say(a,"Hi")
    vn.say(a,"Yes, this is rendered in real time in Minecraft")
    vn.say(a,"Except for the voice  over")
    vn.show(a,"shrug")
    vn.say(a,"Didn't put in that feature yet, sorry")
    vn.show(a,"normal")
    vn.say(a,"But anyway, this is the first part tutorial of the Brand New Mob Talker mod")
    vn.say(a,"All the link's in the description, so  let's get right to it!")
    vn.show_custom(a,"present",16,9,4,8,2,1)
    vn.show_custom("asset","modrinth",16,9,10,6,6,1)
    vn.say(a,"This... is  the Mob Talker Framewor!")
    vn.show_custom(a,"normal",16,9,4,8,2,1)
    vn.say(a,"Made this in like... half a month? A madlad's attempt at reviving an abandonware so to speak.")
    vn.say(a,"It has almost all of the functionality of the old mod and more. I think the only limitation is that it cannot overwrite a mob's behavior. And I think that's for the best, in terms of compatibility I mean")
    vn.say(a,"But anyway, install this mod like any other mod. Just drag it into your minecraft mod folder.")
    vn.say(a,"Of course, just like the old mod, you still need to install some scripts! Due to the fact  that I *just* finished  this mod, I don't think many scripts exists yet.")
    vn.show_custom(a,"shrug",16,9,4,8,2,1)
    vn.say("I got a Discord Server for Discussion and Query and you can find my custom script there, just sayin'")
    vn.say(a,"But yeah, depending on when you watch this video, the scripts may not exists yet.")
    vn.show_custom(a,"normal",16,9,4,8,2,1)
    vn.say(a,"I got one made for Cupa tho, which we'll explore after this.")
    vn.say(a,"So yeah...")
    vn.remove("modrinth")
    vn.show(a,"normal")
    vn.say(a,"Sorry, doesn't support animation yet, still working on it")
    vn.say(a,"Anyway, Installing Scripts is quite  easy")
    vn.say(a,"It's  the same as installing a resourcepack")
    vn.say(a,"No like, literally... Lemme show you...")
    vn.next("resouce_pack_install")
    vn.finish()

    vn.label("resouce_pack_install")
    vn.show(a,"happy")
    vn.say(a,"There, done!")
    vn.show(a,"normal")
    vn.say(a,"that's it, that's the entire installation")
    vn.say(a,"Now let's take a closer look at the Resource Pack page...")
    vn.show_custom("asset","resource_pack",16,9,10,6,6,1)
    vn.show_custom(a,"normal",16,9,4,8,2,1)
    vn.say(a,"There's this thing called  'Trigger Word', so what is it, actually?")
    vn.say(a,"Well, it's best if I show you...")
    vn.next("intro_credit")
    vn.finish()

    vn.label("intro_credit")
    vn.show(a,"normal")
    vn.say("And that's everything you need  to know about installing this mod")
    vn.say(a,"To recap, all you have to do install the mod like any other, install the script like resource pack, and name a mob with the Trigger Word.")
    vn.say(a,"Thanks for watching, the next videos  will talk about how to make scripts!")
    vn.say(a,"Have fun then see ya!")
    vn.next("sdk_installation")
    vn.finish()
    return vn.dialogueDict
from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
a = Andr

def story():
    
    vn.start()
    vn.label("beginning") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(a,"normal") # show function will automatically create a path. "normal" is the sprite name, normal.png
    vn.say(a,"Hello, it's been a while")
    vn.show(a,"happy")
    vn.say(a,"Nice to meet you again player! And before you ask, yes, everything you see is rendered in real time in Minecraft")
    vn.show(a,"normal")
    vn.say(a,"The developer, Ars, asked me to explain to all of you about the new version of the Mob Talker mod for Minecraft Java 1.20.1")
    vn.show(a,"tired")
    vn.say(a,"He's probably doing a voice over... Sorry if it sounds weird.")
    vn.show(a,"normal")
    vn.say(a,"But anyway, this is the first part tutorial of the Brand New Mob Talker mod")
    vn.say(a,"All the link's in the description, so  let's get right to it!")
    vn.show_custom(a,"happy",16,9,4,8,2,1)
    vn.show_custom("asset","modrinth",16,9,10,6,6,1)
    vn.say(a,"This... is  the Mob Talker Framework!")
    vn.show_custom(a,"normal",16,9,4,8,2,1)
    vn.say(a,"The dev put in... half a month of work? It's still a bit rough around the edges, but as you can see, it's functional")
    vn.say(a,"It has almost all of the functionality of the old mod and more. I think the only limitation is that it cannot overwrite a mob's behavior. And I think that's for the best, in terms of compatibility I mean")
    vn.say(a,"But anyway, install this mod like any other mod. Just drag it into your minecraft mod folder.")
    vn.say(a,"Of course, just like the old mod, you still need to install some scripts! Due to the fact  that Ars *just* finished  this mod, I don't think many scripts exists yet.")
    vn.show_custom(a,"happy",16,9,4,8,2,1)
    vn.say(a,"Thankfully the dev has prepared a Discord Server for discussion, query, and perhaps in the near future... a place where people can share their scripts!")
    vn.show_custom(a,"tired",16,9,4,8,2,1)
    vn.say(a,"Though... so far... there's only like... 4 people in there... No one has made a script yet")
    vn.say(a,"It's a bit disheartening, but hopefully more people realize this mod's back to life now and can start making script")
    vn.show_custom(a,"normal",16,9,4,8,2,1)
    vn.say(a,"There is one script made by the dev, about Cupa.")
    vn.say(a,"So hopefull it'll be enough to convince people to try their hands at making script!")
    vn.remove("modrinth")
    vn.show(a,"normal")
    vn.say(a,"Sorry, doesn't support animation yet, the dev is still working on it")
    vn.say(a,"Anyway, Installing Scripts is quite  easy")
    vn.say(a,"It's  the same as installing a resourcepack")
    vn.say(a,"No like, literally...")
    vn.show(a,"happy")
    vn.say(a,"Take it away Ars!")
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
    vn.say(a,"There's this thing called 'Trigger Word', so what is it, actually?")
    vn.say(a,"Back to you Ars")
    vn.next("intro_credit")
    vn.finish()

    vn.label("intro_credit")
    vn.show(a,"normal")
    vn.say(a,"And that's everything you need to know about installing this mod")
    vn.say(a,"To recap, all you have to do install the mod like any other, install the script like resource pack, and name a mob with the Trigger Word.")
    vn.show(a,"happy")
    vn.say(a,"Thanks for watching, the next videos  will talk about how to make scripts!")
    vn.say(a,"Looking forward to what you guys can create with this mod!")
    vn.next("sdk_installation")
    vn.finish()
    return vn.dialogueDict
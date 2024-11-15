from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Ars" 
a = Andr

def story():
    
    vn.start()
    vn.label("beginning") 
    vn.show(a,"tired")
    vn.say(a,"Ars... The last take wasn't so bad, was it?")
    vn.say(p,"It still sounds weird...")
    vn.say(a,"This is an entire Visual Novel Engine, Running in Minecraft")
    vn.say(a,"No one has done this in 10 years! Give yourself some credit.")
    vn.say(p,"Yeah, I know, I know... But like...")
    vn.say(a,"You're getting tired Ars... Come on, let's end this...")
    vn.say(p,"No, let's do it, one more time...")    
    vn.say(a,".")
    vn.show(a,"sad")
    vn.say(a,"..")
    vn.say(a,"...")
    vn.show(a,"normal")
    vn.say(a,"Alright then...")
    vn.say(a,"But we'll do it my way")
    vn.say(p,"Huh?")
    vn.say(a,"We'll make this simple... Feature Listing")
    vn.say(p,"What about the linear one take mechanism? Are we really going to just pretend that it doesn't exxist?")
    vn.say(a,"Nope! Feature Listing")
    vn.show(a,"happy")
    vn.say(a,"Let's keep it simple Ars, just like your programming philosophy~")
    vn.say(p,"Alright, let's do it your way...")
    vn.unlock_dialogue("dsl","sdk","lua","grid","anarchy","python","old_mod","toymaker")
    vn.label("feature_listing")
    vn.next("feature_listing")
    vn.show(a,"normal")
    vn.say(a,"Alright then, which one should we show off next??")
    vn.label("page1")
    vn.choice({
        "sprite_system":"Sprite System",
        "compatibility" : "Mod Compatibility",
        "variables":"Variables",
        "page2":"Next One"
    })
    vn.label("page2")
    vn.choice({
        "day_night":"Day Night System",
        "idle_chat_system" : "Idle Chats",
        "background":"Background Change",
        "page3":"Next One"
    })
    vn.label("page3")
    vn.choice({
        "script_import":"Resource Pack System",
        "mob_talker" : "The Mob Talker Item",
        "page1":"Return",
        "end":"That's all"
    })

    vn.label("sprite_system")
    vn.say(a,"Alright, let's show off what we can do with Sprites!")
    vn.show_left(a,"happy")
    vn.say(a,"Here I am!")
    vn.show_right(a,"happy")
    vn.say(a,"Now I'm here")
    vn.say(a,"normal")
    vn.say(a,"Oh, and don't worry, we're not limited to only single character or a script...")
    vn.show_custom(a,"happy",16,9,4,8,2,1)
    vn.show_custom("asset","modrinth",16,9,10,6,6,1)
    vn.say(a,"Tada! It's the Modrinth Page where you can download the mod!")
    vn.show_custom(a,"normal",16,9,4,8,2,1)
    vn.say(a,"This is just an overview, details on how to do script manipulation will explained during later tutorials")
    vn.show(a,"happy")
    vn.say(a,"Back to you Ars!")
    vn.remove("modrinth")
    vn.say(p,"Right, thank you Andr")
    vn.jumpTo("feature_listing")

    vn.label("compatibility")
    vn.show(a,"normal")
    vn.say(a,"Let's talk compatibility")
    vn.say(a,"Good news is, this mod requires no dependency")
    vn.say(a,"The Visual Novel Engine is written in pure java and...")
    vn.say(a,"Ars, do you want to...")
    vn.say(p,"No, I don't want to relive it, just... assume this thing runs on witch craft and it's compatible with anything.")
    vn.say(a,"Right... But yes, you shouldn't have any trouble with adding this mod to any modpack or even using the library into your own mod")
    vn.say(a,"That's how flexible this mod is~")
    vn.jumpTo("feature_listing")

    vn.label("variables")
    vn.say(a,"Hmm... What's a clever way to show off variable system...")
    vn.say(p,"Hmm...")
    vn.say(a,"Oh, I know~")
    vn.next("variable_finish")
    vn.finish()
    
    vn.label("variable_finish")
    vn.show(a,"tired")
    vn.say(a,"Ars... The last take wasn't so bad, was it?")
    vn.say(p,"Wait huh?")
    vn.show(a,"happy")
    vn.say(a,"Just kidding! As you can see, I can remember the last  thing we talked about even after you quit the dialogue screen or even close the game entirely.")
    vn.say(p,"Yeah, that's a clever way of showing it...")
    vn.jumpTo("feature_listing")

    vn.label("day_night")
    vn.say(a,"Hmm... This is straightforward...")
    vn.condNight([
        vn.say(a,"It's night time in game now~",True)
    ])
    vn.condDay([
        vn.say(a,"It's day time in game now~",True)
    ])
    vn.jumpTo("feature_listing")

    vn.label("idle_chat_system")
    vn.show(a,"happy")
    vn.say(a,"Oh I love this one! Thanks for adding this feature Ars!")
    vn.say(p,"Personally, I just hate it when a script is over and you can't do anything anymore")
    vn.say(p,"Feels more fun if script maker can add an infinite amount of random conversation into the script they're making")
    vn.say(a,"Yep! Anyway, let's trigger one~")
    vn.idle_chats()


    vn.next("sdk_installation")
    vn.finish()
    return vn.dialogueDict
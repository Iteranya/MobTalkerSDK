from core.modules import VisualNovelModule
from core.compiler import compile
# -------------------------------------------------------
# This is the Example of a Single File Script
# -------------------------------------------------------

# So like, a standalone script will compile into a single script
# Think of it like a single 100k words word document.
# If that your style, this is how you do it

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
a = Andr
p = "Player" 
storyName = "demo" # This will be the name of the Json File and the Trigger Word

def story():


    # Come on now, it's intuitive enough~
    vn.setVar("background",False)
    vn.start()
    vn.label("start") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(c,"happy")
    vn.say(c,"Oh hey Player! Long time no see! Ahaha~")
    vn.show(c,"normal")
    vn.say(c,"Anyway, it's been a while~")
    vn.say(c,"When was the last version again?")
    vn.say(c,"1.8?? What's the current version?")
    vn.show(c,"scared")
    vn.say(c,"1.21!? I've been dead for  that long!?")
    vn.show(c,"angry")
    vn.say(c,"Can't believe this mod's been abandoned for that long!!!")
    vn.say(c,"I mean how hard can it be to remake this mod???")
    vn.show_right(a,"normal")
    vn.say(a, "It wasn't easy Cupa, recreating this mod requires the use of DSL")
    vn.show_left(c, "scared")
    vn.say(c, "Bloody hell! Andr, where did you come from?")
    vn.show_right(a,"normal")
    vn.say(a, "I was in the Stronghold Perusing the archive for...")
    vn.show_left(c, "angry")
    vn.say(c, "I was being rhetoric... Anyway, why are you here?")
    vn.say(a, "I'm here to explain how this mod work. The fact that they see this means that they downloaded the framework, but not load a single a script.")
    vn.show_left(c,"normal")
    vn.say(c, "Ahh... You go do that then~")
    vn.remove(c)
    vn.show(a,"normal")
    vn.say(a, "Mmm, good to meet you player~")
    vn.say(a, "Let's go somewhere else more comfortable...")
    vn.background("end.png")
    vn.modVar("background",True)
    vn.say(a, "Now what do you wish to know?")
    vn.label("demo_menu") 
    vn.show(a,"normal")
    vn.choice({
        "about_you": "I wanna know about you...",
        "dev_history": "Why so long to recreate?",
        "dev_excuses":"Where's the default scripts?",
        "next":"I like to ask something else"
    })

    vn.label("next")
    vn.choice({
        "mod_feature" : "What does this mod offer?",
        "mod_sdk":"How to make my own custom script?",
        "bugs":"Known bugs? Any problem?",
        "next2":"I like to ask something else",
    })
    vn.label("next2")
    vn.condSame("background",True,[
        vn.choice({
                "mod_compatibility" : "Is this mod compatible with [Insert Mod Here]",
                "community":"Where to find community made scripts?",
                "background": "Why are we in the void?",
                "end": "That's all, thanks!"
            },True)
    ])
    vn.choice({
                "mod_compatibility" : "Is this mod compatible with [Insert Mod Here]",
                "community":"Where to find community made scripts?",
                "void": "Can you send me back to the void?",
                "end": "That's all, thanks!"
            })
    vn.label("void")
    vn.show(a,"happy")
    vn.say(a,"For Sure!")
    vn.background("end.png")
    vn.say(a, "There we go, the void~")
    vn.jumpTo("demo_menu")

    vn.label("background")
    vn.say(a,"Oh, no worries, we're not actually in the void")
    vn.say(a,"Just showing off what the mod can do!")
    vn.clear_background()
    vn.modVar("background",False)
    vn.say(a,"There, all back to normal~")
    vn.jumpTo("demo_menu")

    vn.label("bugs")
    vn.say(a,"Since this is a framework, some bugs can be not from this mod itself...")
    vn.say(a, "Soo, let me list off some known bugs as of right now, ahem...")
    vn.say(a, "1. We don't support multiple character sprite yet")
    vn.say(a, "The dev is working on that currently, most likely this bug is already fixed")
    vn.say(a, "This is the mod's fault, not the SDK's fault, so, report the issue correctly")
    vn.say(a, "2. The images are not displayed correctly")
    vn.say(a, "As of right now, the size of the image are hardcoded to 530 by 900 pixels")
    vn.say(a, "3. There is no way to programatically remove a sprite  that's already appeared, only replace")
    vn.say(a, "All of these sprite and image showing issue is being reworked as of writing this")
    vn.say(a, "The dev is looking to solve problem 1 and 2 at the same time right now")
    vn.show(a,"tired")
    vn.say(a, "See minecraft just updated how they handle Screens and it kinda throw them off...")
    vn.show(a, "normal")
    vn.say(a,"So yeah, send some love his way alright???")
    vn.jumpTo("demo_menu")

    vn.label("about_you")
    vn.show(a,"shy")
    vn.say(a,"About me... Umm...")
    vn.say(a,"I was a character designed by AT2, a digital artist. Inspired by an Enderman...")
    vn.say(a,"I suppose the dev who remade this mod haven't really asked for AT2's permission to use my character sprite")
    vn.show(a,"normal")
    vn.say(a,"If you are seeing this, we apologize for using your artwork")
    vn.say(a,"This is in good faith in the spirit and legacy of the original mod")
    vn.say(a,"Is there anything else you wish to know?")
    vn.jumpTo("demo_menu")

    vn.label("dev_history")
    vn.say(a,"Ah... about that...")
    vn.say(a,"Please don't blame the original developer for 'abandoning' this project")
    vn.say(a,"The Mob Talker Mod is deceptively complicated due to a simple thing...")
    vn.show_left(a, "normal")
    vn.show_custom("asset","old-dsl",16,9,10,6,6,1) # Way simpler, don't you think, seriously
    vn.say(a,"The developer must create a DSL or a Domain Specific Language")
    vn.say(a,"This is what the original Mob Talker Script looks like...")
    vn.say(a,"Think about it, you have to translate this script into something that Minecraft can read")
    vn.say(a,"In essence, you're creating an entire Programming Language and a Game Engine")
    vn.show(a,"tired")
    vn.say(a,"Not to mention you have to make the programming language interop with Java and run the Game Engine inside of Minecraft")
    vn.choice({
        "lua": "Why not use Lua?",
        "cool": "Oh, okay cool, so how did the dev do it?"
    })
    vn.label("lua")
    vn.show(a,"normal")
    vn.say(a,"Good Question")
    vn.say(a,"Lua seems to be an obvious choice. It is lightweight and many mods rely on it.")
    vn.say(a,"Why not write the script in Lua? Define a few methods to control the screen?")
    vn.say(a,"The main problem faced by the dev of *this* mod, is that Lua is an Interpreted Language")
    vn.say(a,"Java on the other hand is compiled language")
    vn.show(a,"tired")
    vn.say(a, "What happens is that Java will try to run the entire script at once...")
    vn.say(a, "Getting Java to interpret lua line by line is extremely hard, you see?")
    vn.say(a,"This is most likely why most people abandoned this project")
    vn.show(a,"normal")
    vn.say(a,"An experienced Java Developer would understand how hard it is to get Lua or any scripting language to Interop with Java")
    vn.say(a, "A non experienced Java developer would just get stuck after realizing they need to make a new programming language for this")
    vn.say(a, "Because, to recreate this mod properly, you HAVE to make something that a community can use")
    vn.say(a, "A way to create a DSL that is human readable and can be read by java.")
    vn.say(a,"And thus, the developer of this mod, created this")

    vn.label("cool")
    vn.remove("asset","old-dsl")
    vn.show_left(a, "normal")
    vn.show_custom("asset","python-dsl",16,9,10,6,6,1)
    vn.say(a, "This is a DSL written in Python.")
    vn.say(a, "Instead of getting Lua to interop with Java, the developer sidestepped this problem entirely")
    vn.say(a, "The developer created a Python SDK Framework that translates python-dsl readable script...")
    vn.say(a, "Into Json FSM (Finite State Machine)")
    vn.say(a, "This Json FSM is very easy to interpret and read in Java")
    vn.say(a, "All the dev has to do is to make a simple class that can read the Json FSM")
    vn.say(a, "Mod creator and players can just put this Json FSM into the mod Config folder.")
    vn.say(a, "And that's a little history of how this mod is created")
    vn.remove("asset","python-dsl")
    vn.show(a,"normal")
    vn.say(a, "Is there anything else you wish to know?")
    vn.jumpTo("demo_menu")

    vn.label("dev_excuses")
    vn.say(a, "I was contractually obligated to inform you that...")
    vn.say(a, "Ahem...")
    vn.say(a, "The developer of this mod, Iteranya, is not responsible with any content written or created in the game")
    vn.say(a, "If there's a person claiming that there's a 'default' or 'official' script for this mod...")
    vn.say(a, "They are lying")
    vn.say(a, "To answer your other question about 'default' script")
    vn.say(a, "The developer is working on it, but they are most likely not going to claim it to be 'official', most likely under pseudonym")
    vn.say(a, "And that's all I can tell you")
    vn.say(a, "Is there anything else?")
    vn.choice({
        "avoid": "Why do you sound so defensive?",
        "demo_menu":"Yeah, that's all, thank you!"
    })
    
    vn.label("avoid")
    vn.show(a,"tired")
    vn.say(a,"To be frank with you, the dev had no intention on making this mod safe for work")
    vn.say(a,"Nor does the dev has any intention on making a PG version script")
    vn.say(a,"In other words, the dev chooses not to make an official script due to legal/ethical/moral issues")
    vn.say(a,"Now, let's talk about something else")
    vn.jumpTo("demo_menu")

    vn.label("mod_feature")
    vn.say(a, "In a sense, this is 'VN Cutscenes Mod', it empowers mod maker to add 'cutscenes' into their game")
    vn.say(a, "By cutscenes, it's things like what you're seeing right now")
    vn.say(a, "Everything in this mod is very barebones, you see? It's made for collaboration")
    vn.say(a, "What you've seen so far is everything it has to offer")
    vn.say(a, "Dialogue, Branching Path, Sprite Showing, Background Swapping, etc")
    vn.say(a, "There's really not much to say, you see?")
    vn.say(a, "Ah, it also supports minecraft slash commmands")
    vn.say(a, "For more technical details, feel free to check the dev's github page.")
    vn.say(a, "It's attached in where you find this mod")

    vn.label("mod_sdk")
    vn.say(a, "Making the script is simple.")
    vn.say(a, "Well you need to use the Mob Talker SDK to create a script")
    vn.say(a, "https://github.com/Iteranya/MobTalkerSDK")
    vn.say(a, "Can you click that link? Probably not...")
    vn.say(a, "But yes, using the SDK, it will turn the human readable script into Json")
    vn.say(a, "More information on how to use the SDK can be found in the github page")
    vn.say(a, "That json will then be sent to the minecraft mod to read. Any question?")
    vn.jumpTo("demo_menu")

    vn.label("mod_compatibility")
    vn.say(a, "This mod is surprisingly compatible and easy to maintain.")
    vn.say(a, "Due to a lack of Java Interop and separation of concerns... The only 'modded' part is the screen/gui")
    vn.say(a, "The Game Engine that reads the Json FSM is written in Pure Java")
    vn.say(a, "You don't even have to worry about cross-version script compatiblity")
    vn.show(a, "happy")
    vn.say(a, "Personally I love this approach, the Mob Talker Mod might become timeless again!")
    vn.say(a, "The CMM team is still active with making cute mob models too!")
    vn.say(a, "Imagine this possibilities~")
    vn.show(a, "normal")
    vn.say(a, "But yes, mod creator still have to work on adding script if they wish to use this framework")
    vn.say(a, "Do you have anymore questions?")
    vn.jumpTo("demo_menu")

    vn.label("community")
    vn.say(a,"There should be a Discord Link in this Mod's download page")
    vn.show(a,"happy")
    vn.say(a,"Feel free to make your own script! Make your own character, the Overworld and beyond is your oyster~")
    vn.say(a,"The dev's desire is just to recreate, revive, and immortalize this mod! Adding the beauty of 2D CG Graphics in Minecraft")
    vn.show(a,"shy")
    vn.say(a,"The other desire is to date me and Cupa...")
    vn.show(a,"normal")
    vn.say(a,"But really, at the end of the day, the dev only provide the tools")
    vn.say(a,"So please don't go reporting for bug about the lack of interaction... okay?")
    vn.say(a, "Something else you want to ask?")
    vn.jumpTo("demo_menu")

    vn.label("end")
    vn.show(a,"happy")
    vn.say(a,"Happy to Help, see you later Player!")
    vn.finish()


    return vn.dialogueDict


def main():compile(storyname=storyName,script=story()) # Yeah, just run this file :v

if __name__ == "__main__":
    main() 

from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Ars # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Player" 
a = Ars

def story():
    
    vn.start()
    vn.label("sdk_installation") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(a,"normal") # show function will automatically create a path. "normal" is the sprite name, normal.png
    vn.say(a,"Alright, are you ready for talking about SDK Installation?")
    vn.show(a,"happy")
    vn.say(a,"Because I'm not!!!")
    vn.show(a,"tired")
    vn.say(a,"Haaa... Alright now...")
    vn.say(a,"Let's start from the very beginning...")
    vn.background(a,"sdk_page")
    vn.remove(a)
    vn.say(a,"Let's focus on the technicalities for now, ahem...")
    vn.say(a,"This is the mod's SDK github page, SDK stands for Script Development Kit, not Standard Development Kit.")
    vn.say(a,"Just... a little trivia there...")
    vn.say(a,"Anyway, if you look at the readme file, you get a 3 step instruction on how to install the mod.")
    vn.clear_background()
    vn.show_custom("asset","installation_flow",16,9,14,6,2,1)
    vn.say(a,"Behold! A Three Step Installation Procedure")
    vn.say(a,"First, just make a new folder")
    vn.say(a,"Second, just go and git clone it")
    vn.say(a,"Third... Have I... told you to download Python???")
    vn.say(a,"A-anyway... You can... Uhhh...")
    vn.say(a,"Download Python First and then follow these steps...")
    vn.say(a,"And I guess you need VS Code...")
    vn.say(a,"I haven't... really thought about the image assets required for this script.")
    vn.say(a,"So... apologies in advance, future me...")
    vn.background("python_download")
    vn.say(a,"Download python, install it, the basic")
    vn.clear_background()
    vn.background("vscode_download")
    vn.say("I recommend VS Code, but yeah, download it")
    vn.say("Next up is... you open the stuff you cloned into VS-Code")
    vn.clear_background()
    vn.background("vscode_workshop")
    vn.say(a,"You should have this next...")
    vn.say(a,"In this screen, there are quite a few folders.")
    vn.say(a,"All you need to focus on is the 'Workshop Folder'")
    vn.say(a,"There's the MultiFileDemo and SingleFileDemo")
    vn.say(a,"For now, open the single file demo.")
    vn.say(a,"This is an example of a demo script.")
    vn.say(a,"We'll talk about basic scripting after this video, but for now, try to run the script.")
    vn.say(a,"Just... click the  run button at the top right of the screen.")
    vn.say(a,"You should find a new file titled 'demo.json'")
    vn.say(a,"What can you do  with  this file?")
    vn.say(a,"You can fire up your minecraft instance or  you can run it here in terminal Visual Novel")
    vn.say(a,"Or... you can insert this single  json file into your 'config/mobtalkerredux/' folder and run it in Minecraft")
    vn.next("finish_sdk_installation")
    vn.finish()

    vn.label("finish_sdk_installation")
    vn.show(a,"normal")
    vn.say(a,"If you've come to the point of running the slash command...")
    vn.say(a,"That means installation is successful")
    vn.say(a,"Running SingleFileDemo and MultiFileDemo always yields one script")
    vn.say(a,"Basically, whether you organize your project with multiple files or a single monolothic file, the end result is the same, a single Json File")
    vn.say(a,"Anyway, that's the end of it, have fun then!")
    vn.next("basic_usage")
    return vn.dialogueDict
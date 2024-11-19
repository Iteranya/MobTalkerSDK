from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
a = Andr
p = "Ars" 

def story():

    vn.start()
    vn.label("start") # This is a 'Label', it will be used by the jump and choice to know where to go
    vn.show(a,"normal")
    vn.say(a,"Can we do this once? Single take, no redo","a-01")
    vn.say(p,"Well yeah, YOUR part, but...","p-01")
    vn.say(p,"I'm ESL as heck, people can understand us because of this fancy dialogue box. Take it  away and NO ONE will understand what we're trying to say.","p-02")
    vn.say(a,"Ah... It's that kind of challenge huh... Can't you use AI to enhance your voice?","a-02")
    vn.say(p,"I already did... This is AI enhanced...","p-04")
    vn.say(a,"How about this... We'll combine both approach. We can start with me explaining clearly the steps. Then you will show it how it's done in classic VS Code video tutorial setting, then we'll go back here and I'll explain the next step and you'll go back and show how it's done in VS Code.","a-03")
    vn.say(p,"Ooooh! That's perfect!!! Okay~ Let's try it!","p-06")
    vn.show(a,"happy")
    vn.say(a,"Great! Let's start then, ahem...","a-04")
    vn.next("tutorial")
    
    vn.label("tutorial")
    vn.show(a,"normal")
    vn.say(a,"What's next?","a-05")
    vn.label("page_1")
    vn.choice({
        "install":"SDK Installation",
        "workspace_setup":"Workspace Setup",
        "script_writing":"Script Writing",
        "page_2": "Next"
    })
    vn.label("page_2")
    vn.choice({
        "assets":"Asset Files",
        "exporting":"Exporting",
        "page_1":"Go Back",
        "end":"Finished! Wooooo!!!"
    })

    vn.label("install")
    vn.show(a,"happy")
    vn.say(a,"Installing the SDK! Don't worry, this is very easy!","a-06")
    vn.show(a,"normal")
    vn.say(a,"Ars have done extra length to make SDK installation as easy as possible. He does wish this tool to be able to be used by  non-developer. This project requires no external dependency, build files, or whatever fancy frameworks usually needs. Everything is written in pure python.","a-07")
    vn.say(a,"Even then, it's still a bit tricky if you've never wrote a single line of code your entire life.","a-08")
    vn.say(a,"So please bear with us...","a-09")

    vn.show_custom("asset","python_download",16,9,16,9,1,1)
    vn.say(a,"First thing you want to do is install Python. You can install it like any other program. The SDK requires a version of python above 3.7","a-10")

    vn.show_custom("asset","vs_code_download",16,9,16,9,1,1)
    vn.say(a,"Next is downloading your IDE, for this example, we use VS Code","a-11")
    vn.say(p,"Yeah, VS Code, NOT Visual Studio")
    vn.show(a,"tired")
    vn.say(a,"Yes... it's very easy for beginners to download Visual Studio instead of VS Code. This is what the download page for VS Code looks like.","a-12")
    vn.show(a,"normal")
    vn.say(a,"Again, it's VS Code, not Visual Studio.","a-13")
    vn.say(p,"[REDACTED] Bloatware...")
    vn.say(a,"Language Ars, language... Anyway, after you download and install that...","a-14")

    vn.show_custom("asset","sdk_download",16,9,16,9,1,1)
    vn.say(a,"The next thing you want to do is head over to SDK page. In this page, you want to click the green code button and download zip","a-15")
    vn.say(a,"Alternatively, you can clone it, but for this tutorial, we'll go with the most familiar method for non-programmer, that is... Downloading a Zip","a-16")
    vn.say(p,"Oh actually, can you also Star it? It'll look good in my resume! Help land a good job yeah?")
    vn.show(a,"tired")
    vn.say(a,"...")
    vn.say(p,"Sorry, continue...")
    vn.show(a,"normal")

    vn.show_custom("asset","sdk_folder",16,9,16,9,1,1)
    vn.say(a,"Put your zip into any folder of your liking, extract the content, and from here you have a few options","a-17")
    vn.show(a,"normal")
    vn.say(a,"First thing you can do is opening VS Code. Choose the folder where you extract your script and open it in VS Code.","a-18")
    vn.say(a,"Another way to do it is through terminal. Just type 'cmd' at the bar of windows explorer and type code .","a-19")

    vn.show_custom("asset","default_ide",16,9,16,9,1,1)
    vn.say(a,"Regardless of the method, you want to have this windows open. Alright Ars, your turn, show  them how  it's done! Video style~","a-20")
    vn.say(p,"Oh boy, here goes something... Apologies in advance for the ESL...")
    vn.say(p,"You will have a sudden appreciation for dialogue box after this.")
    vn.finish()

    vn.label("workspace_setup")
    vn.say(a,"Once you have everything installed and setup, let's have a little tour around the workspace","a-21")
    vn.say(a,"There are 2 folders... Mediafile and Workshop","a-22")
    vn.show_custom("asset","default_ide",16,9,16,9,1,1)
    vn.show_custom("asset","project_tree_default",16,9,4,8,7,1)
    vn.say(a,"The workshop folder is where you will do your script writing. Inside it, you will see multiFileDemo, singleFileDemo, characters, and sound","a-23")
    vn.say(a,"Everything related to script making will be done inside the workshop folder, go ahead and open that. There should be 2 folders in there, core and script","a-24")
    vn.say(a,"Core contains the 'under the hood' part of the SDK. You don't have to worry about it. If an error show up, it's probably in your script, not in 'Core'. You only need to mess with Core if you're a Mod Developer or you wish to add new feature.","a-25")
    vn.say(a,"Script folder contains the 'scripts' used by multiFileDemo, you can use that folder to manage your work into different scripts. Under the hood they will be compiled into a single json script. It's really only there to help you organize your project.","a-26")
    vn.say(p,"Delete it")
    vn.say(a,"Eh?","a-27")
    vn.say(p,"Out of scope, this tutorial will focus on singleFile, you can safely delete the script folder and the multifiledemo file.")
    vn.say(a,"Ah... alright, so now it should look like this...","a-28")
    vn.show_custom("asset","project_tree_workshop",16,9,4,8,7,1)
    vn.say(a,"The 'singleFileDemo.py is an example of what a single 'script' looks like. You can either rename and modify it directly or copy it into another file and work with that.","a-29")
    vn.say(a,"Alright then Ars, show them how to setup the workspace","a-30")
    vn.finish()

    vn.label("script_writing")
    vn.show(a,"happy")
    vn.say(a,"Oh, it's the fun part!","a-31")
    vn.show(a,"normal")
    vn.say(a,"Before you make your script, you want to first define your characters. Head on over to characters.py","a-32")
    vn.show_custom("asset","characters_py",16,9,16,9,1,1)
    vn.say(a,"There should be me and Cupa there. Go ahead and make a new character~","a-33")
    vn.say(a,"After that, well, it's your turn Ars!","a-34")
    vn.say(p,"The dreaded part... Gods how do I make this concise?")
    vn.say(a,"Just make a simple show case script. What about for Iron Golem?","a-35")
    vn.say(p,"Huh... Alright then, let me try... Perfect chance to show off how versatile this mod is too~")
    vn.say(p,"Let me make an iron golem real quick, then the game.")
    vn.say(p,"It's... not going to attack you... right?")
    vn.show(a,"tired")
    vn.say(a,"Ah... I... Maybe fence it, just in case...","a-36")
    vn.finish()

    vn.label("assets")
    vn.say(a,"A visual novel isn't complete without, well, the visuals... So here's how you can add the images~","a-37")
    vn.show_custom("asset","project_tree_mediafile",16,9,4,8,7,1)
    vn.say(a,"Pay attention to the mediafile at the very top. There are two type of images, 'asset' and 'characters'","a-38")
    vn.say(a,"Asset contains every image that *isn't* a character sprite while sprite contains only character sprite","a-39")
    vn.say(a,"You should have mine and Cupa's character sprite built in, you can check how we structured it.","a-40")
    vn.say(a,"Your turn Ars, show them how you can add the Iron Golem's character sprite in there.","a-41")
    vn.say(p,"It's... Safe For Work, right?")
    vn.say(a,"Eh? Umm... Maybe??? It's clearly 'mannequin-like' so I suppose it is...","a-42")
    vn.finish()

    vn.label("exporting")
    vn.say(a,"Once you've compiled the script and put all your assets in the correct place, you can start exporting your project.","a-43")
    vn.show_custom("asset","export_py",16,9,16,9,1,1)
    vn.say(a,"If you did everything correctly, you can simply open 'export.py' and change the details. It really don't matter what you put in description or even trigger word. But you want to make everything descriptive enough.","a-44")
    vn.say(a,"Also *just in case*, don't use 'space' when naming your project. Minecraft might throw a fuss...","a-45")
    vn.say(a,"Once everything's setup, go ahead and press play at the top right corner. A zip file will appear in the project's main directory.","a-46")
    vn.show(a,"happy")
    vn.say(a,"Your turn Ars! Show them how easy it is!","a-47")
    vn.finish()

    vn.label("end")
    vn.show(a,"happy")
    vn.say(a,"Yay~","a-48")
    vn.show(a,"tired")
    vn.say(a,"Please don't do a retake, it's good enough","a-49")
    vn.say(p,"Oh that's up to me in the future, will they be able to pull off that smooth transition into VS Code with zero editing???")
    vn.say(a,"Ahh... That's fair...","a-50")
    vn.show(a,"normal")
    vn.say(a,"Well then, thanks for watching everyone!","a-51")
    vn.say(a,"Take care then~","a-52")
    vn.say(p,"See ya!")
    vn.say(p,"Join discord for technical queries! Share the video so more people know this exists and more scripts get made!")
    vn.finish()

    return vn.dialogueDict
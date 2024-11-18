from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Ars" 
a = Andr

def story():
    
    vn.label("sdk")
    vn.say(a,"Let's talk about the SDK","a-70")
    vn.say(p,"The Script Development Kit? I guess it's an essential tool to create a script.","p-40")
    vn.say(a,"It only contains 3 files right?","a-71")
    vn.say(p,"Technically, yeah, there's only 3 'core' files... Like, yeah, those are everything","p-41")
    vn.say(a,"And it doesn't have any build files or any dependency?","a-72")
    vn.say(p,"Nope, it's just an ordinary workspace to create script, that's it!","p-42")
    vn.show(a,"tired")
    vn.say(a,"If only you show  this level of pragmatism in your videos...","a-73")
    vn.say(p,"It's really hard to be simple and pragmatic in something so subjective Andr...","p-43")
    vn.show(a,"normal")
    vn.say(a,"Well, since it's very subjective, that just means the standard is up to you, no?","a-74")
    vn.say(p,"Well... Yeah... I guess...","p-44")
    vn.finish()

    vn.label("dsl")
    vn.say(a,"How hard was it to recreate this mod anyway?","a-75")
    vn.say(p,"I want to scream","p-45")
    vn.show(a,"tired")
    vn.say(a,"That hard huh???","a-76")
    vn.show(a,"normal")
    vn.say(p,"Well, for one, I have to create a 'Scripting Language' no? I need a way to let Script Maker to... well, make scripts and like...","p-46")
    vn.say(p,"And oh boy... lemme tell you, it was Computer Science level shit... It was miracle, just sheer dumb luck and miracle, I figured it out.","p-47")
    vn.say(p,"Basically, instead of getting a programming language to interop with Java, which was [REDACTED] impossible and how the Mob Talker 2 did it, I decided to use Json FSM","p-48")
    vn.say(a,"Mm, you told me this, the 'secret sauce' behind this mod's success","a-77")
    vn.say(p,"Yeah, I have to  literally abstract this mod into nothing but raw data!","p-49")
    vn.say(p,"By the way, viewers, pro tip, try abstracting problem down into pure data or information before you go looking for the proper method. It will help you in the long run, I promise","p-50")
    vn.say(a,"That's right, once reduced to data, you can focus on how to acquire or create your very own method to tackle that specific information.","a-78")
    vn.say(p,"Still... If I never discovered FSM method... This mod will never be revived...","p-51")
    vn.finish()
    
    vn.label("lua")
    vn.say(a,"You tried Lua integration didn't you?","a-79")
    vn.say(p,"I am going to scream...","p-52")
    vn.say(a,"Owww... Sorry for making you relive that","a-80")
    vn.say(p,"You ever seen a stack overflow error? In Java????","p-53")
    vn.show(a,"tired")
    vn.say(a,"No...","a-81")
    vn.say(p,"Exactly, that's how bad it was... Holy shit...","p-54")
    vn.say(p,"Who knew... Who Knew! Running an Interpreted Language in a Compiled Language environment was a terrible idea!?","p-55")
    vn.say(p,"No wonder Mob Talker 2 was discontinued, Geez... Must've been a NIGHTMARE to code...","p-56")
    vn.show(a,"normal")
    vn.say(a,"Hey, have some respect, you might not be here without them...","a-82")
    vn.say(p,"Fair enough... Yeah, thanks a lot Mob Talker 2 team, hope this mod is up to your standard!","p-57")
    vn.finish()

    vn.label("grid")
    vn.say(a,"Hmm, you made your own Custom UI System, right?","a-83")
    vn.say(p,"Oh yeah, the grid system! I love it! Like, that's my favorite part!","p-58")
    vn.say(a,"Me too! I love how you really look for a method that's so easy to use, given the limitation","a-84")
    vn.say(p,"Yeah, well, I do need to find an easy way for Script Maker to position and resize their images however they like. I figured  that most would be artists and like... Grids, yknow?","p-59")
    vn.say(a,"Yeah, you can just create layout in graph paper and code it in with minimal issue without having to worry about pixels. Just work with Image Ratio and that's it~","a-85")
    vn.say(p,"Welp, it still doesn't support animation though, so... Yeah...","p-60")
    vn.say(a,"Chin up! You'll figure it out~","a-86")
    vn.finish()

    vn.label("anarchy")
    vn.say(a,"Anarchy Driven Development","a-87")
    vn.say(p,"Honestly surprised how well it worked","p-61")
    vn.say(a,"I thought you were being ironic. How does it work, even?","a-88")
    vn.say(p,"By raising a Middle Finger to all the proper frameworks and best practice?","p-62")
    vn.say(a,"I think your code is clean enough, what do you mean not following proper practice?","a-89")
    vn.say(p,"No, it's not about code quality, it's about how  you solve problem. Like, step away from the  'Obvious' solution and ask yourself. Do you REALLY need to do that to solve your problem???","p-63")
    vn.say(p,"You'd be surprised by how many times the answer can be 'no' and you figured out a more elegant solution to a problem","p-64")
    vn.say(p,"Like, for example, do I REALLY need to create a custom mob??? Nope, just Name Tag's enough and wouldn't you know it? This mod's compatible with like... thousands of Mob mods out there.","p-65")
    vn.say(a,"Ahhh.... I get it. So it's about avoiding the 'obvious' solution whenever possible?","a-90")
    vn.say(p,"Yep, this mod is born out of avoiding 'obvious' solutions.","p-66")
    vn.say(p,"I... I shouldn't be too proud of that...","p-67")
    vn.show(a,"happy")
    vn.say(a,"I think it's okay to be proud of it!","a-91")
    vn.finish()

    vn.label("old_mod")
    vn.say(a,"So... How's this mod compared to the old mod?","a-92")
    vn.say(p,"Well, in a sense, this mod has all the feature of the old and more, except...","p-68")
    vn.say(p,"Ugh... The AI System... Like, how did they do that?","p-69")
    vn.say(a,"AI?","a-93")
    vn.say(p,"Yeah, the old mod actually hijacked the mob's AI. You can make mob follow you and such through the script... Which is... wow, just,  how the hell???","p-70")
    vn.say(a,"That's actually impressive! Any plans to implement it?","a-94")
    vn.say(p,"Hell no, may as well kiss any sort of Mod Compatibility good bye! Not to mention updating Minecraft Version gonna be a total nightmare...","p-71")
    vn.show(a,"happy")
    vn.say(a,"Well, there's always a trade off!","a-95")
    vn.finish()
    return vn.dialogueDict
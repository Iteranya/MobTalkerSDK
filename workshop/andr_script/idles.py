from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
p = "Ars" 
a = Andr

def story():
    
    vn.label("sdk")
    vn.say(a,"Let's talk about the SDK")
    vn.say(p,"The Script Development Kit? I guess it's an essential tool to create a script.")
    vn.say(a,"It only contains 3 files right?")
    vn.say(p,"Technically, yeah, there's only 3 'core' files... Like, yeah, those are everything")
    vn.say(a,"And it doesn't have any build files or any dependency?")
    vn.say(p,"Nope, it's just an ordinary workspace to create script, that's it!")
    vn.show(a,"tired")
    vn.say(a,"If only you show  this level of pragmatism in your videos...")
    vn.say(p,"It's really hard to be simple and pragmatic in something so subjective Andr...")
    vn.show(a,"normal")
    vn.say(a,"Well, since it's very subjective, that just means the standard is up to you, no?")
    vn.say(p,"Well... Yeah... I guess...")
    vn.finish()

    vn.label("dsl")
    vn.say(a,"How hard was it to recreate this mod anyway?")
    vn.say(p,"I want to scream")
    vn.show(a,"happy")
    vn.say(a,"That hard huh???")
    vn.show(a,"normal")
    vn.say(p,"Well, for one, I have to create a 'Scripting Language' no? I need a way to let Script Maker to... well, make scripts and like...")
    vn.say(p,"And oh boy... lemme tell you, it was Computer Science level shit... It was miracle, just sheer dumb luck and miracle, I figured it out.")
    vn.say(p,"Basically, instead of getting a programming language to interop with Java, which was how the Mob Talker 2 did it, I decided to use Json FSM")
    vn.say(a,"Mm, you told me this, the 'secret sauce' behind this mod's success")
    vn.say(p,"Yeah, I have to  literally abstract this mod into nothing but raw data!")
    vn.say(p,"By the way, viewers, pro tip, try abstracting problem down into pure data or information before you go looking for the proper method. It will help you in the long run, I promise")
    vn.say(a,"That's right, once reduced to data, you can focus on how to acquire or create your very own method to tackle that specific information.")
    vn.say(p,"Still... If I never discovered FSM method... This mod will never be revived...")
    vn.finish()
    
    vn.label("lua")
    vn.say(a,"You tried Lua integration didn't you?")
    vn.say(p,"I'm gonna scream...")
    vn.say(a,"Owww... Sorry for making you relive that")
    vn.say(p,"You ever seen a stack overflow error? In Java????")
    vn.show(a,"tired")
    vn.say(a,"No...")
    vn.say(p,"Exactly, that's how bad it was... Holy shit...")
    vn.say(p,"Who knew... Who Knew! Running an Interpreted Language in a Compiled Language environment was a terrible idea!?")
    vn.say(p,"No wonder Mob Talker 2 was discontinued, Geez... Must've been a NIGHTMARE to code...")
    vn.show(a,"normal")
    vn.say(a,"Hey, have some respect, you might not be here without them...")
    vn.say(p,"Fair enough... Yeah, thanks a lot Mob Talker 2 team, hope this mod is up to your standard!")
    vn.finish()

    vn.label("grid")
    vn.say(a,"Hmm, you made your own Custom UI System, right?")
    vn.say(p,"Oh yeah, the grid system!")
    vn.say(p,"I love it")
    vn.say(a,"Me too! It's actually quite ingenious, turning complex blit and system pixels and such, into a simple Intuitive Grid System")
    vn.say(p,"Yeah, well, I do need to find an easy way for Script Maker to position and resize their images however they like. I figured  that most would be artists and like... Grids, yknow?")
    vn.say(a,"Yeah, and  not  only that, they can create layout in graph paper and code it in with minimal issue without having to worry about pixels. Just work with Image Dimension and that's it~")
    vn.say(p,"Welp, it still doesn't support animation though, so... Yeah...")
    vn.finish()

    vn.label("anarchy")
    vn.say(a,"Anarchy Driven Development")
    vn.say(p,"Honestly surprised how well it worked")
    vn.say(a,"How does it work, even?")
    vn.say(p,"By raising a Middle Finger to all the proper frameworks and best practice?")
    vn.say(a,"I think your code is clean enough, what do you mean not following proper practice?")
    vn.say(p,"No, it's not about code quality, it's about how  you solve problem. Like, step away from the  'Obvious' solution and ask yourself. Do you REALLY need to do that to solve your problem???")
    vn.say(p,"You'd be surprised by how many times the answer can be 'no' and you figured out a more elegant solution to a problem")
    vn.say(p,"Like, for example, do I REALLY need to create a custom mob??? Nope, just Name Tag's enough and wouldn't you know it? This mod's compatible with like... thousands of Mob mods out there.")
    vn.say(a,"Ahhh.... I get it. So it's about avoiding the 'obvious' solution whenever it's working?")
    vn.say(p,"Yep, this mod is born out of avoiding 'obvious' solutions.")
    vn.say(p,"I... I shouldn't be too proud of that...")
    vn.show(a,"happy")
    vn.say(a,"I think it's okay to be proud of it!")
    vn.finish()

    vn.label("old_mod")
    vn.say(a,"So... How's this mod compared to the old mod?")
    vn.say(p,"Well, in a sense, this mod has all the feature of the old and more, except...")
    vn.say(p,"Ugh... The AI System... Like, how did they do that?")
    vn.say(a,"AI?")
    vn.say(p,"Yeah, the old mod actually hijacked the mob's AI. You can make mob follow you and such through the script... Which is... wow, just,  how the hell???")
    vn.say(a,"That's actually impressive! Any plans to implement it?")
    vn.say(p,"Hell no, may as well kiss any sort of Mod Compatibility good bye!")
    vn.show(a,"happy")
    vn.say(a,"Well, there's always a trade off!")
    vn.finish()
    return vn.dialogueDict
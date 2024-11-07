from core.modules import VisualNovelModule
# This is the Example Script, obviously~

from characters import Cupa,Andr # Import characters you've defined in characters.py
vn = VisualNovelModule()
c = Cupa 
a = Andr
p = "Player" 

def story():
    
    vn.label("idle_chat")
    vn.idle_chats()

    vn.label("pick_up")
    vn.show(c,"angry")
    vn.say(c,"But for real, you have to work on your pick up lines, yknow?")
    vn.jumpTo("andrFourthWallBreak")

    vn.label("cupa_want_to_say")
    vn.show(c,"normal")
    vn.say(c,"Hmmm... So Player...")
    vn.show(c,"shy")
    vn.say(c,"I just want to say...")
    vn.jumpTo("andrFourthWallBreak")

    vn.label("andrFourthWallBreak")
    vn.show(a,"normal")
    vn.say(a,"Excuse Me")
    vn.show_left(c,"scared")
    vn.say(c,"What the fuck, Andr? What are you doing here?!")
    vn.say(a,"Sorry for the 4th wall break. This is a 'random conversation' that triggers when the 'current day' conversation has been exhausted. I'm here to bring some informations.")
    vn.show_left(c,"angry")
    vn.say(c,"Look, just keep it quick...")
    vn.say(a,"Mm, So here's the thing... Due to 'technical', limitation, the Developer Ars Iteranya have decided not to add a 'real' time or day mechanic. Instead, they cheated, well, not cheated, but rather mark it as a feature.")
    vn.say(a,"The point of day feature is to stop people from speedrunning through the game, yes? That and points of immersion. Iteranya saw this and they decided to just... Skip the entire minecraft handling part of things.")
    vn.say(a, "So, let me explain how... This works, ahem...")
    vn.say(a, "In a nutshell, time progression can only happen at night when you go to sleep.")
    vn.show(a,"shy")
    vn.say(a, "And... well... in a sense... A script maker has to write a 'good night' scene between the mob and player. Since this can only be triggered at night, they have to wait until nighttime.")
    vn.show_left(c,"tired")
    vn.say(c, "Wouldn't the player just speedrun through the night?")
    vn.show(a,"tired")
    vn.say(a,"Good point, Cupa, yes, the player can just speedrun through the night")
    vn.say(a,"To combat this, script maker can create 'morning' scene that can only be accessed during daytime. Again, this does not prevent players from speedrunning, but it does it well.")
    vn.show_left(c,"angry")
    vn.say(a,"Another more 'forceful' solution is to have time passes as if character goes to sleep using direct slash command injection. So talking to mob girl during nighttime is another way to pass time.")
    vn.show(a,"normal")
    vn.say(a,"That's not all, sorry, let's talk about 'idle chat'.")
    vn.say(a,"There are 2 functions in the SDK, 'unlock_events' and 'idle_chat'. The command 'idle_chat' will play a random event from the 'unlock_events'")
    vn.say(a,"...")
    vn.show_left(c,"tired")
    vn.say(c,"You're done?")
    vn.say(a,"Do you have any more ques-")
    vn.say(c,"You're DONE!")
    vn.show(c,"angry")
    vn.say(c,"Thanks for the information, I was in the middle of some heart to heart with Player here")
    vn.say(a,"Mm, apologies for that. I will go now")
    vn.remove(a)
    vn.say(c,"Ugh... The nerve of that girl...")
    vn.show(c,"tired")
    vn.say(c,"...")
    vn.show(c,"normal")
    vn.say(c,"shy")
    vn.say(c,"Soo... Yeah... thanks... Looking forward to see this mod to its completion.")
    vn.say(c, "Ah, right, just skip to nighttime to see the 'day' management in action.")
    vn.finish()


    
    return vn.dialogueDict
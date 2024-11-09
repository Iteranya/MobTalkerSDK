# This is the Module
# Basically,  if you're looking to expand the SDK's current functionality...
# Just add new method here
# Adding new class unfortunately still doesn't work, (Yet), I'm working on it
# Feel free to customize it to your system~
from core.model import Character

class VisualNovelModule(): # Module Class, just add more function as you like
    def __init__(self):
        self.dialogueDict = []

    def initialize(self,scriptName):
        self.dialogueDict.append({
            "type":"meta",
            "action":"initialize",
            "scriptName": scriptName
        })
    
    def start(self):
        result = {
            "type":"meta",
            "action":"start"
        }
        self.dialogueDict.append(result)
        return result

    def say(self,character,content,transition = False):
        name = ""
        if isinstance(character, Character):
            name = character.name
        elif(character  == None):
            name = ""
        else:
            name = character
        print("Compiling: "+content)
        result = {
            "type":"dialogue",
            "action":"say",
            "label":name,
            "content":content
        }
        if(transition==False):
            self.dialogueDict.append(result)
        return result
    
    def background(self,background):
        result = {
            "type":"modify_background",
            "background":"asset/"+background
        }
        self.dialogueDict.append(result)
        return result
    
    def clear_background(self):
        result = {
            "type":"clear_background"
        }
        self.dialogueDict.append(result)
        return result

    def show(self,character,sprite,transition=False):
        if isinstance(character, Character): 
            location = "characters/"+character.id+"/"+character.outfit+"/"+sprite+".png"
            print("Compiling: "+sprite)
            result = {
                "type":"show_sprite",
                "action":"show",
                "sprite":character.id,
                "location":location,
                "position":"CENTER",
                "wRatio": 16,
                "hRatio": 9,
                "wFrameRatio":4,
                "hFrameRatio":8,
                "column":7,
                "row":1
            }
            if(transition==False):
                self.dialogueDict.append(result)
            return result
        else:
            pass

    def show_custom(self,character,sprite,wRatio,hRatio,wFrameRatio,hFrameRatio,colPos,rowPos,nested=False):
        if isinstance(character, Character): 
            location = "characters/"+character.id+"/"+character.outfit+"/"+sprite+".png"
            print("Compiling: "+sprite)
            result = {
                "type":"show_sprite",
                "action":"show",
                "sprite":character.id,
                "location":location,
                "position":"CUSTOM",
                "wRatio": wRatio,
                "hRatio": hRatio,
                "wFrameRatio":wFrameRatio,
                "hFrameRatio":hFrameRatio,
                "column":colPos,
                "row":rowPos
            }
            if(nested==False):
                self.dialogueDict.append(result)
            return result
        elif isinstance(character,str):
            location = character+"/"+sprite+".png"
            print("Compiling: "+sprite)
            result = {
                "type":"show_sprite",
                "action":"show",
                "sprite":sprite,
                "location":location,
                "position":"CUSTOM",
                "wRatio": wRatio,
                "hRatio": hRatio,
                "wFrameRatio":wFrameRatio,
                "hFrameRatio":hFrameRatio,
                "column":colPos,
                "row":rowPos
            }
            if(nested==False):
                self.dialogueDict.append(result)
            return result
        else:
            pass

    def show_left(self,character,sprite,transition=False):
        if isinstance(character, Character): 
            location = "characters/"+character.id+"/"+character.outfit+"/"+sprite+".png"
            print("Compiling: "+sprite)
            result = {
                "type":"show_sprite",
                "action":"show",
                "sprite":character.id,
                "location":location,
                "position":"LEFT",
                "wRatio": 16,
                "hRatio": 9,
                "wFrameRatio":4,
                "hFrameRatio":8,
                "column":3,
                "row":1
            }
            if(transition==False):
                self.dialogueDict.append(result)
            return result
        else:
            pass

    def show_right(self,character,sprite,transition=False):
        if isinstance(character, Character): 
            location = "characters/"+character.id+"/"+character.outfit+"/"+sprite+".png"
            print("Compiling: "+sprite)
            result = {
                "type":"show_sprite",
                "action":"show",
                "sprite":character.id,
                "location":location,
                "position":"LEFT",
                "wRatio": 16,
                "hRatio": 9,
                "wFrameRatio":4,
                "hFrameRatio":8,
                "column":10,
                "row":1
            }
            if(transition==False):
                self.dialogueDict.append(result)
            return result
        else:
            pass
    
    def remove(self,character,sprite="",transition=False):
        if isinstance(character, Character): 
            print("Compiling: "+sprite)
            result = {
                "type":"remove_sprite",
                "action":"remove_character",
                "sprite":character.id
            }
            if(transition==False):
                self.dialogueDict.append(result)
            return result
        elif isinstance(character,str):
            print("Compiling: "+sprite)
            result = {
                "type":"remove_sprite",
                "action":"remove",
                "sprite":sprite,
            }
            if(transition==False):
                self.dialogueDict.append(result)
            return result
        else:
            pass
        
        
    def choice(self,choice: dict,nested=False):
        print(choice)
        result = {
            "type":"choice",
            "action":"choice",
            "choice":[{"label": key, "display": value} for key, value in choice.items()]
        }
        if(nested==False):
            self.dialogueDict.append(result)
        return result
        

    def label(self,labelName:str):
        print("Compiling: "+labelName)
        result = {
            "type":"label",
            "action" : "label",
            "label":labelName
        }
        self.dialogueDict.append(result)
        return result

    def jumpTo(self,labelName:str,transition=False):
        print("Compiling:" + labelName)
        result = {
            "type":"transition",
            "action":"jump",
            "label": labelName
        }
        if(transition==False):
            self.dialogueDict.append(result)
        return result

    def finish(self):
        print("Compiling A Finish Line")
        result = {
            "type":"finish_dialogue",
            "action": "finish_dialogue"
        }
        self.dialogueDict.append(result)
        return result
        

    def setVar(self,varName:str,init:any):
        print("Compiling: "+varName)
        result = {
            "type":"meta",
            "action": "create_var", 
            "var": varName,
            "init":init
        }
        self.dialogueDict.append(result)
        return result

    # You can use (-) instead of subVar
    def addVar(self,varName:str, addAmount:int):
        print("Compiling: "+varName)
        result = {
            "type":"modify_variable",
            "action": "increment_var", 
            "var": varName, 
            "value": addAmount
            }
        self.dialogueDict.append (result)
        return result

    def subVar(self,varName:str, subAmount:int):
        print("Compiling: "+varName)
        result = {
            "type":"modify_variable",
            "action": "subtract_var", 
            "var": varName, 
            "value": subAmount
        }
        self.dialogueDict.append(result)
        return result

    def modVar(self,varName:str, value:any):
        print("Compiling: "+varName)
        result = {
            "type":"modify_variable",
            "action": "modify_var", 
            "var": varName, 
            "value": value
        }
        self.dialogueDict.append(result)
        return result
    
    def next(self,label):
        result = {
            "type":"next",
            "action":"next",
            "label":label
        }
        self.dialogueDict.append(result)
        return result
    
    def night_choice(self,choice: dict,nested=False):
        print(choice)
        result = {
            "type":"night_choice",
            "action":"choice",
            "choice":[{"label": key, "display": value} for key, value in choice.items()]
        }
        if(nested==False):
            self.dialogueDict.append(result)
        return result
    
    def idle_chats(self):
        result = {
            "type":"idle_chat",
            "action":"idle_chat"
        }
        self.dialogueDict.append(result)
        return result
    
    def unlock_dialogue(self,events:list):
        result = {
            "type":"unlock_dialogues",
            "action":"unlock_dialogues",
            "events":events
        }
        self.dialogueDict.append(result)
        return result
    
    def condNight(self,actions):
        print("Compiling: Night Condition")
        result = {
            "type":"conditional",
            "action":"conditional",
            "var": "Nyaaa~",
            "condition": "night",
            "actions":actions
        }
        self.dialogueDict.append(result)
        return result
    
    def condDay(self,actions):
        print("Compiling: Day Condition")
        result = {
            "type":"conditional",
            "action":"conditional",
            "var": "Nyaaa~",
            "condition": "day",
            "actions":actions
        }
        self.dialogueDict.append(result)
        return result


    def condSame(self,varName: str, equalValue, actions):
        print("Compiling: "+varName)
        result = {
            "type":"conditional",
            "action":"conditional",
            "condition": "equal",
            "var": varName,
            "value": equalValue,
            "actions":actions
        }
        self.dialogueDict.append(result)
        return result

    def condNotSame(self,varName: str, equalValue, actions: list):
        print("Compiling: "+varName)
        result = {
            "type":"conditional",
            "action":"conditional",
            "condition": "not_equal",
            "var": varName,
            "value": equalValue,
            "actions": actions
        }
        self.dialogueDict.append(result)
        return result

    def condLessThan(self,varName:str, lessThanValue, actions: list):
        print("Compiling: "+varName)
        result = {
            "type":"conditional",
            "action":"conditional",
            "condition": "less_than",
            "var": varName,
            "value": lessThanValue,
            "actions": actions
        }
        self.dialogueDict.append(result)
        return result

    def condMoreThan(self,varName:str, moreThanValue, actions: list):  
        print("Compiling: "+varName)
        result = {
            "type":"conditional",
            "action":"conditional",
            "condition": "greater_than",
            "var": varName,
            "value": moreThanValue,
            "actions": actions
        }
        self.dialogueDict.append(result)
        return result
    
    def getGamemode(self,transition = True):
        result = {
            "type":"command",
            "action":"get_gamemode"
        }
        if(transition==False):
            self.dialogueDict.append(result)
        
        return result

    def customCommand(self,minecraftCommmand:str):
        result = {
            "type":"command",
            "action":"custom_commmand",
            "command":minecraftCommmand
        }
        self.dialogueDict.append(result)
        return result
    
    def givePlayer(self,itemId:str,amount:int):
        result = {
            "type":"give_player",
            "action":"give_player",
            "item_id":itemId,
            "amount":amount
        }
        self.dialogueDict.append(result)
        return result
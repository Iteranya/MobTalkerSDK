# This is the Module
# Basically,  if you're looking to expand the SDK's current functionality...
# Just add new method here
# Adding new class unfortunately still doesn't work, (Yet), I'm working on it
# Feel free to customize it to your system~
from core.model import Character

scriptDict = []

class VisualNovelModule(): # Module Class, just add more function as you like
    
    def initialize(self,scriptName):
        scriptDict.append({
            "type":"meta",
            "action":"initialize",
            "scriptName": scriptName
        })
    
    def start(self):
        result = {
            "type":"meta",
            "action":"start"
        }
        scriptDict.append(result)
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
            scriptDict.append(result)
        return result
    
    def background(self,background):
        result = {
            "type":"modify_background",
            "background":"asset/"+background
        }
        scriptDict.append(result)
        return result
    
    def clear_background(self):
        result = {
            "type":"clear_background"
        }
        scriptDict.append(result)
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
                "wFrameRatio":5,
                "hFrameRatio":8,
                "column":7,
                "row":1
            }
            if(transition==False):
                scriptDict.append(result)
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
                scriptDict.append(result)
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
                scriptDict.append(result)
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
                "wFrameRatio":5,
                "hFrameRatio":8,
                "column":3,
                "row":1
            }
            if(transition==False):
                scriptDict.append(result)
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
                "wFrameRatio":5,
                "hFrameRatio":8,
                "column":10,
                "row":1
            }
            if(transition==False):
                scriptDict.append(result)
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
                scriptDict.append(result)
            return result
        elif isinstance(character,str):
            print("Compiling: "+sprite)
            result = {
                "type":"remove_sprite",
                "action":"remove",
                "sprite":sprite,
            }
            if(transition==False):
                scriptDict.append(result)
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
            scriptDict.append(result)
        return result
        

    def label(self,labelName:str):
        print("Compiling: "+labelName)
        result = {
            "type":"label",
            "action" : "label",
            "label":labelName
        }
        scriptDict.append(result)
        return result

    def jumpTo(self,labelName:str,transition=False):
        print("Compiling:" + labelName)
        result = {
            "type":"transition",
            "action":"jump",
            "label": labelName
        }
        if(transition==False):
            scriptDict.append(result)
        return result

    def finish(self):
        print("Compiling A Finish Line")
        result = {
            "type":"finish_dialogue",
            "action": "finish_dialogue"
        }
        scriptDict.append(result)
        return result
        

    def setVar(self,varName:str,init:any):
        print("Compiling: "+varName)
        result = {
            "type":"meta",
            "action": "create_var", 
            "var": varName,
            "init":init
        }
        scriptDict.append(result)
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
        scriptDict.append (result)
        return result

    def subVar(self,varName:str, subAmount:int):
        print("Compiling: "+varName)
        result = {
            "type":"modify_variable",
            "action": "subtract_var", 
            "var": varName, 
            "value": subAmount
        }
        scriptDict.append(result)
        return result

    def modVar(self,varName:str, value:any):
        print("Compiling: "+varName)
        result = {
            "type":"modify_variable",
            "action": "modify_var", 
            "var": varName, 
            "value": value
        }
        scriptDict.append(result)

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
        scriptDict.append(result)
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
        scriptDict.append(result)
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
        scriptDict.append(result)
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
        scriptDict.append(result)
        return result
    
    def getCompiledScript(self):
        return scriptDict

class MinecraftModule():

    def getGamemode(self,transition = True):
        result = {
            "type":"command",
            "action":"get_gamemode"
        }
        if(transition==False):
            scriptDict.append(result)
        
        return result

    def customCommand(self,minecraftCommmand:str):
        result = {
            "type":"command",
            "action":"custom_commmand",
            "command":minecraftCommmand
        }
        scriptDict.append(result)
        return result
    
    def givePlayer(self,itemId:str,amount:int):
        result = {
            "type":"give_player",
            "action":"give_player",
            "item_id":itemId,
            "amount":amount
        }
        scriptDict.append(result)
        return result

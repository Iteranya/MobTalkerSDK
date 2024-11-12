import json


def compileVN(script):
    # The story 'script' file, automatically compiles into a list of dict, each one represents a state
    script_actions = script
    # Go ahead and turn on the following to check the list of dict, each one represents a state
    # print(script_actions)
    flat = flattenVN(script_actions)
    check(flat)
    return flat

def check(actions: list[dict]):
    existing_label = []
    existing_jump = []
    existing_id = {}

    for action in actions:
            if action["type"] == "label":
                existing_label.append(action["label"])
            elif action["type"] == "transition":
                existing_jump.append(action["label"])
            elif action["type"] == "unlock_dialogues":
                existing_jump+=action["events"]
            elif action["type"] == "choice":
                # Collect jump labels inside choice
                for choice in action["choice"]:
                    existing_jump.append(choice["label"])
            else:
                action_id = action["id"]
                if action_id in existing_id:
                    existing_id[action_id].append(action)
                else:
                    existing_id[action_id] = [action]
        
        # Check if any jump points to a non-existing label
    for jump in existing_jump:
        if jump not in existing_label:
            raise ValueError(f"Label not found: {jump}\n\nA jumpTo or a 'choice' or an 'unlock event' statement is pointing to a non-existent label called: {jump}. You can bypass this error and watch as your game crashes to a Null Pointer Exception when running this script. Or you can do a Ctrl+F and look for {jump} and make sure that it goes somewhere.")
    
    # Check for duplicate IDs and provide detailed error messages
    for action_id, actions_with_id in existing_id.items():
        if len(actions_with_id) > 1:
            action_details = "\n".join(str(action) for action in actions_with_id)
            raise ValueError(f"Duplicate action found:\n{action_details}\n\nThis usually happens because you forgot to add 'True' inside nested conditionals. Yeah, I know, weird, but you have specifically tell this thing when you make a nested statement of any kind... Sorry for  the weird workaround, I'm still working on a more graceful way of handling nested conditionals. Just mark nested as 'True' aight?")





# Flatten Conditional Statement
# To make the FSM as simple and lightweight as possible, we use custom Integer Id Indexing
# (TODO: Figure out if we can skip manual int indexing and use array indexing)
def flattenVN(actions: list[dict]) -> list[dict]:
    updated_actions = []
    actionIndex = 0 # First state in the FSM
    for action in actions:
        action["id"] = actionIndex # Put the state 0 or current number as 'id'
        if action["type"] == "conditional": # Conditionals are special
            subactions = []
            # There is no easy way to explain this
            # But basically... We want to...
            # Yeah, no I'm not explaining this, figure it out yourself future me.
            for subaction in action["actions"]:
                actionIndex += 1
                subaction["id"] = actionIndex
                subactions.append(subaction)
                
            action["end"] = actionIndex+1
            updated_actions.append(action)
            updated_actions+=subactions
            actionIndex +=1
            
        else:
            updated_actions.append(action)
            actionIndex +=1
            
    return updated_actions

def save_to_json_file(data: list[dict], file_path: str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def compile(storyname,script):
    print("Compiling VN script to FSM...")
    fsm =compileVN(script)
    save_to_json_file(fsm,storyname+".json")
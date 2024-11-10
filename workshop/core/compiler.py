import json


def compileVN(script):
    # The story 'script' file, automatically compiles into a list of dict, each one represents a state
    script_actions = script
    # Go ahead and turn on the following to check the list of dict, each one represents a state
    # print(script_actions)
    check(script_actions)
    return flattenVN(script_actions)

def check(actions: list[dict]):
    existing_label = []
    existing_jump = []
    
    # Collect existing labels and jumps
    for action in actions:
        if action["type"] == "label":
            existing_label.append(action["label"])
        elif action["type"] == "transition":
            existing_jump.append(action["label"])
        elif action["type"] == "choice":
            # Collect jump labels inside choice
            for choice in action["choice"]:
                existing_jump.append(choice["label"])
    
    # Check if any jump points to a non-existing label
    for jump in existing_jump:
        if jump not in existing_label:
            raise ValueError(f"Jump points to a non-existing label: {jump}")



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
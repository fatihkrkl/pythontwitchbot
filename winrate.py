import requests, json, asyncio
riot_api_key="RGAPI-e73a48f0-7297-4af7-aa16-59ba44d48a54"

json_path = "iron1.json"

puuid_path= "iron1puuid.json"

def load_stack(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

stack = load_stack(json_path)

puuid_stack= load_stack(puuid_path)

# Function to save the stack to a JSON file
def save_stack():
    with open(json_path, 'w') as file:
        json.dump(stack, file, indent=4)

def save_puuid():
    with open(puuid_path, 'w') as file:
        json.dump(puuid_stack, file, indent=4)

# Function to push an element onto the stack

def push(element):
    stack.append(element)
    save_stack()

def pushpuuid(element):
    puuid_stack.append(element)
    save_puuid()

# Function to pop an element from the stack
def pop():
    if stack:
        element = stack.pop()
        save_stack()
        return element
    else:
        return None  # Stack is empty

def poppuuid():
    if puuid_stack:
        element = puuid_stack.pop()
        save_puuid()
        return element
    else:
        return None  # Stack is empty



def search():
    page=0
    while page<5:
        page=page+1
        print(str(page))
        link="https://euw1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/CHALLENGER/I?page="+str(page)+"&api_key="+riot_api_key
        resp =requests.get(link)
        if "summonerId" in resp.json()[0]:
            print(len(stack))
            for p in resp.json():
                push(p["summonerId"])
        else:
            break
                        
            

def sum2puuid():
    for x in stack:
        link="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/"+x+"?api_key="+riot_api_key
        resp= requests.get(link)
        if resp.json():
            if "puuid" in resp.json():
                puuid=resp.json()["puuid"]
                pushpuuid(puuid)
                print(puuid)
        

sum2puuid()
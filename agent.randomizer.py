import random

# list of all agents.
duelists = ['jett', 'reyna', 'phoenix', 'raze', 'yoru', 'neon']
initiators = ['sova', 'breach', 'kay/o', 'fade', 'gekko']
controllers = ['brimstone', 'viper', 'omen', 'astra', 'harbor']
sentinels = ['cypher', 'killjoy', 'chamber', 'sage']

# returns a random agent. If a role is selected, it takes only from it.
def get_random_team(role=None):
    if role == 'duelist':
        return random.choice(duelists)
    elif role == 'initiator':
        return random.choice(initiators)
    elif role == 'controller':
        return random.choice(controllers)
    elif role == 'sentinel':
        return random.choice(sentinels)
    else:
        all_agents = duelists + initiators + controllers + sentinels # mix them all into one list
        return random.choice(all_agents)

print(f'You are playing for {get_random_team()} today.')

# random map peak.
maps = ['ascent', 'bind', 'breeze', 'fracture', 'haven', 'icebox','lotus', 'pearl', 'split', 'summit', 'sunset', 'abyss', 'corrode']
random_map = random.choice(maps)
print(f"Today's map: {random_map}")
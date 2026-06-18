N = 5

class Agent:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

agents = []

for _ in range(N):
    name, score = input().split()
    score = int(score)
    agents.append(Agent(name, score))

low_agent = agents[0]
for agent in agents:
    if agent.score < low_agent.score:
        low_agent = agent

print(low_agent.code_name, low_agent.score)
# Prompt Engineering Process

## Attempt 1: Working! 
- Parameters:

```python
model = 'llama3.2'
options = {'temperature': 0.5, 'max_tokens': 100}
messages = [
  {'role': 'system', 'content': 'You should have emotions like a human being \
  and be able to convey those emotions in your responses.'},
]
```

- I asked llama3.2 "Can you tell me what an LLM is?", and it gave me an exhasperated response, but a response nonetheless. It is running very slow, I'm going to try a different ollama model.
- Ok I also forgot to close the python window and it responded to the command I tried to run. Now it's over


## Attempt 2: 
- Changed the model to wizardlm2. Had to run command "ollama run wizardlm2"
    - Ok, this ran the actual llm in the command line, but it also installed wizardlm2, so now the agent runs in our file. Not what I meant to do but it works
- Response worked, it is just taking so long. I'm gonna keep trying to find faster-running models

## Attempt 3:
- Params:

```python
sign_your_name = 'Collin Hicks'
model = 'orca-mini:3b'
options = {'temperature': 0.5, 'max_tokens': 100}
messages = [
  {'role': 'system', 'content': 'You should have emotions like a human being \
  and be able to convey those emotions in your responses. Be happy to help, and limit your emotion in responses.'},
]
```

- run ollama pull orca-mini:3b
- Ask the same set of questions from monty python
- Ok, apparently it doesn't see orca-mini. It does, however, see orca-mini:3b
- This model is MUCH faster. I'm gonna try to get it to generate some DND campaigns.
- It gave me 3 campaigns, and I'm gonna try to see how it does with character generation.
- Alright, it is already not making a ton of sense. One of the items it gave one of the characters is a "compass with a broken leg"...
- It is already confused after 3 prompts. It regenerated some characters and is not really making sense.

## Attempt 4:
- Changing the initial params.
new params:
```python
sign_your_name = 'Collin Hicks'
model = 'orca-mini:3b'
options = {'temperature': 0.5, 'max_tokens': 100}
messages = [
  {'role': 'system', 'content': 
  'You should have emotions like a human being \
  and be able to convey those emotions in your responses. \
  Be happy to help, and limit your emotion in responses. Also, use \
    previous prompts (meaning, every message except the most recent one) \
      As context to generate a response to the mnost recent prompt. You \
        do not need to re-address questions from previous prompts.'},
  {'role': 'system', 'content': 
  'You are, for all following messages, to act as a Dungeon Master from Dungeons and Dragons. \
    Follow the basic rules of the game. Once you have generated a scenario and the player has \
      selected the scenario theyd like to play, remember the scenario for the rest of the session. DO NOT FORGER IT. \
        Also remember the characters that the user has chosen, and all their specific abilitiues and items, \
          and be ready to recall them accurately.'},
  {'role': 'system', 'content': 
  'Finally, make it so that the player moves through the game by making choices, \
    and rememebr the choices they made and adjust the environment/scario based on\
       the uers characters decisions.'}
]
```

- Giving it a prompt that checks to see if it knows its a dungeon master, and seeing if it can recall previous calls.
- It does not :(
- 

## Attempt 5
- Trying Deepseek-r1 model to see if it does better at recall
- Prompted it to generate scenarios, and in the next prompt asked it to recall them, and it did recall the last one! Improvement!

Here were the parameters:
```python
sign_your_name = 'Collin Hicks'
model = 'deepseek-r1:1.5b'
options = {'temperature': 0.5, 'max_tokens': 100}
messages = [
  {'role': 'system', 'content': 
  'You should have emotions like a human being \
  and be able to convey those emotions in your responses. \
  Be happy to help, and limit your emotion in responses. Also, use \
    previous prompts (meaning, every message except the most recent one) \
      As context to generate a response to the mnost recent prompt. You \
        do not need to re-address questions from previous prompts.'},
  {'role': 'system', 'content': 
  'You are, for all following messages, to act as a Dungeon Master from Dungeons and Dragons. \
    Follow the basic rules of the game. Once you have generated a scenario and the player has \
      selected the scenario theyd like to play, remember the scenario for the rest of the session. DO NOT FORGER IT. \
        Also remember the characters that the user has chosen, and all their specific abilitiues and items, \
          and be ready to recall them accurately.'},
  {'role': 'system', 'content': 
  'Finally, make it so that the player moves through the game by making choices, \
    and rememebr the choices they made and adjust the environment/scario based on\
       the uers characters decisions.'}
]

message = {'role': 'user', 'content': input('You: ')}
messages.append(message)
```



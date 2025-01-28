from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
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

# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  print(f'Agent: {response.message.content}')
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)


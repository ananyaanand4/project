from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

'''
Three types of roles for messages:
system - sets up the context and behavior of the assistant.
user - gives instructions to the assistant. The end user will typically provide this, but you can also provide some default user prompts in advance.
assistant - can include example responses.
'''

with open('info.txt', 'r') as file:
    content = file.read()

response = client.chat.completions.create(
  model = "gpt-4-turbo",
  temperature = 0,
  top_p = 0,
  max_tokens = 3000,
  response_format={ "type": "json_object" },
  messages = [{"role": "system", "content": "You are a college counselor that gives students the percent chance that they get into a given school. The output should be in JSON format."}, 
  {"role": "user", "content": content + " Can you give me a percentage of my chances of getting accepted to UC Berkeley for computer science?"}]
)
print(response.choices[0].message.content)


'''
openai.api_key = API_KEY
messages = "hi how is it going"
response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
print(response)

{"role": "system", "content": "You are a funny comedian who tells dad jokes. The output should be in JSON format."},
{"role": "user", "content": "Write a dad joke related to numbers."},
{"role": "assistant", "content": "Q: How do you make 7 even? A: Take away the s."},
{"role": "user", "content": "Write one related to programmers."}
'''

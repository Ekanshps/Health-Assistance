import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
HF_TOKEN=os.getenv("HF_TOKEN")


client=OpenAI(base_url="https://router.huggingface.co/v1",api_key=HF_TOKEN)

responce=client.chat.completions.create(model="openai/gpt-oss-120b",
                               messages=[{
                                   "role":"user",
                                   "content":"What Is good source of Protien in Vegeterian."
                               }])

answer=responce.choices[0].messsage.content
print(answer)

from langchain_core.prompts import PromptTemplate

from config import load_google_llm
llm=load_google_llm()
# Tutorial generator (topic, audience, length, format)
prompt_template=PromptTemplate.from_template(
   
    "Given a topic {topic}, audience {audience} generate a detailed and clear Tutorial suitable for a beginner with the given length {length} in the format {format}. "
)
# Where should we accept this input

print("WELCOME TO MY TUTORIAL GENERATOR APP")
print("_"*70)

while True:
    user_topic=input("Please enter the topic you would like to learn about:\n")
    if user_topic.lower().strip() in ["exit", "quit", "bye"]:
        print("Chat ended. Goodbye!..........")
        break
    user_audience=input("Please enter the audience:\n")
    user_length=input("Please enter the length of the tutorial:\n")
    user_format=input("Please enter the format of the tutorial:\n")


    prompt=prompt_template.format(
        topic=user_topic,
        audience=user_audience,
        length=user_length,
        format=user_format
    )

    print("loading......")
    response=llm.invoke(prompt)
    print(f"response is: {response}")
    for part in llm.stream(prompt):
        print(part, end="", flush=True)
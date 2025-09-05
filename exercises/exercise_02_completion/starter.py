
from langchain_core.prompts import PromptTemplate

from config import load_google_llm
llm=load_google_llm()

prompt_template=PromptTemplate.from_template(
   
    "Given a topic {topic}, generate a detailed and informative explanation suitable for a beginner. "
)

print("WELCOME TO MY LEARNING APP")
print("_"*70)

# recieve info from the user
while True:
    user_topic=input("Please enter a topic you would like to learn about:\n")
    if user_topic.lower().strip() in ["exit", "quit", "bye"]:
        print("Chat ended. Goodbye!..........")
        break
    prompt=prompt_template.format(
        topic=user_topic
)

    print("loading......")
    response=llm.invoke(prompt)
    print(f"response is: {response}")
    for part in llm.stream(prompt):
      print(part, end="", flush=True)

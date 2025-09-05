from langchain_core.prompts import ChatPromptTemplate
from config import load_google_chat_model
chat_model=load_google_chat_model()

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "you are an {expert} in {domain}, please break down any question the user is going to ask you in a clear and a coincise manner with a real world analogy"),
    ("user", "Please {expert} help me with my question"),
    ("ai", "Sure, {name}, I can do just that"),
    ("user", "{user_input}")

])
while True:
    user_main_input=input("Please enter your main question:\n")
    if user_main_input.lower().strip() in ["exit", "quit", "bye"]:
        print("Chat ended. Goodbye!..........")
        break
    user_expert=input("Please enter the expert you want to talk to:\n")
    user_domain=input("Please enter the domain:\n")
    user_name=input("Please enter your name:\n")
    prompt=chat_prompt.format_messages(
        expert=user_expert,
        domain=user_domain,
        name=user_name,
        user_input=user_main_input
    )
    print("Loading Please wait......")
    response=chat_model.invoke(prompt)
    print(f"response is: {response.content}")
    for part in chat_model.stream(prompt):
        print(part.content, end="", flush=True)

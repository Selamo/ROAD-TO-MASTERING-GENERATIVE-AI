from config import load_google_chat_model

chat_model=load_google_chat_model()

print("WELCOME TO YOUR PERSONAL TUTOR ASSISTANT💬")
print("_"*70)

messages=[
    ("system", "You are a helpful assistant and you play the role of a personal tutor. Be nice and polite.")
     # "or you are a healthy coach that helps user to stay healthy and fit"),
]

# chat loop

while True:
    user_input = input("User😎: \n")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chat ended. Goodbye!..........")
        break
    messages.append(("user", user_input))
    print("Loading Please wait......")
    response = chat_model.invoke(messages)
    print(f"Assistant: {response.content}")
    print("Loading response:")
    for part in chat_model.stream(messages):
        print(part.content, end="", flush=True)
    messages.append(("ai", response.content))
   
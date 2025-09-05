
from langchain_core.prompts import PromptTemplate

from config import load_google_llm
llm=load_google_llm()

prompt_template=PromptTemplate.from_template(
   
    "Given ingredients {ingredients} and the {cuisine} generate a detailed and informative recipe suitable for a beginner. "
)

def validate_template_variables(template, variables):
    missing = [var for var in template.input_variables if not variables.get(var)]
    if missing:
        raise ValueError(f"Missing required variables: {', '.join(missing)}")

print("WELCOME TO MY LEARNING APP")
print("_"*70)

while True:
    user_ingredients = input("Please enter the ingredients you will like to use:\n")
    if user_ingredients.lower().strip() in ["exit", "quit", "bye"]:
        print("Chat ended. Goodbye!..........")
        break
    user_cuisine = input("User😎: Enter the cuisine please\n")
    variables = {
        "ingredients": user_ingredients,
        "cuisine": user_cuisine
    }
    try:
        validate_template_variables(prompt_template, variables)
        prompt = prompt_template.format(**variables)
        print("loading......")
        response = llm.invoke(prompt)
        print(f"response is: {response}")
        for part in llm.stream(prompt):
            print(part, end="", flush=True)
    except ValueError as e:
        print(f"Error: {e}")

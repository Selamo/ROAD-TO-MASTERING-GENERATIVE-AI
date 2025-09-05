import os
import sys
from langchain_core.messages import HumanMessage
# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from config.config import environmental_variables, load_google_llm, load_google_chat_model

# Configuration Management


# Model Selection System
class ModelSelector:
    def __init__(self):
        self.models = {
            "1": "Google LLM",
            "2": "Google Chat Model",
        }

    def select_model(self):
        print("Select a model:")
        for key, value in self.models.items():
            print(f"{key}: {value}")
        choice = input("Enter model number: ")
        if choice == "1":
            return "google_llm"
        elif choice == "2":
            return "google_chat_model"
        else:
            return None

# Template Library
class TemplateLibrary:
    def __init__(self):
        self.templates = {
            "1": "Translate the following English text to French: '{text}'",
            "2": "Summarize the following text: '{text}'",
            "3": "Write a poem about: '{text}'",
        }

    def select_template(self):
        print("Select a template:")
        for key, value in self.templates.items():
            print(f"{key}: {value.split(':')[0]}")
        choice = input("Enter template number: ")
        return self.templates.get(choice)

# AI Interaction
class AIInteraction:
    def __init__(self, model_name):
        if model_name == "google_llm":
            self.model = load_google_llm()
        elif model_name == "google_chat_model":
            self.model = load_google_chat_model()
        else:
            self.model = None

    def generate_content(self, prompt, stream=False):
        if not self.model:
            print("Model not loaded.")
            return

        print(f"Generating content with model: {self.model.model}")
        print(f"Prompt: {prompt}")
        if stream:
            for chunk in self.model.stream(prompt):
                print(chunk, end="", flush=True)
            print()
        else:
            response = self.model.invoke(prompt)
            print(f"Response: {response}")

    def chat(self, messages, stream=False):
        if not self.model:
            print("Model not loaded.")
            return
        print(f"Chatting with model: {self.model.model}")
        print(f"Messages: {messages}")
        if stream:
            for chunk in self.model.stream(messages):
                print(chunk.content, end="", flush=True)
            print()
        else:
            response = self.model.invoke(messages)
            print(f"Response: {response.content}")


# User Interface Layer
class UILayer:
    def __init__(self):
        self.config = Config()
        if not self.config.API_KEY:
            print("Error: GOOGLE_API_KEY environment variable not set.")
            exit()
        self.model_selector = ModelSelector()
        self.template_library = TemplateLibrary()

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Completion Model")
            print("2. Chat Model")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.completion_menu()
            elif choice == "2":
                self.chat_menu()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def completion_menu(self):
        model_name = self.model_selector.select_model()
        if not model_name:
            print("Invalid model selected.")
            return

        ai_interaction = AIInteraction(model_name)

        while True:
            print("\n--- Completion Menu ---")
            print("1. Freeform Prompt")
            print("2. Template-based Prompt")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                prompt = input("Enter your prompt: ")
                stream = input("Stream response? (y/n): ").lower() == 'y'
                ai_interaction.generate_content(prompt, stream)
            elif choice == "2":
                template = self.template_library.select_template()
                if not template:
                    print("Invalid template selected.")
                    continue
                text = input("Enter the text: ")
                prompt = template.format(text=text)
                stream = input("Stream response? (y/n): ").lower() == 'y'
                ai_interaction.generate_content(prompt, stream)
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")


    def chat_menu(self):
        model_name = self.model_selector.select_model()
        if not model_name:
            print("Invalid model selected.")
            return

        ai_interaction = AIInteraction(model_name)
        messages = []

        while True:
            print("\n--- Chat Menu ---")
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            messages.append(HumanMessage(content=user_input))
            stream = input("Stream response? (y/n): ").lower() == 'y'
            ai_interaction.chat(messages, stream)
            # In a real app, you would append the model's response to messages


# Error Handling System
def main():
    try:
        ui = UILayer()
        ui.main_menu()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

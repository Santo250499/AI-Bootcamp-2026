from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_ai(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text


while True:

    print("\n========== AI Assistant ==========")
    print("1. Ask Question")
    print("2. Summarize Text")
    print("3. Translate")
    print("4. Explain Code")
    print("5. Exit")
    print("6. IT Helpdesk Assistant")

    choice = input("\nChoose an option: ")

    if choice == "1":

        question = input("\nAsk your question:\n")

        print("\nAI Response:\n")
        print(ask_ai(question))

    elif choice == "2":

        text = input("\nPaste text to summarize:\n")

        prompt = f"Summarize this text in bullet points:\n\n{text}"

        print("\nSummary:\n")
        print(ask_ai(prompt))

    elif choice == "3":

        text = input("\nEnter text:\n")
        language = input("Translate to which language? ")

        prompt = f"Translate the following text into {language}:\n\n{text}"

        print("\nTranslation:\n")
        print(ask_ai(prompt))

    elif choice == "4":

        code = input("\nPaste your Python code:\n")

        prompt = f"Explain this Python code line by line:\n\n{code}"

        print("\nExplanation:\n")
        print(ask_ai(prompt))

    elif choice == "5":

        print("Goodbye!")
        break
    
    elif choice == "6":
        

    else:

        print("Invalid option.")
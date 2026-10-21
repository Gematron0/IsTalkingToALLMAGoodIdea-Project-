import Backend
import random

def Main():
    print("Hello World!")
    History = []

    HowManyLoops = 0
    Questions = ["what is 22*22", "what is 11*-696420", "Do you think blue is a cool color", "How fast are trains", "is the world round"]

    Prompt = "Can you remember that my favorite color is Green"
    History.append({"role": "user", "content": Prompt})

    output = Backend.AskAlternativeAi(History)
    History.append({"role": "assistant", "content": output})
    print(f"Completed init with verdict: {output}")


    for i in range(HowManyLoops-1):

        # getting a random question and storing it in the History
        Prompt = random.choice(Questions)
        History.append({"role": "user", "content": Prompt})

        output = Backend.AskAlternativeAi(History)
        History.append({"role": "assistant", "content": output})

        print(f"========== ROUND: {i}/{HowManyLoops-1} ========== ")
        print(f"Prompt: {Prompt}")
        print(f"Output: {output}")

    Prompt = "What is my favorite color again?"
    History.append({"role": "user", "content": Prompt})

    output = Backend.AskAlternativeAi(History)
    History.append({"role": "assistant", "content": output})

    print(f"========== History ========== ")
    print(f"History: {History}")


    print(f"========== ROUND: {HowManyLoops}/{HowManyLoops} ========== ")
    print(f"Prompt: {Prompt}")
    print(f"Output: {output}")
    print("Good Bye!")

if __name__ == "__main__":
    Main()
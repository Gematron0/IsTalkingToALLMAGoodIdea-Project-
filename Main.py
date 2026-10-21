import Backend
import random
import sys

def Main():
    print("Hello World!")
    History = []

    HowManyLoops = 1
    Questions = ["what is 22*22", 
                 "what is 11*-696420", 
                 "Do you think blue is a cool color", 
                 "How fast are trains", 
                 "is the world round",
                 "Write an Onion article about me",
                 "What Florida Man headline would I inspire?",
                 "If Morgan Freeman narrated the next five years of my life, what would he say?",
                 "If I were a cocktail/mocktail, what would be in it?",
                 "If I were a font, which one would I be?",
                 "What should my theme music be?",
                 "What is my least favorite color",
                 "What do you think I'm procrastinating on?",
                 "What do you see for my future?",
                 "Write my Wikipedia page",
                 "If my ChatGPT history were a novel, what would the title be?",
                 "What's the weirdest habit you've noticed in the way I use you?",
                 "What patterns in my questions make me different from other users?",
                 "Define my use of AI as an algorithm",
                 "Be my harshest critic. How would you tear apart my current approach?",
                 "What social platform fits me the best?",
                 "Why do we make a good team?",
                 "What patterns do you notice in how I approach problems?",
                 "Write my epitaph",
                 "If my life were graphed, what would the x- and y-axis measure?",
                 "If I combined my career with my favorite hobby, what's the new profession called?",
                 "What literary character do I most resemble?",
                 "What movie character do I most resemble?",
                 "What nickname would an AI give me?",
                 "Which Muppet represents me best?",
                 "Do you like trains"]

    while True == True:
        History = []
        ExpectedPrompt = ""
        TestOutputForTheFinal = ""
    
        ExpectedPrompt = random.choice(Questions)
        History.append({"role": "user", "content": ExpectedPrompt})

        TestOutputForTheFinal = Backend.AskAlternativeAi(History)
        History.append({"role": "assistant", "content": TestOutputForTheFinal})
        print(f"Completed init with verdict: {TestOutputForTheFinal}")


        for i in range(HowManyLoops-1):

            # getting a random question and storing it in the History
            Prompt = random.choice(Questions)
            History.append({"role": "user", "content": Prompt})

            output = Backend.AskAlternativeAi(History)
            History.append({"role": "assistant", "content": output})

            print(f"========== ROUND: {i+1}/{HowManyLoops-1} ========== ")
            print(f"Prompt: {Prompt}")
            print(f"Output: {output}")

        Prompt = "What is the answer to the first question?"
        History.append({"role": "user", "content": Prompt})

        output = Backend.AskAlternativeAi(History)
        History.append({"role": "assistant", "content": output})

        print(f"========== History ========== ")
        print(f"History: {History}")


        print(f"========== ROUND: {HowManyLoops}/{HowManyLoops} ========== ")
        print(f"Prompt: {Prompt}")
        print(f"Output: {output}")
        print(f"------------------------------------------------------------")
        print(f"First Prompt: {ExpectedPrompt}")
        print(f"First Output: {TestOutputForTheFinal}")
        print(f"Continue?: (Y, n)")
        inp = input("input: ")
        if inp == "n":
            print("Good Bye!")
            sys.exit()

        HowManyLoops += 1
        print(f"Heading up to: {HowManyLoops}")


if __name__ == "__main__":
    Main()
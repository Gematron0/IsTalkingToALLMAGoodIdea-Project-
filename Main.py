import Backend

def Main():
    print("Hello World!")
    #Backend.ask_openai("Test Input, just respond")
    data = Backend.AskAlternativeAi("what is 72*134")
    print(f"Output: {data}")

if __name__ == "__main__":
    Main()
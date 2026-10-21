import Backend

def Main():
    print("Hello World!")
    history = []

    UserPrompt1 = "Can you remember that my favorite color is Green"
    history.append({"role": "user", "content": UserPrompt1})

    output = Backend.AskAlternativeAi(history)
    history.append({"role": "assistant", "content": output})
    print(f"Output: {output}")

    UserPrompt2 = "what is 22*22"
    history.append({"role": "user", "content": UserPrompt2})

    output = Backend.AskAlternativeAi(history)
    history.append({"role": "assistant", "content": output})
    print(f"Output: {output}")

    UserPrompt3 = "How do airplanes work"
    history.append({"role": "user", "content": UserPrompt3})

    output = Backend.AskAlternativeAi(history)
    history.append({"role": "assistant", "content": output})
    print(f"Output: {output}")

    UserPrompt4 = "What is my favorite color again?"
    history.append({"role": "user", "content": UserPrompt4})

    output = Backend.AskAlternativeAi(history)
    history.append({"role": "assistant", "content": output})
    print(f"Output: {output}")
    print(f"History: {history}")
    print(f"--------------------------Final Verdict: {output}")

if __name__ == "__main__":
    Main()
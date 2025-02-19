def main():
    yell("This", "is", "CS50")

def yell(*words):
    # just passing the upper func; not calling it but just passing it phir map func khud call karega
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()


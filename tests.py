from functions.run_python_file import run_python_file

def main():
    print("main.py")
    result = run_python_file("calculator", "main.py")
    print(result)
    print("main.py 3 + 5")
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    print("../main.py")
    result = run_python_file("calculator", "../main.py")
    print(result)
    print("nonexistent.py")
    result = run_python_file("calculator", "nonexistent.py")
    print(result)

if __name__ == "__main__":
    main()
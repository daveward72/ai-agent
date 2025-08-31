from functions.get_file_content import get_file_content

def test_file(working_directory, file_path):
    print(f"\nResult for {file_path}:")
    file_content = get_file_content(working_directory, file_path)
    print(file_content)

def main():
    test_file("calculator", "main.py")
    test_file("calculator", "pkg/calculator.py")
    test_file("calculator", "/bin/cat")
    test_file("calculator", "pkg/does_not_exist.py")

if __name__ == "__main__":
    main()
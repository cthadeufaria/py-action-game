"""Script that formats all code with Black, does type checking with mypy and runs the Flake8 linter."""

import os

print("\nTESTING ALL FILES\n".center(24))

print(" ⚡ First running black formatter...\n")
os.system("black .")
print("\nDone!")

print("\n 💪 Now checking types with mypy...\n")
os.system("mypy --strict .")
print("\nDone!")
mypy_ans = input("\n\t 🤔 Did it return any errors? [y/N] ")

if mypy_ans.strip().lower() == "y":
    print("\n\tThat's ok! 👍\n\tFix them and run this script again.")

else:
    print("\n 🔥 Now running flake8 linting...\n")
    os.system("flake8 --extend-ignore E501 .")
    print("\nDone!")

    print("\nThat's it. 🚀")
    print("Remember to fix any remaining errors before commiting your code! 😎\n")

import re

# Define the custom functions
def bol(x):
    print(x)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Simulating the preprocessor
def preprocess_and_execute(code):
    if not code.strip().startswith('start'):
        raise SyntaxError("Invalid syntax. Code must start with 'start'.")
    if not code.strip().endswith('END'):
        raise SyntaxError("Invalid syntax. Code must end with 'END'.")

    # Remove the 'start' and 'END' keywords
    code = code.replace('start', '', 1).strip()
    code = code.rsplit('END', 1)[0].strip()

    # Split code into lines and initialize processed_lines list
    lines = code.split('\n')
    processed_lines = []

    # Iterate through each line
    for line in lines:
        stripped_line = line.strip()
        
        # Ignore empty lines and lines with only whitespace
        if not stripped_line:
            continue
        
        # If the line starts with 'rakh ', replace 'rakh' with ''
        if stripped_line.startswith("rakh "):
            line = line.replace("rakh ", "", 1)
            processed_lines.append(line)
        
        # If the line contains 'bol', 'add', 'subtract', 'multiply', 'divide', 'agr', 'nhi to', or 'chalta rah', add it to processed_lines
        elif re.search(r'\bbol\b', stripped_line) or re.search(r'\badd\b', stripped_line) or re.search(r'\bsubtract\b', stripped_line) or re.search(r'\bmultiply\b', stripped_line) or re.search(r'\bdivide\b', stripped_line) or re.search(r'\bagr\b', stripped_line) or re.search(r'\bnhi to\b', stripped_line) or re.search(r'\bchalta rah\b', stripped_line):
            processed_lines.append(line)
        
        # If the line does not start with a comment and is not valid syntax, raise a SyntaxError
        elif stripped_line and not stripped_line.startswith("#"):
            raise SyntaxError("Invalid syntax. Use 'rakh' to declare variables.")
    
    # Join processed_lines into a single string
    code = '\n'.join(processed_lines)
    
    # Replace custom keywords with Python keywords
    code = code.replace("bol", "print")
    code = code.replace("add", "+")
    code = code.replace("subtract", "-")
    code = code.replace("multiply", "*")
    code = code.replace("divide", "/")
    code = code.replace("agr", "if")
    code = code.replace("nhi to", "else")
    code = code.replace("chalta rah", "while")
    
    # Execute the processed code
    exec(code)

# Get user input from the terminal
print("Enter your code (type 'END' on a new line to finish):")
user_code_lines = []
user_code_started = False
while True:
    line = input()
    if line.strip().upper() == 'END':
        user_code_lines.append(line)
        break
    if line.strip().upper() == 'START':
        user_code_started = True
    if user_code_started:
        user_code_lines.append(line)

user_code = '\n'.join(user_code_lines)

# Execute the user code
try:
    preprocess_and_execute(user_code)
except SyntaxError as e:
    print(e)

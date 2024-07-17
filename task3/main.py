def is_balanced(string):
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []

    for char in string:
        if char in bracket_pairs:
            stack.append(char)

        elif char in bracket_pairs.values():
            if not stack:
                return "Несиметрично"
            last_open = stack.pop()

            if bracket_pairs[last_open] != char:
                return "Розділювачі різних видів у парі"
    
    if stack:
        return "Несиметрично"
    
    return "Симетрично"

examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for example in examples:
    result = is_balanced(example)
    print(f"{example}: {result}")

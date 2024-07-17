from collections import deque

def check_for_palindrome(text):
    d = deque()
    prepared_text = list("".join(text.split()).lower())
    d.extend(prepared_text)
    
    while True:
        if not d:
            result = f"String {text} is a palindrome"
            break
        else:
            try:
                if not d.pop() == d.popleft():
                    result = f"String {text} is not a palindrome"
                    break
            except IndexError:
                result = f"String {text} is a palindrome"

    return result

test_list = ["level", "level non LEVEL", "palindrome", "radar", "some text"]
for test in test_list:
    print(check_for_palindrome(test))

import collections

# Функція для перевірки на паліндром
def is_palindrome(s):
    formatted_str = ''.join(e for e in s if e.isalnum()).lower()
    deque = collections.deque(formatted_str)

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False
    return True

test = ["noon", "cat", "some men interpret nine memos", "European Union", "madam i'm Adam", "радар", "дід", "фіаско"]
for string in test:
    print(f"Рядок '{string}' є паліндромом: {is_palindrome(string)}")

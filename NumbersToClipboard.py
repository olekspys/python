import pyperclip
import re

text = pyperclip.paste()
numbers = re.findall(r'\d+', text)
unique_numbers = sorted(set(numbers), key=lambda x: int(x))
result = ', '.join(unique_numbers)
pyperclip.copy(result)
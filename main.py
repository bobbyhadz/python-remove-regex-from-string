# Remove characters matching Regex from a String in Python

import re

my_str = '!bobby @hadz #com $abc'

result = re.sub(r'[!@#$]', '', my_str)
print(result)  # 👉️ 'bobby hadz com abc'

result = re.sub(r'[^!@#$]', '', my_str)
print(result)  # 👉️ '!@#$'
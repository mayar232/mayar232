from pathlib import Path

path = Path("C:/Users/DELL/Desktop/math")
for file in path.iterdir():
    if file.is_file():
        print(file.name)

        with open(file, "r", encoding="utf-8") as f:
         for line in f:
            print(line.strip())
 ###########################################################################
from pathlib import Path

path = Path("C:/Users/DELL/Desktop/math")

for file in path.iterdir():
    if file.is_file():

        print("math", file.name)

        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) > 0:
                name = lines[0].strip()
            else:
                    name = "Not found"

            if len(lines) > 1:
                    number = lines[1].strip()
            else:
                number = "Not found"

            if len(lines) > 2:
                description = "".join(lines[2:]).strip()
            else:
                description = "Not found"

        print("Name:", name)
        print("Number:", number)
        print("Description:", description)
        print("Example:", "Not found")
        print("-" * 30)
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

path = Path(""C:/Users/DELL/Desktop/math"")

for file in path.iterdir():
    if file.is_file():

        print("math", file.name)

        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        name = lines[0].strip() if len(lines) > 0 else "Not found"
        number = lines[1].strip() if len(lines) > 1 else "Not found"
        description = "".join(lines[2:]).strip() if len(lines) > 2 else "Not found"

        print("Name:", name)
        print("Number:", number)
        print("Description:", description)
        print("Example:", "Not found")
        print("-" * 30)

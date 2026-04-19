
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
            example = []
            description = []
            

            for i in range(2, len(lines)):
                line = lines[i].strip()

                if "example" in line.lower():
                    

                    example.append(line)
                else:
                    description.append(line)

        print("Name:", name)
        print("Number:", number)
        print("Example:", example)
        print("Description:", description)
        print("-------------------------")
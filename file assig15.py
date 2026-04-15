from pathlib import Path

path = Path("C:/Users/DELL/Desktop/math")
for file in path.iterdir():
    if file.is_file():
        print(file.name)

        with open(file, "r", encoding="utf-8") as f:
         for line in f:
            print(line.strip())
 
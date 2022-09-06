counter = 0
file = open("project-files/wordlist.txt", "w")

while counter < 10000:
    file.write(f"{str(counter).zfill(4)}\n")
    counter += 1

file.close()
# manipulating pdf
import pikepdf
# visuallizing progress
from tqdm import tqdm

# load password file
pwds = [line.strip() for line in open("project-files\wordlist.txt")]

# iterate over passwords
for pwd in tqdm(pwds, f"Decrypting PDF: "):
    try:
        # attempt to open pdf file with password
        with pikepdf.open("project-files/protected-file.pdf", password=pwd+"1") as pdf:
            # password decryption success
            print("\n[+] Password found: ", pwd+"1")
            break
    # in the case of an incorrect password
    except Exception as e:
        # continue iteration
        continue
else:
    print("[-] Password was not found")
    print("Exiting...")
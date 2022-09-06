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
        with pikepdf.open("project-files/protected-file.pdf", password=pwd) as pdf:
            # password decryption success
            print("[+] Password foiund: ", pwd)
            break
    # in the case of an incorrect password
    except:
        # continue iteration
        continue
    else:
        print("[-] Password was not found")
        print("Exiting...")
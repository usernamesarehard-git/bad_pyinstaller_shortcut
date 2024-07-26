import subprocess as sb

print("this needs to be in the same directory to work\n")
print("(don't add the .py)\n\n")

filename = input("file name: ") + ".py"

command = f"python -m PyInstaller --onefile {filename}"

output = sb.run(command)

if output.returncode == 0:
    print("done!")
else:
    print("i kinda fucked up.")
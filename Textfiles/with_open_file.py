
#in this way files are automaticaly closed
with open("jabberlocky.txt", "r") as jabber:
  for line in jabber:
    print(line.rstrip())

with open ("jabberlocky.txt", "r") as jabber:
  # returns list of lines as string. Every line ends up with
  # new line character \n
  lines = jabber.readlines()
print("-" * 80)
print(lines)
print("-" * 80)
print(lines[-1:])

#reverse order
for line in reversed(lines):
  print(line)

print("-" * 80)
# 'r' mode is the default one, you can skip mode if open
# it for reading
with open("jabberlocky.txt") as jabber:
  # read file text as string
  text = jabber.read()
#reverse order
for char in reversed(text):
  print(char, end="")

print("-" * 30)

with open("jabberlocky.txt") as jabber:
  while True:
    line = jabber.readline().rstrip()
    print(line)
    if "jubjub" in line.casefold():
      break

print("-" * 30)

with open("jabberlocky.txt") as jabber:
  for line in jabber:
    print(line.rstrip())

    if "jubjub" in line.casefold():
      break 

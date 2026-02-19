#open function open the file and return an object that you can work with
#"r" is the mode and stands for reading. You can't for instance write on it
jabber = open("jabberlocky.txt", "r")

#loop through every line
for line in jabber:
  print(line, end="")

#closing file
jabber.close()

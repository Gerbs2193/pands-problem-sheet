def letterfrequency(filename, letter):
      file = open(filename, 'r')
      text = file.read()
      return text.count(letter)
print(letterfrequency('week07testing.txt', 'e'))
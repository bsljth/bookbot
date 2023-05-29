def num_words(content):
  words = content.split()
  return len(words)

with open("books/frankenstein.txt") as f:
  file_text = f.read()
  print(num_words(file_text))


from alph_dict import alph_dict

def num_words(words_arr):
  return len(words_arr)

def num_chars(words_arr, alph_dict):
  alphs = "abcdefghijklmnopqrstuvwxyz"
  for word in words_arr:
    word = word.lower()
    for char in word:
      if char in alphs:
        alph_dict[char] += 1
  return alph_dict

def main():
  file_path = "books/frankenstein.txt"
  with open(file_path) as f:
    text_from_file = f.read()
    words_in_file = text_from_file.split()

    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words(words_in_file)} words found in the document")
    print(num_chars(words_in_file, alph_dict))

main()
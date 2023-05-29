## bookbot
bookbot is a guided project that I had to do for the [boot.dev](https://boot.dev) back-end engineering online coding bootcamp.

Bookbot reads a `.txt` file and processes the text for specific information such as counting the number of words in the text, the number of times each English alphabet occurs in the text etc.

To run this program in your local system, first clone this repo (duh!).

Navigate into the folder created by cloning.

Before you run the project, create, within the project folder, a new folder called `books` (you can choose any name you want, but you'll have to make the relevant changes in `main.py`) and save any `.txt` file within the folder.

For this project, I was asked to download a `.txt` version of Mary Shelley's Frankenstein from [here](https://raw.githubusercontent.com/asweigart/codebreaker/master/frankenstein.txt).

Save this file in the `books` folder. Make sure the path of the file is correct in the `main.py` file.


To run the programme, enter the following command into your terminal (make sure you are in the project's root folder):

```
$ python main.py
```
or depending on your operating system, run:
```
$ python3 main.py
```


You can also use [Codon](https://github.com/exaloop/codon) to compile a binary of the file like this:
```
$ codon build main.py
```


and run the program like this:
```
$ ./main
```

or if you are on Windows:
```
$ ./main.exe
```
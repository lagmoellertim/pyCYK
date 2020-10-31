# pyCYK

1.  Details

2.  How to use pyCYK

3.  License

4.  Credits



## 1. Details

- pyCYK is an implementation of the [Cocke-Younger-Kasami-Algorithm](https://en.wikipedia.org/wiki/CYK_algorithm) in Python

- It is used to check if a string is part of a grammar

- The grammar has to be context-free and in the [Chomsky normal form](https://en.wikipedia.org/wiki/Chomsky_normal_form)



## 2. How to use pyCYK

### 2.1 Installation

First, you need to clone or download this repository. After that, open the folder and run this command:

```bash
pip3 install -r requirements.txt
```



## 2.2 Usage

To use pyCYK in your project, you first need to import it.

```python
from cyk import CYK
```

Then, you need to define a [startstate](https://en.wikipedia.org/wiki/Finite-state_machine#Start_state), the grammar and the word. This is an example for it:

```python
startstate = "S"

grammar = {
    startstate:["VaE","VbF"],
    "G":["GG","a","b","VaVb"],
    "E":["GVa","a"],
    "F":["GVb","b"],
    "Va":["a"],
    "Vb":["b"]
}

word = "abacba"
```

Next, you need to create an object of the pyCYK class, which includes the startstate and the grammar.

```python
cyk = CYK(grammar, startstate)
```

To check whether a word is part of the language or not, use this:

```python
cyk.checkWord(word) #Returns True or False
```

If you want to see the table that is generated as a part of this algorithm, use this:

```python
cyk.outputTable(word)
```



# 3. License

This implementation is published under the MIT License.

# 4. Credits

This implementation is developed by Tim-Luca Lagmöller.


# 5. Donations / Sponsors

I'm part of the official GitHub Sponsors program where you can support me on a monthly basis.

<a href="https://github.com/sponsors/lagmoellertim" target="_blank"><img src="https://github.com/lagmoellertim/shared-repo-files/raw/main/github-sponsors-button.png" alt="GitHub Sponsors" height="35px" ></a>

You can also contribute by buying me a coffee (this is a one-time donation).

<a href="https://ko-fi.com/lagmoellertim" target="_blank"><img src="https://github.com/lagmoellertim/shared-repo-files/raw/main/kofi-sponsors-button.png" alt="Ko-Fi Sponsors" height="35px" ></a>

Thank you for your support!



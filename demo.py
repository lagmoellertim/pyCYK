from cyk import CYK

startstate = "S"

grammar = {
    startstate:["VaE","VbF"],
    "G":["GG","a","b","VaVb"],
    "E":["GVa","a"],
    "F":["GVb","b"],
    "Va":["a"],
    "Vb":["b"]
}

cyk = CYK(grammar, startstate)

word = "abacba"

print(cyk.checkWord(word))

cyk.outputTable(word)
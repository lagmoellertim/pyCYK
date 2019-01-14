from tabulate import tabulate

class CYK:
    def __init__(self, grammar, startstate):
        self.grammar = grammar
        self.startstate = startstate

    def __getValidCombinations(self, left_collection_set, right_collection_set):
        valid_combinations = []
        for num_collection, left_collection in enumerate(left_collection_set):
            right_collection = right_collection_set[num_collection]
            for left_item in left_collection:
                for right_item in right_collection:
                    combination = left_item + right_item
                    for key, value in self.grammar.items():
                        if combination in value:
                            if not key in valid_combinations:
                                valid_combinations.append(key)
        return valid_combinations

    def __getCollectionSets(self, full_table, x_position, x_offset):
        table_segment = []
        y_position = 0
        while x_offset >= 2:
            item_set = full_table[y_position][x_position:x_position+x_offset]
            if x_offset > len(item_set):
                return None
            table_segment.append(item_set)
            x_offset -= 1
            y_position += 1
        vertical_combinations = []
        horizontal_combinations = []
        for item in table_segment:
            vertical_combinations.append(item[0])
            horizontal_combinations.append(item[-1])
        return vertical_combinations[::-1], horizontal_combinations
        
    def __generateTable(self, word):
        table = [[]]
        for letter in word:
            valid_states = []
            for key, value in self.grammar.items():
                if letter in value:
                    valid_states.append(key)
            table[0].append(valid_states)
        for x_offset in range(2,len(word)+1):
            table.append([])
            for x_position in range(len(word)):
                collection_sets = self.__getCollectionSets(table, x_position, x_offset)
                if collection_sets:
                    table[-1].append(self.__getValidCombinations(*collection_sets))
        
        return table
        
    def checkWord(self, word):
        return self.startstate in self.__generateTable(word)[-1][-1]
        
    def outputTable(self, word):
        table = self.__generateTable(word)
        pretty_table = [
            [
                ",".join(sorted(y)) if y != [] else u"\u2205" for y in x
            ] for x in table
        ]
        
        print(tabulate(pretty_table, list(word), tablefmt="grid"))
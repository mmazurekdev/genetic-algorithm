from genetic_library import GeneticAlgorithm, Element
from genetic_library.selection_models import elite_selection_model

from random import randint, choice

TARGET = "Czesc, tu Mateusz z mmazurek.dev :D"


class Text(Element):
    POSSIBILITIES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

    def __init__(self, text):
        self.text = text
        super().__init__()

    def _perform_mutation(self):
        random_index = randint(0, len(self.text) - 1)
        text_as_list = list(self.text)
        text_as_list[random_index] = choice(self.POSSIBILITIES)
        self.text = "".join(text_as_list)

    def crossover(self, element2: 'Element' ) -> 'Element':
        length = int(randint(0, len(self.text) - 1))
        new_text = self.text[:length] + element2.text[length:]

        return Text(new_text)

    def evaluate_function(self):
        diff = 0
        for letter1, letter2 in zip(self.text, TARGET):
            if letter1 != letter2:
                diff += 1
        return diff

    def __repr__(self):
        return self.text


def first_population_generator():
    return [Text(''.join(choice(Text.POSSIBILITIES) for _ in range(len(TARGET)))) for _ in range(100)]


def stop_condition(string, current_fitness, i):
    return current_fitness == 0


ga = GeneticAlgorithm(first_population_generator, elite_selection_model, stop_condition)
ga.run()

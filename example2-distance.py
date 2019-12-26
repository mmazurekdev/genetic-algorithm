from genetic_library import GeneticAlgorithm, Element
from genetic_library.selection_models import elite_selection_model

from random import randint, sample
from math import sqrt

START_POINT = [(1, 1)]
END_POINT = [(1, 1)]
# POINTS = [(randint(0, 40), randint(0, 40)) for k in range(50)]
POINTS = [(3, 4), (11, 5), (27, 23), (27, 25), (22, 32), (24, 34), (19, 38), (17, 37), (7, 40), (8, 36),
          (8, 28), (16, 21), (14, 17), (25, 11), (24, 19), (32, 26), (29, 34), (27, 34), (38, 36), (35, 12), (33, 8),
          (31, 2), (24, 5), (23, 3), (17, 3), (16, 3), (24, 11), (21, 21), (23, 21), (17, 10), (19, 7), (33, 14),
          (38, 18), (34, 19), (20, 30), (9, 38), (6, 27), (7, 12), (3, 15), (0, 24), (5, 30), (3, 33), (4, 33),
          (6, 28), (7, 6), (4, 4), (2, 10), (2, 23), (8, 20)]


class Route(Element):
    def __init__(self, points):
        self.points = points
        super().__init__()

    def _perform_mutation(self):
        first = randint(1, len(self.points) - 2)
        second = randint(1, len(self.points) - 2)

        self.points[first], self.points[second] = self.points[second], self.points[first]

    def crossover(self, element2: 'Element') -> 'Element':
        child_points = self.points[1:int(len(self.points) / 2)]
        for point in element2.points:
            if point not in child_points and point not in END_POINT + START_POINT:
                child_points.append(point)

            if len(child_points) == len(element2.points):
                break
        return Route(START_POINT + child_points + END_POINT)

    def evaluate_function(self):
        def _calculate_distance(x1, x2, y1, y2):
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        sum = 0
        for i, p in enumerate(self.points):
            if i + 1 > len(self.points) - 1:
                break
            next_point = self.points[i + 1]
            sum += _calculate_distance(p[0], next_point[0], p[1], next_point[1])

        return sum

    def __repr__(self):
        return str(self.points)


def first_generation_generator():
    return [Route(START_POINT + sample(POINTS, len(POINTS)) + END_POINT) for _ in range(100)]


def stop_condition(string, current_fitness, i):
    return i == 3000


ga = GeneticAlgorithm(first_generation_generator, elite_selection_model, stop_condition)
ga.run()

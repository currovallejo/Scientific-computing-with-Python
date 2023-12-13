import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
pepe= prob_calculator.Hat(blue=4, red=2, green=6)
# print(pepe.colors)
# print(pepe.draw(35))
# print(pepe.draw(3))
# print(pepe.draw(3))
# print(pepe.draw(3))
# print(pepe.draw(3))



probability = prob_calculator.experiment(
    hat=pepe,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
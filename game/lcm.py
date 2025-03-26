import random
import math

RULES = "Find the smallest common multiple of given numbers."

def generate_round():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    correct_answer = str(math.lcm(*numbers))
    return question, correct_answer

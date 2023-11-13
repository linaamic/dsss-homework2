import unittest
from math_quiz import random_int, random_math_operation, generate_problem_and_answer


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_math_operation(self):
        random_operation = random_math_operation()
        # Test if operator returns either +, - or *
        self.assertTrue(random_operation == "*" or random_operation == "+" or random_operation == "-")
        # Test if operator is of type str
        self.assertTrue(type(random_operation) == str)
        

    def test_generate_problem_and_answer(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (1, 4, '*', '1 * 4', 4),
                (2, 4, '*', '2 * 4', 8),
                (5, 5, '*', '5 * 5', 25),
                (3, 6, '-', '3 - 6', -3),
                (6, 3, '-', '6 - 3', 3),
            ]
            # for all test cases check whether problem and answer are as expected
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_problem_and_answer(num1, num2, operator)
                self.assertTrue(problem == expected_problem)
                self.assertTrue(answer == expected_answer)
                

if __name__ == "__main__":
    unittest.main()

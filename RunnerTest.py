import unittest
import test_12_1


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = test_12_1.Runner('Олег')
        for walk in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = test_12_1.Runner('Ольга')
        for run in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_3 = test_12_1.Runner('Олеся')
        for walk in range(10):
            runner_3.walk()
        runner_4 = test_12_1.Runner('Олаф')
        for run in range(10):
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

if __name__ == '__main__':
    unittest.main()

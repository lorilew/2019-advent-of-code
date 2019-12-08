import unittest

from solutions.day_6 import _count_helper, count_orbits, read_orbits, sol_6, sol_6_b


class MyTestCase(unittest.TestCase):
    def test_sol_6(self):
        with open("../../resources/input_6.txt", "r") as f:
            data_str = f.read()
            result = sol_6(data_str)
            self.assertEqual(147223, result)

    def test_sol_6_mini(self):
        data = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
        result = sol_6(data)
        self.assertEqual(42, result)

    def test_read_orbits(self):
        data = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
        orbit_tree = {
            "B": "COM",
            "C": "B",
            "D": "C",
            "E": "D",
            "F": "E",
            "G": "B",
            "H": "G",
            "I": "D",
            "J": "E",
            "K": "J",
            "L": "K",
        }
        result = read_orbits(data)
        self.assertDictEqual(orbit_tree, result)

    def test_count_orbits_longer(self):
        orbit_tree = {
            "B": "COM",
            "C": "B",
            "D": "C",
            "E": "D",
            "F": "E",
            "G": "B",
            "H": "G",
            "I": "D",
            "J": "E",
            "K": "J",
            "L": "K",
        }
        result = count_orbits(orbit_tree)
        self.assertEqual(42, result)

    def test_count_orbits(self):
        data = {"B": "COM", "C": "B", "D": "C"}
        result = count_orbits(data)
        self.assertEqual(6, result)

    def test_count_helper(self):
        data = {"B": "COM", "C": "B", "D": "C"}
        result = _count_helper(data, "D")
        self.assertEqual(3, result)

    def test_sol_6_mini(self):
        data = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN"
        result = sol_6_b(data)
        self.assertEqual(4, result)

    def test_sol_6_proper(self):
        with open("../../resources/input_6_b.txt", "r") as f:
            data_str = f.read()
            result = sol_6_b(data_str)
            self.assertEqual(340, result)


if __name__ == "__main__":
    unittest.main()

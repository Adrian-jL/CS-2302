import unittest
import project_seven

class Testp7(unittest.TestCase):
    
    def test_ed(self):
        self.assertEqual(project_seven.edit_Distance("tape", "hat", 4, 3) , 3)
        self.assertEqual(project_seven.edit_Distance("money", "miner", 5, 5) , 2)
        self.assertEqual(project_seven.edit_Distance(" ", " ", 0, 0) , 0)
        self.assertEqual(project_seven.edit_Distance("a", " ", 1, 0) , 1)
        self.assertEqual(project_seven.edit_Distance("abc", " ", 3, 0) , 3)

if __name__ == "__main__":
    unittest.main()
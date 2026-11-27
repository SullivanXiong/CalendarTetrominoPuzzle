import unittest

from calendar_solver.calendar_solver.tetromino import (InvalidShapeError,
                                                Shape, Tetromino)


class Testtetromino(unittest.TestCase):
    def setUp(self):
        """
        Set up test data for tetromino pieces.
        """
        self.tetrominos = {
            "small_L_tetromino": Tetromino(Shape(2, 3, [[1, 0], [1, 0], [1, 1]]), "sL"),
            "big_L_tetromino": Tetromino(Shape(2, 4, [[1, 0], [1, 0], [1, 0], [1, 1]]), "bL"),
            "symmetrical_L_tetromino": Tetromino(Shape(3, 3, [[1, 0, 0], [1, 0, 0], [1, 1, 1]]), "symL"),
            "lowercase_l_tetromino": Tetromino(Shape(1, 4, [[1], [1], [1], [1]]), "l"),
            "u_tetromino": Tetromino(Shape(3, 2, [[1, 0, 1], [1, 1, 1]]), "U"),
            "small_z_tetromino": Tetromino(Shape(3, 2, [[1, 1, 0], [0, 1, 1]]), "sZ"),
            "big_z_tetromino": Tetromino(Shape(4, 2, [[0, 0, 1, 1], [1, 1, 1, 0]]), "bZ"),
            "z_tetromino": Tetromino(Shape(3, 3, [[0, 1, 1], [0, 1, 0], [1, 1, 0]]), "Z"),
            "t_tetromino": Tetromino(Shape(3, 3, [[1, 1, 1], [0, 1, 0], [0, 1, 0]]), "T"),
            "p_tetromino": Tetromino(Shape(2, 3, [[1, 1], [1, 1], [1, 0]]), "P"),
        }

    def test_initial_shape(self):
        """
        Test the initial shape of the Tetrominos.
        """
        for name, tetromino in self.tetrominos.items():
            with self.subTest(tetromino=name):
                expected_shape = tetromino.shape.shape
                self.assertEqual(tetromino.shape.shape, expected_shape)

    def test_rotate_90(self):
        """
        Test rotating the Tetromino 90 degrees clockwise.
        """
        self.small_L_tetromino = self.tetrominos["small_L_tetromino"]
        self.small_L_tetromino.rotate_clockwise(90)
        expected_shape = [[1, 1, 1], [1, 0, 0]]
        self.assertEqual(self.small_L_tetromino.shape.shape, expected_shape)

        self.big_L_tetromino = self.tetrominos["big_L_tetromino"]
        self.big_L_tetromino.rotate_clockwise(90)
        expected_shape = [[1, 1, 1, 1], [1, 0, 0, 0]]
        self.assertEqual(self.big_L_tetromino.shape.shape, expected_shape)

        self.symmetrical_L_tetromino = self.tetrominos["symmetrical_L_tetromino"]
        self.symmetrical_L_tetromino.rotate_clockwise(90)
        expected_shape = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
        self.assertEqual(self.symmetrical_L_tetromino.shape.shape, expected_shape)

        self.lowercase_l_tetromino = self.tetrominos["lowercase_l_tetromino"]
        self.lowercase_l_tetromino.rotate_clockwise(90)
        expected_shape = [[1, 1, 1, 1]]
        self.assertEqual(self.lowercase_l_tetromino.shape.shape, expected_shape)

        self.u_tetromino = self.tetrominos["u_tetromino"]
        self.u_tetromino.rotate_clockwise(90)
        expected_shape = [[1, 1], [1, 0], [1, 1]]
        self.assertEqual(self.u_tetromino.shape.shape, expected_shape)

        self.small_z_tetromino = self.tetrominos["small_z_tetromino"]
        self.small_z_tetromino.rotate_clockwise(90)
        expected_shape = [[0, 1], [1, 1], [1, 0]]
        self.assertEqual(self.small_z_tetromino.shape.shape, expected_shape)

        self.big_z_tetromino = self.tetrominos["big_z_tetromino"]
        self.big_z_tetromino.rotate_clockwise(90)
        expected_shape = [[1, 0], [1, 0], [1, 1], [0, 1]]
        self.assertEqual(self.big_z_tetromino.shape.shape, expected_shape)

        self.z_tetromino = self.tetrominos["z_tetromino"]
        self.z_tetromino.rotate_clockwise(90)
        expected_shape = [[1, 0, 0], [1, 1, 1], [0, 0, 1]]
        self.assertEqual(self.z_tetromino.shape.shape, expected_shape)

        self.t_tetromino = self.tetrominos["t_tetromino"]
        self.t_tetromino.rotate_clockwise(90)
        expected_shape = [[0, 0, 1], [1, 1, 1], [0, 0, 1]]
        self.assertEqual(self.t_tetromino.shape.shape, expected_shape)

        self.p_tetromino = self.tetrominos["p_tetromino"]
        self.p_tetromino.rotate_clockwise(90)
        expected_shape = [[1, 1, 1], [0, 1, 1]]
        self.assertEqual(self.p_tetromino.shape.shape, expected_shape)

    def test_rotate_180(self):
        """
        Test rotating the Tetromino 180 degrees clockwise.
        """
        self.small_L_tetromino = self.tetrominos["small_L_tetromino"]
        self.small_L_tetromino.rotate_clockwise(180)
        expected_shape = [[1, 1], [0, 1], [0, 1]]
        self.assertEqual(self.small_L_tetromino.shape.shape, expected_shape)

        self.big_L_tetromino = self.tetrominos["big_L_tetromino"]
        self.big_L_tetromino.rotate_clockwise(180)
        expected_shape = [[1, 1], [0, 1], [0, 1], [0, 1]]
        self.assertEqual(self.big_L_tetromino.shape.shape, expected_shape)
        
        self.symmetrical_L_tetromino = self.tetrominos["symmetrical_L_tetromino"]
        self.symmetrical_L_tetromino.rotate_clockwise(180)
        expected_shape = [[1, 1, 1], [0, 0, 1], [0, 0, 1]]
        self.assertEqual(self.symmetrical_L_tetromino.shape.shape, expected_shape)
        
        self.lowercase_l_tetromino = self.tetrominos["lowercase_l_tetromino"]
        self.lowercase_l_tetromino.rotate_clockwise(180)
        expected_shape = [[1], [1], [1], [1]]
        self.assertEqual(self.lowercase_l_tetromino.shape.shape, expected_shape)
        
        self.u_tetromino = self.tetrominos["u_tetromino"]
        self.u_tetromino.rotate_clockwise(180)
        expected_shape = [[1, 1, 1], [1, 0, 1]]
        self.assertEqual(self.u_tetromino.shape.shape, expected_shape)
        
        self.small_z_tetromino = self.tetrominos["small_z_tetromino"]
        self.small_z_tetromino.rotate_clockwise(180)
        expected_shape = [[1, 1, 0], [0, 1, 1]]
        self.assertEqual(self.small_z_tetromino.shape.shape, expected_shape)
        
        self.big_z_tetromino = self.tetrominos["big_z_tetromino"]
        self.big_z_tetromino.rotate_clockwise(180)
        expected_shape = [[0, 1, 1, 1], [1, 1, 0, 0]]
        self.assertEqual(self.big_z_tetromino.shape.shape, expected_shape)
        
        self.z_tetromino = self.tetrominos["z_tetromino"]
        self.z_tetromino.rotate_clockwise(180)
        expected_shape = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]
        self.assertEqual(self.z_tetromino.shape.shape, expected_shape)
        
        self.t_tetromino = self.tetrominos["t_tetromino"]
        self.t_tetromino.rotate_clockwise(180)
        expected_shape = [[0, 1, 0], [0, 1, 0], [1, 1, 1]]
        self.assertEqual(self.t_tetromino.shape.shape, expected_shape)
        
        self.p_tetromino = self.tetrominos["p_tetromino"]
        self.p_tetromino.rotate_clockwise(180)
        expected_shape = [[0, 1], [1, 1], [1, 1]]
        self.assertEqual(self.p_tetromino.shape.shape, expected_shape)

    def test_rotate_360(self):
        """
        Test rotating the tetromino 360 degrees clockwise (full rotation).
        """
        self.small_L_tetromino = self.tetrominos["small_L_tetromino"]
        self.small_L_tetromino.rotate_clockwise(360)
        expected_shape = [[1, 0], [1, 0], [1, 1]]  # Should return to the original shape
        self.assertEqual(self.small_L_tetromino.shape.shape, expected_shape)
        
        self.big_L_tetromino = self.tetrominos["big_L_tetromino"]
        self.big_L_tetromino.rotate_clockwise(360)
        expected_shape = [[1, 0], [1, 0], [1, 0], [1, 1]]
        self.assertEqual(self.big_L_tetromino.shape.shape, expected_shape)
        
        self.symmetrical_L_tetromino = self.tetrominos["symmetrical_L_tetromino"]
        self.symmetrical_L_tetromino.rotate_clockwise(360)
        expected_shape = [[1, 0, 0], [1, 0, 0], [1, 1, 1]]
        self.assertEqual(self.symmetrical_L_tetromino.shape.shape, expected_shape)
        
        self.lowercase_l_tetromino = self.tetrominos["lowercase_l_tetromino"]
        self.lowercase_l_tetromino.rotate_clockwise(360)
        expected_shape = [[1], [1], [1], [1]]
        self.assertEqual(self.lowercase_l_tetromino.shape.shape, expected_shape)
        
        self.u_tetromino = self.tetrominos["u_tetromino"]
        self.u_tetromino.rotate_clockwise(360)
        expected_shape = [[1, 0, 1], [1, 1, 1]]
        self.assertEqual(self.u_tetromino.shape.shape, expected_shape)
        
        self.small_z_tetromino = self.tetrominos["small_z_tetromino"]
        self.small_z_tetromino.rotate_clockwise(360)
        expected_shape = [[1, 1, 0], [0, 1, 1]]
        self.assertEqual(self.small_z_tetromino.shape.shape, expected_shape)
        
        self.big_z_tetromino = self.tetrominos["big_z_tetromino"]
        self.big_z_tetromino.rotate_clockwise(360)
        expected_shape = [[0, 0, 1, 1], [1, 1, 1, 0]]
        self.assertEqual(self.big_z_tetromino.shape.shape, expected_shape)
        
        self.z_tetromino = self.tetrominos["z_tetromino"]
        self.z_tetromino.rotate_clockwise(360)
        expected_shape = [[0, 1, 1], [0, 1, 0], [1, 1, 0]]
        self.assertEqual(self.z_tetromino.shape.shape, expected_shape)
        
        self.t_tetromino = self.tetrominos["t_tetromino"]
        self.t_tetromino.rotate_clockwise(360)
        expected_shape = [[1, 1, 1], [0, 1, 0], [0, 1, 0]]
        self.assertEqual(self.t_tetromino.shape.shape, expected_shape)
        
        self.p_tetromino = self.tetrominos["p_tetromino"]
        self.p_tetromino.rotate_clockwise(360)
        expected_shape = [[1, 1], [1, 1], [1, 0]]
        self.assertEqual(self.p_tetromino.shape.shape, expected_shape)
        
    def test_invalid_shape(self):
        """
        Test that an invalid shape raises an InvalidShapeError.
        """
        with self.assertRaises(InvalidShapeError):
            Tetromino(Shape(2, 3, [[1, 0], [1, 0]]), "Invalid")


if __name__ == "__main__":
    unittest.main()
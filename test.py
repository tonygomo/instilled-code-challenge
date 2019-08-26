import unittest

from main import InvalidInputError, parse_fragments, calculate_uvt

class TestParseFragments(unittest.TestCase):
    def test_parse_strings(self):
        """It should parse correctly formatted strings."""
        parsed = parse_fragments('0-1000', '1500-2000')
        self.assertEqual(parsed, [(0, 1000), (1500, 2000)])
    
    def test_invalid_input(self):
        """It should raise an exception if input is invalid."""
        with self.assertRaises(InvalidInputError):
            parse_fragments('0-1000', '1500-twoThousand')


class TestCalculateUvt(unittest.TestCase):
    def test_addition(self):
        """It should add together all given fragments."""
        uvt = calculate_uvt((0, 1000), (1000, 2000), (2000, 3000))
        self.assertEqual(uvt, 3000)
    
    def test_unsorted(self):
        """It should handle fragments being passed out-of-order."""
        uvt = calculate_uvt((1000, 2000), (2000, 3000), (0, 1000))
        self.assertEqual(uvt, 3000)
    
    def test_overlaps(self):
        """It should handle overlapping fragments without double counting."""
        uvt = calculate_uvt((0, 1000), (1000, 2000), (1500, 3000))
        self.assertEqual(uvt, 3000)
    
    def test_non_contiguous_fragments(self):
        """It should handle non-contiguous fragments."""
        uvt = calculate_uvt((0, 1000), (2000, 2500), (3000, 4000))
        self.assertEqual(uvt, 2500)
    
    def test_duplicates(self):
        """It should not double count duplicate fragments."""
        uvt = calculate_uvt((0, 1000), (0, 1000))
        self.assertEqual(uvt, 1000)
    
    def test_contained_fragments(self):
        """It should handle fragments contained within other fragments."""
        uvt = calculate_uvt((0, 1000), (200, 800))
        self.assertEqual(uvt, 1000)


if __name__ == '__main__':
    unittest.main()
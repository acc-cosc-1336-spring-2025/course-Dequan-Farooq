import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        sequence1 = "GAGCCTACTAACGGGAT"
        sequence2 = "CATCGTAATGACGGCCT"
        expected_distance = 7
        actual_distance = get_hamming_distance(sequence1, sequence2)

        self.assertEqual(actual_distance, expected_distance)

    def test_get_dna_complement(self):
        dna_sequence = "AAAACCCGGT"
        expected_complement = "TTTTGGGCCA"

        actual_complement = get_dna_complement(dna_sequence)

        self.assertEqual(actual_complement, expected_complement)


if __name__ == '__main__':
    unittest.main()



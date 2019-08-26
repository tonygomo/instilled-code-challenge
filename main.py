import re
import sys

class InvalidInputError(Exception):
    pass

def calculate_uvt(*args):
    """
    Calculates the UVT of the given fragments.
    Takes any number of fragments as integer tuples.
    Returns the UVT as an integer.

    Eg.
    calculate_uvt((0, 1000), (1000, 2000))
    2000
    """
    fragments = sorted(args, key = lambda x: x[0])
    total = previous = 0
    for fragment in fragments:
        start, finish = fragment # Expands fragment tuple to separate vars
        if finish > previous: # Avoids double counting
            total += finish - max(previous, start) # Handles overlaps
            previous = finish
    return total

def parse_fragments(*args):
    """
    Parses string fragments to a list of integer tuples.
    If any of the args don't match the expected format,
    raises an InvalidInputError.

    Eg.
    parse_fragments('0-1000','1000-2000')
    [(0, 1000), (1000, 2000)]
    """
    parsed = []
    for arg in args:
        if not re.match(r'^\d+-\d+$', arg):
            raise InvalidInputError()

        # The split() method returns a list,
        # map() converts each list entry to ints,
        # then tuple() converts map obj to a tuple.
        parsed.append(tuple(map(int, arg.split('-'))))

    return parsed


if __name__ == '__main__':
    try:
        fragments = parse_fragments(*sys.argv[1:])
    except InvalidInputError:
        print('Usage: python main.py 0-1000 2000-3000 2500-4000')
    else:
        total = calculate_uvt(*fragments)
        print(total)
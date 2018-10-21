def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Different strand lengths!')
    return sum(map(lambda x, y: x != y, strand_a, strand_b))

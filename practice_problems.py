"""Coding practice problems"""

def count_appearances(elements):
    element_counts_map = {}
    for element in elements:
        if element in element_counts_map:
            element_counts_map[element] += 1
        else:
            element_counts_map[element] = 1
    return element_counts_map

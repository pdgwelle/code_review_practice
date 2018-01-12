"""Coding practice problems"""

def count_appearances(elements):
    element_counts_map = {}
    for element in elements:
        element_counts_map[element] = element_counts_map.get(element, 0) + 1
    return element_counts_map

## Some miscellaneous comments that I think we should delete
## Blah Blah Blah
## Blah blah blah

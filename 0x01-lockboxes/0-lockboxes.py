#!/usr/bin/python3

"""
A Lockbox tasks that determine if boxes can unlock
"""


def canUnlockAll(boxes):

    """ Determines if all box can be unlock with keys in boxes
    Returns
        True if all boxes can be unlock else false.
    """
    visited = set()
    queue = [0]

    visited.add(0)
    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]
        for key in keys:
            if key < len(boxes) and key not in visited:
                visited.add(key)
                queue.append(key)
    return len(visited) == len(boxes)

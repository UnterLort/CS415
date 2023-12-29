# @Kyle Stewart @queue.py version 1

def enqueue(list, item):
    # Add an item to the list
    list.append(item)


def dequeue(list):
    # Check if list is empty
    if len(list) == 0:
        # If list is empty return None
        return None
    # If list is not, remove the first item in the list
    return list.pop(0)

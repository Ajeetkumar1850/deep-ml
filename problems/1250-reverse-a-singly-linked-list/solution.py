
def reverse_linked_list(values, method="iterative"):
    if method == "iterative":
        return values[::-1]

    elif method == "recursive":
        def reverse(items):
            if len(items) <= 1:
                return items
            return reverse(items[1:]) + [items[0]]

        return reverse(values)

    else:
        raise ValueError("method must be 'iterative' or 'recursive'")

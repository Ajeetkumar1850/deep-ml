def process_operations(operations):
    queue_in = []
    queue_out = []

    stack = []
    min_stack = []

    result = []

    for op in operations:
        command = op[0]

        if command == "enqueue":
            queue_in.append(op[1])

        elif command == "dequeue":
            if not queue_out:
                while queue_in:
                    queue_out.append(queue_in.pop())

            result.append(queue_out.pop())

        elif command == "mpush":
            val = op[1]
            stack.append(val)

            if not min_stack:
                min_stack.append(val)
            else:
                min_stack.append(min(val, min_stack[-1]))

        elif command == "mpop":
            min_stack.pop()
            result.append(stack.pop())

        elif command == "mtop":
            result.append(stack[-1])

        elif command == "mmin":
            result.append(min_stack[-1])

    return result
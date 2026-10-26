
def ledger(operations):
    grants = []
    results = []

    for op in operations:
        if op[0] == "add":
            _, credits, expiry = op
            grants.append([credits, expiry])

        elif op[0] == "charge":
            _, amount, time = op
            consumed = 0

            # Earliest expiry first; stable order breaks ties.
            order = sorted(
                range(len(grants)),
                key=lambda i: grants[i][1]
            )

            for i in order:
                credits, expiry = grants[i]

                if expiry > time and amount > 0:
                    take = min(credits, amount)
                    grants[i][0] -= take
                    amount -= take
                    consumed += take

            results.append(consumed)

        elif op[0] == "balance":
            _, time = op
            total = sum(
                credits
                for credits, expiry in grants
                if expiry > time
            )
            results.append(total)

    return results

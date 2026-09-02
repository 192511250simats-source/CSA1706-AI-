# Alpha-Beta Pruning

def alphabeta(depth, node_index, maximizing, values, alpha, beta):
    if depth == 0:
        return values[node_index]

    if maximizing:
        best = -1000

        for i in range(2):
            value = alphabeta(
                depth - 1,
                node_index * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        for i in range(2):
            value = alphabeta(
                depth - 1,
                node_index * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alphabeta(3, 0, True, values, -1000, 1000)

print("Optimal value:", result)

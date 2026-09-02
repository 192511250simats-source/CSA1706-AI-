# Minimax Algorithm for Tic Tac Toe

def minimax(depth, is_maximizing, scores):
    if depth == 0:
        return scores[0]

    if is_maximizing:
        best = -1000

        for score in scores:
            value = minimax(depth - 1, False, [score])
            best = max(best, value)

        return best

    else:
        best = 1000

        for score in scores:
            value = minimax(depth - 1, True, [score])
            best = min(best, value)

        return best


scores = [3, 5, 2, 9]

best_score = minimax(2, True, scores)

print("Best score using Minimax:", best_score)

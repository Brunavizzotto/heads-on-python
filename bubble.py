scores = [60, 70, 80, 90, 10, 55, 20, 21, 44, 56, 57, 48, 14, 74]

high_scores = 0

lenght = len(scores)

for i in range(lenght):
    print("bubble solution #" + str(i), 'score', scores[i])
    if scores[i] > high_scores:
        high_scores = scores[i]

print('bubbles test:' + str(lenght))
print('highest score:' + str(high_scores))

best_solutions = []

for i in range(lenght):
    if high_scores == scores[i]:
        best_solutions.append(i)

print('best solution #' + str(best_solutions) + ' score:' + str(high_scores))

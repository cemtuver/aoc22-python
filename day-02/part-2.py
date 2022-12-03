with open("input.txt") as f:
    lines = f.read().split("\n")

score_rock = 1
score_paper = 2
score_scissors = 3
score_win = 6
score_draw = 3
score_lose = 0
score_dict = {
    "A X": score_scissors + score_lose,
    "A Y": score_rock + score_draw,
    "A Z": score_paper + score_win,
    "B X": score_rock + score_lose,
    "B Y": score_paper + score_draw,
    "B Z": score_scissors + score_win,
    "C X": score_paper + score_lose,
    "C Y": score_scissors + score_draw,
    "C Z": score_rock + score_win,
}

total_score = 0
for line in lines:
    total_score += score_dict[line]

print(total_score)

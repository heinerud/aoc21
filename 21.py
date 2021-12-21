import functools
import itertools


def part1(p1, p2):
    def move(player, x):
        new_position = (player[0] + x - 1) % 10 + 1
        return new_position, player[1] + new_position

    def roll_dice():
        for n in itertools.cycle(range(1, 101)):
            yield n

    dice = roll_dice()
    rolls = 0
    while True:
        score = sum(next(dice) for _ in range(3))
        rolls += 3
        p1 = move(p1, score)
        if p1[1] >= 1000:
            break

        score = sum(next(dice) for _ in range(3))
        rolls += 3
        p2 = move(p2, score)
        if p2[1] >= 1000:
            break

    ans = rolls * min(p1[1], p2[1])
    print(ans)
    assert ans == 989352


# Heavily inspired by William Y. Feng's YouTube video
# https://youtu.be/tEPgMuqZZGE
def part2(p1, p2):
    ways_to_score = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    def backtrack(p, n):
        return (p - n - 1) % 10 + 1

    @functools.cache
    def ways_to_score_given(pos, score, turn, initial_pos):
        if turn == 0:
            return 1 if (score == 0 and pos == initial_pos) else 0

        if score <= 0:
            return 0

        if score - pos >= 21:
            return 0

        ways = 0
        for s in ways_to_score:
            previous_pos = backtrack(pos, s)
            previous_score = score - pos
            ways += ways_to_score[s] * ways_to_score_given(
                previous_pos, previous_score, turn - 1, initial_pos
            )

        return ways

    def wins(pos, other_pos, is_p1):
        num_wins = 0
        # Turns is guessed
        for end_pos_win, end_pos_lose, score_win, score_lose, turn in itertools.product(
            range(1, 11), range(1, 11), range(21, 31), range(21), range(20)
        ):
            num_wins += ways_to_score_given(
                end_pos_win, score_win, turn, pos
            ) * ways_to_score_given(end_pos_lose, score_lose, turn - is_p1, other_pos)

        return num_wins

    p1_wins = wins(p1, p2, True)
    p2_wins = wins(p2, p1, False)
    max_wins = max(p1_wins, p2_wins)
    print(max_wins)
    assert max_wins == 430229563871565


if __name__ == "__main__":
    with open("./21.in") as f:
        lines = f.read().splitlines()

    p1, p2 = (int(x.split(": ")[1]) for x in lines)
    part1((p1, 0), (p2, 0))
    part2(p1, p2)

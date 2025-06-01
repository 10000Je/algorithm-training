def stone_game(n, cur_player=True, memo={}):
    if n == 1 or n == 3:
        return not cur_player
    if n == 2:
        return cur_player
    if (n-1, not cur_player) not in memo:
        memo[(n-1, not cur_player)] = stone_game(n-1, not cur_player, memo)
    if (n-3, not cur_player) not in memo:
        memo[(n-3, not cur_player)] = stone_game(n-3, not cur_player, memo)
    if memo[(n-1, not cur_player)] != cur_player and memo[(n-3, not cur_player)] != cur_player:
        return not cur_player
    else:
        return cur_player

n = int(input())
print('SK' if stone_game(n) else 'CY')
def relationship_status(from_member, to_member, social_graph):
    from_follows = to_member in social_graph.get(from_member, {}).get("following", [])
    to_follows = from_member in social_graph.get(to_member, {}).get("following", [])
    if from_follows and to_follows:
        return "friends"
    elif from_follows:
        return "follower"
    elif to_follows:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    n = len(board)

    for i in range(n):
        first = board[i][0]
        if first and all(cell == first for cell in board[i]):
            return first

    for j in range(n):
        first = board[0][j]
        if first and all(board[i][j] == first for i in range(n)):
            return first

    first_diag = board[0][0]
    if first_diag and all(board[i][i] == first_diag for i in range(n)):
        return first_diag

    anti_diag_start = board[0][n - 1]
    if anti_diag_start and all(board[i][n - 1 - i] == anti_diag_start for i in range(n)):
        return anti_diag_start

    return "NO WINNER"


def eta(first_stop, second_stop, route_map):

    route = {start: (end, info['travel_time_mins']) for (start, end), info in route_map.items()}
    
    travel_time = 0
    current = first_stop
    
    while current != second_stop:
        next_stop, time = route[current]
        travel_time += time
        current = next_stop

    return travel_time

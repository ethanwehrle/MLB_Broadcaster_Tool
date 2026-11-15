import statsapi

# Find IDs for teams and players
statsapi.lookup_team('blue jays')        # Toronto's id is 141
statsapi.lookup_player('guerrero')

# Readable output, good for checking things
print(statsapi.standings())
pk = statsapi.last_game(141)
print(statsapi.boxscore(pk))
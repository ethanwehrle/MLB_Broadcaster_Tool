# Stats API is MLB API call. Not offically supported by MLB, use https://github.com/toddrob99/MLB-StatsAPI/wiki/Function:-get 
import statsapi
import json

#games = statsapi.schedule(date='2026-06-30')
#print(len(games))
#print(games[0])

sched = statsapi.get('schedule', {'sportId': 1, 'date': '2026-06-30'})
#print(sched.keys())
#print(sched['dates'])

with open('schedule.json', 'w') as f:
    json.dump(sched, f, indent=2)


feed = statsapi.get('game', {'gamePk': 745155})
print(feed.keys())
plays = feed['liveData']['plays']['allPlays']
print(len(plays))   # about 70-90: one per plate appearance

first = plays[0]
print(first['result']['event'])            # e.g. 'Flyout'
print(first['matchup']['batter']['fullName'])
print(first['matchup']['pitcher']['fullName'])
print(first['about']['inning'], first['about']['halfInning'])
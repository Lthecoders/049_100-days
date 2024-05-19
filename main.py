green = '\033[32m'

f = open("high.score", "r")

high_score = f.read().split()

f.close()
player_1_name = high_score[0]
player_1_score = high_score[1]

player_2_name = high_score[2]
player_2_score = high_score[3]

player_3_name = high_score[4]
player_3_score = high_score[5]

player_4_name = high_score[6]
player_4_score = high_score[7]

if int(player_1_score) > int(player_2_score) and int(player_1_score) > int(
    player_3_score) and int(player_1_score) > int(player_4_score):
  print(
      f'{green}\n\n{player_1_name} has higest score of {player_1_score} among all 4 players 😲'
  )

elif int(player_2_score) > int(player_1_score) and int(player_2_score) > int(
    player_3_score) and int(player_2_score) > int(player_4_score):
  print(
      f'{green}\n\n{player_2_name} has higest score of {player_2_score} among all 4 players 😲'
  )

elif int(player_3_score) > int(player_1_score) and int(player_3_score) > int(
    player_2_score) and int(player_3_score) > int(player_4_score):
  print(
      f'{green}\n\n{player_3_name} has higest score of {player_3_score} among all 4 players 😲'
  )

elif int(player_4_score) > int(player_1_score) and int(player_4_score) > int(
    player_2_score) and int(player_4_score) > int(player_3_score):
  print(
      f'{green}\n\n{player_4_name} has higest score of {player_4_score} among all 4 players 😲'
  )

# by doing this programe we come to know how to data from the file and work on it
# and present an new ouput on console

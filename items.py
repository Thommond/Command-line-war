

class Player_stats(object):

    player_stats = {
        intelligence: 10,
        strength: 0,
        luck:  0,
        charisma: 0,  # player can set personal stat's that will assist him with the game
        swiftness: 0,
        health: 100,
        gas_mask = 1,
        rifle = 1,
        rations = 10
    }

    def __init__(self):
        print('somthing')

    def check(self, player_stat, stat_name):
        self.player_stat = player_stat
        if player_stat = 'All':
            player_stats[intelligence] = 100
            player_stats[strength] = 100
            player_stats[swiftness] = 100
            player_stats[charisma] = 100
            player_stats[luck] = 100
            print('Your 100% bud!!!')

        elif:
            print(f'Alright {player_stat} will be added to {stat_name}')

        else:
            print("""The entered feild does not meet requirments. Your
            addition to your stat must be 5 or 10 nothing else.""")


class MachineGunnerBoss(object):
    def __init__(self):
        print('We need his health and death statement which will notify the completion of the level')

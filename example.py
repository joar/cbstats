#!/usr/bin/env python3
import cbstats, datetime
if __name__ == '__main__':
    stats = cbstats.CraftBukkitStats('/home/jwandborg/bukkit-1.3/')

#    print( stats.get_properties() )
#    print( stats.get_property('') )

    usageStats = stats.get_usage_stats()
    
    print('''# Server stats for mc.wandborg.se

Operators: {ops}

Online right now: {users_connected}

Average user session length: {average_session_length}
'''.format( 
            average_session_length = datetime.timedelta(
                seconds = int( usageStats['connectedAverage'] )
                ),
            timezone = 'UTC',
            ops = ', '.join( stats.get_operators() ),
            users_connected = ', '.join( stats.connected )
            )
        )
    
    print('# Toplist - Time online\n')
    for user, time in usageStats['timePerUser'].items():
        print('{time} {user}'.format(
                time = datetime.timedelta(
                    seconds = int( time )
                    ),
                user = user
                )
              )
        
    if not len( usageStats['timePerUser'] ):
        print('No users have connected yet')

    print('\n# Configuration\n')
    for key, value in stats.get_properties().items():
        print('{key}: {value}'.format(
                key = key,
                value = value
                )
              )

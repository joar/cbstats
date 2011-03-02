#!/usr/bin/python3
import re, time, datetime, collections

''' This contains things you can customise without basic knowledge of Python '''

''' The full path to CraftBukkit's server.log '''
file_server_log = "/home/jwandborg/bukkit-1.3/server.log"

''' You should not go further than this if you do not know what you are doing.
- And if you change something, make sure you backup this script, I've already lost this to a crash once. '''

f = open( file_server_log, encoding = "utf-8")
lines = f.read().splitlines()

connected = dict()
times = list()
out_log = list()

for line in lines:
    ''' Search for a line in the server log that matches the "connected" pattern '''
    match_connect = re.search('^(?P<date>[0-9-]+) (?P<time>[0-9:]+) (.*) (?P<user>\w+) \[/(?P<address>[0-9.:]+)\] logged', line)
    if match_connect:
        groups = match_connect.groups()
        
        out_log.append('{date} {time} {name} connected'.format( debug=groups, date=match_connect.group('date'), time=match_connect.group('time'), name=match_connect.group('user') ) )
        
        time_connect = time.strptime( match_connect.group('date') + ' ' + match_connect.group('time'), '%Y-%m-%d %H:%M:%S')
        connected[ match_connect.group('user') ] = time_connect

    ''' Search for a line in the server log that matches the "disconnected" pattern '''
    match_disconnect = re.search('^(?P<date>[0-9-]+) (?P<time>[0-9:]+) (.*) (?P<user>\w+) lost connection: disconnect\.(\w+)$', line)
    if match_disconnect:
        time_disconnect = time.strptime( match_disconnect.group('date') + ' ' + match_disconnect.group('time'), '%Y-%m-%d %H:%M:%S')
        delta = ( time.mktime( time_disconnect ) -time.mktime(  connected[ match_disconnect.group('user') ] ) )
        delta_format = datetime.timedelta( seconds=int(delta) )
        out_log.append('{date} {time} {name} disconnected ({delta})'.format( date=match_disconnect.group('date'), time=match_disconnect.group('time'), name=match_disconnect.group('user'), delta=delta_format ) )
        times.append( {'user': match_disconnect.group('user'), 'time': delta } )

connected_time_total = float()
connected_time_total_discarded = 0
connected_time_per_user = dict()

for connected_time in times:
    ''' Sum up times for all users, filter out really short connects '''
    if connected_time['time'] > 120:
        connected_time_total += connected_time['time']
    else:
        connected_time_total_discarded += 1
        
    ''' Collect total time, segment per user '''
    if not connected_time['user'] in connected_time_per_user:
        connected_time_per_user[ connected_time['user'] ] = connected_time['time']
    else:
        connected_time_per_user[ connected_time['user'] ] += connected_time['time']

''' Calculate average logged on time based on overall total logged on time and number of log ons '''
connected_time_average = datetime.timedelta( seconds=int( connected_time_total / ( len( times ) - connected_time_total_discarded ) ) )

''' Order times per user to be sorted as a high-score list '''
connected_time_per_user = collections.OrderedDict(
    sorted( 
        connected_time_per_user.items(), 
        key = lambda t: t[1],
        reverse = True
        )
    )


if __name__ == '__main__':
#    print( dict( connected_time_per_user ) )
    print('''# Server stats for mc.wandborg.se

Times are expressed in {timezone}
Average user session length: {average_session_length}
'''.format( 
            average_session_length=connected_time_average, 
            timezone='UTC'
#            timezone=time.tzname[0] + '/' + time.tzname[1]
            )
        )
    
    for user, time in connected_time_per_user.items():
        print('{time} {user}'.format(
                time = datetime.timedelta(
                    seconds = int( time )
                    ),
                user = user
                )
              )

    ''' Place the most recent log entries at top '''
    ''' Disabled for the time being
    out_log.reverse()
    
    for line in out_log:
        print( line )
    '''

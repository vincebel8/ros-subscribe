import roslibpy

ROS_HOST='192.168.50.27' # MKZ IP
ROS_PORT=9090 # Rosbridge port

def run():
    client = roslibpy.Ros(host=ROS_HOST, port=ROS_PORT)
    client.run()
    while client.is_connected:
       gps_sub = roslibpy.Topic(client, '/gps/fix', 'sensor_msgs/NavSatFix')
       gps_sub.subscribe(callback)

def callback(data):
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)

    print('longitude: ' + str(data['longitude']) + ' latitude: ' + str(data['latitude'])+' Date_time: ' + str(datetime_NY))

run()

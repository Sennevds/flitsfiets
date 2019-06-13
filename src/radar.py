#!/usr/local/bin/python3.6

import json
from ops241.radar import OPS241Radar
from ops241.radar import Command
import time
import mysql.connector
import time
import config

start_millis = -1
end_millis = -1
top_speed = -1
current_milli_time = lambda: int(round(time.time() * 1000))

start = current_milli_time()
mydb = mysql.connector.connect(
  host= config.host,
  user= config.username,
  passwd= config.password,
  database= config.database
)
mycursor = mydb.cursor()
sql = "INSERT INTO speed (speed, too_fast) VALUES (%s, %s)"



with OPS241Radar() as radar:
    print(radar.get_module_information())
    data = radar.read()
    while True:
        data = radar.read()
        if len(data) > 0:
            try:
                data1 = json.loads(data)
                if 'speed' in data1:
                    kph = float(data1['speed'])
                    if kph < 0:
                        kph = -kph
                    if kph != 0.0:
                        if start_millis == -1:
                            start_millis = current_milli_time()
                            end_millis = start_millis + 90.0 / kph
                            top_speed = kph
                        else:
                            if kph > top_speed:
                                end_millis = start_millis + 90.0 / kph
                                top_speed = kph
                        print( current_milli_time())
                        print( kph )
                        print( current_milli_time() + 90000.0 / kph )
            except Exception as e:
                print(f"Something went wrong: {e}")

        if end_millis != -1 and end_millis < current_milli_time():
            print( "Report: " )
            print( top_speed )
            print( "kph" )
            if top_speed > 30:
                val = (top_speed, 1)
            else:
                val = (top_speed, 0)
            mycursor.execute(sql, val)
            mydb.commit()

            start_millis = -1
            end_millis = -1
            top_speed = -1

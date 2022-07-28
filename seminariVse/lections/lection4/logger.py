from datetime import datetime as dt

def temperature_loger(data):
    time = dt.now().strftime('%H:%M')
    with open('loger.csv', 'a') as file:
        file.write('{}; temperature; {}\n'
                    .format(time, data))

def pressure_loger(data):
    time = dt.now().strftime('%H:%M')
    with open('loger.csv', 'a') as file:
        file.write('{}; pressure; {}\n'
                    .format(time, data))

def wind_speed_loger(data):
    time = dt.now().strftime('%H:%M')
    with open('loger.csv', 'a') as file:
        file.write('{}; wind_speed; {}\n'
                    .format(time, data))
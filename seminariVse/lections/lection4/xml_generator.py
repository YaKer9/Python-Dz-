from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view

def create(device = 1):
    xml = '<xml>\n'
    xml += '     <temperature units = "c">{}</temperature>\n'\
        .format(temperature_view(device))
    xml += '     <wind_speed_view units = "c">{}</temperature>\n'\
        .format(wind_speed_view(device))
    xml += '     <pressure units = "c">{}</temperature>\n'\
        .format(pressure_view(device))
    xml += '<xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml

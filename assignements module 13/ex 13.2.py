# Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format. The information is fetched from the airport database used on this course. For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK. The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.

import mariadb
print(mariadb.__version__)
from flask import Flask

app = Flask(__name__)


def get_airport_details(icao):
    connection = mariadb.connect(
        host='localhost',
        port=3306,
        database='flight_game',
        user='root',
        password='Gaetrig1992.',
        autocommit=True
    )
    cursor = connection.cursor(dictionary=True)

    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    connection.close()
    return result


@app.route('/airport/<icao>')
def airport_info(icao):
    data = get_airport_details(icao)

    return {
            "ICAO": icao,
            "Name": data['name'],
            "Location": data['municipality']
    }



if __name__ == '__main__':
    app.run(debug=True, port=5000)
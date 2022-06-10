import psycopg2
from psycopg2.extras import RealDictCursor
import bottle
from bottle import route, run, debug, template, request, response, Bottle
import json

connection = psycopg2.connect(
    database='lab2_v2',
    user='postgres',
    password='postgres',
    host="127.0.0.1",
    port="5432")
if (connection):
    print('OK')
else:
    print("Not OK")

cursor = connection.cursor(cursor_factory=RealDictCursor)


def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


@route('/select_photos', method=['OPTIONS', 'GET'])
@enable_cors
def select_photos():
    cursor.execute(
        "SELECT DISTINCT id, created_at, width, height, color, description, likes, user_id FROM photos")
    result = cursor.fetchall()

    return json.dumps(result,  indent=4, sort_keys=False, default=str)


@route('/select_users', method=['OPTIONS', 'GET'])
@enable_cors
def select_users():
    cursor.execute(
        "SELECT DISTINCT * FROM users")
    result = cursor.fetchall()

    return json.dumps(result,  indent=4, sort_keys=False, default=str)


@route('/select_pie', method=['OPTIONS', 'GET'])
@enable_cors
def select_pie():
    cursor.execute(
        "SELECT DISTINCT username, total_likes, total_photos FROM users ORDER BY total_likes DESC")
    result = cursor.fetchall()

    return json.dumps(result,  indent=4, sort_keys=False, default=str)


@route('/select_locations', method=['OPTIONS', 'GET'])
@enable_cors
def select_locations():
    cursor.execute(
        "SELECT count(users) AS user, location FROM users WHERE location IS NOT NULL GROUP BY location ORDER BY COUNT(users) DESC")
    result = cursor.fetchall()

    return json.dumps(result,  indent=4, sort_keys=False, default=str)


@route('/select_updates', method=['OPTIONS', 'GET'])
@enable_cors
def select_updates():
    cursor.execute(
        "SELECT COUNT(*) as tim , created_at FROM photos GROUP BY created_at")
    result = cursor.fetchall()

    return json.dumps(result,  indent=4, sort_keys=False, default=str)


@route('/select_radar')
@enable_cors
def select():
    cursor.execute(
        "SELECT DISTINCT username, total_likes, total_photos FROM users WHERE total_photos < 1000")
    result = cursor.fetchall()

    return json.dumps(result,  indent=4, sort_keys=False, default=str)


run(host='localhost', port=5050, debug=True)

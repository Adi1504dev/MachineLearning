import socket
import time

from flask import Flask
import psycopg2
import redis

app = Flask(__name__)

hostname = socket.gethostname()

time.sleep(5)

# PostgreSQL connection

conn = psycopg2.connect(
    #service name(in docker container) becomes host name
    host="postgres",
    database="testdb",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
)
""")

conn.commit()

# Redis connection
# Docker Compose creates an internal network where each service name
# becomes a hostname. The Redis container is reachable using host="redis".
#
# Note that container-to-container communication uses Redis's internal
# listening port (6379 by default), not the host-mapped port defined
# in docker-compose.yml. Port mappings such as "6379:6379" are only
# required when accessing Redis from outside Docker (e.g., from the host machine).
#
# If Redis is reconfigured to listen on a different internal port,
# the port specified below must match that internal container port.

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

redis_client.set("company", "American Express")


@app.route("/")
def home():

    cursor.execute(
        "INSERT INTO employee(name) VALUES('Aditya') RETURNING id"
    )

    emp_id = cursor.fetchone()[0]

    conn.commit()

    company = redis_client.get("company")

    return f"""
    <h1>Docker Demo</h1>

    <p><b>Container Hostname:</b> {hostname}</p>

    <p><b>Inserted Employee ID:</b> {emp_id}</p>

    <p><b>Redis Value:</b> {company}</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
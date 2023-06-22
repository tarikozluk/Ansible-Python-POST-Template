from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
import json
import time
import redis_monitor_request
import Elastic_notification
import RabbitMQ_monitor_request
import app_watcher
from elasticapm.contrib.flask import ElasticAPM


load_dotenv()

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
          'SERVICE_NAME': 'Middleware and Application Monitoring',
          #'SECRET_TOKEN': '',
          'SERVER_URL': '{}'.format(os.getenv("ELASTIC_APM_SERVER_URL")),
}
apm = ElasticAPM(app)
app = Flask(__name__)


# http://localhost:5000/monitorredis?server_1=server1&server_2=server2&server_3=server3&server_4=server4&service=Redis&istirak=mycompany
@app.route('/monitorredis', methods=['GET'])
def redis_monitor():
    server_1 = request.args.get('server_1')
    server_2 = request.args.get('server_2')
    server_3 = request.args.get('server_3')
    server_4 = request.args.get('server_4')
    service = request.args.get('service')
    istirak = request.args.get('istirak')
    redis_monitor_request.mail_redis(
        server_1=server_1,
        server_2=server_2,
        server_3=server_3,
        server_4=server_4,
        service=service,
        istirak=istirak)
    return jsonify({"server_1": server_1, "server_2": server_2, "server_3": server_3, "server_4": server_4, "service": service,"istirak": istirak})

# http://localhost:5000/monitorelkthree?server_1=server1&server_2=server2&server_3=server3&service=ELK&istirak=mycompany&node=3
@app.route('/monitorelkthree', methods=['GET'])
def elk_monitor():
    server_1 = request.args.get('server_1')
    server_2 = request.args.get('server_2')
    server_3 = request.args.get('server_3')
    service = request.args.get('service')
    istirak = request.args.get('istirak')
    node = request.args.get('node')
    Elastic_notification.mail_three_elk(
        server_1=server_1,
        server_2=server_2,
        server_3=server_3,
        service=service,
        istirak=istirak,
        node=node)
    return jsonify({"server_1": server_1, "server_2": server_2, "server_3": server_3, "service": service,"istirak": istirak, "node": node})

# http://localhost:5000/monitorelksix?server_1=server1&server_2=server2&server_3=server3&server_4=server4&server_5=server5&server_6=server6&service=ELK&istirak=mycompany&node=6
@app.route('/monitorelksix', methods=['GET'])
def elk_monitor_six():
    server_1 = request.args.get('server_1')
    server_2 = request.args.get('server_2')
    server_3 = request.args.get('server_3')
    server_4 = request.args.get('server_4')
    server_5 = request.args.get('server_5')
    server_6 = request.args.get('server_6')
    service = request.args.get('service')
    istirak = request.args.get('istirak')
    node = request.args.get('node')
    Elastic_notification.mail_six_elk(
        server_1=server_1,
        server_2=server_2,
        server_3=server_3,
        server_4=server_4,
        server_5=server_5,
        server_6=server_6,
        service=service,
        istirak=istirak,
        node=node)
    return jsonify({"server_1": server_1, "server_2": server_2, "server_3": server_3, "server_4": server_4, "server_5": server_5, "server_6": server_6, "service": service,"istirak": istirak, "node": node})

# http://localhost:5000/monitorrabbitmq?server_1=server1&server_2=server2&server_3=server3&service=RabbitMQ&istirak=mycompany
@app.route('/monitorrabbitmq', methods=['GET'])
def rabbitmq_monitor():
    server_1 = request.args.get('server_1')
    server_2 = request.args.get('server_2')
    server_3 = request.args.get('server_3')
    service = request.args.get('service')
    istirak = request.args.get('istirak')
    RabbitMQ_monitor_request.mail_rabbit(
        server_1=server_1,
        server_2=server_2,
        server_3=server_3,
        service=service,
        istirak=istirak)
    return jsonify({"server_1": server_1, "server_2": server_2, "server_3": server_3, "service": service,"istirak": istirak})

# http://localhost:5000/monitorapp?url_adress=app.com&Dev_Team=DEV&service=IIS&istirak=mycompany&http_https=http&SSL_izleme=No
@app.route('/monitorapp', methods=['GET'])
def app_monitor():
    url_adress = request.args.get('url_adress')
    Dev_Team = request.args.get('Dev_Team')
    service = request.args.get('service')
    istirak = request.args.get('istirak')
    http_https = request.args.get('http_https')
    SSL_izleme = request.args.get('SSL_izleme')
    app_watcher.mail_app(
        url_adress=url_adress,
        Dev_Team=Dev_Team,
        service=service,
        istirak=istirak,
        http_https=http_https,
        SSL_izleme=SSL_izleme)
    return jsonify({"url_adress": url_adress, "Dev_Team": Dev_Team, "service": service,"istirak": istirak, "http_https": http_https, "SSL_izleme": SSL_izleme})



if __name__ == '__main__':
    app.run(host=os.getenv("URL"), port=5000)

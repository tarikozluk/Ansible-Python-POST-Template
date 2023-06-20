# Ansible Python POST Template

This repository contains a template for using Ansible to make HTTP POST requests using Python service.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

The Ansible Python POST Template provides a starting point for making HTTP POST requests using Ansible and Python. It includes a sample playbook and Python script that demonstrate how to send POST requests to a specified endpoint.
Our purpose is sending an API request to Ansible API via Flask API by using Python. So we can create a monitoring request with mail notification. (Redis, Elasticsearch, RabbitMQ)

## Prerequisites

Before using this template, make sure you have the following prerequisites:

- Ansible and AWX (version 5.10.0 or higher)
- Python (version 3.8 or higher)

## Installation

To install the necessary dependencies, follow these steps:

1. Clone this repository:

   ```bash
   $ git clone https://github.com/tarikozluk/Ansible-Python-POST-Template.git
   ```

   ```bash
   $ pip install -r requirements.txt
   ```
  
2. Create a windows or ubuntu service or just run the main code
    ```bash
    $ python api_main.py
    ```
## Usage
  Send requests via http for your simple installation the it will automatically redirect by using Ansible yml options(those you can view in yml)
  
  For Redis
  ```bash
  http://localhost:5000/monitorredis?server_1=server1&server_2=server2&server_3=server3&server_4=server4&service=Redis&istirak=mycompany
  ```
  For Elasticsearch 
  ```bash
  http://localhost:5000/monitorelkthree?server_1=server1&server_2=server2&server_3=server3&service=ELK&istirak=mycompany&node=3
  http://localhost:5000/monitorelksix?server_1=server1&server_2=server2&server_3=server3&server_4=server4&server_5=server5&server_6=server6&service=ELK&istirak=mycompany&node=6
  ```
  For RabbitMQ
  ```bash
  http://localhost:5000/monitorrabbitmq?server_1=server1&server_2=server2&server_3=server3&service=RabbitMQ&istirak=mycompany
  ```
   

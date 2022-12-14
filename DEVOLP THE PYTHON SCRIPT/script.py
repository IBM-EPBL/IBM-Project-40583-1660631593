import time
import sys
import ibmiotf.application
import ibmiotf.device
organization = "c5ah4g"
deviceType = "App-1"
deviceId = "13"
authMethod = "token"
authToken = "12345678"
def myCommandCallback(cmd):
   print("Command received: %s" % cmd.data)
   if cmd.data['command'] == 'motoron':
      print("Motor On IS RECEIVED")
   elif cmd.data['command'] == 'motoroff':
      print("Motor Off IS RECEIVED")
   if cmd.command == "setInterval":
      if 'interval' not in cmd.data:
         print("Error - command is missing required information: 'interval'")
   else:
    interval = cmd.data['interval']
    elif cmd.command == "print":
   if 'message' not in cmd.data:
      print("Error - command is missing required information: 'message'")
   else:
      output = cmd.data['message']
      print(output)
   try:
      deviceOptions = {"org": organization, "type":deviceType,"id": deviceId, "auth-method":authMethod, "auth-token": authToken}
      deviceCli = ibmiotf.device.Client(deviceOptions)
 except Exception as e:
      print("Caught exception connecting device: %s" %
      str(e))
      sys.exit()
      deviceCli.connect()
while True:
      deviceCli.commandCallback = myCommandCallback
      deviceCli.disconnect()
Node Red Flow.json
[{
 "id": "6a097760.653918",
 "type": "tab",
 "label": "IBMIOT(smart Agriculture)",
 "disabled": false,
 "info": ""
}, {
 "id": "4fdd8d20.76a9b4",
 "type": "ibmiot in",
 "z": "6a097760.653918",
 "authentication": "apiKey",
 "apiKey": "233183d6.16ba7c",
 "inputType": "evt",
 "logicalInterface": "",
 "ruleId": "",
 "deviceId": "BME280_Sensor",
 "applicationId": "",
 "deviceType": "ESP32_Controller",
 "eventType": "+",
 "commandType": "",
 "format": "json",
 "name": "IBM IoT",
 "service": "registered",
 "allDevices": "",
 "allApplications": "",
 "allDeviceTypes": "",
 "allLogicalInterfaces": "",
 "allEvents": true,
 "allCommands": "",
 "allFormats": "",
 "qos": 0,
 "x": 130,
 "y": 440,
 "wires": [
 ["8d0c40d3.848cd", "6aa78b4a.da3eb4",
"5642999c.ed7868", "c396573b.e8d738"]
 ]
}, {
 "id": "c396573b.e8d738",
 "type": "debug",
 "z": "6a097760.653918",
 "name": "",
 "active": false,
 "tosidebar": true,
 "console": false,
 "tostatus": false,
 "complete": "payload",
 "targetType": "msg",
 "x": 770,
 "y": 360,
 "wires": []
}, {
 "id": "8a49f2d5.e9d07",
 "type": "ui_gauge",
 "z": "6a097760.653918",
 "name": "",
 "group": "28e6141.0c047ec",
 "order": 0,
 "width": "6",
 "height": "4",
 "gtype": "gage",
 "title": "Humidity",
 "label": "%Percentage",
 "format": "{{value}}",
 "min": 0,
 "max": "100",
 "colors": ["#00b500", "#e6e600", "#ca3838"],
 "seg1": "",
 "seg2": "",
 "x": 800,
 "y": 540,
 "wires": []
}, {
 "id": "9e820fb2.1ded5",
 "type": "ui_gauge",
 "z": "6a097760.653918",
 "name": "",
 "group": "28e6141.0c047ec",
 "order": 0,
 "width": "6",
 "height": "4",
 "gtype": "gage",
 "title": "Temperature",
 "label": "??C Celcius",
 "format": "{{value}}",
 "min": 0,
 "max": "100",
 "colors": ["#00b500", "#e6e600", "#ca3838"],
 "seg1": "",
 "seg2": "",
 "x": 770,
 "y": 660,
 "wires": []
}, {
 "id": "6aa78b4a.da3eb4",
 "type": "function",
 "z": "6a097760.653918",
 "name": "Temperature",
 "func":
"msg.payload=msg.payload.d.temperature;\nreturn
msg;",
 "outputs": 1,
 "noerr": 0,
 "x": 410,
 "y": 560,
 "wires": [
 ["c396573b.e8d738", "9e820fb2.1ded5",
"687d6f13.98f7c"]
 ]
}, {
 "id": "8d0c40d3.848cd",
 "type": "function",
 "z": "6a097760.653918",
 "name": "Humidity",
 "func":
"msg.payload=msg.payload.d.humidity;\nreturn msg;",
 "outputs": 1,
 "noerr": 0,
 "x": 420,
 "y": 500,
 "wires": [
 ["c396573b.e8d738", "8a49f2d5.e9d07",
"a4f00796.520788"]
 ]
}, {
 "id": "5642999c.ed7868",
 "type": "function",
 "z": "6a097760.653918",
 "name": "SoilMoisture",
 "func":
"msg.payload=msg.payload.d.objectTemp;\nreturn msg;",
 "outputs": 1,
 "noerr": 0,
 "x": 430,
 "y": 440,
 "wires": [
 ["c396573b.e8d738", "dad1ab68.86f798",
"9888ac53.4a285"]
 ]
}, {
 "id": "dad1ab68.86f798",
 "type": "ui_gauge",
 "z": "6a097760.653918",
 "name": "",
 "group": "28e6141.0c047ec",
 "order": 2,
 "width": "6",
 "height": "4",
 "gtype": "gage",
 "title": "Soil Moisture",
 "label": "% Percentage",
 "format": "{{value}}",
 "min": 0,
 "max": "100",
 "colors": ["#00b500", "#e6e600", "#ca3838"],
 "seg1": "",
 "seg2": "",
 "x": 810,
 "y": 420,
 "wires": []
}, {
 "id": "9de2a117.06e1d",
 "type": "http request",
 "z": "6a097760.653918",
 "name": "",
 "method": "GET",
 "ret": "obj",
 "paytoqs": false,
 "url":
"http://api.openweathermap.org/data/2.5/weather?q=Pon
da,IN&appid=c17ea99bbf41216723c2071ce90c3633",
 "tls": "",
 "persist": false,
 "proxy": "",
 "authType": "",
 "x": 510,
 "y": 240,
 "wires": [
 ["c396573b.e8d738", "91b4e81a.972888",
"4bcf3c9.21fd4c4", "2c496973.5626d6",
"3552343c.1a23ac"]
 ]
}, {
 "id": "cbdf50d7.8bd57",
 "type": "inject",
 "z": "6a097760.653918",
 "name": "",
 "topic": "",
 "payload": "",
 "payloadType": "date",
 "repeat": "5",
 "crontab": "",
 "once": true,
 "onceDelay": "5",
 "x": 150,
 "y": 300,
 "wires": [
 ["9de2a117.06e1d"]
 ]
}, {
 "id": "f8fb8426.88b758",
 "type": "ibmiot out",
 "z": "6a097760.653918",
 "authentication": "apiKey",
 "apiKey": "233183d6.16ba7c",
 "outputType": "cmd",
 "deviceId": "BME280_Sensor",
 "deviceType": "ESP32_Controller",
 "eventCommandType": "command",
 "format": "json",
 "data": "Data",
 "qos": 0,
 "name": "IBM IoT",
 "service": "registered",
 "x": 560,
 "y": 100,
 "wires": []
}, {
 "id": "2deb666d.10728a",
 "type": "ui_button",
 "z": "6a097760.653918",
 "name": "",
 "group": "d251626d.10cec",
 "order": 2,
 "width": 0,
 "height": 0,
 "passthru": false,
 "label": "Motor on",
 "tooltip": "",
 "color": "",
 "bgcolor": "",
 "icon": "",
 "payload": "{\"command\":\"motoron\"}",
 "payloadType": "json",
 "topic": "",
 "x": 160,
 "y": 60,
 "wires": [
 ["f8fb8426.88b758", "c396573b.e8d738"]
 ]
}, {
 "id": "154a1e0e.e80672",
 "type": "ui_button",
 "z": "6a097760.653918",
 "name": "",
 "group": "d251626d.10cec",
 "order": 3,
 "width": 0,
 "height": 0,
 "passthru": false,
 "label": "Motoroff",
 "tooltip": "",
 "color": "",
 "bgcolor": "",
 "icon": "",
 "payload": "{\"command\":\"motoroff\"}",
 "payloadType": "json",
 "topic": "",
 "x": 160,
 "y": 160,
 "wires": [
 ["f8fb8426.88b758", "c396573b.e8d738"]
 ]
}, {
 "id": "6329ceb0.9a74",
 "type": "ui_text",
 "z": "6a097760.653918",
 "group": "a9434212.30379",
 "order": 0,
 "width": 0,
 "height": 0,
 "name": "",
 "label": "Temperature",
 "format": "{{msg.payload}}",
 "layout": "row-spread",
 "x": 970,
 "y": 140,
 "wires": []
}, {
 "id": "5d4cb33b.861edc",
 "type": "ui_text",
 "z": "6a097760.653918",
 "group": "a9434212.30379",
 "order": 1,
 "width": 0,
 "height": 0,
 "name": "",
 "label": "Humidity",
 "format": "{{msg.payload}}",
 "layout": "row-spread",
 "x": 980,
 "y": 200,
 "wires": []
}, {
 "id": "d85fe3cc.9ca31",
 "type": "ui_text",
 "z": "6a097760.653918",
 "group": "a9434212.30379",
 "order": 0,
 "width": 0,
 "height": 0,
 "name": "",
 "label": "Region",
 "format": "{{msg.payload}}",
 "layout": "row-spread",
 "x": 980,
 "y": 260,
 "wires": []
}, {
 "id": "e00de3f6.29978",
 "type": "ui_text",
 "z": "6a097760.653918",
 "group": "a9434212.30379",
 "order": 3,
 "width": 0,
 "height": 0,
 "name": "",
 "label": "Weather Description",
 "format": "{{msg.payload}}",
 "layout": "row-spread",
 "x": 1020,
 "y": 320,
 "wires": []
}, {
 "id": "9888ac53.4a285",
 "type": "ui_chart",
 "z": "6a097760.653918",
 "name": "",
 "group": "309c8230.4f9bde",
 "order": 3,
 "width": 0,
 "height": 0,
 "label": "Soil moisture",
 "chartType": "line",
 "legend": "false",
 "xformat": "HH:mm:ss",
 "interpolate": "linear",
 "nodata": "",
 "dot": false,
 "ymin": "",
 "ymax": "",
 "removeOlder": 1,
 "removeOlderPoints": "",
 "removeOlderUnit": "3600",
 "cutout": 0,
 "useOneColor": false,
 "useUTC": false,
 "colors": ["#1f77b4", "#aec7e8", "#ff7f0e",
"#2ca02c", "#98df8a", "#d62728", "#ff9896",
"#9467bd", "#c5b0d5"],
 "useOldStyle": false,
 "outputs": 1,
 "x": 820,
 "y": 460,
 "wires": [
 []
 ]
}, {
 "id": "a4f00796.520788",
 "type": "ui_chart",
 "z": "6a097760.653918",
 "name": "",
 "group": "309c8230.4f9bde",
 "order": 4,
 "width": 0,
 "height": 0,
 "label": "Humidity",
 "chartType": "line",
 "legend": "false",
 "xformat": "HH:mm:ss",
 "interpolate": "linear",
 "nodata": "",
 "dot": false,
 "ymin": "",
 "ymax": "",
 "removeOlder": 1,
 "removeOlderPoints": "",
 "removeOlderUnit": "3600",
 "cutout": 0,
 "useOneColor": false,
 "useUTC": false,
 "colors": ["#1f77b4", "#aec7e8", "#ff7f0e",
"#2ca02c", "#98df8a", "#d62728", "#ff9896",
"#9467bd", "#c5b0d5"],
 "useOldStyle": false,
 "outputs": 1,
 "x": 800,
 "y": 580,
 "wires": [
 []
 ]
}, {
 "id": "687d6f13.98f7c",
 "type": "ui_chart",
 "z": "6a097760.653918",
 "name": "",
 "group": "309c8230.4f9bde",
 "order": 5,
 "width": 0,
 "height": 0,
 "label": "Temperature",
 "chartType": "line",
 "legend": "false",
 "xformat": "HH:mm:ss",
 "interpolate": "linear",
 "nodata": "",
 "dot": false,
 "ymin": "",
 "ymax": "",
 "removeOlder": 1,
 "removeOlderPoints": "",
 "removeOlderUnit": "3600",
 "cutout": 0,
 "useOneColor": false,
 "useUTC": false,
 "colors": ["#1f77b4", "#aec7e8", "#ff7f0e",
"#2ca02c", "#98df8a", "#d62728", "#ff9896",
"#9467bd", "#c5b0d5"],
 "useOldStyle": false,
 "outputs": 1,
 "x": 810,
 "y": 700,
 "wires": [
 []
 ]
}, {
 "id": "91b4e81a.972888",
 "type": "change",
 "z": "6a097760.653918",
 "name": "Temperature",
 "rules": [{
 "t": "set",
 "p": "payload",
 "pt": "msg",
 "to": "payload.main.temp",
 "tot": "msg"
 }],
 "action": "",
 "property": "",
 "from": "",
 "to": "",
 "reg": false,
 "x": 750,
 "y": 120,
 "wires": [
 ["6329ceb0.9a74"]
 ]
}, {
 "id": "4bcf3c9.21fd4c4",
 "type": "change",
 "z": "6a097760.653918",
 "name": "Humidity",
 "rules": [{
 "t": "set",
 "p": "payload",
 "pt": "msg",
 "to": "payload.main.humidity",
 "tot": "msg"
 }],
 "action": "",
 "property": "",
 "from": "",
 "to": "",
 "reg": false,
 "x": 740,
 "y": 180,
 "wires": [
 ["5d4cb33b.861edc"]
 ]
}, {
 "id": "2c496973.5626d6",
 "type": "change",
 "z": "6a097760.653918",
 "name": "Region",
 "rules": [{
 "t": "set",
 "p": "payload",
 "pt": "msg",
 "to": "payload.name",
 "tot": "msg"
 }],
 "action": "",
 "property": "",
 "from": "",
 "to": "",
 "reg": false,
 "x": 740,
 "y": 240,
 "wires": [
 ["d85fe3cc.9ca31"]
 ]
}, {
 "id": "3552343c.1a23ac",
 "type": "change",
 "z": "6a097760.653918",
 "name": "Weather Description",
 "rules": [{
 "t": "set",
 "p": "payload",
 "pt": "msg",
 "to": "payload.weather.0.description",
 "tot": "msg"
 }],
 "action": "",
 "property": "",
 "from": "",
 "to": "",
 "reg": false,
 "x": 780,
 "y": 300,
 "wires": [
 ["e00de3f6.29978"]
 ]
}, {
 "id": "233183d6.16ba7c",
 "type": "ibmiot",
 "z": "",
 "name": "",
 "keepalive": "60",
 "serverName": "",
 "cleansession": true,
 "appId": "",
 "shared": false
}, {
 "id": "28e6141.0c047ec",
 "type": "ui_group",
 "z": "",
 "name": "Smart Agriculture",
 "tab": "d669ffca.1402d",
 "order": 6,
 "disp": true,
 "width": "6",
 "collapse": false
}, {
 "id": "d251626d.10cec",
 "type": "ui_group",
 "z": "",
 "name": "Motor Commands",
 "tab": "d669ffca.1402d",
 "order": 1,
 "disp": true,
 "width": "6",
 "collapse": false
}, {
 "id": "a9434212.30379",
 "type": "ui_group",
 "z": "",
 "name": "Weather Forecast",
 "tab": "d669ffca.1402d",
 "order": 3,
 "disp": true,
 "width": "6",
 "collapse": false
}, {
 "id": "309c8230.4f9bde",
 "type": "ui_group",
 "z": "",
 "name": "Graphical Representation",
 "tab": "d669ffca.1402d",
 "order": 5,
 "disp": true,
 "width": "6",
 "collapse": false
}, {
 "id": "d669ffca.1402d",
 "type": "ui_tab",
 "z": "",
 "name": "Smart Agriculture",
 "icon": "dashboard",
 "disabled": false,
 "hidden": false
}]

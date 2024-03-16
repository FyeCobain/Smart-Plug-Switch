# `Smart Plug Switch`

A simple Python script to turn on/off a Tuya smart plug with _**tinytuya**_

### Requirements
> Please refer to **[jasonacox / tinituya](https://github.com/jasonacox/tinytuya)**

### Usage

It requires 5 arguments, as shown in the following examples:
1. Device ID:
```
yuz27478210335e1374guq
```
2. Device IP ('Auto' is slower):
```
192.168.1.80 || Auto
```
3. Local security key:
```
TFo-=A;&N3AXypQt
```
4. Protocol Version:
```
3.3
```
5. New state:
```
on || off
```

### On:

```
"smart_plug_switch.py" "yuz27478210335e1374guq" "Auto" "TFo-=A;&N3AXypQt" "3.3" ON
```

### Off:

```
"smart_plug_switch.py" "yuz27478210335e1374guq" "192.168.1.80" "TFo-=A;&N3AXypQt" "3.3" off
```
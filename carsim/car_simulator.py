import paho.mqtt.client as mqtt
import tkinter
import random
import time

# Costanti per i tasti da associare
THROTTLE = 'w'
BRAKE = 's'
STEERING_LEFT = 'a'
STEERING_RIGHT = 'd'
GEAR_UP = 'e'
GEAR_DOWN = 'q'
RESET = 'r'

# Crea il client MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Connetti al broker MQTT
client.connect("localhost")

throttle_value = 0
brake_value = 0
steering_value = 0
gear_value = 0
speed = 0
acceleration = 0
steering_angle = 0
gear = 0

# interfaccia grafica con tkinter con tasti da associare che servono come acceleratore, freno, sterzo, cambio marcia
def key_input(event):
    global throttle_value, brake_value, steering_value, gear, speed, acceleration, steering_angle
    key_press = event.keysym.lower()
    print(key_press)
    if key_press == THROTTLE:
        throttle_value += 1
        brake_value -= 1
    elif key_press == BRAKE:
        brake_value += 1
        throttle_value -= 1
    elif key_press == STEERING_LEFT:
        steering_value -= 1
    elif key_press == STEERING_RIGHT:
        steering_value += 1
    elif key_press == GEAR_UP:
        gear += 1
    elif key_press == GEAR_DOWN:
        gear -= 1
    elif key_press == RESET:
        throttle_value = 0
        brake_value = 0
        steering_value = 0
        gear = 0
    speed = abs(throttle_value - brake_value) * 10
    acceleration = throttle_value - brake_value
    steering_angle = steering_value * 10
    client.publish("car/gear", str(gear))
    client.publish("car/accelerator", str(throttle_value))
    client.publish("car/brake", str(brake_value))
    client.publish("car/steering", str(steering_angle))
    client.publish("car/speed", str(speed))
    client.publish("car/acceleration", str(acceleration))

# Crea la finestra tkinter
root = tkinter.Tk()
root.bind_all('<Key>', key_input)
root.mainloop()

import paho.mqtt.client as mqtt
import tkinter

# Funzione chiamata quando si riceve un messaggio sul topic sottoscritto
def on_message(client, userdata, message):
    #aggiorna i dati dei sensori
    if message.topic == "car/gear":
        gear_label.config(text="Gear: " + message.payload.decode())
    elif message.topic == "car/accelerator":
        accelerator_label.config(text="Accelerator: " + message.payload.decode())
    elif message.topic == "car/brake":
        brake_label.config(text="Brake: " + message.payload.decode())
    elif message.topic == "car/steering":
        steering_label.config(text="Steering: " + message.payload.decode())
    elif message.topic == "car/speed":
        speed_label.config(text="Speed: " + message.payload.decode())
    elif message.topic == "car/acceleration":
        acceleration_label.config(text="Acceleration: " + message.payload.decode())

# Crea il client MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# Imposta la funzione da chiamare quando si riceve un messaggio
client.on_message = on_message

# Connetti al broker MQTT
client.connect("localhost")

# Sottoscrivi al topic dei dati dei sensori
client.subscribe("car/gear")
client.subscribe("car/accelerator")
client.subscribe("car/brake")
client.subscribe("car/steering")
client.subscribe("car/speed")
client.subscribe("car/acceleration")

# interfaccia grafica con tkinter con visualizzazione della plancia di bordo
root = tkinter.Tk()
root.title("Dashboard")
root.geometry("800x600")

# Crea un'etichetta per visualizzare i dati dei sensori
label = tkinter.Label(root, text="Dati dei sensori")
label.pack()
# crea labels per visualizzare i dati dei sensori vuote
gear_label = tkinter.Label(root, text="Gear: ")
gear_label.pack()
accelerator_label = tkinter.Label(root, text="Accelerator: ")
accelerator_label.pack()
brake_label = tkinter.Label(root, text="Brake: ")
brake_label.pack()
steering_label = tkinter.Label(root, text="Steering: ")
steering_label.pack()
speed_label = tkinter.Label(root, text="Speed: ")
speed_label.pack()
acceleration_label = tkinter.Label(root, text="Acceleration: ")
acceleration_label.pack()

# Inizia il loop per processare i messaggi ricevuti
client.loop_start()

# Avvia la finestra tkinter
root.mainloop()

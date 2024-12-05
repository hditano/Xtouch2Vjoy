import mido
import pyvjoy

# Crear un objeto vJoy para interactuar con el dispositivo virtual
joystick = pyvjoy.VJoyDevice(1)  # El número 1 corresponde al primer dispositivo vJoy

def list_midi_ports():
    """Listar todos los puertos MIDI disponibles"""
    ports = mido.get_input_names()
    print("Puertos MIDI disponibles:")
    for idx, port in enumerate(ports):
        print(f"{idx}: {port}")
    return ports

def map_midi_to_vjoy(msg):
    """Mapear los eventos MIDI a botones de vJoy"""
    if msg.type == 'note_on':
        if msg.velocity > 0:  # Solo si la tecla está siendo presionada
            # Asignamos la nota a un botón en vJoy (ej. nota 60 -> botón 1)
            joystick.set_button(msg.note, 1)  # Establecer el botón presionado
            print(f"Botón {msg.note} presionado")
    elif msg.type == 'note_off':
        # Cuando se libera la tecla, se desactiva el botón
        joystick.set_button(msg.note, 0)  # Establecer el botón liberado
        print(f"Botón {msg.note} liberado")

def read_midi_input(port_name):
    """Leer entradas MIDI y mapearlas a vJoy"""
    with mido.open_input(port_name) as inport:
        print(f"Escuchando en el puerto: {port_name}")
        print("Presiona Ctrl+C para salir.")
        try:
            for msg in inport:
                map_midi_to_vjoy(msg)  # Mapeamos los mensajes MIDI a vJoy
        except KeyboardInterrupt:
            print("Saliendo del programa.")

if __name__ == "__main__":
    # Listar puertos MIDI y seleccionar uno
    ports = list_midi_ports()
    if not ports:
        print("No se encontraron dispositivos MIDI.")
    else:
        selected_port = input("Selecciona un puerto MIDI por número: ")
        try:
            selected_port = int(selected_port)
            if 0 <= selected_port < len(ports):
                read_midi_input(ports[selected_port])
            else:
                print("Número de puerto inválido.")
        except ValueError:
            print("Por favor ingresa un número válido.")
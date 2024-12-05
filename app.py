import mido
import pyvjoy

# Create a vJoy object to interact with the virtual device
joystick = pyvjoy.VJoyDevice(1)  # Number 1 corresponds to the first vJoy device

def list_midi_ports():
    """List all available MIDI ports"""
    ports = mido.get_input_names()
    print("Available MIDI ports:")
    for idx, port in enumerate(ports):
        print(f"{idx}: {port}")
    return ports

def map_midi_to_vjoy(msg):
    """Map MIDI events to vJoy buttons"""
    if msg.type == 'note_on':
        if msg.velocity > 0:  # Only if the key is being pressed
            # Map the note to a button on vJoy (e.g., note 60 -> button 1)
            joystick.set_button(msg.note, 1)  # Set the button as pressed
            print(f"Button {msg.note} pressed")
    elif msg.type == 'note_off':
        # When the key is released, the button is deactivated
        joystick.set_button(msg.note, 0)  # Set the button as released
        print(f"Button {msg.note} released")

def read_midi_input(port_name):
    """Read MIDI input and map it to vJoy"""
    with mido.open_input(port_name) as inport:
        print(f"Listening on port: {port_name}")
        print("Press Ctrl+C to exit.")
        try:
            for msg in inport:
                map_midi_to_vjoy(msg)  # Map the MIDI messages to vJoy
        except KeyboardInterrupt:
            print("Exiting the program.")

if __name__ == "__main__":
    # List MIDI ports and select one
    ports = list_midi_ports()
    if not ports:
        print("No MIDI devices found.")
    else:
        selected_port = input("Select a MIDI port by number: ")
        try:
            selected_port = int(selected_port)
            if 0 <= selected_port < len(ports):
                read_midi_input(ports[selected_port])
            else:
                print("Invalid port number.")
        except ValueError:
            print("Please enter a valid number.")

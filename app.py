import mido
import pyvjoy

# Axis mapping to vJoy constants
axis = {
    'X': 0x30,   # X-axis
    'Y': 0x31,   # Y-axis
    'Z': 0x32,   # Z-axis
    'RX': 0x33,  # Rotational X
    'RY': 0x34,  # Rotational Y
    'RZ': 0x35,  # Rotational Z
    'SL0': 0x36, # Slider 0
    'SL1': 0x37, # Slider 1
    'WHL': 0x38, # Wheel
    'POV': 0x39  # Point-of-View
}

# Initialize vJoy device
joystick = pyvjoy.VJoyDevice(1)  # Assumes vJoy Device 1

def map_midi_to_vjoy(msg):
    """Map MIDI events from X-Touch Mini to vJoy axes."""
    try:
        if msg.type == 'control_change':
            # Map CC numbers to vJoy axes
            cc_to_axis = {
                1: axis['X'],    # CC1 -> X-axis
                2: axis['Y'],    # CC2 -> Y-axis
                3: axis['Z'],    # CC3 -> Z-axis
                4: axis['RX'],   # CC4 -> Rotational X
                5: axis['RY'],   # CC5 -> Rotational Y
                6: axis['RZ'],   # CC6 -> Rotational Z
                7: axis['SL0'],  # CC7 -> Slider 0
                #8: axis['SL1'],   # CC8 -> Slider 1 - Disabled due to Vjoy Limitation of 8 axis
                9: axis['SL1']    # CC9 > Slider 1
            }
            if msg.control in cc_to_axis:
                # Map CC value (0–127) to vJoy axis range (0–32767)
                axis_id = cc_to_axis[msg.control]
                axis_value = int(msg.value * (32767 / 127))  # Scale value
                joystick.set_axis(axis_id, axis_value)
                print(f"Mapped CC{msg.control} to vJoy Axis {hex(axis_id)} with value {axis_value}")
            else:
                print(f"Unhandled Control Change: CC{msg.control} with value {msg.value}")
        elif msg.type == 'note_on':
            joystick.set_button(msg.note + 1, 1)  # Map Note-On to button press
            print(f"Button {msg.note + 1} pressed")
        elif msg.type == 'note_off':
            joystick.set_button(msg.note + 1, 0)  # Map Note-Off to button release
            print(f"Button {msg.note + 1} released")
        else:
            print(f"Unhandled MIDI message type: {msg.type}")
    except Exception as e:
        print(f"Error handling MIDI message: {e}")

def read_midi_input(port):
    """Read MIDI input and pass messages to the mapping function."""
    with mido.open_input(port) as inport:
        print("Listening for MIDI messages...")
        for msg in inport:
            print(f"Received MIDI message: {msg}")
            map_midi_to_vjoy(msg)

# Main script
if __name__ == "__main__":
    # List available MIDI input ports
    ports = mido.get_input_names()
    print("Available MIDI ports:")
    for i, port in enumerate(ports):
        print(f"{i}: {port}")
    
    # Select MIDI port
    selected_port = int(input("Select MIDI port number: "))
    read_midi_input(ports[selected_port])

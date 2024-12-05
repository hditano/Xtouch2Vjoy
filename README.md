# MIDI to vJoy Mapper

This script maps MIDI Control Change (CC) and Note On/Off messages from a Behringer X-Touch Mini to vJoy virtual joystick inputs. It allows you to control vJoy axes and buttons using MIDI devices.

## Features

- Maps up to 8 MIDI CC messages to vJoy axes (X, Y, Z, RX, RY, RZ, SL0, SL1).
- Maps MIDI Note On/Off messages to vJoy buttons.
- Supports scaling MIDI CC values (0--127) to vJoy axis range (0--32,767).
- Designed for compatibility with the Behringer X-Touch Mini.

---

## Requirements

### Hardware

- A MIDI device (e.g., Behringer X-Touch Mini).

### Software

- Python 3.7 or newer.
- The following Python packages:
 - `mido` (for MIDI input handling)
 - `pyvjoy` (for interacting with vJoy)

To install the required Python packages, use:

```bash
pip install mido pyvjoy `
```

### Additional Tools

-   vJoy Virtual Joystick Driver. Ensure vJoy is installed and configured with a virtual joystick.

* * * * *

Installation
------------

1.  Clone or download this repository to your local machine.
2.  Ensure Python and required libraries are installed.
3.  Verify your vJoy configuration supports the required axes and buttons.

* * * * *

Usage
-----

1.  **Connect your MIDI device** (e.g., Behringer X-Touch Mini) to your computer.
2.  **Run the script**:

    bash

    Copy code

    `python script.py`

3.  **Select the MIDI port**:
    -   The script lists all available MIDI input ports.
    -   Enter the number corresponding to your device.
4.  **Interact with your MIDI device**:
    -   Turn knobs or sliders to send CC messages, mapped to vJoy axes.
    -   Press buttons to trigger Note On/Off messages, mapped to vJoy buttons.

* * * * *

MIDI-to-vJoy Mapping
--------------------

### Axis Mapping

| MIDI CC Number | vJoy Axis | Description |
| --- | --- | --- |
| CC1 | X | X-axis |
| CC2 | Y | Y-axis |
| CC3 | Z | Z-axis |
| CC4 | RX | Rotational X |
| CC5 | RY | Rotational Y |
| CC6 | RZ | Rotational Z |
| CC7 | SL0 | Slider 0 |
| CC9 | SL1 | Slider 1 |

### Button Mapping

-   **MIDI Notes** are mapped to vJoy buttons sequentially.
    -   For example, MIDI Note 0 triggers vJoy Button 1, Note 1 triggers Button 2, etc.

* * * * *

Known Limitations
-----------------

-   vJoy supports a maximum of 8 axes, which restricts the number of mappable CC controls.
-   CC8 is disabled in this implementation due to this limitation.
-   Ensure your MIDI device is sending the expected CC messages for proper mapping.

* * * * *

Debugging and Logs
------------------

-   The script prints incoming MIDI messages to the console.
-   It also logs the mapping of CC messages and button presses for troubleshooting.
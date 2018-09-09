from time import sleep
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print(available_ports)

# Open the second port (Should connect to Kontak4)
midiout.open_port(1)


def on(c, k, v):
    midiout.send_message([0x90 + c, k, v])


def off(c, k):
    midiout.send_message([0x80 + c, k])


on(1, 60, 112)
sleep(0.05)
off(1, 60)
on(2, 67, 100)
sleep(0.5)
off(2, 67)


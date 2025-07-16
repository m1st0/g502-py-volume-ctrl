# G502 Linux Volume Control Buttons

This project lets you map Logitech G502 mouse buttons to control PipeWire (PulseAudio) volume on Linux (Wayland or X11), using evdev.

## Why this?

On Linux with PipeWire, the system and KDE typically apply volume changes only to the default audio sink. However, many users run setups where the default sink is not the actual output device, causing volume keys and KDE controls to not affect real audio output.

This project provides a custom Python script and simple shell scripts to directly control volume and mute on the correct PipeWire sink associated with your Logitech G502 mouse buttons.

It avoids relying on KDE’s default volume mapping or complex interception tools, reducing dependencies like systemd and providing a secure, maintainable solution.

By sharing this, we demonstrate an understanding of Linux device input handling, PipeWire audio control, and practical scripting to solve real-world problems — valuable for Linux users and developers alike.

## Features

- Use side buttons to raise and lower volume
- Optionally toggle mute
- Prevents events from triggering browser "back/forward" actions
- Works without udevmon, simpler setup

## Requirements

- Python 3
- `evdev` Python package
- PipeWire or PulseAudio
- EasyEffects
- KDE if desired

## Setup

1. Install Python package:

```
pip install evdev
```

2. Install udev rule and retrigger udev updates or restart for permission updates to hold.
3. Run the Python file to listen for your G502 side buttons to affect PipeWire's main sink regardless of others.  (Mute was universal in operation so it was left alone.)

## Installing udev Rules

Copy the provided udev rule to `/etc/udev/rules.d/` with root permissions:

```
sudo cp 99-uinput.rules /etc/udev/rules.d/
sudo chown root:root /etc/udev/rules.d/99-uinput.rules
sudo chmod 644 /etc/udev/r
ules.d/99-uinput.rules
sudo udevadm control --reload
sudo udevadm trigger
```

## License

This project is licensed under the BSD 2-Clause License. See the [LICENSE.txt](LICENSE.txt) file for details.

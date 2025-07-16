#!/usr/bin/env python3
# Helps take mouse input mapping to the correct volume event.

# Copyright (c) 2025 Maulik Mistry mistry01@gmail.com#
# Author: Maulik Mistry
# Please share support: https://www.paypal.com/paypalme/m1st0

# License: BSD License 2.0
# Copyright (c) 2023–2025, Maulik Mistry
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import evdev
import subprocess
import os
import evdev.uinput as uinput

device_path = '/dev/input/by-path/pci-0000:00:14.0-usb-0:5:1.0-event-mouse'
device = evdev.InputDevice(device_path)

script_dir = os.path.dirname(os.path.realpath(__file__))

# Create virtual device with same capabilities
ui = uinput.UInput.from_device(device, name='VolumeForwarder')

device.grab()

try:
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_KEY and event.value == 1:
            if event.code == evdev.ecodes.BTN_BACK:
                subprocess.Popen([os.path.join(script_dir, "lower_volume.zsh")])
                continue
            elif event.code == evdev.ecodes.BTN_FORWARD:
                subprocess.Popen([os.path.join(script_dir, "raise_volume.zsh")])
                continue
            #elif event.code == evdev.ecodes.BTN_TASK:
                #subprocess.Popen([os.path.join(script_dir, "toggle_mute.zsh")])
                #continue

        # Forward all other events
        ui.write_event(event)
        ui.syn()
finally:
    device.ungrab()
    ui.close()

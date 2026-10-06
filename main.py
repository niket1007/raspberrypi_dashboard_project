#!/usr/bin/env python3

import dbus.mainloop.glib

from advertisement import Advertisement
from bletools import BleTools, Agent
from service import Application, NotificationService


def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = BleTools.get_bus()
    adapter = BleTools.find_adapter(bus)

    print(f"Using adapter: {adapter}")

    # Keep the Bluetooth adapter powered.
    BleTools.power_adapter(bus, adapter)

    # Build GATT application.
    app = Application(bus)
    service = NotificationService(bus)
    app.add_service(service)

    # Build advertisement and authentication agent.
    advertisement = Advertisement(bus)
    agent = Agent(bus, "/org/bluez/nsw/agent")

    # Register everything with BlueZ.
    app.register(adapter)
    advertisement.register(adapter)
    BleTools.register_agent(bus, agent)

    print()
    print("============================================")
    print(" BLE notification receiver")
    print("============================================")
    print("Device : NRPI")
    print("Service: 6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
    print("RX     : 6E400002-B5A3-F393-E0A9-E50E24DCCA9E")
    print()
    print("Waiting for Gadgetbridge...")
    print("Press Ctrl+C to stop.")
    print()

    try:
        app.run()
    except KeyboardInterrupt:
        print("\nStopping...")


if __name__ == "__main__":
    main()

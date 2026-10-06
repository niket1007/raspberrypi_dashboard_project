import dbus
import dbus.service

from bletools import (
    BLUEZ_SERVICE_NAME,
    DBUS_PROP_IFACE,
    LE_ADVERTISING_MANAGER_IFACE,
)

LE_ADVERTISEMENT_IFACE = "org.bluez.LEAdvertisement1"

DEVICE_NAME = "NRPI"
SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"

ADVERTISEMENT_PATH = "/org/bluez/nsw/advertisement0"


class Advertisement(dbus.service.Object):
    def __init__(self, bus):
        self.bus = bus
        super().__init__(bus, ADVERTISEMENT_PATH)

    def get_path(self):
        return dbus.ObjectPath(ADVERTISEMENT_PATH)

    def get_properties(self):
        return {
            LE_ADVERTISEMENT_IFACE: {
                "Type": dbus.String("peripheral"),
                "LocalName": dbus.String(DEVICE_NAME),
                "ServiceUUIDs": dbus.Array(
                    [SERVICE_UUID],
                    signature="s",
                ),
            }
        }

    @dbus.service.method(
        DBUS_PROP_IFACE,
        in_signature="s",
        out_signature="a{sv}",
    )
    def GetAll(self, interface):
        if interface != LE_ADVERTISEMENT_IFACE:
            raise dbus.exceptions.DBusException(
                "org.freedesktop.DBus.Error.InvalidArgs"
            )
        return self.get_properties()[LE_ADVERTISEMENT_IFACE]

    @dbus.service.method(LE_ADVERTISEMENT_IFACE)
    def Release(self):
        print("Advertisement released")

    def register(self, adapter):
        manager = dbus.Interface(
            self.bus.get_object(BLUEZ_SERVICE_NAME, adapter),
            LE_ADVERTISING_MANAGER_IFACE,
        )

        manager.RegisterAdvertisement(
            self.get_path(),
            {},
            reply_handler=lambda: print("BLE advertisement registered"),
            error_handler=lambda e: print(
                "BLE advertisement registration failed:", e
            ),
        )

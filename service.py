import dbus
import dbus.service
import dbus.mainloop.glib

from gi.repository import GLib

from bletools import (
    BLUEZ_SERVICE_NAME,
    DBUS_OM_IFACE,
    DBUS_PROP_IFACE,
    GATT_MANAGER_IFACE,
)

GATT_SERVICE_IFACE = "org.bluez.GattService1"
GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"

APP_PATH = "/org/bluez/nsw"
SERVICE_PATH = APP_PATH + "/service0"
RX_PATH = SERVICE_PATH + "/char0"
# TX_PATH = SERVICE_PATH + "/char1"

SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
RX_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
# TX_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"


class Application(dbus.service.Object):
    def __init__(self, bus):
        self.bus = bus
        self.services = []
        super().__init__(bus, APP_PATH)

    def get_path(self):
        return dbus.ObjectPath(APP_PATH)

    def add_service(self, service):
        self.services.append(service)

    @dbus.service.method(
        DBUS_OM_IFACE,
        out_signature="a{oa{sa{sv}}}",
    )
    def GetManagedObjects(self):
        response = {}

        for service in self.services:
            response[service.get_path()] = service.get_properties()

            for characteristic in service.characteristics:
                response[characteristic.get_path()] = (
                    characteristic.get_properties()
                )

        return response

    def register(self, adapter):
        manager = dbus.Interface(
            self.bus.get_object(BLUEZ_SERVICE_NAME, adapter),
            GATT_MANAGER_IFACE,
        )

        manager.RegisterApplication(
            self.get_path(),
            {},
            reply_handler=lambda: print("GATT application registered"),
            error_handler=lambda e: print(
                "GATT application registration failed:", e
            ),
        )

    def run(self):
        GLib.MainLoop().run()


class Service(dbus.service.Object):
    def __init__(self, bus, path, uuid, primary=True):
        self.bus = bus
        self.path = path
        self.uuid = uuid
        self.primary = primary
        self.characteristics = []
        super().__init__(bus, path)

    def get_path(self):
        return dbus.ObjectPath(self.path)

    def add_characteristic(self, characteristic):
        self.characteristics.append(characteristic)

    def get_properties(self):
        return {
            GATT_SERVICE_IFACE: {
                "UUID": dbus.String(self.uuid),
                "Primary": dbus.Boolean(self.primary),
                "Characteristics": dbus.Array(
                    [c.get_path() for c in self.characteristics],
                    signature="o",
                ),
            }
        }


class Characteristic(dbus.service.Object):
    def __init__(self, bus, path, uuid, flags, service):
        self.bus = bus
        self.path = path
        self.uuid = uuid
        self.flags = flags
        self.service = service
        super().__init__(bus, path)

    def get_path(self):
        return dbus.ObjectPath(self.path)

    def get_properties(self):
        return {
            GATT_CHRC_IFACE: {
                "Service": self.service.get_path(),
                "UUID": dbus.String(self.uuid),
                "Flags": dbus.Array(self.flags, signature="s"),
                "Descriptors": dbus.Array([], signature="o"),
            }
        }

    @dbus.service.method(
        DBUS_PROP_IFACE,
        in_signature="s",
        out_signature="a{sv}",
    )
    def GetAll(self, interface):
        if interface != GATT_CHRC_IFACE:
            raise dbus.exceptions.DBusException(
                "org.freedesktop.DBus.Error.InvalidArgs"
            )
        return self.get_properties()[GATT_CHRC_IFACE]


class RXCharacteristic(Characteristic):
    def __init__(self, bus, service):
        super().__init__(
            bus,
            RX_PATH,
            RX_UUID,
            ["write", "write-without-response"],
            service,
        )
        self.buffer = b""

    @dbus.service.method(
        GATT_CHRC_IFACE,
        in_signature="aya{sv}",
    )
    def WriteValue(self, value, options):
        data = bytes(value)

        if not data:
            return

        print(f"RX raw: {data!r}")
        self.buffer += data

        while b"\n" in self.buffer:
            line, self.buffer = self.buffer.split(b"\n", 1)
            line = line.strip()

            if not line:
                continue

            text = line.decode("utf-8", errors="replace")

            if text.startswith("GB("):
                print(f"📥 [Notification from Phone]: {text}")
            else:
                print(f"📥 [RX]: {text}")


# class TXCharacteristic(Characteristic):
#     def __init__(self, bus, service):
#         super().__init__(
#             bus,
#             TX_PATH,
#             TX_UUID,
#             ["read", "notify"],
#             service,
#         )
#         self.notifying = False
#         self.value = b""

#     @dbus.service.method(
#         GATT_CHRC_IFACE,
#         in_signature="a{sv}",
#         out_signature="ay",
#     )
#     def ReadValue(self, options):
#         return dbus.Array(self.value, signature="y")

#     @dbus.service.method(GATT_CHRC_IFACE)
#     def StartNotify(self):
#         if self.notifying:
#             return

#         self.notifying = True
#         print("TX notifications enabled")

#     @dbus.service.method(GATT_CHRC_IFACE)
#     def StopNotify(self):
#         self.notifying = False
#         print("TX notifications disabled")

#     @dbus.service.signal(
#         DBUS_PROP_IFACE,
#         signature="sa{sv}as",
#     )
#     def PropertiesChanged(self, interface, changed, invalidated):
#         pass

#     def notify(self, data):
#         if not self.notifying:
#             return

#         self.value = bytes(data)

#         self.PropertiesChanged(
#             GATT_CHRC_IFACE,
#             {"Value": dbus.Array(self.value, signature="y")},
#             [],
#         )


class NotificationService(Service):
    def __init__(self, bus):
        super().__init__(
            bus,
            SERVICE_PATH,
            SERVICE_UUID,
            True,
        )

        self.rx = RXCharacteristic(bus, self)
        # self.tx = TXCharacteristic(bus, self)

        self.add_characteristic(self.rx)
        # self.add_characteristic(self.tx)

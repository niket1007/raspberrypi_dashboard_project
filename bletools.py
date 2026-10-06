import dbus
import dbus.exceptions

BLUEZ_SERVICE_NAME = "org.bluez"
ADAPTER_IFACE = "org.bluez.Adapter1"
GATT_MANAGER_IFACE = "org.bluez.GattManager1"
LE_ADVERTISING_MANAGER_IFACE = "org.bluez.LEAdvertisingManager1"
AGENT_MANAGER_IFACE = "org.bluez.AgentManager1"
DBUS_OM_IFACE = "org.freedesktop.DBus.ObjectManager"
DBUS_PROP_IFACE = "org.freedesktop.DBus.Properties"


class InvalidArgsException(dbus.exceptions.DBusException):
    _dbus_error_name = "org.freedesktop.DBus.Error.InvalidArgs"


class NotSupportedException(dbus.exceptions.DBusException):
    _dbus_error_name = "org.bluez.Error.NotSupported"


class BleTools:
    @staticmethod
    def get_bus():
        return dbus.SystemBus()

    @staticmethod
    def find_adapter(bus):
        om = dbus.Interface(
            bus.get_object(BLUEZ_SERVICE_NAME, "/"),
            DBUS_OM_IFACE,
        )

        objects = om.GetManagedObjects()

        for path, props in objects.items():
            if (
                GATT_MANAGER_IFACE in props
                and LE_ADVERTISING_MANAGER_IFACE in props
            ):
                return path

        raise RuntimeError("No BlueZ LE GATT/advertising adapter found")

    @staticmethod
    def power_adapter(bus, adapter):
        props = dbus.Interface(
            bus.get_object(BLUEZ_SERVICE_NAME, adapter),
            DBUS_PROP_IFACE,
        )
        props.Set(ADAPTER_IFACE, "Powered", dbus.Boolean(True))

    @staticmethod
    def register_agent(bus, agent):
        manager = dbus.Interface(
            bus.get_object(BLUEZ_SERVICE_NAME, "/org/bluez"),
            AGENT_MANAGER_IFACE,
        )

        try:
            manager.RegisterAgent(agent.get_path(), "NoInputNoOutput")
            print("BlueZ agent registered")
        except dbus.exceptions.DBusException as e:
            print("Agent registration failed:", e)
            return

        try:
            manager.RequestDefaultAgent(agent.get_path())
            print("BlueZ agent is default agent")
        except dbus.exceptions.DBusException as e:
            print("Could not make agent default:", e)


class Agent(dbus.service.Object):
    AGENT_IFACE = "org.bluez.Agent1"

    def __init__(self, bus, path):
        self.bus = bus
        self.path = path
        super().__init__(bus, path)

    def get_path(self):
        return dbus.ObjectPath(self.path)

    @dbus.service.method(AGENT_IFACE)
    def Release(self):
        print("BlueZ agent released")

    @dbus.service.method(AGENT_IFACE, in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        raise dbus.exceptions.DBusException("org.bluez.Error.Rejected")

    @dbus.service.method(AGENT_IFACE, in_signature="ou")
    def DisplayPinCode(self, device, pincode):
        print(f"Pairing PIN: {int(pincode):06d}")

    @dbus.service.method(AGENT_IFACE, in_signature="o", out_signature="u")
    def RequestPasskey(self, device):
        raise dbus.exceptions.DBusException("org.bluez.Error.Rejected")

    @dbus.service.method(AGENT_IFACE, in_signature="ouq")
    def DisplayPasskey(self, device, passkey, entered):
        print(
            f"Pairing passkey: {int(passkey):06d} "
            f"(entered={int(entered)})"
        )

    @dbus.service.method(AGENT_IFACE, in_signature="ou")
    def RequestConfirmation(self, device, passkey):
        print(
            f"Pairing confirmation requested for "
            f"{int(passkey):06d}; accepting"
        )

    @dbus.service.method(AGENT_IFACE, in_signature="o")
    def RequestAuthorization(self, device):
        print("Pairing authorization requested; accepting")

    @dbus.service.method(AGENT_IFACE, in_signature="os")
    def AuthorizeService(self, device, uuid):
        print(f"Service authorization requested: {uuid}; accepting")

    @dbus.service.method(AGENT_IFACE)
    def Cancel(self):
        print("Pairing cancelled")

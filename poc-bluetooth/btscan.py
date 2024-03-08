import bluetooth

devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)

for addr, name in devices:
    print("Name: {} \t Addr: {}".format(name, addr))

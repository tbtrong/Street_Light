from digi.xbee.devices import XBeeDevice
from time import strftime, sleep

#Setting the baud rate
Baud_Rate = 9600

REMOTE_NODE_ID = "XBEE_A"


def main():
    Number = 0
    while(1):
        try:
            Port = "/dev/ttyUSB" + str(Number)
            device = XBeeDevice(Port, Baud_Rate)
            device.open()

            # Obtain the remote XBee device from the XBee network.
            xbee_network = device.get_network()
            remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
            if remote_device is None:
                print("Could not find the remote device")
                exit(1)
            time_string = strftime('%H:%M')
            if time_string == "14:26":# Set up time
                device.send_data(remote_device, "1/80")
                sleep(1)
                device.send_data(remote_device, "2/50")
                sleep(10)
            if time_string == "14:27":
                device.send_data(remote_device, "1/30")
                sleep(1)
                device.send_data(remote_device, "2/20")
                sleep(10)
            if time_string == "14:28":
                device.send_data(remote_device, "1/0")
                sleep(1)
                device.send_data(remote_device, "2/0")
                sleep(10)
        except:
            Number = Number + 1
        finally:
            if device is not None and device.is_open():
                device.close()

if __name__ == '__main__':
    main()

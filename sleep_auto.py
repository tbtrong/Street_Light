from digi.xbee.devices import XBeeDevice
from time import strftime, sleep


###Xbee Port
##Port = 'COM6'
#Setting the baud rate
Baud_Rate = 9600

REMOTE_NODE_ID = "XBEE_A"


def main():
    Number = 0
    while 1:
        try:
            Port = "COM" + str(Number)
            device = XBeeDevice(Port, Baud_Rate)
            device.open()

            # Obtain the remote XBee device from the XBee network.
            xbee_network = device.get_network()
            remote_device = xbee_network.discover_device(REMOTE_NODE_ID)
            if remote_device is None:
                print("Could not find the remote device")
                exit(1)
            device.send_data(remote_device, "1/100")
            sleep(1)
            device.send_data(remote_device, "2/100")
            
            sleep(1)

            device.send_data(remote_device, "1/70")
            sleep(1)
            device.send_data(remote_device, "2/60")
            
            sleep(1)
            
            device.send_data(remote_device, "1/50")
            sleep(1)
            device.send_data(remote_device, "2/40")
                    
            sleep(1)
            
            device.send_data(remote_device, "1/30")
            sleep(1)
            device.send_data(remote_device, "2/20")
                            
            sleep(1)
            
            device.send_data(remote_device, "1/0")
            sleep(1)
            device.send_data(remote_device, "2/0")
            sleep(7)
        except:
            Number = Number + 1
        finally:
            if device is not None and device.is_open():
                device.close()

if __name__ == '__main__':
    main()


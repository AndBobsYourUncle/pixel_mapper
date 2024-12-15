import sacn
import time

sender = sacn.sACNsender()  # provide an IP-Address to bind to if you want to send multicast packets from a specific interface
sender.start()  # start the sending thread
# sender.activate_output(1)  # start sending out data in the 1st universe
# sender[1].multicast = True  # set multicast to True
# sender[1].destination = "192.168.20.100"  # or provide unicast information.
# Keep in mind that if multicast is on, unicast is not used

number_pixels = 500

number_universes = number_pixels // 170

universes = []

for i in range(number_universes+1):
    universes.append([])

    sender.activate_output(i+1)
    sender[i+1].destination = "192.168.20.100"

for i in range(number_pixels):
    universes[i // 170] += [255, 255, 255]

for i in range(number_universes+1):
    print("Universe: ", i+1, "Length: ", len(universes[i]))

    sender[i+1].dmx_data = tuple(universes[i])

time.sleep(10)  # send the data for 10 seconds
sender.stop()  # do not forget to stop the sender

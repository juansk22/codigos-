import network, time, urequests
from machine import Pin,ADC
from dht import DHT11

sensorDHT = DHT11(Pin(15))




def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True



if conectaWifi ("INFORMATICA2", "Adminredp2017"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    url = "https://api.thingspeak.com/update?api_key=2JK7MT71JGI27V3J&field1=0 "  
    
    while (True):
        time.sleep(1)
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity()
        kelvin = temp + 273
        far = (temp*9)/5 + 32

        print("T={:02d}C H={:02d}%  K= {:02d}k F={:02}".format(temp, hum, kelvin,far))


        respuesta = urequests.get(url+"&field1="+str(temp)+"&field2="+str(hum)+"&field3="+str(kelvin)+"&field4="+str(far))
        print(respuesta.text)
        print (respuesta.status_code)
        respuesta.close ()
 
else:
       print ("Imposible conectar")
       miRed.active (False)
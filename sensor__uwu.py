import network, time, urequests
from machine import Pin,ADC


sensor = ADC(Pin(36))
led = Pin(15, Pin.OUT)

file = open("lectura.csv","w")


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
      
    url = "https://api.thingspeak.com/update?api_key=VMCXBE8MWCXGT52I"  
    
    while (True):
       
        lectura = (sensor.read_u16())
        time.sleep(0.25)
        print ("Lectura ={:02d}".format (lectura))



        file.write(str("lectura ={:02d}".format (lectura) ))
        file.flush()
        
        respuesta = urequests.get(url+"&field1="+str(lectura))
        print(respuesta.text)
        print (respuesta.status_code)
        respuesta.close ()
 
else:
       print ("Imposible conectar")
       miRed.active (False)
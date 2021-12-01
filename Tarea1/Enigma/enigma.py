#!/usr/bin/env python
# coding: utf-8

# # Tareas de SPSI
# 
# > Grupo 22
# >
# > Ana Buendía Ruiz-Azuaga
# >
# > Paula Villanueva Núñez

# ## Tarea 2
# **Máquina Enigma**

# In[1]:


import sys


# In[2]:


ANILLO_BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# In[3]:


class Rotor:
    def __init__(self, notch, ringstellung, wiring):
        '''
        Constructor de la clase Rotor, recibe el notch, ringstelling y wiring de un rotor
        '''
        self.anillo = ANILLO_BASE
        self.notch = notch
        self.ringstellung = ringstellung
        self.wiring = wiring

        
    def aplicar_ringstellung(self, ringstellung):
        '''
        Metodo para aplicar el ringstellung al rotor
        '''
        indice_anillo = ANILLO_BASE.find(ringstellung)
        
        self.wiring = list(self.wiring)
        
        # Vamos reemplazando el wiring
        for i in range (0, len(self.wiring)):
            indice = ANILLO_BASE.find(self.wiring[i]) + indice_anillo
            self.wiring[i] = ANILLO_BASE[indice % 26]
            
        # Convertimos el wiring a cadena de nuevo   
        cadena = ""
        for c in self.wiring:
            cadena += c
        
        self.wiring = cadena
        # Colocamos el wiring para que empiece por la posicion adecuada
        self.wiring = self.wiring[-indice_anillo:]+self.wiring[:-indice_anillo]
        
        
        self.ringstellung = ringstellung
        
    
    def aplicar_grundstellung(self, grundstellung):
        '''
        Metodo para aplicar grundstellung al rotor
        '''
        
        # Estar en la ventanita es estar al principio de la cadena
        indice = self.anillo.find(grundstellung)
        
        self.anillo = self.anillo[indice:] + self.anillo[:indice]
        self.wiring = self.wiring[indice:] + self.wiring[:indice]
        

    def cifrar_caracter(self, car):
        '''
        Metodo para cifrar un caracter con un rotor
        Devuelve el caracter cifrado
        '''
        # Guardo posicion de la letra en el alfabeto
        indice = ANILLO_BASE.find(car)
        
        # Accedemos a wiring de la letra
        letra = self.wiring[indice]
        
        # Convertimos la letra segun corresponde en wiring
        ind = self.anillo.find(letra)
        
        return ANILLO_BASE[ind]
    
    def inv_cifrar_caracter(self, car):
        '''
        Metodo para cifrar un caracter en sentido inverso usando un rotor
        Devuelve el caracter cifrado
        '''
        # Guardo posicion de la letra en el alfabeto
        indice = ANILLO_BASE.find(car)
        
        # Accedemos a wiring de la letra
        letra = self.anillo[indice]
        
        # Convertimos la letra segun corresponde en wiring
        ind = self.wiring.find(letra)
        
        return ANILLO_BASE[ind]
    
    def rotar(self):
        '''
        Metodo para rotar un rotor una posicion
        '''
        # Avanzo anillo y wiring una posicion
        self.anillo = self.anillo[1:] + self.anillo[:1]
        self.wiring = self.wiring[1:] + self.wiring[:1]

    
    def comprobar_vuelta_completa(self):
        '''
        Metodo que comprueba si el rotor ha dado una vuelta completa.
        Devuelve true si la ha dado, false si no
        '''
        # Dar vuelta completa es que el caracter de la ventana esté en el notch
        return self.anillo[0] in self.notch


# In[4]:


ROTOR_I = {"notch": "Q", "ringstellung": "A", "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ"}
    
ROTOR_II = {"notch": "E", "ringstellung": "A", "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE"}
    
ROTOR_III = {"notch": "V", "ringstellung": "A", "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO"}
    
ROTOR_IV = {"notch": "J", "ringstellung": "A", "wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB"}
    
ROTOR_V = {"notch": "Z", "ringstellung": "A", "wiring": "VZBRGITYUPSDNHLXAWMJQOFECK"}
    
ROTOR_VI = {"notch": "ZM", "ringstellung": "A", "wiring": "JPGVOUMFYQBENHZRDKASXLICTW"}
    
ROTOR_VII = {"notch": "ZM", "ringstellung": "A", "wiring": "NZJHGRCXMYSWBOUFAIVLPEKQDT"}
    
ROTOR_VIII = {"notch": "ZM", "ringstellung": "A", "wiring": "FKQHTLXOCBJSPDZRAMEWNIUYGV"}
    
ROTOR_BETA = {"notch": "", "ringstellung": "A", "wiring": "LEYJVCNIXWPBQMDRTAKZGFUHOS"}
    
ROTOR_GAMMA = {"notch": "", "ringstellung": "A", "wiring": "FSOKANUERHMBTIYCWLQPZXVGJD"}


# In[5]:


class Reflector:
    
    def __init__(self, config_reflector):
        '''
        Constructor de la clase Reflector, recibe el wiring del reflector
        '''
        self.reflector = list(config_reflector)
        
    def reflejar(self, car):
        '''
        Metodo para reflejar (cifrar) un caracter usando el reflector
        '''
        indice = ANILLO_BASE.find(car)
        
        # Accedemos a wiring de la letra
        letra = self.reflector[indice]
        
        # Convertimos la letra segun corresponde en wiring
        ind = ANILLO_BASE.find(letra)
        return ANILLO_BASE[ind]


# In[6]:


REFLECTOR_B = {"reflector": "YRUHQSLDPXNGOKMIEBFZCWVJAT"}
    
REFLECTOR_C = {"reflector": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}
    
REFLECTOR_B_THIN = {"reflector": "ENKQAUYWJICOPBLMDXZVFTHRGS"}
    
REFLECTOR_C_THIN = {"reflector": "RDOBJNTKVEHMLFCWZAXGYIPSUQ"}


# In[7]:


class Plugboard:
    def __init__(self, sustituciones):
        '''
        Constructor de PLugboard, recibe una lista de las sustituciones en el teclado
        '''
        parejas = sustituciones.split(" ")
        
        self.mapa = {}
        
        # Asignamos cada letra consigo misma
        for letra in ANILLO_BASE:
            self.mapa[letra] = letra
        # Intercambiamos las letras indicadas
        for elem in parejas:
            self.mapa[elem[0]] = elem[1]
            self.mapa[elem[1]] = elem[0]
    
    def sustituir_letra(self, car):
        '''
        Metodo para sustituir una letra por su letra correspondiente
        '''
        return self.mapa[car]


# In[8]:


class MaquinaEnigmaM4:
    '''Clase para modelar máquina enigma  Wehrmacht con posibilidad de simular una Kriegsmarine'''
    
    def __init__(self, reflector, rotores, ringstellung, grundstellung, clavijas):
        '''Constructor de la clase con el modelo de la maquina, configuracion inicial de los rotores y reflector'''
        
        if len(rotores) != 4 or len(rotores) != len(ringstellung) or len(rotores) != len(grundstellung):
                sys.exit("Error, la máquina Kriegsmarine M4 no puede tener un número de rotores distinto de 4 o las especiifcaciones de ringstellung y grundstellung no se corresponden con los rotores ")
        
        # Invierto vectores para hacer más comoda la iteración
        rotores = rotores[::-1]
        ringstellung = ringstellung[::-1]
        grundstellung = grundstellung[::-1]
        
        
        # Añado rotores a maquina enigma
        self.rotores = []
        for rotor in rotores:
            self.rotores.append(Rotor(rotor['notch'], rotor['ringstellung'], rotor['wiring']))
        
        # Añado ringstellung
        self.ringstellung = ringstellung
        
        # Aplico ringstellung a cada rotor
        for i in range(0, len(ringstellung)):
            self.rotores[i].aplicar_ringstellung(self.ringstellung[i])
        
        # Añado grunstellung
        self.grundstellung = grundstellung
        
        # Aplico grundstellung a cada rotor
        for i in range(0, len(grundstellung)):
            self.rotores[i].aplicar_grundstellung(self.grundstellung[i])
        
        # Añado clavijas
        self.clavijas = clavijas
        self.plugboard = Plugboard(self.clavijas)
        
        # Añado reflector
        self.reflector = Reflector(reflector['reflector'])
    
    
    def cifrar_caracter(self, car):
        '''
        Metodo para cifrar un carater usando la maquina enigma
        '''
        # Aplico plugboard
        car = self.plugboard.sustituir_letra(car)
        
        # Comprobar si los rotores necesitan girar. El ultimo rotor no gira
        girar = [True, False, False, False]
        
        for i in range(0, len(girar)-1):
            if self.rotores[i].comprobar_vuelta_completa():
                girar[i+1] = True
                
        for i in range(0, len(girar)-1):
            if girar[i]:
                self.rotores[i].rotar()
    
        # Rotación doble del segundo rotor
        if girar[2]:
            self.rotores[1].rotar()
        
        # Cifro caracter en cada rotor
        for rotor in self.rotores:
            car = rotor.cifrar_caracter(car)
            
        # Reflejo caracter
        car = self.reflector.reflejar(car)
        
        # Cifro caracter inversamente en cada rotor
        for rotor in reversed(self.rotores):
            car = rotor.inv_cifrar_caracter(car)
        
        # Aplico plugboard
        car = self.plugboard.sustituir_letra(car)
        
        return car
    
    def cifrar(self, texto):
        '''
        Metodo para cifrar un texto
        '''
        # Inicializamos el texto cifrado como la cadena vacía
        texto_cifrado = ""
        
        # Ciframos caracter a caracter y vamos añadiendolo al texto cifrado
        for car in texto:
            if (car != " "):
                texto_cifrado += self.cifrar_caracter(car)
            
        return texto_cifrado
    
    
        


# ## Tarea 3
# 
# **Descifrando el texto con la máquina enigma M4**

# In[9]:


# Establecemos los parametros de la enigma
reflector = REFLECTOR_C_THIN
rotores = [ROTOR_BETA, ROTOR_V, ROTOR_VI, ROTOR_VIII]
ringstellung = "EPEL"
grundstellung = "NAEM"
steckern = "AE BF CM DQ HU JN LX PR SZ VW"

# Declaramos maquina enigma
maquina = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

# Obtenemos nuevo grundstellung
nuevo_grundstellung = "QEOB"
grundstellung = maquina.cifrar(nuevo_grundstellung)

# Configuramos la nueva Enigma con el grundstellung que hemos obtenido
enigma = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

mensaje = "DUHF TETO LANO TCTO UARB BFPM HPHG CZXT DYGA HGUF XGEW KBLK GJWL QXXT GPJJ AVTO CKZF SLPP QIHZ FXOE BWII EKFZ LCLO AQJU LJOY HSSM BBGW HZAN VOII PYRB RTDJ QDJJ OQKC XWDN BBTY VXLY TAPG VEAT XSON PNYN QFUD BBHH VWEP YEYD OHNL XKZD NWRH DUWU JUMW WVII WZXI VIUQ DRHY MNCY EFUA PNHO TKHK GDNP SAKN UAGH JZSM JBMH VTRE QEDG XHLZ WIFU SKDQ VELN MIMI THBH DBWV HDFY HJOQ IHOR TDJD BWXE MEAY XGYQ XOHF DMYU XXNO JAZR SGHP LWML RECW WUTL RTTV LBHY OORG LGOW UXNX HMHY FAAC QEKT HSJW DUHF TETO"

# Quitar 8 ultimos caracteres y 8 primeros, con espacios   
mensaje = mensaje[10:len(mensaje)-10]

# Ciframos el mensaje
mensaje_cifrado = enigma.cifrar(mensaje)


print(f"\nMensaje original:\n {mensaje}")
print(f"\nMensaje cifrado:\n {mensaje_cifrado}")


# ### Cómo es compatible con la Máquina Enigma M3
# 
# La M4 configurada con el reflector B_Thin y rueda griega Beta en posición A y Ringstellung A, simula la M3 con reflector B. Por otra parte si es configurada con el reflector C_Thin y rueda griega Gamma en posición A y Ringstellung A, simula la M3 con reflector C.

# ## Tarea 4
# 
# **Protocolo de uso de la enigma que haga que el receptor sepa a quién de su unidad debe dirigir el mensaje recibido, que no sea capaz de leer su contenido y que sin embargo el oficial receptor sí pueda hacerlo por sus propios medios**

# Para enviar un mensaje desde tierra usando una máquina M3 a una máquina M4, teniendo como destinatario una persona determinada. Es importante que ninguna persona salvo a la que va dirigida el mensaje pueda entenderlo, pero sepa a quién se lo debe transmitir y este pueda descifrarlo.
# 
# Para lograr esto, vamos a cifrar el mensaje dos veces con distintas configuraciones. La primera vamos a cifrar el mensaje privado usando una configuración secreta para cualquiera salvo para el emisor y receptor. Después, en la segunda, al mensaje previamente cifrado se añadirá la información del destinatario, es decir, a quién va dirigido el mensaje real. Ciframos este mensaje con al configuración del día, conocida por todos. 

# Paula está en un submarino, y Ana está en tierra. Ana quiere mandarle el mensaje "Hay un traidor en tu tripulación, está planeando un motín".
# 
# La configuración privada que solo conocen Ana y Paula de la máquina Enigma es:
# 
# 
# Rueda griega: Beta
# 
# Rotores: II, IV, I
# 
# Reflector: B_thin
# 
# Ringstellung: AAAA
# 
# Grundstellung: AAAA
# 
# Clavijas: AT BL DF GJ HM NW OP QY RZ VX
# 
# Clave del mensaje: NANA

# In[10]:


# Establecemos los parametros de la enigma
reflector = REFLECTOR_B_THIN
rotores = [ROTOR_BETA, ROTOR_II, ROTOR_IV, ROTOR_I]
ringstellung = "AAAA"
grundstellung = "AAAA"
steckern = "AT BL DF GJ HM NW OP QY RZ VX"

# Declaramos maquina enigma
maquina = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

# Usamos la clave para obtener el grundstellung
nuevo_grundstellung = "NANA"
grundstellung = maquina.cifrar(nuevo_grundstellung)

# Configuramos la nueva Enigma con el grundstellung que hemos obtenido
enigma = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

mensaje = "HAY UN TRAIDOR EN TU TRIPULACION X ESTA PLANEANDO UN MOTIN XX"

# Formateamos el mensaje en grupos de 4 caracteres
mensaje = "HAYU NTRA IDOR ENTU TRIP ULAC IONX ESTA PLAN EAND OUNM OTIN XX"

mensaje_cifrado = enigma.cifrar(mensaje)

# Añadimos caracteres de verificacion
verificacion = " BANA ANAN "

mensaje_cifrado = verificacion + mensaje_cifrado + verificacion 

print(f"\nMensaje original:\n {mensaje}")
print(f"\nMensaje cifrado:\n {mensaje_cifrado}")


# Ahora añadimos al mensaje cifrado resultante el destinatario al que va dirigido y lo ciframos con la configuración del día.
# 
# Rueda griega: Gamma
# 
# Rotores: IV, III, VIII
# 
# Reflector: C_thin
# 
# Ringstellung: AAAA
# 
# Grundstellung: AAAA
# 
# Clavijas: CH EJ NV OU TY LG SZ PK DI QB
# 
# Clave: PUPU

# In[11]:


# Establecemos los parametros de la enigma
reflector = REFLECTOR_C_THIN
rotores = [ROTOR_GAMMA, ROTOR_IV, ROTOR_III, ROTOR_VIII]
ringstellung = "AAAA"
grundstellung = "AAAA"
steckern = "AT BL DF GJ HM NW OP QY RZ VX"

# Declaramos maquina enigma
maquina = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

# Usamos la clave para obtener el grundstellung
nuevo_grundstellung = "PUPU"
grundstellung = maquina.cifrar(nuevo_grundstellung)

# Configuramos la nueva Enigma con el grundstellung que hemos obtenido
enigma = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

mensaje = "PARA LA OFICIAL PAULA XX " + mensaje_cifrado

mensaje_cifrado2 = enigma.cifrar(mensaje)

#Añadimos los caracteres de verificacion

verificacion = " JAJA JEJE "

mensaje_cifrado2 = verificacion + mensaje_cifrado2 + verificacion


print(f"\nMensaje original:\n {mensaje}")
print(f"\nMensaje cifrado:\n {mensaje_cifrado2}")


# El mensaje cifrado "ZOIEKWJYXQQFQBTXIMDSBNRRVXOCKMEIOPGWSQDLDPFUZKSTXDODQIOHSTPHNQHJMVTZHG" es el que vamos a enviar al submarino. Este mensaje llega al receptor que descifra todos los mensajes. El operario recibe el mensaje y se dispone a descifrarlo con los parámetros del día, obteniendo así lo siguiente:

# In[12]:


# Establecemos los parametros de la enigma
reflector = REFLECTOR_C_THIN
rotores = [ROTOR_GAMMA, ROTOR_IV, ROTOR_III, ROTOR_VIII]
ringstellung = "AAAA"
grundstellung = "AAAA"
steckern = "AT BL DF GJ HM NW OP QY RZ VX"

# Declaramos maquina enigma
maquina = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

# Usamos la clave para obtener el grundstellung
nuevo_grundstellung = "PUPU"
grundstellung = maquina.cifrar(nuevo_grundstellung)

# Configuramos la nueva Enigma con el grundstellung que hemos obtenido
enigma = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

# Quitar 8 ultimos caracteres y 8 primeros   
mensaje = mensaje_cifrado2[10:len(mensaje_cifrado2)-10]

mensaje_descifrado2 = enigma.cifrar(mensaje)


print(f"\nMensaje original:\n {mensaje}")
print(f"\nMensaje cifrado:\n {mensaje_descifrado2}")


# De esta forma el receptor al descifrar el mensaje puede ver un mensaje dirigido a la oficial Paula, pero no el mensaje en sí. El operario le pasa a Paula el mensaje, que en privado en su habitación lo descifra con las claves privadas de las que dispone.

# In[13]:


# Establecemos los parametros de la enigma
reflector = REFLECTOR_B_THIN
rotores = [ROTOR_BETA, ROTOR_II, ROTOR_IV, ROTOR_I]
ringstellung = "AAAA"
grundstellung = "AAAA"
steckern = "AT BL DF GJ HM NW OP QY RZ VX"

# Declaramos maquina enigma
maquina = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

# Usamos la clave para obtener el grundstellung
nuevo_grundstellung = "NANA"
grundstellung = maquina.cifrar(nuevo_grundstellung)

# Configuramos la nueva Enigma con el grundstellung que hemos obtenido
enigma = MaquinaEnigmaM4(reflector, rotores, ringstellung, grundstellung, steckern)

# Eliminamos la parte del mensaje de "Para la oficial PaulaXX", es decir, nos quedamos con el mensaje cifrado del prinicipio
indice = mensaje_descifrado2.find('XX')
mensaje = mensaje_descifrado2[indice+2:]


# Quitar 8 ultimos caracteres y 8 primeros  
mensaje = mensaje[8:len(mensaje)-8]

mensaje_descifrado = enigma.cifrar(mensaje)


print(f"\nMensaje original:\n {mensaje}")
print(f"\nMensaje cifrado:\n {mensaje_descifrado}")


# Así, Paula ha recibido el mensaje de Ana sin que nadie, ni siquiera el operario que cifra o descifra los mensajes, pueda leer su contenido y evita el motín.

# In[ ]:





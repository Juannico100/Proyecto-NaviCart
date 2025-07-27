
from HC1SR04 import HCSR04
from machine import Pin,PWM
import time
from math import sin,radians

sensor = HCSR04(trigger_pin = 23, echo_pin = 22)
pm1,pm2,pm3,pm4 = (2,4,16,17)

in1 = Pin(pm1,mode = Pin.OUT)
in2 = Pin(pm2,mode = Pin.OUT)
in3 = Pin(pm3,mode = Pin.OUT)
in4 = Pin(pm4,mode = Pin.OUT)
boton_boot = Pin(0, Pin.IN, Pin.PULL_UP)

def distancia():
    return sensor.distance_cm()

def motor_1_adelante():
    in1.value(0)
    in2.value(1)


def motor_2_adelante():
    in3.value(1)
    in4.value(0)
    
    
def motor_1_atras():
    in1.value(1)
    in2.value(0)


def motor_2_atras():
    in3.value(0)
    in4.value(1)

def calibrar():
    
    d0 = distancia()
    #print(distancia())
    
    motor_1_adelante()
    motor_2_adelante()
    
    time.sleep(1)
    
    d1 = distancia()
    #print(distancia())
    
    velocidad = (d0 - d1)
    #print(velocidad)
    
    d0 = distancia()
    #print(distancia())
    
    time.sleep(0.1)
    
    motor_1_atras()
    motor_2_atras()
    
    time.sleep(1)
    
    d1 = distancia()
    #print(distancia())
    
    velocidad = ((d1-d0)+velocidad)/2
    
    detener()
    #print("\n",velocidad)
    
    return velocidad



def girar_derecha(angulo):
    
    r = 5
    rad = (3.141592 * angulo)/180
    s = (r * rad)/vel
    
    motor_1_adelante()
    motor_2_atras()
    time.sleep(s)
    
    detener()
    
def girar_izquierda(angulo):
    
    r = 5
    rad = (3.141592 * angulo)/180
    s = (r * rad)/vel
    
    motor_1_atras()
    motor_2_adelante()
    time.sleep(s)
    
    detener()

def avanzar(distancia):

    s = distancia/vel
    motor_1_adelante()
    motor_2_adelante()
    time.sleep(s)
    
    detener()
    
def detener():
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)

time.sleep(5)

vel = calibrar()


time.sleep(1)

total = 30

n = total //10

for i in range(n):
    avanzar(10)
    time.sleep(0.12)
    distancia = sensor.distance_cm()
    #print(distancia)
    
    if distancia < 30:
        detener()
        flag = True
        medida = 0
        i = 0
        
        while flag or medida < 2 * distancia:
            flag = False
            girar_izquierda(5)
            medida = sensor.distance_cm()
            #print(medida)
            i += 1
        
        girar_izquierda(5)
        avanzar(distancia * 2)
        
        girar_derecha(i * 5 +5)
        avanzar(5)
        girar_derecha(90)
        cateto = ((distancia) * sin(radians(i * 5 +5 )))
        
        avanzar(cateto)
        
        girar_izquierda(90)
        
        avanzar(total - distancia - 5)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(false)

TRIG = 23
ECHO = 24
BUZZ = 4

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(BUZZ,GPIO.OUT)

def buzzer():
	GPIO.output(BUZZ,GPIO.HIGH)
	print("Bip")
	time.sleep(delay)
	GPIO.output(BUZZ.GPIO.LOW)
	print("Bip yok")
	time.sleep(delay)
	
while True:
	GPIO.output(TRIG, False)
	print("Olculuyor...")
	time.sleep(0.1)
	
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	
	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()
	
	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()
		pulse_duration = pulse_end - pulse_start
		
		distance = pulse_duration * 17150
		distance = round(distance, 2)
        
	if distance > 2 and distance < 10:
		print("Mesafe:",distance - 0.5,"cm")
		GPIO.output(BUZZ, GPIO.HIGH)
	elif distance > 10 and distance < 20:
		print("Mesafe:",distance - 0.5,"cm")
		delay=0.02
		buzzer()
	elif distance > 20 and distance < 30:
		print("Mesafe:",distance - 0.5,"cm")
		delay=0.03
		buzzer()
	elif distance > 30 and distance < 40:
		print("Mesafe:",distance - 0.5,"cm")
		delay=0.05
		buzzer()
	elif distance > 40 and distance < 50:
		print("Mesafe:",distance - 0.5,"cm")
		delay=0.075
		buzzer()
	elif distance > 50 and distance < 60:
		print("Mesafe:",distance - 0.5,"cm")
		delay=0.1
		buzzer()
	elif distance > 60 and distance < 70:
		print("Mesafe:",distance - 0.5,"cm")
		delay=0.125
		buzzer()
	elif distance > 70 and distance < 80:
		print("Mesafe:",distance - 0.5,"cm")
		delay=0.150
		buzzer()
		
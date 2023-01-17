import ctypes
import time

OLED = ctypes.CDLL('/home/gr3atj0b/pi_lcd/Ubuntu/OLED.so')

OLED.ssd1306_begin(0x00,0X3C)

while True:
	OLED.LCD_DisplayTemperature()
	time.sleep(3)
	OLED.LCD_DisPlayCpuMemory()
	time.sleep(3)
	OLED.LCD_DisplaySdMemory()
	time.sleep(3)


import board
import time
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.cursor = True

while True:
	lcd.clear()
	lcd.message = "Blue"
	lcd.color = [0, 0, 100]
	time.sleep(5)
	lcd.clear()
	lcd.message = "Pink!"
	lcd.color = [100, 0, 100]
	time.sleep(5)
	lcd.clear()
	lcd.message = "Yellow"
	lcd.color = [100, 100, 0]
	time.sleep(5)
	lcd.clear()
	lcd.message = "Full White"
	lcd.color = [100, 100, 100]
	time.sleep(5)

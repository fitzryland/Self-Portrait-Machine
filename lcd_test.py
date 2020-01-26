import board
import time
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.color = [100, 0, 100]
lcd.message = "BOOOOM!";

while True:
	lcd.clear()
	lcd.message = "Light Blue"
	lcd.color = [25, 25, 100]
	time.sleep(5)
	lcd.clear()
	lcd.message = "Pink!"
	lcd.color = [100, 0, 100]
	time.sleep(5)

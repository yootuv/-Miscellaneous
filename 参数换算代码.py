list = [192, 196, 200, 204, 208, 212, 216]
print("输入ADC：",end = '')
ADC = int(input())
print("输入SPI频率(MHz)：",end = '')
SPI = int(input())
for i in list:
    result = i**2 * ADC / (SPI*1000000)
    print(str(round(result * 1000,1))+'ms')


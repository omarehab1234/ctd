def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# for checking the mode is correct
def check():
    mode = 0
    print("mode 1 for celsius to fahrenheit\nmode 2 for fahrenheit to celsius\nmode 3 for exit")
    while(mode not in  [1,2,3]):
        try:
            mode = int(input("Enter mode from (1,2,3): "))
            if mode not in  [1,2,3]:
                raise ValueError("Invalid mode")
            else:
                return mode
        except ValueError as e:
            print(e)

cont = True

while(cont):
    mode = check()
    if mode == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}")
    elif mode == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}")
    else:
        cont = False

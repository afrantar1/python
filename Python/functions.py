import datetime

def sum_two_numbers(number_a, number_b): # dodelimo vrednosti spremenljivkama
    result = number_a + number_b

    def inner_function ():
        thing = "chair"
        print(thing)
        print(result)

    inner_function()

    return result
# zgoraj je definicija funkcije spodaj ko pa določimo vrednosti pa je klic



def turn_light_on():
    print("The light is turned on")
turn_light_on()

def get_current_time_formatted(label, time_now):
    #turn_light_on() # če dodamo še nekam drugam to ni več čista funkcija
    return f"{label}{datetime.datetime.now()}"

#time_now = datetime.datetime.now()
print(get_current_time_formatted("The time is: ", time_now))

my_age = 35
#print(result) to ni dostopno izven funkcije
result = 12 # nahaja se zunaj funkcije in ne deluje na funkcijo

print(sum_two_numbers(35, 5)) #informacije pošljemo v funkcijo - določitev obeh vrednosti in sprintam
print(result)


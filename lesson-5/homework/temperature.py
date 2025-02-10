from decimal import Decimal
def convert_cel_to_far(temp_in_cel):
    temp_in_far=temp_in_cel*9/5+32
    return "{:.2f}".format(round(temp_in_far,2))
def convert_far_to_cel(temp_in_far):
    temp_in_cel=(temp_in_far-32)*5/9
    return "{:.2f}".format(round(temp_in_cel,2))

temp_in_f=float(input("Enter a temperature in degrees F: "))
temp_in_c=convert_far_to_cel(temp_in_f)
print(temp_in_f,"degrees F =",temp_in_c,"degrees C")

temp_in_c=float(input("Enter a temperature in degrees C: "))
temp_in_f=convert_cel_to_far(temp_in_c)
print(temp_in_c,"degrees C =",temp_in_f,"degrees F")


# Assign num_int as 15. Display its datatype. Convert it to float and string, display again
num_int = 15
print(f"num_int: {num_int}, type: {type(num_int)}")

num_float = float(num_int)
print(f"num_float: {num_float}, type: {type(num_float)}")
num_str = str(num_int)
print(f"num_str: {num_str}, type: {type(num_str)}")



# Assign num_str as "25". Add 10 to it after data type conversion and print the result
num_str = "25"
result = int(num_str) + 10
print(f"Result: {result}")

# Assign float_num as 10.5. Convert it to string, add '10' and print the result
float_num = 10.5
result = str(float_num) + '10'
print(f"Result: {result}")

# Assign is_active as True. Convert it to string and print the result and its data type
is_active = True
is_active_str = str(is_active)
print(f"is_active_str: {is_active_str}, type: {type(is_active_str)}")

# Assign num_1 as '5' and num_2 as '2.5'. Convert both to float and print their sum
num_1 = '5'
num_2 = '2.5'
sum_result = float(num_1) + float(num_2)
print(f"Sum: {sum_result}")
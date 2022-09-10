print("coding tasks")

#------------------------------------------------------------------------------

'''
1. Implement palindrome using iterator(for loop) and generator mechanism.
'''

# def isPalindrome(str):
#
#     for i in range(0, int(len(str)/2)):
#
#         if str[i] != str[len(str)-i-1]:
#
#             return False
#         return True
#
# str = "nayan"
#
# print(isPalindrome(str))

#==============================================================================================================
# -----------------------------------------------------------------------------------------------------------

'''

2. Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9 
		         10 + 11 + 12 + 13
				 46
				 
'''

#
# def sum_of_digit(num1 , num2):
#     return int(num1) + int(num2)
#
# num1 = list(str(int(input("enter the first number: "))))
# num2 = list(str(int(input("enter the second number: "))))
#
# res = list(map(sum_of_digit, num1, num2))
# temp = 0
#
# for i in res:
#     temp = temp + i
# print("final output : ", temp)

#===================================================================================
'''
3. st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba
'''

#===================================================================================






#===================================================================================================
'''
4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format
'''


# from collections import Counter
# some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# counts = dict(Counter(some_list))
# duplicates = {key:value for key, value in counts.items() if value > 1}
# print(duplicates)

#=================================================================================================
'''
5. # t1 = (1, 2, 3, "a", "c") 
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")
'''

print(''*20, "5. ---------------", '' * 20)
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in lis2 and isinstance(i, int):
                lis2.append(i)
                lis1.append((t + i))
                break
    else:
        for i in t2:
            if i not in lis2 and isinstance(i, str):
                lis2.append(i)
                lis1.append((t + i))
                break

print(lis1)



#====================================================================================================
'''
6. #Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196
'''

# def remove_zero_from_ip(ip_address):
#
#     new_ip_add=".".join([str(int(i))for i in ip_address.split(".")])
#     return new_ip_add;
# print(remove_zero_from_ip("216.08.094.196"))


##=============================================================================================

'''
7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]

'''
#
# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# print(list(map(lambda  x:int(x),str(l).replace("[",'').replace("]","").split(","))))

#============================================================================================

'''
8. Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line 
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total 
'''

# st = "ab@#cd!ef"
#
#
# def reverseString(text):
#     index = -1
#     for ind in range(len(text) - 1, int(len(text) / 2), -1):
#
#         if text[ind].isalpha():
#             temp = text[ind]
#             while True:
#                 index += 1
#                 if text[index].isalpha():
#                     text[ind] = text[index]
#                     text[index] = temp
#                     break
#     return text
#
#
# ans = reverseString(list(st))
#
# print("Output : ", "".join(ans))






##=======================================================================================================

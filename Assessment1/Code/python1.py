

def one(input1, input2):
 a = [input1, input2]
 if len(a[0]) == len(a[1]):
    y = (a[0] + ' ' +  a[1])
 else:
    y = max(a , key = len)
 return y



 

def two(input):
    string = input.lower().split("bert")
    print(string)
    if len(string)%2 == 0:
        return ''
    else:
        return "".join(string[(int(len(string)/2))])



def three(arg1):
 
 if arg1 % 3 == 0 and arg1 % 5 == 0:
    return "fizzbuzz" 
 if arg1 % 3 == 0:
    return "fizz"
 if arg1 % 5 == 0:
    return "buzz"
 else:
    return "null"

	# <QUESTION 4>

    # Given a string seperate the string into the individual numbers present, then add each digit of each number to get a final value for each number

	# String example = "55 72 86"
	
	# "55" will = the integer 10
	# "72" will = the integer 9
	# "86" will = the integer 14
	
	# You then need to return the highest value, in the example above this would be 14.
	 
    # <EXAMPLES>

	# four("55 72 86") → 14
	# four("15 72 80 164") → 11
	# four("555 72 86 45 10") → 15

	# <HINT>

	# help(int) for working with numbers and help(str) for working with Strings.

def four(arg1):
 num = arg1.split()
 num = list(map(int, num)) 
 print(num)
 x =[]
 result = 0
 for i in num:
     y = i
     while y > 0:
         rem = y % 10
         result = result + rem
         y = int(y/10)
     x.append(y)
 print(x)
 return max(x)

	# <QUESTION 5>

    # Given a large string that represents a csv, the structure of each record will be as follows:
    
    # owner,nameOfFile,encrypted?,fileSize
    
    # "Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445"
    
    # For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    # Do not include duplicate names.
	# If all records are encrypted, return an empty Array.
    
    # <EXAMPLES>
    
    # five("Jeff,private.key,False,1445") → ["Jeff"]
	# five("Bert,private.key,True,1447,Bert,public.key,True,1318,Jeff,private.key,False,1445") → ["Jeff"]
	# five("Bert,private.key,False,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") → ["Bert","Jeff"]
    # five("Bert,private.key,True,1447,Bert,public.key,False,1318,Jeff,private.key,False,1445") → ["Bert","Jeff"]
    
	# <HINT>

	# Dont't forget, False is a String, not a Boolean value in the Tests above.

	# help(str) and help(list), you might also need to use a function that can create a list of numbers for you, try help(range).

def five(input):
	return []

	# <QUESTION 6>

    # There is a well known mnemonic which goes "I before E, except after C", which is used to determine which order "ei" or "ie" should be in a word.
    
    # Write a function which returns the boolean True if a string follows the mnemonic, and returns the boolean False if not.

	# <EXAMPLES>

    # six("ceiling") → True
    # six("believe") → True
    # six("glacier") → False
    # six("height") → False

	# <HINT>

	# Step through the logic here in order to solve the problem, you may find help(range) helpful.


def six(input):

    return False



def seven(word):
 x = list(word.lower())
 y = list("aeiou")
 count = 0
 for i in x:
    if i in y:
        count += 1
 return count



def eight(x):
    import math
    return math.factorial(x)



def nine (inputString, char):
 x = inputString.replace(" ","")
 x = list(x)
 y = 0
 for i in x:
    if i == char:
        y = x.index(i)
 if y > 0:
     return y+1
 else:
     return y-1 

 
def ten(string, value, char):
 x = string.lower()
 y = x.index(char) + 1
 if y == value:
    return True
 else:
    return False
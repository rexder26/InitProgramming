# Write a Program That Converts Number to Amharic Word.
# Thu Aug 18 07:24:48 PM EAT 2022
# Nathan Hailu , Insa Assignment #1

# Pseudo Code
# 1 We accept an input from the user with number.
# 2 We make a list of numberWords
# 3 we split user input in to 3 3 parts
# 4 we split the 3 part in 1 single integer 
# 5 we name the single integer based on the int place
# 6 combine the 3 3 parts together.
# 7 print it out with a final_result



# Lets Start Coding...


oneth = ['','አንድ', 'ሁለት', 'ሶስት', 'አራት', 'አምስት', 'ስድስት', 'ሰባት', 'ስምንት', 'ዘጠኝ']
tenth = ['አሥር', 'አስራ አንድ', 'አስራ ሁለት', 'አስራ ሶስት', 'አስራ አራት', 'አስራ አምስት', 'አስራ ስድስት', 'አስራ ሰባት', 'አስራ ስምንት', 'አስራ ዘጠኝ']
tenthPower = ['','','ሀያ', 'ሰላሳ', 'አርባ', 'ሀምሳ', 'ስልሳ', 'ሰባ', 'ሰማንያ', 'ዘጠና', 'መቶ']
HighNUM = ['', 'ሺህ', 'Million', 'Billion']

def converter(number, index):  # This will Do the processing of the numbers and assigning to the text
    
    if number=='0':
        return 'ዜሮ'    
   
    length = len(number) #count 
    
    number = number.zfill(3) #adds 3 zero       -> REMOVE THIS LINE---------------------- 
    print("========zero adding:",number,"========")   # -> REMOVE THIS LINE -----------------------
    words = ''
    print("100th-split1: ",int(number[0])) # -> REMOVE THIS LINE----------------------
    print("ten-split2: ",int(number[1])) # -> REMOVE THIS LINE--------------------
    print("one-split3: ",int(number[2]))   # -> REMOVE THIS LINE-------------------
    highDigit = int(number[0]) # split the input 1th place
    tenthDigit = int(number[1]) # split the input 10th place
    oneDigit = int(number[2]) # split the input 100th place
    
    if number[0] == '0':    # Converting the 1th place & if #1 is 0 remove it
        words += ''
    else:
        oneth[highDigit]
    print("======================")
    print("100th-word:",words)    # -> REMOVE THIS LINE------------------------
    words += ' መቶ ' if not words == '' else '' # add hundred to the word if it is not empty
    print("add-hundred-word:",words)    # -> REMOVE THIS LINE-------------------------
    print("======================")
    if(tenthDigit > 1): 
        words += tenthPower[tenthDigit] + ' '
        print("1st",words)  # -> REMOVE THIS LINE-------------------------
        words += oneth[oneDigit]
        print("2rd",words)  # -> REMOVE THIS LINE-------------------------
    elif(tenthDigit == 1):
        words += tenth[(int(tenthDigit + oneDigit) % 10) - 1] # adds the tenth and oneth digit, divide it to 10 and subsctract 1 from the the reminder.
        print("=============maths part==========")
        print("10th: ",tenthDigit)
        print("1th: ",oneDigit)                                         # what is the reminder of 4/10 2/10 3/10 5/10 /.....??
        print("Addition: ",int(tenthDigit + oneDigit))
        print("Reminder: ",int(tenthDigit + oneDigit)%10)                    #  This helps to know the 1st part of the text 11,000 ... 19,000 bc we have tenth place for them only we donr have 21,000 
        print("Substracted: ",(int(tenthDigit + oneDigit) % 10) - 1)
    elif(tenthDigit == 0):
        words += oneth[oneDigit]  # Jumps the tenth place if there is no tenth digit

    if(words.endswith('ዜሮ')):
        words = words[:-len('ዜሮ')]   # ??? what is endswith?
    else:
        words += ' '
     
    if(not len(words) == 0):    
        words += HighNUM[index]  # if the length of word is zero add '' to the word
        
    return words
    
def getWords(number):   # this will Do the Combining of the integers and the words together
    length = len(str(number))
    print("Length of the Number: ",length)
    if length>12:
        return 'This program supports upto አስራ ሁለት digit numbers.'
    
    if length % 3 == 0:         # sepatrate the text into 3 3 parts
        count = length // 3
    else:
        count = length // 3 + 1

    copy = count
    words = []  # Resets the words list
 
    for i in range(length-1, -1, -3):   # start from length-1 , decrease by 3 and stop before -1 returned 
        print("[@] looping:",i,"@@@@@@@@")
        words.append(converter(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))  #   ??  what is this part
        count -= 1
        print("listing the words: ", words)
    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp
    

    return final_words
# End Main Logic

# Reading number from user
number = int(input('Enter any number: '))

try:
    print("======================")
    print('"%d" in Amharic is Read As: "%s"' %(number, getWords(number)))
except ValueError:
    print('[x] Nothing is Entered to the place. Program Closeing...')



# In this file I am going to import moudules from my PhoneBook_Contact_info. 

print ("")

print ( """ Hello there, I am your digtal phonebook. Go ahead and enter who you are looking for. """ )

# Here I just imported the module

import PhoneBook_Contact_info

# In this section I just imported the varibles from my INFO PHONE BOOK FILE (name1) (name2) (name3) (name4) (name5)

policeofficer = PhoneBook_Contact_info.name1
Pizza73 = PhoneBook_Contact_info.name2
Uber = PhoneBook_Contact_info.name3
Clearviwe = PhoneBook_Contact_info.name4
Walmart = PhoneBook_Contact_info.name5

# In this code I am using the (input) statement.
 
find = ( input ( " Who are you looking for sir ? " ))

# And here I am using the (if) statement so the code can give you results as you ask for it.

if find == "policeofficer":
    print ( " Here is your contact info that you asked for: " , policeofficer )

# Finally the last code is a (else) statement to give a massege if what you looked for does not exist.

else:
    print ( " That contact does not exist sorry ! " )

find = ( input ( " Who else are you looking for sir ? " ))

if find == "Pizza73":
    print ( " Here is what you asked for: " , Pizza73 )

else:
    print ( " That contact does not exist sorry ! " )

find = ( input ( " Who else are you looking for sir ? " ))

if find == "Uber":
    print ( " Here are the results: " , Uber)

else:
    print ( " sorry we didn't find anything ! " )


find = ( input ( " Who else are you looking for ? " ))

if find == "Clearviwe":
    print ( " Here are the results: " , Clearviwe)

else:
    print ( " SORRY NO RESULTS ! " )

find = ( input ( " you have reached your limits for looking up contact information in our digital phone book, this is the last lookup for you ! " ))

if find == "Walmart":
    print ( " Here you go: " , Walmart)
    
else:
    print ( " No results found ! " )









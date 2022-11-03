def print_melon_delivery_report(delivery_file):
    """Function formats and prints text from a file.
    
    Function expects a str containing file name. The text from the file
    will be formatted and presented in the following fashion:

    'Delivered {10} {example melon}s for a total of ${1}.' 

    Note: Brackets included in example to indicate information taken from file."""

    delivery_report = open(delivery_file) #declare variable with the value of the opened file argument

    for line in delivery_report:    #loops throught lines of file
        line = line.rstrip()        #strips away blank space on the right for each line
        words = line.split('|')     #creates list of strings for each line, delimited by "|"

        #declares variables with the values of the items in the 'words' list, indicated by respective index
        melon = words[0]            
        count = words[1]
        amount = words[2]

        #prints formatted statement using information from each line of the file
        print(f"Delivered {count} {melon}s for total of ${amount}.")
    print()                     #prints line for readability
    delivery_report.close()     #closes the opened text file after all lines have been read

#following three code blocks print the day for each report and 
#then calls the print_melon_delivery_report function with that day's 
#report as the argument
print("Day 1")
print_melon_delivery_report("um-deliveries-day-1.txt")

print("Day 2")
print_melon_delivery_report("um-deliveries-day-2.txt")

print("Day 3")
print_melon_delivery_report("um-deliveries-day-3.txt")

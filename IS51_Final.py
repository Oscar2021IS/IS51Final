"""
the program is will calculate the class average 
it will take the values from the txt file

it will take the list of grades
it will calculate the average  using the average function

it will print "the number of grades"
the it will print "the average grades"


end
"""
"""
def main():
    file = "Final.txt"
    calculate_percent_above_average(file)

def calculate_percent_above_average(file):
    infile = open(file, "r")
    listGrades = [int(line.rstrip()) for line in infile]
    infile.close()
    length = len(listGrades)
    sum1 = sum(listGrades)
    avg = sum1 / length
    print("Number of grades:", length)
    print("Average grade:", avg)
    counter = 0
    for item in listGrades:
        if item > avg:
            counter += 1
    percentHigher = counter / length
    print("Percent of grades above average:", end =" ")
    print("{0:.2%}".format(percentHigher))

main()








"""
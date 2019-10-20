# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:32:37 2019

@author: Eesh Gupta
"""

def main():
    Mon_Classes= []
    Tue_Classes= []
    Wed_Classes= []
    Thu_Classes= []
    Fri_Classes= []
    Sat_Classes= []
    Sun_Classes= []




    myFile = open("f.txt", "rt")

    lines = myFile.readlines()

    ##filtering out uselesss info
    for line in lines:
        if line.find("Course material information") != -1:
            last_line = lines.index(line) 
            break
    #print(last_line)
    start_line = 9
    relevant_lines = lines[9]

    ##finding relevant lines
    for line in lines[start_line:last_line]: 

        line = line.split()

        if (line[0] == 'Monday') or (line[0] =='Tuesday') or (line[0] =='Wednesday') or (line[0] =='Thursday')or (line[0] =='Friday') or (line[0] =='Saturday') or (line[0] =='Sunday'): #or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday' or 'Sunday'):



            #fixing 12 hour format to 24 hour format
            if line[2] == 'PM':
                #correct for 12PM case
                string = line[1]
                if string[0:2] == '12':
                    line[1] = float(string[0:string.index(":")])+ ((float(string[string.index(":") +1:string.index(":") +3]))/60)
                else:
                    line[1] = float(string[0:string.index(":")])+12.0 + ((float(string[string.index(":") +1:string.index(":") +3]))/60)
            else:
                string = line[1]
                line[1] = float(string[0:string.index(":")])+ ((float(string[string.index(":") +1:string.index(":") +3]))/60)


            if line[5] == 'PM':
                #correct for 12PM case
                string = line[4]
                if string[0:2] == '12':
                    line[4] = float(string[0:string.index(":")])+ ((float(string[string.index(":") +1:string.index(":") +3]))/60)
                else:
                    line[4] = float(string[0:string.index(":")])+12.0 + ((float(string[string.index(":") +1:string.index(":") +3]))/60)
            else:
                string = line[4]
                line[4] = float(string[0:string.index(":")])+ ((float(string[string.index(":") +1:string.index(":") +3]))/60)

            #adding [start class time, end class time, class location, class campus]
            if line[0] == 'Monday':
                Mon_Classes.append([line[1], line[4], line[6], line[7]])
            elif line[0] == 'Tuesday' :
                Tue_Classes.append([line[1], line[4], line[6], line[7]])
            elif line[0] == 'Wednesday' :
                Wed_Classes.append([line[1], line[4], line[6], line[7]])
            elif line[0] == 'Thursday' :
                Thu_Classes.append([line[1], line[4], line[6], line[7]])
            elif line[0] ==  'Friday' :
                Fri_Classes.append([line[1], line[4], line[6], line[7]])
            elif line[0] == 'Saturday' :
                Sat_Classes.append([line[1], line[4], line[6], line[7]])
            elif line[0] ==  'Sunday':
                Sun_Classes.append([line[1], line[4], line[6], line[7]])

    #sorting all arrays
    Mon_Classes = sorted(Mon_Classes)
    Tue_Classes = sorted(Tue_Classes)
    Wed_Classes = sorted(Wed_Classes)
    Thu_Classes = sorted(Thu_Classes)
    Fri_Classes = sorted(Fri_Classes)
    Sat_Classes = sorted(Sat_Classes)
    Sun_Classes = sorted(Sun_Classes)


    #commutes
    days_classes = [Mon_Classes, Tue_Classes, Wed_Classes, Thu_Classes, Fri_Classes, Sat_Classes, Sun_Classes]
    commutes = [[], [], [], [], [], [], []]

    day = 0
    while day<7:
        if len(days_classes[day]) >1:
            class_ = 1
            while class_<len(days_classes[day]):
                if days_classes[day][class_-1][3] != days_classes[day][class_][3]:
                    com_time= days_classes[day][class_-1][1]
                    com_from = days_classes[day][class_-1][2]
                    com_to= days_classes[day][class_][2]
                    commutes[day].append([com_time, com_from.split('-')[0], com_to.split('-')[0]])
                class_+=1
        day+=1

    #contents = myfile.read()         # read the entire file into a string
    #myfile.close()                   # close the file
    #print(contents)  

    myFile.close()
    return commutes

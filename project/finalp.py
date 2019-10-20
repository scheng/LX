# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:32:37 2019

@author: Eesh Gupta
"""
def p(s):
    Mon_Classes= []
    Tue_Classes= []
    Wed_Classes= []
    Thu_Classes= []
    Fri_Classes= []
    Sat_Classes= []
    Sun_Classes= []

    s = s.split('By Day')[1].split('Course material')[0]
    print(s)
    string = s.split()

    ##finding relevant lines
    i=0
    while i< len(string):

        if (string[i] == 'Monday') or (string[i] =='Tuesday') or (string[i] =='Wednesday') or (string[i] =='Thursday')or (string[i] =='Friday') or (string[i] =='Saturday') or (string[i] =='Sunday'): #or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday' or 'Sunday'):



            #fixing 12 hour format to 24 hour format
            if string[i+2] == 'PM':
                #correct for 12PM case
                st = string[i+1]
                if st[0:2] == '12':
                    string[i+1] = float(st[0:st.index(":")])+ ((float(st[st.index(":") +1:st.index(":") +3]))/60)
                else:
                    string[i+1] = float(st[0:st.index(":")])+12.0 + ((float(st[st.index(":") +1:st.index(":") +3]))/60)
            else:
                st = string[i+1]
                string[i+1] = float(st[0:st.index(":")])+ ((float(st[st.index(":") +1:st.index(":") +3]))/60)


            if string[i+5] == 'PM':
                #correct for 12PM case
                st = string[i+4]
                if st[0:2] == '12':
                    string[i+4] = float(st[0:st.index(":")])+ ((float(st[st.index(":") +1:st.index(":") +3]))/60)
                else:
                    string[i+4] = float(st[0:st.index(":")])+12.0 + ((float(st[st.index(":") +1:st.index(":") +3]))/60)
            else:
                st = string[i+4]
                string[i+4] = float(st[0:st.index(":")])+ ((float(st[st.index(":") +1:st.index(":") +3]))/60)

            #adding [start class time, end class time, class location, class campus]
            if string[i] == 'Monday':
                Mon_Classes.append([string[i+1], string[i+4], string[i+6], string[i+7]])
            elif string[i] == 'Tuesday' :
                Tue_Classes.append([string[i+1], string[i+4], string[i+6], string[i+7]])
            elif string[i] == 'Wednesday' :
                Wed_Classes.append([string[i+1], string[i+4], string[i+6], string[i+7]])
            elif string[i] == 'Thursday' :
                Thu_Classes.append([string[i+1], string[i+4], string[i+6], string[i+7]])
            elif string[i] ==  'Friday' :
                Fri_Classes.append([string[i+1], string[i+4], string[i+6], string[i+7]])
            elif string[i] == 'Saturday' :
                Sat_Classes.append([string[i+1], string[i+4], string[i+6], string[i+7]])
            elif string[i] ==  'Sunday':
                Sun_Classes.append([string[i+1], string[i+4], string[i+6], string[i+7]])
        i+=1

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
                    commutes[day].append([com_time, com_from, com_to])
                class_+=1
        day+=1
    return commutes

    

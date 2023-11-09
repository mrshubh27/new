import random

print("1.Book A train ticket")
print ("2.Exit")
i = input(print("Enter the option\n"))
if i== "1":
    print("Enter your starting city location in form:like Pune")
    mystart = input("")
    if mystart=="Mumbai" or mystart=="Pune" or mystart=="Thane" or mystart=="Pimpri-Chichwad" or mystart=="Kalyan" or mystart=="Dombivli" or mystart=="Vasai" or mystart=="Virar" or mystart=="Sambhajinagar" \
            or mystart=="Navi-Mumbai" or mystart=="Solapur"  or mystart=="Mira-Bhayandar" or mystart=="Bhiwandi" or mystart=="Nizampur" or mystart=="Amravati" or mystart=="Nanded" or mystart=="Kolhapur" \
            or mystart=="Akola" or mystart=="Panvel" or mystart=="Ulhasnagar" or mystart == "Sangali" or mystart=="Miraj" or mystart=="Malegoan" or mystart=="Jalgoan" or mystart=="Latur" or mystart=="Dhule" \
            or mystart == "Ahmednagar" or mystart=="Chandrapur" or mystart=="Parbhani" or mystart=="Ichalkaranji" or mystart=="Jalna" or mystart=="Ambarnath" or mystart=="Bhusawal" or mystart=="Ratnagiri" \
            or mystart=="Beed" or mystart=="Gondia" or mystart == "Satara" or mystart=="Barshi" or mystart=="Yavatmal" or mystart=="Achalpur" or mystart=="Osmanabad" or mystart=="Nandurbar" or mystart=="Wardha"\
            or mystart=="Udgir" or mystart=="Hinganghat" or mystart=="Kandivali" or mystart=="Goa" or mystart=="Nagpur":
        print("Enter the destination city location")
        mydest = input("")
        if mydest == "Mumbai" or mydest == "Pune" or mydest == "Thane" or mydest == "Pimpri-Chichwad" or mydest == "Kalyan" or mydest == "Dombivli" or mydest == "Vasai" or mydest == "Virar" or mydest == "Sambhajinagar" \
                or mydest == "Navi-Mumbai" or mydest == "Solapur" or mydest == "Mira-Bhayandar" or mydest == "Bhiwandi" or mydest == "Nizampur" or mydest == "Amravati" or mydest == "Nanded" or mydest == "Kolhapur" \
                or mydest == "Akola" or mydest == "Panvel" or mydest == "Ulhasnagar" or mydest == "Sangali" or mydest == "Miraj" or mydest == "Malegoan" or mydest == "Jalgoan" or mydest == "Latur" or mydest == "Dhule" \
                or mydest == "Ahmednagar" or mydest == "Chandrapur" or mydest == "Parbhani" or mydest == "Ichalkaranji" or mydest == "Jalna" or mydest == "Ambarnath" or mydest == "Bhusawal" or mydest == "Ratnagiri" \
                or mydest == "Beed" or mydest == "Gondia" or mydest == "Satara" or mydest == "Barshi" or mydest == "Yavatmal" or mydest == "Achalpur" or mydest == "Osmanabad" or mydest == "Nandurbar" or mydest == "Wardha" \
                or mydest == "Udgir" or mydest == "Hinganghat" or mydest == "Kandivali" or mydest == "Goa" or mydest == "Nagpur":
            print("Enter the month: like March or July")
            mymonth = input("")
            if mymonth == "January" or mymonth == "February" or mymonth == "March" or mymonth == "April" or mymonth == "May" or mymonth == "June" or mymonth == "July" or mymonth == "August" or \
                    mymonth == "September" or mymonth == "October" or mymonth == "November" or mymonth == "December":
                print("Enter the date like 07 or 27")
                mydate = input()
                if mydate == "01" or mydate == "02" or mydate == "03" or mydate == "04" or mydate == "05" or mydate == "06" or mydate == "07" or mydate == "08" or mydate == "09" or mydate == "10" \
                        or mydate == "11" or mydate == "12" or mydate == "13" or mydate == "14" or mydate == "15" or mydate == "16" or mydate == "17" or mydate == "18" or mydate == "19" or mydate == "20" \
                        or mydate == "21" or mydate == "22" or mydate == "23" or mydate == "24"  or mydate == "25" or mydate == "26" or mydate == "27" or mydate == "28" or mydate == "29" or mydate == "30" \
                        or mydate == "31" & mymonth == "January" or mydate == "01" & mymonth == "February":
                        print("Choose the type of train: like Express\n" , "1. Local\n" , "2. Express\n" , "3. Super-Fast\n" , "4. Shatabdi")
                        mychoice = input("")
                        if mychoice == "Local" or "Express" or "Super-Fast" or "Shatabdi":
                            print("The available timings are ", "\n1", random.randrange(0, 13), ":",random.randrange(0, 60), "\n2", random.randrange(0, 13), ":", random.randrange(0, 60),
                                  "\n3", random.randrange(0, 13),":", random.randrange(0, 60), "\n4", random.randrange(0, 13), ":",random.randrange(0, 60), "\n5", random.randrange(0, 13), ":",
                                  random.randrange(0, 60),"\n6", random.randrange(0, 13),":", random.randrange(0, 60), "\n7", random.randrange(0, 13), ":",random.randrange(0, 60), "\n8", random.randrange(0, 13), ":", random.randrange(0, 60),
                                  "\n9", random.randrange(0, 13),":", random.randrange(0, 60), "\n10", random.randrange(0, 13), ":",random.randrange(0, 60), "\n11", random.randrange(0, 13), ":",
                                  random.randrange(0, 60), "\n12", random.randrange(0, 13),":", random.randrange(0, 60))
                            mytime = input("")
                            if mytime == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" or "11" or "12":
                                print("To confirm your ticket from " + mystart + " to " + mydest + " on " + mydate + " " + mymonth + " on time " + mytime + " with " + mychoice + " train.",
                                      "\nPlease select \n1 To Continue and print ticket", "\n2 To cancel and exit")
                                myselect = input("")
                                if myselect == "1":
                                    print("Your train ticket is confirmed from " + mystart + " to " + mydest + " on " + mydate + " " + mymonth + " on time " + mytime + " for " + mychoice + " train & your otp is" , random.randrange(00000,99999))
                                    print("Thank you for booking, have a safe and great journey........!")
                                else:
                                    print("You select the exit option\n")
                            else:
                                print("Enter the valid option\n")
                        else:
                            print("Enter the valid option\n")
                else:
                    print("Enter valide date option\n")
            else:
                print("Enter the valid month option\n")
        else:
            print("Enter the valid destination city option\n")
    else:
        print("Enter the valid starting city option\n")
else:
    print("You have choose exit option!\n")


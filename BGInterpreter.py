from random import randint
import random

O2_HighRange= 100
O2_LowRange= 80
CO2_HighRange= 45
CO2_LowRange= 35
pH_HighRange = 7.45
pH_LowRange= 7.35
pH_MidRange= 7.40
Bicarb_High= 28
Bicarb_Low= 22
Case_Generator = randint(1,13)

print("Welcome to the ABG generator and interpreter.")
print("Enter 1 to access the interpreter which looks at your results.")
UserC= input("Enter 2 to obtain random results and try to interpret them yourself.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Code for Case generation. Generates somewhat randomly but more accurate than total random. Does not give unsolvable cases.

if UserC == '2':
	
	if Case_Generator == 1:
	    User_CO2 =randint(46,70)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.1,7.34)
	    User_Bicarb =randint(22,28)
	if Case_Generator == 2:
	    User_CO2 =randint(15,35)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.46,7.7)
	    User_Bicarb =randint(22,28)
	if Case_Generator == 3:
	    User_CO2 =randint(35,45)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.46,7.7)
	    User_Bicarb =randint(29,45)
	if Case_Generator == 4:
	    User_CO2 =randint(35,45)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.1,7.34)
	    User_Bicarb =randint(5,21)
	if Case_Generator == 5:
	    User_CO2 =randint(46,70)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.46,7.7)
	    User_Bicarb =randint(29,45)
	if Case_Generator == 6:
	    User_CO2 =randint(15,35)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.1,7.34)
	    User_Bicarb =randint(5,21)
	if Case_Generator == 7:
	    User_CO2 =randint(15,35)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.46,7.7)
	    User_Bicarb =randint(5,21)
	if Case_Generator == 8:
	    User_CO2 =randint(46,70)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.1,7.34)
	    User_Bicarb =randint(29,45)
	if Case_Generator == 9:
	    User_CO2 =randint(46,70)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.41,7.45)
	    User_Bicarb =randint(29,45)
	if Case_Generator == 10:
	    User_CO2 =randint(15,35)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.35,7.39)
	    User_Bicarb =randint(5,21)
	if Case_Generator == 11:
	    User_CO2 =randint(46,70)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.35,7.39)
	    User_Bicarb =randint(29,45)
	if Case_Generator == 12:  #URALK
	    User_CO2 =randint(15,35)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.41,7.45)
	    User_Bicarb =randint(5,21)
	if Case_Generator == 13:
	    User_CO2 =randint(35,45)
	    User_O2 =randint(80,100)
	    User_pH =random.uniform(7.35,7.45)
	    User_Bicarb =randint(22,28)
	User_pH= round(User_pH,2)
	#End of Case generator
	print("pH=" + str(User_pH))
	print("CO2=" + str(User_CO2) )
	print("Bicarb=" + str(User_Bicarb) )
	ToContinue= input("Press Enter here to continue to the answers.")






"""
#Easy number generation. Tends to not generate viable situations. This code can be discarded.
User_CO2= randint(25,45)
User_Bicarb= randint(14,34)
User_pH= random.uniform(7.25,7.55)
User_pH= round(User_pH,2)
User_O2= randint(80,100)
"""


if UserC == '1':
	User_pH= input("Please enter your pH: ")
	User_pH= float(User_pH)
	if User_pH < 6.8 or User_pH > 7.8:
	    print("pH is physiologically impossible. Please double check your results or instrumentation.")
	    quit() #Ends program if pH is invalid.
	User_CO2= input("Please enter your CO2 in mmHg: ")
	User_O2= input("Please enter your 02 in mmHg: ")
	User_Bicarb= input("Please enter your Bicarb in mmol/L: ")




User_CO2= float(User_CO2)
User_O2= float(User_O2)
User_Bicarb= float(User_Bicarb)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if User_pH < pH_LowRange and User_CO2 > CO2_HighRange and User_Bicarb >= Bicarb_Low and User_Bicarb <= Bicarb_High:
    print("Patient might be in Respiratory Acidosis ")
elif User_pH > pH_HighRange and User_CO2 < CO2_LowRange and User_Bicarb >= Bicarb_Low and User_Bicarb <= Bicarb_High:
    print("Patient might be in Respiratory Alkalosis ")
elif User_pH > pH_HighRange and User_Bicarb > Bicarb_High and User_CO2 >= CO2_LowRange and User_CO2 <= CO2_HighRange:
    print("Patient might be in Metabolic Alkalosis ")
elif User_pH < pH_LowRange and User_Bicarb < Bicarb_Low and User_CO2 >= CO2_LowRange and User_CO2 <= CO2_HighRange:
    print("Patient might be in Metabolic Acidosis ")

elif User_pH > pH_HighRange and User_CO2 > CO2_HighRange and User_Bicarb > Bicarb_High:
    print("Patient might be in Partially Compensated Metabolic Alkalosis")
elif User_pH < pH_LowRange and User_CO2 < CO2_LowRange and User_Bicarb < Bicarb_Low:
    print("Patient might be in Partially Compensated Metabolic Acidosis")
elif User_pH < pH_LowRange and User_CO2 > CO2_HighRange and User_Bicarb > Bicarb_High:
    print("Patient might be in Partially Compensated Respiratory Acidosis")
elif User_pH > pH_HighRange and User_CO2 < CO2_LowRange and User_Bicarb < Bicarb_Low:
    print("Patient might be in Partially Compensated Respiratory Alkalosis")

#I have not yet  validated the fully compensated versions for user input code. 
elif User_pH <= pH_HighRange and User_pH >= pH_MidRange and User_CO2 > CO2_HighRange and User_Bicarb > Bicarb_High:
    print("Patient might be in Fully Compensated Metabolic Alkalosis")
elif User_pH <= pH_MidRange and User_pH >= pH_LowRange and User_CO2 < CO2_LowRange and User_Bicarb < Bicarb_Low:
    print("Patient might be in Fully Compensated Metabolic Acidosis")
elif User_pH <= pH_MidRange and User_pH >= pH_LowRange and User_CO2 > CO2_HighRange and User_Bicarb > Bicarb_High:
    print("Patient might be in Fully Compensated Respiratory Acidosis")
elif User_pH <= pH_HighRange and User_pH >= pH_MidRange and User_CO2 < CO2_LowRange and User_Bicarb < Bicarb_Low:
    print("Patient might be in Fully Compensated Respiratory Alkalosis")

elif User_pH <= pH_HighRange and User_pH >= pH_LowRange and User_CO2 >= CO2_LowRange and User_CO2 <= CO2_HighRange and User_Bicarb >= Bicarb_Low and User_Bicarb <= Bicarb_High:
    print("Patient blood gas results appear normal.")
else:
    print("Results are abnormal. Consider issues with test collection/analysis or a mixed acid-base disorder.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if User_O2 < 80 and User_O2 > 0:
    print("Patient O2 levels indicate hypoxemia.")
if User_O2 > 100:
    print("Patient is probably on oxygen therapy.")

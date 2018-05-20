import re
# news='Today Agriculture Development Bank proposed a plan for the ADB headquarters to be shifted.'
news= 'Today Century Bank Limited proposed a plan for the CBD headquarters to be shifted. Nepal Hydro Developers NIB'
x=['NEPSE']
NHDL = re.compile(r'(Nepal\sHydro\sDevelopers)|(NHDL)')
if NHDL.search(news):
    x.append('NHDL')

NIB = re.compile(r'(Nepal\sInvestment\sBank)|(NIB)')
if NIB.search(news):
    x.append('NIB')

print(x)

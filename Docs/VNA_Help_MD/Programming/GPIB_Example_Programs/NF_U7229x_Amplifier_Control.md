# Example Setup for U7229x Amplifier Control

Note: The method described on this page has been superseded by the [External
Noise Amplifier](../../Applications/Noise_Figure.htm#External_Noise_Amplifier)
feature.

Amplifiers are often used to improve the over system noise figure. U7229x
amplifiers can be controlled with the Noise Figure Macro feature so that
during noise power measurements, the amplifier is in the high gain state, and
during the S-parameter measurements, the amplifier is in the low gain state. A
dwell time of 0.5 seconds is recommended.

The Macro commands needed to control the amplifier on the output port are
here:

[SENSe<ch>:NOISe:SWEep:MACRo:STATe <bool>](../GP-
IB_Command_Finder/Sense/Noise.htm#SweMacrStat)

[SENSe<ch>:NOISe:SWEep:MACRo:FILE:RSPath <string1>,<string2>](../GP-
IB_Command_Finder/Sense/Noise.htm#SweMacrFilRSP)

[SENSe<ch>:NOISe:SWEep:MACRo:FILE:RNPath <string1>,<string2>](../GP-
IB_Command_Finder/Sense/Noise.htm#SweMacrFilRNP)

For example:

SENS:NOIS:SWE:MACR:FILe:RNP "amplifierControl.py","setToAMP"

SENS:NOIS:SWE:MACR:FILe:RSP " amplifierControl.py ","setToTHRU"

SENS:NOIS:SWE:MACR:STAT ON

As shown below, amplifierControl.py is the macro that controls the amplifier,
and it takes input arguments setToAMP and setToTHRU. In the SCPI above,
this assumes that the .py file is placed in the default directory. Otherwise 
the full path can be specified.

## amplifierControl.py

import sys  
import pyvisa  
import time  
  
Mode = (sys.argv[1])  
rm = pyvisa.ResourceManager()  
#replace with VISA connection string of local amplifier:  
myAmplifier = rm.open_resource('USB0::0x2A8D::0x1004::MY0000001::0::INSTR')  
  
if Mode== 'setToAMP':  
myAmplifier.write('ROUTE:CLOSE 1') #turn amplifier ON  
elif Mode== 'setToTHRU' :  
myAmplifier.write('ROUTE:CLOSE 0') #turn amplifier OFF  
else:  
exit  
  
rm.close()

### See Also

[Python Basics](../Learning_about_GPIB/Python_Basics.md)

* * *


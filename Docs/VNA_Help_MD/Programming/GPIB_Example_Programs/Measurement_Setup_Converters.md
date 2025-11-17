# Measurement Setup Converters

The following C# example demonstrates how to set up a modulation distortion
converter measurement.

See the [Modulation Distortion](../GP-
IB_Command_Finder/Sense/Distortion_Measurement.htm) and [Mixer](../GP-
IB_Command_Finder/Sense/MIXerSCPI.htm) commands.

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

def example01():  
pna = VNA(pna_addr)  
pna.write("syst:fpr")  
pna.write("disp:wind1:stat on")  
pna.write("calc:cust:def 'ch1_MGain21','Modulation Distortion
Converters','MGain21'")  
pna.write("disp:wind1:trac1:feed 'ch1_MGain21'")  
pna.write("sens:swe:mode hold")  
  
freq_in_cent = 3.08e9  
freq_in_span = 300e6  
freq_in_star = freq_in_cent - freq_in_span/2  
freq_in_stop = freq_in_cent + freq_in_span/2  
# Mixer frequencies  
pna.write("SENS:MIX:INPut:FREQ:MODE SWEPt") # Mixer settings  
pna.write("SENS:MIX:INPut:FREQ:STAR {}".format(freq_in_star))  
pna.write("SENS:MIX:INPut:FREQ:STOP {}".format(freq_in_stop))  
pna.write("SENS:MIX:LO:FREQ:MODE FIXED")  
pna.write("SENS:MIX:LO:FREQ:FIX 2.2e9")  
pna.write("SENS:MIX:LO:POW 9")  
pna.write("SENS:MIX:OUTP:FREQ:SID LOW")  
pna.write("SENS:MIX:CALC Output")  
pna.write("SENS:MIX:APPLY")  
pna.write("SENS:MIX:LO:NAME 'Port 3'") # First apply the settings, then set LO
Name  
pna.write("SENS:MIX:APPLY")  
# SA frequencies  
pna.write("sens:dist:swe:carr:freq {}".format(freq_in_cent))  
pna.write("sens:freq:cent {}".format(freq_in_cent))  
pna.write("sens:freq:span {}".format(freq_in_span))  
# modulate  
pna.write("syst:conf:edev:stat 'myMXG',ON")  
pna.write("sens:dist:mod:sour 'myMXG'")  
pna.write(r"sour:mod:load 'D:\mod\flat\flat_1001.mdx'")  
pna.write("sour:mod:stat 1")  
#  
pna.write("sens:swe:mode cont")  
# close  
pna.close()  
---


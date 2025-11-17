# Create Leakage Calibration

This example program creates a Leakage Calibration Measurement

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
LeakyCal.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

'setup frequencies  
syst:pres  
SENSe1:FREQuency:STARt 10000000  
SENSe1:FREQuency:STOP 3000000000  
SENSe1:SWEep:POINts 300  
  
'create 1st tier calset  
'selecting a calset on the channel before starting the leakage calibration  
'will automatically select it as 1st tier calset; in this example we use ideal
data  
'but in reality one should select a real calset containing a full/full+
calibration  
cset:del "cset1st"  
sens:corr:cset:cre:def "cset1st","Full 2P(1,2)"  
  
'initialize the leaky cal as 2 port and 4 standards  
sens:corr:coll:leakage:init "[1,2]"  
sens:corr:coll:leakage:count?  
sens:corr:coll:leakage:count 4  
  
'set the expected leaky fixture delay  
sens:corr:coll:leakage:option:type?  
sens:corr:coll:leakage:option:reciprocity:port 1  
sens:corr:coll:leakage:option:reciprocity:delay:value 2.4e-9  
  
'set definition data  
sens:corr:coll:leakage:stan1:def:file "C:\data\leaky\leaky_filter\defT.s2p"  
sens:corr:coll:leakage:stan2:def:file "c:\data\leaky\leaky_filter\defL1S2.s2p"  
sens:corr:coll:leakage:stan3:def:file "c:\data\leaky\leaky_filter\defS1L2.s2p"  
sens:corr:coll:leakage:stan4:def:file "c:\data\leaky\leaky_filter\defL1O2.s2p"  
  
'set measurement data  
'alternatively, one should connect and measure each standard.  
sens:corr:coll:leakage:stan1:meas:file "C:\data\leaky\leaky_filter\T.s2p"  
sens:corr:coll:leakage:stan2:meas:file "c:\data\leaky\leaky_filter\L1S2.s2p"  
sens:corr:coll:leakage:stan3:meas:file "c:\data\leaky\leaky_filter\S1L2.s2p"  
sens:corr:coll:leakage:stan4:meas:file "c:\data\leaky\leaky_filter\L1O2.s2p"  
  
'verify that the cal stds definitions are enough to solve the cal system  
'this may not be 100% accurate  
sens:corr:coll:leakage:verify?  
---


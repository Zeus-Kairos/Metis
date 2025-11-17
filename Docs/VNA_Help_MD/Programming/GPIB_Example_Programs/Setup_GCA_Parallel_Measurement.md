# Setup GCA Parallel Measurement

The following programming example demonstrates how to setup channels (primary
and parallel) and how to enable parallel sweep for the GCA parallel
measurement.

See the[ Gain Compression ](../GP-
IB_Command_Finder/Sense/Gain_Compression.htm)and [GCA Parallel
Measurement](../GP-IB_Command_Finder/SystChanGCS.htm) commands

def gca_parallel_example(pna: VNA):  
pna.write("syst:fpr")  
  
# setup primary channel 1  
pna.write("disp:wind1:stat on")  
pna.write("calc1:meas1:def 'S21:Gain Compression'")  
pna.write("disp:meas1:feed 1")  
pna.write("calc1:meas2:def 'CompGain21:Gain Compression'")  
pna.write("disp:meas2:feed 1")  
pna.write("sens1:swe:mode HOLD")  
pna.write("sens1:gcs:pmap 1,2")  
pna.write("sens1:swe:type LINear")  
pna.write("sens1:gcs:amod PFrequency")  
pna.write("sens1:gcs:swe:freq:poin 100")  
pna.write("sens1:freq:star 100e6")  
pna.write("sens1:freq:stop 10e9")  
pna.write("sens1:bwid 100")  
pna.write("sens1:gcs:pow:star:lev -25")  
pna.write("sens1:gcs:pow:stop:lev -10")  
pna.write("sens1:gcs:swe:pow:poin 16")  
pna.write("sens1:corr:cset:act 'parallel_GCA_001',1")  
pna.write("calc1:meas1:corr:type 'GCA Enh Resp (2,1)'")  
pna.query_opc()  
  
# setup parallel channel 2  
pna.write("disp:wind2:stat on")  
pna.write("calc2:meas3:def 'S21:Gain Compression'")  
pna.write("disp:meas3:feed 2")  
pna.write("calc2:meas4:def 'CompGain21:Gain Compression'")  
pna.write("disp:meas4:feed 2")  
pna.write("sens2:swe:mode HOLD")  
pna.write("sens2:gcs:pmap 3,4")  
pna.write("sens2:swe:type LINear")  
pna.write("sens2:gcs:amod PFrequency")  
pna.write("sens2:gcs:swe:freq:poin 100")  
pna.write("sens2:freq:star 100e6")  
pna.write("sens2:freq:stop 10e9")  
pna.write("sens2:bwid 100")  
pna.write("sens2:gcs:pow:star:lev -25")  
pna.write("sens2:gcs:pow:stop:lev -10")  
pna.write("sens2:gcs:swe:pow:poin 16")  
pna.write("sens2:corr:cset:act 'parallel_GCA_002',1")  
pna.write("calc2:meas3:corr:type 'GCA Enh Resp (4,3)'")  
pna.query_opc()  
  
# enable parallel sweep  
pna.write("SYST:CHAN:GCSetup:PARallel:ENABle 1")  
pna.write("sens1:swe:mode SINGle")  
pna.query_opc()  
---


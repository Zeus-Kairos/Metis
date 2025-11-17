# Direct DPD

The following example demonstrates how to set up a direct DPD measurement.

[See the DPD commands.](../GP-IB_Command_Finder/SourceDPD.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

*idn? syst:fpr disp:wind1:stat on calc:cust:def 'ch1_PIn1','Modulation Distortion','PIn1' disp:wind1:trac1:feed 'ch1_PIn1' calc:cust:def 'ch1_POut2','Modulation Distortion','POut2' disp:wind1:trac2:feed 'ch1_POut2' syst:conf:edev:stat "Device0", on sens:dist:mod:sour "Device0" sour:mod:load "c:\users\instrument\desktop\16QAM.mdx" sour:mod:stat on sens:dist:swe:carr:freq 5e9 sens:dist:swe:pow:carr:lev:port DOUT2 sens:dist:swe:pow:carr:lev 0 sens:dist:path:dut:nom:gain 20.0 sens:dist:path:sour:nom:ampl -9.0 sour:dpd:proc dir sour:dpd:proc? sour:dpd:file:load:ide "c:\users\instrument\desktop\16QAM.mdx" sour:dpd:file:load:ide? sour:dpd:file:save "c:\users\instrument\desktop\16qam.mdpd" sour:dpd:file:save? sour:dpd:corr:coll:dut:evm:span? sour:dpd:corr:coll:dut:evm:iter 5 sour:dpd:corr:coll:dut:evm:iter? sour:dpd:corr:coll:dut:evm:tol -60 sour:dpd:corr:coll:dut:evm:tol? sour:dpd:corr:coll:dut:acp:enab 1 sour:dpd:corr:coll:dut:acp:enab? sour:dpd:corr:coll:dut:acp:span? sour:dpd:corr:coll:dut:acp:gban 1 sour:dpd:corr:coll:dut:acp:gban? sour:dpd:corr:coll:dut:acp:iter 4 sour:dpd:corr:coll:dut:acp:iter? sour:dpd:corr:coll:dut:acp:tol -60 sour:dpd:corr:coll:dut:acp:tol? sour:dpd:corr:coll:pow:enab 1 sour:dpd:corr:coll:pow:enab? sour:dpd:corr:coll:pow:span? sour:dpd:corr:coll:pow:iter 5 sour:dpd:corr:coll:pow:iter? sour:dpd:corr:coll:pow:tol 0.05 sour:dpd:corr:coll:pow:tol? sour:dpd:corr:coll:lo:fthru:enab 0 sour:dpd:corr:coll:lo:fthru:enab? sour:dpd:corr:coll:lo:fthru:iter 6 sour:dpd:corr:coll:lo:fthru:iter? sour:dpd:corr:coll:lo:fthru:tol -80 sour:dpd:corr:coll:lo:fthru:tol? sour:dpd:corr:coll:acq sour:dpd:corr:coll:acq:stat?  
---


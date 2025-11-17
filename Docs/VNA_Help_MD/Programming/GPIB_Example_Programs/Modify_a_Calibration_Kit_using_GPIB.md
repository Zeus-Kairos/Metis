# Modify a Calibration Kit using SCPI

* * *

This Visual Basic program:

  * Modifies Calibration kit number 3

  * Completely defines standard #4 (thru)

To run this program, you need:

  * An established [GPIB interface connection](JavaScript:hhctrl.TextPopup\(GPIBExamples,'Arial,8',10,10,00000000,0xc0ffff\))

##### [ See Other SCPI Example Programs](SCPI_Example_Programs.md)

* * *

'Modifying cal kit number 3  
Calkitnum = 3  
  
'Designate the kit selection to be used for performing cal's  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:SELect " & Val(Calkitnum)  
  
'Reset to factory default values.  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:RESet " & Val(Calkitnum)  
  
'Name this kit with your own name  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:NAME 'My Cal Kit'"  
  
'Assign standard numbers to calibration classes  
'Set Port 1, class 1 (S11A) to be standard #8  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:ORDer1 8"  
'Set Port 1, class 2 (S11B) to be standard #7  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:ORDer2 7"  
'Set Port 1, class 3 (S11C) to be standard #3  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:ORDer3 3"  
'Set Port 1, class 4 (S21T) to be standard #4  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:ORDer4 4"  
'Set Port 2, class 1 (S22A) to be standard #8  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:ORDer5 8"  
'Set Port 2, class 2 (S22B) to be standard #7  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:ORDer6 7"  
'Set Port 2, class 3 (S22C) to be standard #3  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:ORDer7 3"  
'Set Port 2, class 4 (S12T) to be standard #4  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:ORDer8 4"  
  
'Set up Standard #4 completely  
'Select Standard #4; the rest of the commands act on it  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard 4"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:FMIN 300KHz"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:FMAX 9GHz"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:IMPedance 50"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:DELay 1.234 ns"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:LOSS 23e6"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:C0 0"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:C1 1"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:C2 2"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:C3 3"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:L0 10"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:L1 11"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:L2 12"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:L3 13"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:LABel 'My Special Thru'"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:TYPE THRU"  
GPIB.Write "SENSe:CORRection:COLLect:CKIT:STANdard:CHARacteristic Coax"


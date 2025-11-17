# Set Up Sweep Parameters using SCPI

* * *

This Visual Basic program sets up sweep parameters on the Channel 1
measurement.

To run this program, you need:

  * An established [GPIB interface connection](JavaScript:hhctrl.TextPopup\(GPIBExamples,'Arial,8',10,10,00000000,0xc0ffff\))

[ See Other SCPI Example Programs](SCPI_Example_Programs.md)

GPIB.Write "SYSTem:PRESet"  
'Select the measurement  
GPIB.Write "CALCulate:PARameter:SELect 'CH1_S11_1'"  
'Set sweep type to linear  
GPIB.Write "SENSe1:SWEep:TYPE LIN"  
  
'Set IF Bandwidth to 700 Hz  
GPIB.Write "SENSe1:BANDwidth 700"  
  
'Set Center and Span Freq's to 4 GHz  
GPIB.Write "SENSe1:FREQuency:CENTer 4ghz"  
GPIB.Write "SENSe1:FREQuency:SPAN 4ghz"  
  
'Set number of points to 801  
GPIB.Write "SENSe1:SWEep:POINts 801"  
  
'Set sweep generation mode to Analog  
GPIB.Write "SENSe1:SWEep:GENeration ANAL"  
  
'Set sweep time to Automatic  
GPIB.Write "SENSe1:SWEep:TIME:AUTO ON"  
  
'Query the sweep time  
GPIB.Write "SENSe1:SWEep:TIME?  
SweepTime = GPIB.Read


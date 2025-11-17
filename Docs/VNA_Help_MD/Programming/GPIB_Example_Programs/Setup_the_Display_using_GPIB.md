# Set Up the Display using SCPI

* * *

This Visual Basic program:

  * Sets data formatting

  * Turns ON the Trace, Title, and Frequency Annotation

  * Autoscales the Trace

  * Queries Per Division, Reference Level, and Reference Position

  * Turn ON and set averaging

  * Turn ON and set smoothing

To run this program, you need:

  * An established [GPIB interface connection](JavaScript:hhctrl.TextPopup\(GPIBExamples,'Arial,8',10,10,00000000,0xc0ffff\))

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

GPIB.Write "SYSTem:PRESet"  
  
'Select the measurement  
GPIB.Write "CALCulate:PARameter:SELect 'CH1_S11_1'"  
  
'Set the Data Format to Log Mag  
GPIB.Write ":CALCulate1:FORMat MLOG"  
  
'Turn ON the Trace, Title, and Frequency Annotation  
GPIB.Write "Display:WINDow1:TRACe1:STATe ON"  
GPIB.Write "DISPlay:WINDow1:TITLe:STATe ON"  
GPIB.Write "DISPlay:ANNotation:FREQuency ON"  
  
'Autoscale the Trace  
GPIB.Write "Display:WINDow1:TRACe1:Y:Scale:AUTO"  
  
'Query back the Per Division, Reference Level, and Reference Position  
GPIB.Write "DISPlay:WINDow1:TRACe1:Y:SCALe:PDIVision?"  
Pdiv = GPIB.Read  
GPIB.Write "DISPlay:WINDow1:TRACe1:Y:SCALe:RLEVel?"  
Rlev = GPIB.Read  
GPIB.Write "DISPlay:WINDow1:TRACe1:Y:SCALe:RPOSition?"  
Ppos = GPIB.Read  
  
'Turn ON, and average five sweeps  
GPIB.Write "SENSe1:AVERage:STATe ON"  
GPIB.Write "SENSe1:AVERage:Count 5"  
  
'Turn ON, and set 20% smoothing aperture  
GPIB.Write "CALCulate1:SMOothing:STATe ON"  
GPIB.Write "CALCulate1:SMOothing:APERture 20"


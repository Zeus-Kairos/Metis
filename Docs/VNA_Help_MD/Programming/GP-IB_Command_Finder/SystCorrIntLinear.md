## SYSTem:CORRection:INTerpolate:LINear Commands

* * *

The five SYSTem:CORRection:INTerpolate:LINear commands are used as a sequence.
They are not meant to be used independent of the others. The commands perform
linear interpolation on a scalar data of (x,y) pairs based on a primary set of
x and y values to a new mapping based on a desired set of x values. The
desired set of x values (or range) must fall within the primary set of x
values (or range) and can have a different number of points than the primary
data set.

### Definition:

Linear interpolation operates by drawing a straight line between each two
adjacent data points on the primary (x,y) pairs that fall on either side of
the new desired data point represented by (x,y). in other words if

(xi, yi) represents data pairs on the primary data set and (xj,yj)
represents a data point on the interpolated result data set then:

Xi < Xj < Xi+1 and Yj = Yi + [(Yi+1  Yi)/(Xi+1  Xi)] (Xj  Xi)

Note: The primary data set must represent a function on the Cartesian
coordinate system. In other words, for each x value in the primary data set,
there can be only one corresponding Y value.

There are five steps in the sequence:

  1. SYSTem:CORRection:INTerpolate:LINear:INPut:X - loads in the primary X values

  2. SYSTem:CORRection:INTerpolate: LINear:INPut:Y - loads in the primary Y values

  3. SYSTem:CORRection:INTerpolate: LINear:OUTput:X - loads in the desired interpolated X values

  4. SYSTem:CORRection:INTerpolate: LINear:CALCulate - calculates the interpolated Y values

  5. SYSTem:CORRection:INTerpolate: LINear:OUTput:Y? - reads back the interpolated Y values.

### Example

The following function uses the SYSTem:CORRection:INTerpolate: LINear
commands:

Function InterpolateData_Single(inputX() As Double, inputY() As Single,
outputX() As Double, ByRef interpData() As Single) x =
visa_io.ag_send_binBlock64("SYST:CORR:INT:LIN:INP:X ", inputX) x =
visa_io.ag_send_binBlock("SYST:CORR:INT:LIN:INP:Y ", inputY) x =
visa_io.ag_send_binBlock64("SYST:CORR:INT:LIN:OUTP:X ", outputX) x =
visa_io.ag_send_rd("*OPC?") x = visa_io.ag_send_wait("SYST:CORR:INT:LIN:CALC")
x = visa_io.ag_send_rd("*OPC?") interpData =
visa_io.ag_send_rd_binBlock("SYST:CORR:INT:LIN:OUTP:Y?") CheckError End
Function 'Here is a code snippet that uses the function above. 'copy the
B-Response Error term from one calset to another.  'The source calset has a
super set stimulus and 'and the receiving calset has a subset stimulus Dim
BResp_freqList() As Double Dim BResp_Re() As Single Dim BResp_Im() As Single
GetErrorTerm_noChan BResp_Calset, "ResponseTracking(B)", BResp_freqList,
BResp_Re, BResp_Im Dim Noise_freqList() As Double GetCalsetStimulus
calsetName, Noise_freqList, 1, "Noise Figure Cold Source" ' Response Stimulus
Range Dim BResp_Re_interp() As Single Dim BResp_Im_interp() As Single
InterpolateData_Single BResp_freqList, BResp_Re, Noise_freqList,
BResp_Re_interp InterpolateData_Single BResp_freqList, BResp_Im,
Noise_freqList, BResp_Im_interp PutErrorTerm channel, calsetName,
"ResponseTracking(B)", BResp_Re_interp, BResp_Im_interp  
---  
  
##

* * *


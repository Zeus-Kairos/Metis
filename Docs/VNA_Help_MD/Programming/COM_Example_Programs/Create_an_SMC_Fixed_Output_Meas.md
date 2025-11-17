# Create an SMC Fixed Output Measurement with COM

* * *

This VBScript example creates a calibrated SMC fixed output measurement using
a controlled LO. Then a single sweep is taken and data is retrieved.

Requirements:

  * If an external LO is used, it should be configured to match the LOName property of the mixer object.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as SMC.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

option explicit ' Utility function function ToString(complexDataArray) dim
dataAsString dim point for point = 0 to UBound(data) dataAsString =
dataAsString & "(" & data(point,0) & "," & data(point,1) & ") " next ToString
= dataAsString end function dim app set app =
createobject("agilentpna835x.application") app.preset ' Put the channel in
hold (highly recommended) app.ActiveChannel.Hold 1 ' Delete the standard
measurement app.ActiveMeasurement.Delete ' Create an SC21 measurement
app.CreateCustomMeasurementEx 1, "Scalar Mixer/Converter","SC21" ' Set the
number of points to 11 app.ActiveChannel.NumberOfPoints = 11 ' Setup the mixer
parameters for a swept LO, fixed output measurement dim mixer set mixer =
app.ActiveMeasurement mixer.InputStartFrequency = 200e6
mixer.InputStopFrequency = 700e6 mixer.LORangeMode(1) = 0 ' 0 = Swept mode
mixer.OutputFixedFrequency = 3.4e9 mixer.InputPower = -17 mixer.LOPower(1) =
10 'mixer.LOName(1) = "8360" ' The CALCULATE method calculates the LO
frequency from the other parameters, ' It also applies ALL mixer parameters to
the channel. mixer.Calculate 3 ' Calculate the LO range ' Create an S11 in the
same channel app.CreateCustomMeasurementEx 1, "Scalar Mixer/Converter","S11"
dim S11Meas set S11Meas = app.ActiveMeasurement ' Create an IPwr in the same
channel app.CreateCustomMeasurementEx 1, "Scalar Mixer/Converter","IPwr" '
Create an OPwr in the same channel app.CreateCustomMeasurementEx 1, "Scalar
Mixer/Converter","OPwr" ' Perform a single sweep synchronously.
app.ActiveChannel.Single 1 ' Retrieve the SC21 data dim data 'Get the
calibrated values in polar format data = mixer.GetData(1,3) ' 1 =
naCorrectedData, 3 = naDataFormat_Polar wscript.echo "SC21=" & ToString(data)
' Retrieve the S11 data 'Get the calibrated values in polar format data =
S11Meas.GetData(1,3) ' 3 = naDataFormat_Polar wscript.echo "S11=" &
ToString(data)  
---  
  
* * *


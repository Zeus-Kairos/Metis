# Perform a Source Power Cal using COM

* * *

This program can be run in either Visual Basic 6 or as a VBScript program. The
VNA can run *.vbs programs as [macros](../Using_Macros.md).

This program demonstrates:

  * Performing a source power calibration of Port 2 for Channel 1.

  * Reading the calibration data.

Learn more about [Power Calibrations](../../S3_Cals/PwrCalibration.md)

See an example that [Uploads a Source Power
Cal](Upload_a_Source_Power_Cal_using_COM.htm)

[ See Other COM Example Programs](COM_Example_Intro.md)

To run this program, you need:

  * One of the following power meters connected to the VNA through GPIB: E4416A, E4417A, E4418A/B, E4419A/B, 437B, 438A, EPM-441A, EPM-442A

Note: If your power meter is other than these, you can [create your own Power
Meter Driver](../GPIB_Example_Programs/CustomPowerMeterDriver.htm) using our
template.

  * Your PC and VNA both connected to a LAN (for communicating with each other).

To make this program work in VBS, save the following code in a text editor
file such as Notepad and save as *.vbs.

To make this program work in Visual Basic 6:

  1. Create a new project

  2. Click Project, Add New Module, click Open.

  3. Paste the following code into the code window.

  4. Delete the first two lines (comment and Main)

  5. Click Project, Properties. Under Startup Object, select Sub Main

  6. Click Project, References, and select the Keysight PNA Series Type Library.

' Run the Main subroutine  
Main  
Public Sub Main()  
Dim PNA, chan, pwrcal ' VNA COM objects  
Const naPowerMeter = 0, naPowerMeterAndReceiver = 1 ' enum
NASourcePowerCalMethod  
Const naPowerSensor_A = 0 ' enum NAPowerAcquisitionDevice  
Const naCorrectionValues = 0 ' enum NASourcePowerCalBuffer  
Const port = 2 ' VNA port #2 as source port  
Const offset = 0 ' cal power offset value  
Const bDisplay = True ' whether to display data during acquire  
Dim stimulus, calvalues, strResult  
  
' Instantiate our VNA COM objects  
Set PNA = CreateObject("AgilentPNA835x.Application")  
Set chan = PNA.Channels(1)  
Set pwrcal = PNA.SourcePowerCalibrator  
  
' Set the number of sweep points to 21 on Channel 1.  
chan.NumberOfPoints = 21  
  
' Specify the GPIB address of the power meter  
' that will be used in performing the calibration.  
pwrcal.PowerMeterGPIBAddress = 13  
  
' Turn use of the loss table OFF (this assumes there is  
' virtually no loss in the RF path to the power sensor  
' due to a splitter, coupler or adapter).  
pwrcal.UsePowerLossSegments = False  
  
' Turn frequency checking OFF (so one power sensor is used for the entire cal  
' acquisition sweep regardless of frequency span).  
pwrcal.UsePowerSensorFrequencyLimits = False  
  
' Specify a nominal power accuracy tolerance (IterationsTolerance) in dB for
the  
' calibration, and the maximum number of iterations to adjust power at each
point,  
' attempting to achieve within tolerance of the desired power. If at any
stimulus  
' point the power fails to reach within the set tolerance of the desired power  
' after the maximum number of iterations, the power at that point will be set
to the  
' value determined by the last iteration (the Source Power Cal dialog box will  
' indicate the FAIL, but we can still apply the cal if desired when it's
complete).  
' Each iteration is based upon a SETTLED power reading (see comments preceding
the  
' next two properties below).  
pwrcal.IterationsTolerance = 0.1  
pwrcal.MaximumIterationsPerPoint = 3  
  
' The worst-case window of power uncertainty (for a calibration which meets  
' tolerance) is the sum of the iteration tolerance and the power meter
settling  
' tolerance (which is described below).  
' At each stimulus point, the VNA takes power meter readings and determines
when  
' they have settled by comparing the magnitude difference between consecutive  
' readings versus a nominal dB tolerance limit (ReadingsTolerance) on that
magnitude  
' difference. When consecutive readings are within tolerance of each other, or  
' if they are not within tolerance but we've taken a maximum number of
readings  
' (ReadingsPerPoint), the VNA does a weighted average of the readings taken at
that  
' stimulus point and that is considered our settled power reading.  
pwrcal.ReadingsTolerance = 0.1  
pwrcal.ReadingsPerPoint = 5  
  
' Setup of information pertaining to this specific cal acquisition. Includes
the  
' method (type of devices) that will be used to perform the cal -- choose
either  
' naPowerMeter or naPowerMeterAndReceiver. naPowerMeterAndReceiver uses the
power  
' meter for the first iteration of each point and the VNA's reference receiver
for  
' subsequent iterations, so is much faster than using power meter only
naPowerMeter).  
' But the power meter accounts for compression when calibrating at the output
of an  
' active device, whereas the reference receiver cannot unless it is coupled to
the  
' cal reference plane (on a VNA which allows direct access to the receivers).  
' 'offset' specifies if the cal power level is offset (positive value for a
gain,  
' negative value for a loss) from the VNA port power setting on the channel
when  
' no source power cal is active. This is to account for components between the
VNA  
' test port and cal reference plane. In this example, we will calibrate at the
VNA  
' test port, so there is no offset (it is zero).  
' 'bDisplay' indicates whether to display the source power cal dialog during
the  
' source power cal acquisition (the dialog will chart the corrected power
readings).  
pwrcal.SetCalInfo2 naPowerMeter, chan.channelNumber, port, offset, bDisplay  
  
' Perform synchronous source power cal acquisition sweep using the sensor
attached  
' to Channel A of the power meter. This assumes that the power sensor is
already  
' connected to Port 2 of the VNA.  
pwrcal.AcquirePowerReadings naPowerSensor_A, True  
  
' Conclude the calibration. This applies the cal data to VNA channel memory,  
' and turns the correction ON for Port 2 on Channel 1, but does NOT save the  
' calibration.  
pwrcal.ApplyPowerCorrectionValues  
  
' At this point, if you choose to save the instrument state as a ".CST" file,  
' the calibration will be saved with the instrument state in that file.  
' Read the stimulus values from Channel 1.  
stimulus = chan.GetXAxisValues  
  
' Read the source power correction data.  
calvalues = chan.getSourcePowerCalDataEx(naCorrectionValues, port)  
  
' Print the data using a message box (here, Chr returns the ASCII characters  
' for Tab (9) and Linefeed (10)).  
strResult = "Stimulus" & Chr(9) & Chr(9) & "Cal Value" & Chr(10)  
For i = 0 To UBound(stimulus)  
strResult = strResult & stimulus(i) & Chr(9) & calvalues(i) & Chr(10)  
Next  
MsgBox strResult  
End Sub


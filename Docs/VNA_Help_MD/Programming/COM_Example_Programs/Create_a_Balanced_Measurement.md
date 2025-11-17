# Create a Balanced Measurement using COM

* * *

The following program creates several Balanced measurements in separate
windows, generates markers, calculates statistics, and sets limit lines and
queries results.

Note: By their nature, balanced measurements are extremely sensitive to phase
differences between the two RF paths that make up the balanced port,
especially at higher frequencies. A good calibration (not performed in this
example) is critical to achieving good balanced measurement results.

This VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the PNA hard drive as BalancedCOM.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

' PNA application object  
Dim app  
  
' Channel 1 object  
Dim chan1  
  
' start of marker/limit testing range  
Dim minTestStimulus  
  
' end of marker/limit testing range  
Dim maxTestStimulus  
  
' Set to true if you want additional balanced measurements.  
Dim AdditionalMeasurements  
AdditionalMeasurements = 1  
  
' Create / Get the PNA application.  
Set app = CreateObject("AgilentPNA835x.Application")  
' Preset the instrument  
app.Preset  
' Get the Channel 1 object  
Set chan1 = app.Channels(1)  
' Stop data taking for now.  
chan1.Hold true  
' Set up the start / stop frequency for Channel 1 sweep.  
MHZ = 1000000  
GHZ = 1000*MHZ  
chan1.StartFrequency = 10 *MHZ  
chan1.StopFrequency = 1 *GHZ  
chan1.NumberOfPoints = 801  
' Define our test frequency range  
minTestStimulus = 100*MHZ  
maxTestStimulus = 900*MHZ  
' This example uses DUT topology Bal-Bal -  
' a DUT with a balanced input and balanced output.  
'  
' Port mapping for our DUT:  
' logical port 1 = physical ports 1 and 4  
' logical port 2 = physical ports 2 and 3  
' The default is:  
' logical port 1 = physical ports 1 and 2  
' logical port 2 = physical ports 3 and 4  
'  
' logical 1 logical 2  
' ___________  
' 1 ------| |------ 2 +  
' | DUT |  
' 4 ------|___________|------ 3 -  
  
chan1.BalancedTopology.SetBBPorts 1, 4, 2, 3  
  
' Now we create some Bal-Bal measurements.  
' By creating Bal-Bal measurements ("BBAL:..."),  
' the channel is set to Bal-Bal topology,  
' so it is not necessary to do this explicitly  
' with the BalancedTopology.DUTTopology command.  
' We do it here just for clarity:  
  
chan1.BalancedTopology.DUTTopology = 2  
' 0 == SE-Bal, 1 == SE-SE-Bal, 2 == Bal-Bal  
  
' Create four windows, each showing one category of balanced measurement:  
' Create Forward Transmission Measurements in Bal-Bal topology on Channel 1,
window 1  
  
' differential mode transmission  
app.CreateMeasurement 1, "BBAL:SDD21",1,1  
Set sdd21_1 = app.ActiveMeasurement  
  
' differential to common mode conversion  
app.CreateMeasurement 1, "BBAL:SCD21",1,1  
Set scd21_1 = app.ActiveMeasurement  
  
' common to differential mode conversion  
app.CreateMeasurement 1, "BBAL:SDC21",1,1  
Set sdc21_1 = app.ActiveMeasurement  
  
' common mode transmission  
app.CreateMeasurement 1, "BBAL:SCC21",1,1  
Set scc21_1 = app.ActiveMeasurement  
  
' Optionally create some additional measurements  
If AdditionalMeasurements Then  
  
' Create (logical) Port 1 reflection measurements, channel 1, window 2  
app.CreateMeasurement 1, "BBAL:SDD11",1,2 ' differential mode reflection  
app.CreateMeasurement 1, "BBAL:SDC11",1,2 ' C to D mode conversion reflection  
app.CreateMeasurement 1, "BBAL:SCD11",1,2 ' D to C mode conversion reflection  
app.CreateMeasurement 1, "BBAL:SCC11",1,2 ' common mode reflection  
  
' Create Reverse Transmission Measurements, channel 1, window 3  
app.CreateMeasurement 1, "BBAL:SDD12",1,3 ' differential mode transmission  
app.CreateMeasurement 1, "BBAL:SCD12",1,3 ' differential to common mode
conversion  
app.CreateMeasurement 1, "BBAL:SDC12",1,3 ' common to differential mode
conversion  
app.CreateMeasurement 1, "BBAL:SCC12",1,3 ' common mode transmission  
  
' Create (logical) Port 2 reflection measurements in window 4  
app.CreateMeasurement 1, "BBAL:SDD22",1,4 ' differential mode reflection  
app.CreateMeasurement 1, "BBAL:SDC22",1,4 ' C to D mode conversion reflection  
app.CreateMeasurement 1, "BBAL:SCD22",1,4 ' D to C mode conversion reflection  
app.CreateMeasurement 1, "BBAL:SCC22",1,4 ' common mode reflection  
End If  
  
' Set up some limit lines to verify a minimum differential insertion loss  
sdd21_1.LimitTest(1).BeginStimulus = minTestStimulus  
sdd21_1.LimitTest(1).EndStimulus = maxTestStimulus  
sdd21_1.LimitTest(1).BeginResponse = -2  
sdd21_1.LimitTest(1).EndResponse = -2  
sdd21_1.LimitTest(1).Type = 2 ' minimum limit  
sdd21_1.LimitTest.State = 1  
' Limit lines for maximum common mode to differential conversion  
sdc21_1.LimitTest(1).BeginStimulus = minTestStimulus  
sdc21_1.LimitTest(1).EndStimulus = maxTestStimulus  
sdc21_1.LimitTest(1).BeginResponse = -20  
sdc21_1.LimitTest(1).EndResponse = -20  
sdc21_1.LimitTest(1).Type = 1 ' maximum limit  
sdc21_1.LimitTest.State = 1  
' Take a (synchronous) single sweep on channel 1  
chan1.Single true  
  
' Show differential forward transmission statistics.  
sdd21_1.ShowStatistics = true  
  
' Set up user range 1 to limit marker's search range.  
chan1.UserRangeMin(0,1) = minTestStimulus  
chan1.UserRangeMax(0,1) = maxTestStimulus  
  
' Find/Show max common mode to differential conversion, and read back the
frequency.  
sdc21_1.MarkerState(1) = true  
' Set marker 1 to use user range 1  
sdc21_1.Marker(1).UserRange = 1  
sdc21_1.Marker(1).SearchMax  
  
' Find/Show max differential mode insertion loss, and read back the frequency.  
sdd21_1.MarkerState(1) = true  
' Set marker 1 to use user range 1  
sdd21_1.Marker(1).UserRange = 1  
sdd21_1.Marker(1).SearchMin  
If sdd21_1.LimitTestFailed Then  
Wscript.Echo "Differential insertion loss failed: " &
sdd21_1.Marker(1).Stimulus /MHZ & "MHz, " & _sdd21_1.Marker(1).Value(1) & "
dB"  
End If  
  
If sdc21_1.LimitTestFailed Then  
Wscript.Echo "Common to differential conversion failed: " &
sdc21_1.Marker(1).Stimulus/MHZ & "MHz, " & _sdc21_1.Marker(1).Value(1) & " dB"  
End If


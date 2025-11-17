## Set Up FastCW and FIFO

* * *

This example program does the following:

  * Setup an A/R and B/R measurement

  * Turn ON point averaging

  * Set external edge triggering (commented out)

  * Set FIFO and Fast CW

  * Write data into FIFO data buffer

  * Read FIFO data buffer

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as FIFO.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#Setup)

[See the FIFO object.](../COM_Reference/Objects/FIFO_Object.md)

[See Other COM Example Programs](COM_Example_Intro.md)

dim app set app = createobject("Agilentpna835x.application") ' Setup and
measure A/R and B/R app.Reset app.CreateMeasurement 1,"A/R1",0
app.CreateMeasurement 1,"B/R1",0 ' Set IFBW to 600khz (400thousand pts/second)
app.activeChannel.IFBandwidth = 600e3 ' Point Averaging Count = 10
app.activeChannel.AverageMode = 0 ' point app.activeChannel.averagingFactor =
10 app.ActiveChannel.averaging = 1 ' turn on ' Edge triggering - positive edge
'app.TriggerSetup.ExternalTriggerConnectionBehavior(1) = 2 ' BNC1 = trigger
positive edge 'app.TriggerSetup.Source = 2 ' external
'app.ActiveChannel.TriggerMode = 0 'point ' Setup FIFO and Fast CW count
app.ActiveChannel.Hold 1 ' hold - synchronous app.FIFO.State = 1' turn on FIFO
app.FIFO.Clear app.activechannel.sweeptype = 3 ' CW sweep
app.activechannel.fastcwpointcount = 1000000' set the point count to 1million
app.activechannel.single 1 ' synchronous single ' the single will wait until
the end of sweep. 'You do not have to wait until end of sweep to start
emptying FIFO. points = app.fifo.datacount msgbox points ' points == 2000000 '
points = 2million. Took 5 seconds to acquire For I = 0 to 1 ' 2 iterations (2
parameters * 2 sets of 1 million) Dim data Data = app.fifo.data(1000000) Next
msgbox data(0)  
---  
  
* * *


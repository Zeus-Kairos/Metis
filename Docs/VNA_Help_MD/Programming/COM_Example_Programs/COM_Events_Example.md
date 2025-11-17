# COM Events Example

* * *

This Visual Basic program shows how to monitor the end of sweep.

The program will set sweep time to various amounts and BEEPs when sweep is
completed. This method allows other processes to continue while waiting for
end-of-sweep. This program stops after 10 loops.

Note: To avoid Permission Denied problems, this should be run on the VNA and
not a PC. To run it from a PC both units must be "trusted" and on the same
[domain/workgroup](../Learning_about_COM/Configure_for_COM-
DCOM_Programming.htm).

Option Explicit  
Dim na As AgilentPNA835x.Application  
Dim WithEvents naEvnt As AgilentPNA835x.Application  
Dim ch As AgilentPNA835x.Channel  
Dim sweepComplete As Boolean  
  
Private Sub Form_Load()  
  
Dim N As Integer  
Set na = CreateObject("AgilentPNA835x.application")  
na.preset  
Set ch = na.ActiveChannel  
na.DisallowAllEvents ' Turn off all events  
Set naEvnt = na ' Enable event interrupts  
Do  
N = N + 1 ' Loop counter  
ch.sweepTime = 1 + (Rnd * 9) ' Set random sweep-time from 1-10 sec  
sweepComplete = False  
ch.Single False ' Trigger sweep  
naEvnt.AllowEventCategory naEventCategory_CHANNEL, True ' Enable Channel event  
Do  
DoEvents ' Allows other processes to continue  
Loop Until sweepComplete = True  
naEvnt.AllowEventCategory naEventCategory_CHANNEL, False ' Disable event until
ready for next one  
Beep ' Do end-of-sweep processing here;  
  
Loop Until N > 10  
End  
  
End Sub  
  
Private Sub naEvnt_OnChannelEvent(ByVal eventID As Variant, ByVal chNumber As
Variant)  
' In this example we don't care about the channel info  
If eventID = naEventID_CHANNEL_TRIGGER_COMPLETE Then sweepComplete = True  
End Sub  


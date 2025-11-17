# E5091Testset Control

* * *

The following VB Script example exercises the COM commands used to control the
E5091A testset.

For a description of each command, see [E5091Testsets
collection.](../COM_Reference/Objects/E5091Testset_Collection.htm)

Sub Main()  
Set pna = CreateObject("AgilentPNA835x.Application")  
Dim testsets As E5091Testsets  
Set testsets = pna.E5091Testsets  
Dim tset1 As E5091Testset  
Set tset1 = testsets(1)  
tset1.OutputPort(1, 3) = naE5091PortR2  
tset1.ControlLines(1) = 5  
tset1.ShowProperties = True  
tset1.Enabled = True  
MsgBox tset1.ID  
MsgBox tset1.Enabled  
MsgBox tset1.ShowProperties  
' NumberOfPorts property returns 0 when testset not connected  
MsgBox tset1.NumberOfPorts  
MsgBox tset1.OutputPort(1, 3)  
MsgBox tset1.ControlLines(1)  
  
Dim tset2 As E5091Testset  
Set tset2 = testsets(2)  
tset2.Enabled = True  
tset2.ShowProperties = True  
MsgBox tset2.Enabled  
MsgBox tset2.ShowProperties  
End Sub


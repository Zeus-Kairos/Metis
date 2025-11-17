# Establish a VISA Session

* * *

This Visual Basic program demonstrates how to send a SCPI command using VISA
and the Keysight IO libraries. To run this program, you need:

  * Your PC and VNA both connected to a LAN (for communicating with each other).

  * The SICL and VISA components of Keysights I/O Libraries software installed on your PC. Both are included when you install the software, unless you already have another vendor's VISA installed. Then specify Full SICL and VISA installation to overwrite the other vendor's VISA.

  * The module visa32.bas added to your VB project. After you install VISA, the module will be located at C:/VXIPNP/WINNT (or equivalent)/INCLUDE/Visa32.bas

  * A form with two buttons: cmdRun and cmdQuit.

  * Your PC configured to be a VISA LAN Client, and the SICL Server capability enabled on the analyzer. See [Configure for VISA and SICL](../Learning_about_GPIB/Configure_for_VISA_and_SICL.md)

##### [See Other SCPI Example Programs](SCPI_Example_Programs.md)

Note: This example is a piece of a larger VISA program that [performs a source
power calibration.](Perform_a_Source_Cal_using_SCPI.htm)

'Session to VISA Default Resource Manager  
Private defRM As Long  
'Session to VNA  
Private viPNA As Long  
'VISA function status return code  
Private status As Long  
  
Private Sub Form_Load()  
defRM = 0  
End Sub  
  
Private Sub cmdRun_Click()  
' String to receive data from the VNA.  
' Dimensioned large enough to receive scalar comma-delimited values  
' for 21 frequency points (20 ASCII characters per point)  
Dim strReply As String * 420  
  
' Open the VISA default resource manager  
status = viOpenDefaultRM(defRM)  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Open a VISA session (viPNA) to the SICL LAN server  
' at address 16 on the VNA pointed to by the GPIB0  
' VISA LAN Client on this PC.  
' CHANGE GPIB0 TO WHATEVER YOU VNA IS SET TO  
status = viOpen(defRM, "GPIB0::16::INSTR", 0, 0, viPNA)  
If (status < VI_SUCCESS) Then HandleVISAError  
  
' Need to set the VISA timeout value to give all our calls to  
' myGPIBRead sufficient time to complete before a timeout  
' error occurs.  
' For this example, let's try setting the limit to  
' 30000 milliseconds (30 seconds).  
status = viSetAttribute(viPNA, VI_ATTR_TMO_VALUE, 30000)  
If (status < VI_SUCCESS) Then HandleVISAError  
  
  
' Preset the VNA  
status = myGPIBWrite(viPNA, "SYST:PRES")  
If (status < VI_SUCCESS) Then HandleVISAError  
  
  
' Print the data using a message box  
MsgBox strReply  
End Sub  
  
Private Sub cmdQuit_Click()  
' Close the resource manager session (which also closes  
' the session to the VNA).  
If defRM <> 0 Then Call viClose(defRM)  
  
' End the program  
End  
End Sub  
  
Private Function myGPIBWrite(ByVal viHandle As Long, ByVal strOut As String)
As Long  
' The "\+ Chr$(10)" appends an ASCII linefeed character to the  
' output, for terminating the write transaction.  
myGPIBWrite = viVPrintf(viHandle, strOut + Chr$(10), 0)  
End Function  
  
Private Function myGPIBRead(ByVal viHandle As Long, strIn As String) As Long  
myGPIBRead = viVScanf(viHandle, "%t", strIn)  
End Function  
  
Sub HandleVISAError()  
Dim strVisaErr As String * 200  
Call viStatusDesc(defRM, status, strVisaErr)  
MsgBox "*** Error : " \+ strVisaErr, vbExclamation  
End  
End Sub


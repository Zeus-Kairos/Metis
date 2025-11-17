# Perform a Source and Receiver Power Cal using SCPI

* * *

Programming the VNA using COM or using SICL/VISA over LAN (as in this example)
leaves the VNA free to control GPIB devices as needed.

The first example, using Visual Basic, demonstrates the following:

  * Performing a source power calibration of Port 2 for Channel 1.

  * Reading the calibration data.

The second example performs a [Receiver Power
Cal](Perform_a_Source_Cal_using_SCPI.htm#receiver) using VBScript.

Learn more about [Power Calibrations](../../S3_Cals/PwrCalibration.md).

See an example that [Uploads a Source Power
Cal](Uploading_a_Source_Power_Cal_using_SCPI.htm).

[Other SCPI Example Programs](SCPI_Example_Programs.md)

To run this program, you need:

  * One of the following power meters connected to the VNA through GPIB: E4416A, E4417A, E4418A/B, E4419A/B, 437B, 438A, EPM-441A, EPM-442A

Note: If your power meter is other than these, you can [create your own Power
Meter Driver](CustomPowerMeterDriver.htm) using our template.

  * Your PC and VNA both connected to a LAN (for communicating with each other).

  * The SICL and VISA components of Agilents I/O Libraries software installed on your PC (both are included when you install the software, unless you already have another vendor's VISA installed. Then specify Full SICL and VISA installation to overwrite the other vendor's VISA.

  * The module visa32.bas added to your VB project.

  * A form with one button labeled cmdRun.

  * A VISA interface configured on your remote PC to control the VNA. This could be GPIB interface or a [VISA LAN Client](../Learning_about_GPIB/Configure_for_VISA_and_SICL.md).

  * On the VNA connect a Thru cable from port 1 to port 2.

Note: The [SOURce:POWer:CORRection:COLLect:ACQuire](../GP-
IB_Command_Finder/SourceCorrection.htm#aquire) command, when used with a power
meter, cannot be sent over the GPIB unless the power meter is connected to a
different GPIB interface. See the alternative methods described in the command
details.

'Session to VISA Default Resource Manager Private defRM As Long 'Session to
VNA Private viPNA As Long 'VISA function status return code Private status As
Long Private Sub Form_Load() defRM = 0 End Sub Private Sub cmdRun_Click() '
String to receive data from the VNA. ' Dimensioned large enough to receive
scalar comma-delimited values ' for 21 frequency points (20 ASCII characters
per point) Dim strReply As String * 420 Dim strStimulus, strCalValue Dim
strResult As String ' Open the VISA default resource manager status =
viOpenDefaultRM(defRM) If (status < VI_SUCCESS) Then HandleVISAError ' Open a
session (viPNA) to the VNA at "address 16" on the VISA ' interface configured
as "GPIB1" on this PC. This could be a ' VISA LAN Client pointing to the SICL
LAN Server on the VNA, or ' an actual GPIB interface on this PC connected to
the VNA GPIB ' (in which case the power meter would need to be connected to a
' different GPIB interface on the VNA, such as the Keysight 82357A ' USB-to-
GPIB). status = viOpen(defRM, "GPIB0::16::INSTR", 0, 0, viPNA) If (status <
VI_SUCCESS) Then HandleVISAError ' Set the number of sweep points to 21 on
Channel 1. status = myGPIBWrite(viPNA, "SENS1:SWE:POIN 21") If (status <
VI_SUCCESS) Then HandleVISAError ' Specify the GPIB address of the power meter
' that will be used in performing the calibration. status = myGPIBWrite(viPNA,
"SYST:COMM:GPIB:PMET:ADDR 13") If (status < VI_SUCCESS) Then HandleVISAError '
Turn use of the loss table OFF (this assumes there is ' virtually no loss in
the RF path to the power sensor ' due to a splitter, coupler or adapter).
status = myGPIBWrite(viPNA, "SOUR:POW:CORR:COLL:TABL:LOSS OFF") If (status <
VI_SUCCESS) Then HandleVISAError ' Turn frequency checking OFF (so one power
sensor is used for the entire cal ' acquisition sweep regardless of frequency
span). status = myGPIBWrite(viPNA, "SOUR:POW:CORR:COLL:FCH OFF") If (status <
VI_SUCCESS) Then HandleVISAError ' Specify a nominal power accuracy tolerance
(NTOLerance) in dB for the calibration, ' and the maximum number (COUNt) of
iterations to adjust power at each point, ' attempting to achieve within
tolerance of the desired power. If at any stimulus ' point the power fails to
reach within the set tolerance of the desired power ' after the maximum number
of iterations, the power at that point will be set to the ' value determined
by the last iteration (the Source Power Cal dialog box will ' indicate the
FAIL, but we can still apply the cal if desired when it's complete). ' Each
iteration is based upon a SETTLED power reading (see comments preceding the '
next two commands below). status = myGPIBWrite(viPNA,
"SOUR1:POW2:CORR:COLL:ITER:NTOL 0.1") If (status < VI_SUCCESS) Then
HandleVISAError status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR:COLL:ITER:COUN
3") If (status < VI_SUCCESS) Then HandleVISAError ' The worst-case window of
power uncertainty (for a calibration which meets ' tolerance) is the sum of
the iteration tolerance and the power meter settling ' tolerance (which is
described below). ' At each stimulus point, the VNA takes power meter readings
and determine when ' they have settled by comparing the magnitude difference
between consecutive ' readings versus a nominal dB tolerance limit
(NTOLerance) on that magnitude ' difference. When consecutive readings are
within tolerance of each other, or ' if they are not within tolerance but
we've taken a maximum number of readings ' (COUNt), the VNA does a weighted
average of the readings taken at that stimulus ' point and that is considered
our settled power reading. status = myGPIBWrite(viPNA,
"SOUR1:POW2:CORR:COLL:AVER:NTOL 0.1") If (status < VI_SUCCESS) Then
HandleVISAError status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR:COLL:AVER:COUN
5") If (status < VI_SUCCESS) Then HandleVISAError ' Specify if the cal power
level is offset (positive value for a gain, negative ' value for a loss) from
the VNA port power setting on the channel when no source ' power cal is
active. This is to account for components between the VNA test ' port and cal
reference plane. In this example, we will calibrate at the VNA ' test port, so
there is no offset (it is zero). status = myGPIBWrite(viPNA,
"SOUR1:POW2:CORR:OFFS 0 DB") If (status < VI_SUCCESS) Then HandleVISAError '
Show the source power cal dialog during the source power cal acquisition. '
(this is the default, so this command is only necessary if this setting ' may
have been changed beforehand, perhaps by another program). status =
myGPIBWrite(viPNA, "SOUR1:POW2:CORR:COLL:DISP ON") If (status < VI_SUCCESS)
Then HandleVISAError ' Clear the VNAs SCPI status registers because we are
going to be monitoring ' the event status register to detect when the OPC bit
gets set indicating ' the cal ACQuire completed. status = myGPIBWrite(viPNA,
"*CLS") If (status < VI_SUCCESS) Then HandleVISAError ' Setting the I/O
timeout value to 6000 milliseconds (6 seconds), because the ' VNA may take up
to that amount of time to respond to some commands/queries ' while the cal
ACQuire is progressing. status = viSetAttribute(viPNA, VI_ATTR_TMO_VALUE,
6000) If (status < VI_SUCCESS) Then HandleVISAError ' Specify the method (type
of device) that will be used to perform the cal. ' Choose from power meter
(PMETer), power meter and receiver (PMReceiver) ' or just receiver (RECeiver).
' PMReceiver uses the power meter for the first iteration of each point and '
the VNA's reference receiver for subsequent iterations, so is much faster '
than using power meter only. But the power meter accounts for compression '
when calibrating at the output of an active device, whereas the reference '
receiver cannot unless it is coupled to the cal reference plane (on a VNA '
which allows direct access to the receivers). ' Perform the source power cal
acquisition sweep using the sensor attached to ' Channel A of the power meter
(asking for an OPC reply when its done). This ' assumes that the power sensor
is already connected to Port 2 of the VNA. ' We'll put up an hourglass cursor
while waiting for the acquire to complete. Screen.MousePointer = vbHourglass
status = myGPIBWrite(viPNA, "SOUR1:POW:CORR:COLL:ACQ PMET,'ASEN','Port
2',ASYNchronous;*OPC") If (status < VI_SUCCESS) Then HandleVISAError ' Other
valid selections would be the following:  This mode uses Power Meter and
Reference Receiver 'status = myGPIBWrite(viPNA, "SOUR1:POW:CORR:COLL:ACQ
PMR,'BSEN','Port 2',ASYN;*OPC") ' This mode uses VNA receiver only (no power
meter) 'status = myGPIBWrite(viPNA, "SOUR1:POW:CORR:COLL:ACQ REC,'b1','Port
2',ASYN;*OPC") ' Polling in a loop to detect when the OPC bit (bit 0, weight
value 1) gets ' set in the Event Status Register indicating the ACQuire
finished. In this ' type of loop is where you could do other operations in-
between the polling ' (like having your programs user-interface still respond
to user input). ' If instead of Visual Basic you are programming in C or C++,
as an ' alternative to having a polling loop like this, you could set up an
SRQ ' handling function in your program (for example, see the documentation '
supplied with your vendors implementation of VISA on how to register for '
callback when an SRQ event occurs). Do status = myGPIBWrite(viPNA, "*ESR?") If
(status < VI_SUCCESS) Then HandleVISAError status = myGPIBRead(viPNA,
strReply) If (status < VI_SUCCESS) Then HandleVISAError esrByte =
CByte(strReply) Loop While (esrByte And 1) = 0 ' Change mouse cursor from
hourglass back to normal Screen.MousePointer = vbDefault ' Conclude the
calibration. This applies the cal data to VNA channel memory, ' and turns the
correction ON for Port 2 on Channel 1, ' but does NOT save the calibration.
status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR:COLL:SAVE") If (status <
VI_SUCCESS) Then HandleVISAError ' At this point, if you choose to save the
instrument state as a ".CST" file, ' the calibration will be saved with the
instrument state in that file. ' Prepare for doing data transfer in ASCII
format. status = myGPIBWrite(viPNA, "FORM:DATA ASCII") If (status <
VI_SUCCESS) Then HandleVISAError ' Read the stimulus values from Channel 1.
status = myGPIBWrite(viPNA, "SENS1:X?") If (status < VI_SUCCESS) Then
HandleVISAError status = myGPIBRead(viPNA, strReply) If (status < VI_SUCCESS)
Then HandleVISAError ' Tokenize the reply string into an array containing the
values strStimulus = Split(strReply, ",") ' Read the source power correction
data. status = myGPIBWrite(viPNA, "SOUR1:POW2:CORR:DATA?") If (status <
VI_SUCCESS) Then HandleVISAError status = myGPIBRead(viPNA, strReply) If
(status < VI_SUCCESS) Then HandleVISAError ' Tokenize the reply string into an
array containing the values strCalValue = Split(strReply, ",") ' Print the
data using a message box (here, Chr returns the ASCII characters ' for Tab (9)
and Linefeed (10)). strResult = "Stimulus" & Chr(9) & Chr(9) & "Cal Value" &
Chr(10) For i = 0 To UBound(strStimulus) strResult = strResult &
Val(strStimulus(i)) & Chr(9) & Val(strCalValue(i)) & Chr(10) Next MsgBox
strResult End Sub Private Function myGPIBWrite(ByVal viHandle As Long, ByVal
strOut As String) As Long ' The "\+ Chr$(10)" appends an ASCII linefeed
character to the ' output, for terminating the write transaction. myGPIBWrite
= viVPrintf(viHandle, strOut + Chr$(10), 0) End Function Private Function
myGPIBRead(ByVal viHandle As Long, strIn As String) As Long myGPIBRead =
viVScanf(viHandle, "%t", strIn) End Function Sub HandleVISAError() Dim
strVisaErr As String * 200 Call viStatusDesc(defRM, status, strVisaErr) MsgBox
"*** Error : " \+ strVisaErr, vbExclamation ' Close the resource manager
session (which also closes ' the session to the VNA). If defRM <> 0 Then Call
viClose(defRM) End End Sub Public Sub Wait(ByVal mS_delay As Long) Dim t0 As
Single t0 = Timer Do While Timer - t0 < mS_delay / 1000 Dim dummy As Integer
dummy = DoEvents() ' if we cross midnight, back up one day If Timer < t0 Then
t0 = t0 - 86400 Loop End Sub  
---  
  
### Perform a Receiver Power Cal

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file, such as Notepad, and save it
on the VNA hard drive as *.vbs.

[Learn how to setup and run the macro.](../Using_Macros.md#HowToSetup)

Dim pna  
Dim scpi  
Set pna = CreateObject("AgilentPNA835x.Application")  
Set scpi = pna.ScpiStringParser  
' For simplicity, this example starts from the preset instrument state  
scpi.Execute "SYST:PRESet"  
' Turn off continuous sweep  
scpi.Execute "INITiate:CONTinuous OFF"  
' Select the S11 measurement that was created by the instrument preset  
scpi.Execute "CALCulate:PARameter:SELect 'CH1_S11_1'"  
' Change the measurement parameter to measure the B receiver  
scpi.Execute "CALCulate:PARameter:MODify B,1"  
' Specify the Calibration Type, then Prompt  
' to ensure the receiver is connected to port 1.  
scpi.Execute "SENSe:CORRection:COLLect:METHod RPOWer"  
MsgBox "Connect port 1 to port 2 so power is supplied to the B receiver, then
press enter"  
' Acquire the power measurement; returning reply to *OPC? when finished.  
response = scpi.Execute( "SENSe:CORRection:COLLect:ACQuire POWer;*OPC?" )  
' Compute the error term, store to calset and turn on the calibration.  
response = scpi.Execute( "SENSe:CORRection:COLLect:SAVE" )  
MsgBox "Done with calibration."  

* * *


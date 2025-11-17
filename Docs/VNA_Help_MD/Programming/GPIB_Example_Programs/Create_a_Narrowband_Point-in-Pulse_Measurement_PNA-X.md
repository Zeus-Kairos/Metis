## Create a Narrowband Point-in-Pulse Measurement using the PNA-X

* * *

The following SCPI example demonstrates how to create a Narrowband Point-in-
Pulse measurement using the Pulsed Application DLL on the
[PNA-X](../../Support/Configurations.md#PNAX).

It first gets valid configuration settings and then uses those settings to
configure the VNA and internal pulsed generators.

To run this program, you need:

  * PNA-X

  * [Pulsed Application](../../Applications/Narrowband_Pulsed_Application.md) (Option H08)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as PulseProfile.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

Note: Because of the long length of some commands in this example, word
wrapping may occur when copying. These lines require modification after
pasting.

### See Also

  * [Install and register the pulsed .dll](../../Applications/Narrowband_Pulsed_Application.md#Install) on your PC.

  * [ConfigEnhancedNB2](../COM_Reference/Methods/ConfigEnhancedNB2_Method.md) method for sending and returning parameters to the .dll.

  * [ConfigEnhancedNBIFAtten](../COM_Reference/Methods/ConfigEnhancedNBIFAtten_Method.md) method for setting the receiver IF gain.

  * [SCPI IF Configuration](../GP-IB_Command_Finder/Sense/XSensIF.md) commands used in the program.

  * [Other Pulse SCPI examples](SCPI_Example_Programs.md#Pulsed)

//This example shows you how to perform point in pulse measurement based on
//PNA-X in narrowband mode using SCPI commands. public partial class Form1 :
Form { private object pna; private object scpi; private Type srvtype; private
AgilentPNAPulsed.applicationClass pulseApp; public Form1() {
InitializeComponent(); } private string sendScpiCommand(string scpitext) {
object[] parameter = new object[1]; parameter[0] = scpitext; return
(string)srvtype.InvokeMember("parse", BindingFlags.InvokeMethod, null, scpi,
parameter); } private void ConnectToPNA() { srvtype =
Type.GetTypeFromProgID("AgilentPNA835x.Application", true); pna =
Activator.CreateInstance(srvtype); scpi =
srvtype.InvokeMember("ScpiStringParser", BindingFlags.GetProperty, null, pna,
null); } private void NBButton_Click(object sender, EventArgs e) { double dPRF
= 10000, dBW = 500; //PRF=10kHz double dPhysicalIF = 0, dNCO = 0, dClockFreq =
0; System.Array aStage1TapArray = null, aStage2TapArray = null,
aStage3TapArray = null; bool bFixedPRF = true; double dGateDelay = 0.000002,
dGateWidth = 0.000005; //Gate width=50ns double dSWGateDelay = 0, dSWGateWidth
= 0; int iSWGateRamp = 0; double dModPulseWidth = 0.00001;//10 us double
dModPulseDelay = 0;//0us short myAtten = 0; pulseApp = new
AgilentPNAPulsed.applicationClass(); ConnectToPNA(); //Preset PNA-X
sendScpiCommand("*RST"); //Measure S21 sendScpiCommand("DISP:WIND:TRAC1:DEL");
sendScpiCommand("CALCulate:PARameter:DEFine:EXT /'MyMeas/',S21");
sendScpiCommand("DISP:WIND:TRAC1:FEED /'MyMeas/'"); //Set power leveling mode
to Openloop sendScpiCommand("sour:pow1:alc:mode open"); //Send desired pulsed
parameters to the pulsed configuration DLL. //The DLL will return a new set of
pulse parameters to send to the PNA-X.
pulseApp.[ConfigEnhancedNB2](../COM_Reference/Methods/ConfigEnhancedNB2_Method.md)(ref
dPRF, ref dBW, ref dPhysicalIF, ref dNCO, ref dClockFreq, ref aStage1TapArray,
ref aStage2TapArray, ref aStage3TapArray, bFixedPRF, dGateDelay, dGateWidth,
ref dSWGateDelay, ref dSWGateWidth, ref iSWGateRamp); double pulsePeriod = 1 /
dPRF; //Pulse #1 as modulation source sendScpiCommand("[sens:puls:per](../GP-
IB_Command_Finder/Sense/Pulse.htm#period) " \+ pulsePeriod.ToString()); //
100us //Set Pulse1 width sendScpiCommand("[sens:puls1:width](../GP-
IB_Command_Finder/Sense/Pulse.htm#width) " \+ dModPulseWidth.ToString());
//10us //Set Pulse1 delay sendScpiCommand("[sens:puls1:delay](../GP-
IB_Command_Finder/Sense/Pulse.htm#delay) " \+ dModPulseDelay.ToString());
//10us  //Turn on Pulse1 sendScpiCommand("[SENS:PULS1:STAT](../GP-
IB_Command_Finder/Sense/Pulse.htm#state) 1"); //Set modulation source to
Pulse1
sendScpiCommand("[sens:path:conf:elem](../../IFAccess/IF_Path_Configuration.md#elements)
/"PulseModDrive/",/"Pulse1/""); //Enable pulse modulator 1
sendScpiCommand("sens:path:conf:elem /"Src1Out1PulseModEnable/",/"Enable/"");
//Pulse #2 controls receiver gate sendScpiCommand("sens:puls2:width " \+
dGateWidth.ToString()); //50ns sendScpiCommand("sens:puls2:delay " \+
dGateDelay.ToString()); //0  sendScpiCommand("SENS:PULS2:STAT 1");
sendScpiCommand("sens:path:conf:elem /"IFGateA/",/"Pulse2/"");
sendScpiCommand("sens:path:conf:elem /"IFGateB/",/"Pulse2/"");
sendScpiCommand("sens:path:conf:elem /"IFGateR1/",/"Pulse2/"");
sendScpiCommand("sens:path:conf:elem /"IFGateR2/",/"Pulse2/""); //Set IFBW
sendScpiCommand("SENS:BWID " \+ dBW.ToString()); //Configure IF path
sendScpiCommand("sens:path:conf:elem /"IFSigPathAll/",/"NBF/"");
sendScpiCommand("[SENS:IF:FILT:AUTO](../GP-
IB_Command_Finder/Sense/XSensIF.htm#auto) 0");
sendScpiCommand("[SENS:IF:FREQ:AUTO](../GP-
IB_Command_Finder/Sense/XSensIF.htm#FreqAuto) 0");
sendScpiCommand("[SENS:IF:FREQ](../GP-
IB_Command_Finder/Sense/XSensIF.htm#freqValue) " \+ dPhysicalIF.ToString());
// Set filter stages based on pulse parameters
sendScpiCommand("[SENS:IF:FILT:STAGe1:FREQ](../GP-
IB_Command_Finder/Sense/XSensIF.htm#stgFreq) " \+ dNCO.ToString()); //Convert
Stage1TapArray to string string buf1 = new string(' ', 1000); for (int i = 0;
i < aStage1TapArray.GetLength(0); i++) { buf1 = buf1 +
aStage1TapArray.GetValue(i).ToString() \+ ","; } buf1 = buf1.Trim(); buf1 =
buf1.Substring(0, buf1.Length \- 1); //Convert Stage1TapArray to string string
buf2 = new string(' ', 1000); for (int j = 0; j <
aStage2TapArray.GetLength(0); j++) { buf2 = buf2 +
aStage2TapArray.GetValue(j).ToString() \+ ","; } buf2 = buf2.Trim(); buf2 =
buf2.Substring(0, buf2.Length \- 1); //Set IF Filter Stage1 and Stage2
Coeficent sendScpiCommand("[SENS:IF:FILT:STAG1:COEF](../GP-
IB_Command_Finder/Sense/XSensIF.htm#coef) " \+ buf1);
sendScpiCommand("SENS:IF:FILT:STAG2:COEF " \+ buf2); if (dSWGateWidth == 0) //
No valid SW gate { sendScpiCommand("[SENS:IF:FILT:STAG3:TYPE](../GP-
IB_Command_Finder/Sense/XSensIF.htm#stg3Type) 'RECT'");
sendScpiCommand("[SENS:IF:FILT:STAGe3:PAR](../GP-
IB_Command_Finder/Sense/XSensIF.htm#stg3Pcat) 'C'," \+
aStage3TapArray.GetValue(0).ToString());
sendScpiCommand("[SENS:PULS0:STAT](../GP-
IB_Command_Finder/Sense/Pulse.htm#state) 0"); } else {
sendScpiCommand("SENS:IF:FILT:STAGe3:TYPE 'PWIN'");
sendScpiCommand("SENS:IF:FILT:STAGe3:PAR 'C'," \+
aStage3TapArray.GetValue(0).ToString());
sendScpiCommand("SENS:IF:FILT:STAGe3:PAR 'P'," \+ pulsePeriod.ToString());
sendScpiCommand("SENS:IF:FILT:STAGe3:PAR 'D'," \+ dSWGateDelay.ToString());
sendScpiCommand("SENS:IF:FILT:STAGe3:PAR 'W'," \+ dSWGateWidth.ToString());
sendScpiCommand("SENS:IF:FILT:STAGe3:PAR 'R'," \+ iSWGateRamp.ToString());
double pulse0Width = 1 / dClockFreq; sendScpiCommand("sens:puls0:width " \+
pulse0Width.ToString()); sendScpiCommand("sens:puls0:delay 0");
sendScpiCommand("SENS:PULS0:STAT 1"); } pulseApp.ConfigEnhancedNBIFAtten(dPRF,
dGateWidth, ref myAtten);
sendScpiCommand("[sens:path:conf:elem](../../IFAccess/IF_Path_Configuration.md#elements)
/"NBFATNA/",/"" \+ myAtten.ToString() + "/"");
sendScpiCommand("sens:path:conf:elem /"NBFATNB/",/"" \+ myAtten.ToString() +
"/""); sendScpiCommand("sens:path:conf:elem /"NBFATNR1/",/"" \+
myAtten.ToString() + "/""); sendScpiCommand("sens:path:conf:elem
/"NBFATNR2/",/"" \+ myAtten.ToString() + "/""); //Set start and stop frequency
sendScpiCommand("SENS:FREQ:STAR 1000000000"); sendScpiCommand("SENS:FREQ:STOP
2000000000"); //Single Sweep sendScpiCommand("SENS:SWE:MODE SING");
sendScpiCommand("DISP:WIND:TRAC:Y:AUTO"); } }  
---


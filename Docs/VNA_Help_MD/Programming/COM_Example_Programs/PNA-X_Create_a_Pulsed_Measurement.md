## Create a Narrowband Pulsed Measurement using the PNA-X or N522x

* * *

The following COM example demonstrates how to create a narrowband pulsed
measurement using the Pulsed Application DLL on the
[PNA-X](../../Support/Configurations.md#PNAX).

See the example program for [wideband pulsed
measurements](Create_a_Wideband_Pulsed_Measurement_using_the_PNA-X.htm) on the
PNA-X.

It first gets valid configuration settings and then uses those settings to
configure the VNA and internal pulsed generators.

To run this program, you need:

  * PNA-X or N522x

  * [Pulsed Application](../../Applications/Narrowband_Pulsed_Application.md) (Option H08)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Pulse.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

### See Also

  * Learn how to [install and register the pulsed .dll](../../Applications/Narrowband_Pulsed_Application.md#Install) on your PC

  * See the [ConfigEnhancedNB2](../COM_Reference/Methods/ConfigEnhancedNB2_Method.md) method for sending and returning parameters to the .dll.

  * See the [ConfigEnhancedNBIFAtten](../COM_Reference/Methods/ConfigEnhancedNBIFAtten_Method.md) method for setting the receiver IF gain.

  * See the [COM IF Configuration](../COM_Reference/Objects/IIFConfiguration_Object.md) commands used in the program.

  * See the equivalent [SCPI IF Configuration](../GP-IB_Command_Finder/Sense/XSensIF.md) commands.

'Interfaces Dim OApp As AgilentPNA835x.application Dim OIntPG As
AgilentPNA835x.PulseGenerator Dim OPathConf As
AgilentPNA835x.PathConfiguration Dim OFilter As
AgilentPNA835x.SignalProcessingModuleFour Dim OIF As
AgilentPNA835x.IFConfiguration 'Pulsed parameters Dim DPRF As Double Dim DBW
As Double Dim DPhysicalIF As Double Dim DNCO As Double Dim DCF As Double Dim
DGD As Double Dim DGW As Double Dim DSWGD As Double Dim DSWGW As Double Dim
DSWGR As Long Dim LStage1TapArray() As Long Dim LStage2TapArray() As Long Dim
LStage3TapArray() As Long Dim BFixedPRF As Boolean Dim IIFAtten As Integer
'pulsed DLL interface Dim OPulsed As New AgilentPNAPulsed.application 'Pulsed
settings DPRF = 5000 'Hz DBW = 500 'Hz BFixedPRF = True DNCO = 0# DCF = 0# DGD
= 0# DGW = 0.000001 DSWGR = 0# 'Send desired pulsed parameters to the pulsed
configuration DLL. The DLL will return a new set of pulse parameters to send
to the VNA. OPulsed.ConfigEnhancedNB2 DPRF, DBW, DPhysicalIF, DNCO, DCF,
LStage1TapArray, LStage2TapArray, LStage3TapArray, BFixedPRF, DGD, DGW, DSWGD,
DSWGW, DSWGR ' 'Send configuration to VNA ' 'Connect to the VNA application
Set OApp = CreateObject("AgilentPNA835x.Application") 'Create instance of
pulse generators on active channel Set OIntPG =
OApp.ActiveChannel.PulseGenerator 'Create instance of path configuration on
active channel Set OPathConf = OApp.ActiveChannel.PathConfiguration 'Create
instance of digital filter on active channel Set OIF =
OApp.ActiveChannel.IFConfiguration 'Create instance of Hana digital filter on
active channel Set OFilter = OApp.ActiveChannel.SignalProcessingModuleFour
'Set up primary pulse period for internal pulse generators OIntPG.Period = 1 /
DPRF 'Set up internal pulse generator output #1 to drive internal source
modulation OIntPG.Width(1) = 0.0001 '100us OIntPG.Delay(1) = 0.00001 '10us
OIntPG.State(1) = True OPathConf.Element("PulseModDrive").Value = "Pulse1"
'Set up internal pulse generator output #2 to drive internal receiver gates
for a 2 port PNA-X OIntPG.Width(2) = 0.000001 '1us OIntPG.Delay(2) = 0.00005
'50us OIntPG.State(2) = True OPathConf.Element("IFGateA").Value = "Pulse2"
OPathConf.Element("IFGateB").Value = "Pulse2"
OPathConf.Element("IFGateR1").Value = "Pulse2"
OPathConf.Element("IFGateR2").Value = "Pulse2" ' 'Configure VNA in pulsed mode
operation ' 'Turn off ALC and turn on modulator control
OApp.ActiveChannel.ALCLevelingMode(1) = naALCOpenLoop 'Source 1 output #1 ALC
off OPathConf.Element("Src1Out1PulseModEnable").Value = "Enable" 'Enable
Source 1 pulse modulator 'Set path and enable IF gates
OApp.ActiveChannel.IFBandwidth = DBW OPathConf.Element("IFSigPathAll").Value =
"NBF" 'Set filter stages based on pulse parameters OIF.IFFrequency =
DPhysicalIF OIF.IFFrequencyMode = naMANUAL OFilter.Stage1Frequency = DNCO
OFilter.Stage1Coefficients = LStage1TapArray OFilter.Stage2Coefficients =
LStage2TapArray OFilter.Stage3FilterType = "RECT" OFilter.Stage3Parameter("C")
= LStage3TapArray(0) OFilter.FilterMode = naMANUAL 'Set receivers to auto gain
setting OPulsed.ConfigEnhancedNBIFAtten DPRF, DGW, IIFAtten '1us pulse width
OPathConf.Element("NBFATNA").Value = IIFAtten
OPathConf.Element("NBFATNB").Value = IIFAtten
OPathConf.Element("NBFATNR1").Value = IIFAtten
OPathConf.Element("NBFATNR2").Value = IIFAtten MsgBox "Done"  
---  
  
* * *


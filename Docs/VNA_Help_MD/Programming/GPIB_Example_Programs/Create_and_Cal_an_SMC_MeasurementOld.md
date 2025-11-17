# Create and Cal an SMC Measurement using "Session" commands \- Superseded

* * *

Note: This example program uses SCPI commands that were used BEFORE VNA
release A.09.33. While these commands still work, we encourage you to use the
newer SMC commands that were introduced with the A.09.33 release. [See newer
commands](../GP-IB_Command_Finder/Sense/CorrCollGuidSMC.htm) and [example
program](Create_and_Cal_an_SMC_Measurement.htm).

This Visual Basic example creates and calibrates a scalar mixer measurement.

To run this example without modification you need the following:

  * A Mixer setup file saved on the VNA: C:\Program Files(86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxr.

  * If the mixer file uses an external LO source, it must also be attached and configured.

  * An ECAL module that covers the frequency range of the measurement.

  * A power meter must be attached to the VNA. If this example is run in the VNA, the power meter does not need to be attached using a GPIB/USB interface.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example. However, some modification is necessary to make the program run on a
traditional GPIB Interface. For example, during the power meter portion of
this calibration, scpi.Parse will not process a command until the power meter
routine has completed. Traditional GPIB would require a [serial polling
technique](Status_Reporting.htm) to ensure the routine has completed before
proceeding.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as SMC.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim app  
Dim scpi  
' Create / Get the VNA application.  
Set app = CreateObject("AgilentPNA835x.Application")  
Set scpi = app.ScpiStringParser  
'\---Create a Scalar Mixer Forward Measurement  
'First, delete all measurements on the channel  
scpi.Parse "CALC:PAR:DEL:ALL"  
'Create a forward scalar mixer measurement and configure it in  
'channel 1. The first parameter is a unique  
'identifying string (specified by the user) to allow subsequent  
'commands to be directed at this specific measurement.  
scpi.Parse "CALC:CUST:DEF 'My SC21', 'Scalar Mixer/Converter', 'SC21'"  
  
'Setup the new measurement as the 2nd trace in the active window  
scpi.Parse "DISP:WIND:TRAC2:FEED 'My SC21'"  
'Make the new trace the active measurement  
scpi.Parse "CALC:PAR:SEL 'My SC21'"  
'The parameters of the mixer measurement can now be configured.  
'This can be done by either using the individual SENS:MIX commands  
'for each of the parameters or by loading a mixer setup file. This  
'example loads a mixer setup file. The path name  
'for the mixer file may be loaded from other mapped drives  
scpi.Parse "SENS:MIXer:Load ""C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\Mixer\MyMixer.mxr"""  
'\--------------Perform A Scalar Mixer Calibration----------------------  
'Initialize an SMC guided calibration for session number 6  
scpi.Parse "SENS:CORR:COLL:SESS6:INIT ""SMC"""  
'Select to use an ECal for the 2-port cal portion of the procedure  
'To use a mechanical kit you will have to use the following command:  
'scpi.Parse "SENS:CORR:COLL:SESS6:SMC:TWOPort:OPTion ""MECH"""  
scpi.Parse "SENS:CORR:COLL:SESS6:SMC:TWOPort:OPTion ""ECAL"""  
'If you select the mechanical method then you also have to  
'specify the connector types and the cal kits for each of the ports.  
'The comments below show an example of how that is done:  
'scpi.Parse "SENS:CORR:COLL:SESS6:CONN:PORT1:SEL ""APC 3.5 male"""  
'scpi.Parse "SENS:CORR:COLL:SESS6:CONN:PORT2:SEL ""APC 3.5 female"""  
'scpi.Parse "SENS:CORR:COLL:SESS6:CKIT:PORT1:SEL ""85052D"""  
'scpi.Parse "SENS:CORR:COLL:SESS6:CKIT:PORT2:SEL ""85052D"""  
'Specify the ECal module and the ECal characterization for this  
'session. FCA calibrations currently only support ECal module  
'number 1. In this example the factory characterization is used  
'by specifying 0 for the characterization number.  
scpi.Parse "SENS:CORR:COLL:SESS6:SMC:ECAL:CHAR 1,0"  
'Specify the thru measurement method. This applies to both ECal  
'and mechanical calibrations. For ECal 'DEFAULT' will use the ECal  
'thru. Other choices may be used depending on the genders and types  
'of the connectors on the test interface.  
scpi.Parse "SENS:CORR:COLL:SESS6:SMC:TWOP:METH ""DEFAULT"""  
'Omit the isolation part of the 2-port cal  
scpi.Parse "SENS:CORR:COLL:SESS6:SMC:TWOP:OMIT 1"  
'Turn on auto orientation for the ECal  
scpi.Parse "SENS:CORR:COLL:SESS6:SMC:TWOP:ECAL:ORI:STATE 1"  
'Tell the wizard to generate and report the number of steps in this  
'cal session  
Dim steps  
Dim desc  
'Determine the number of steps required to complete the calibration.  
'First send the write command, then the query.  
scpi.Parse "SENS:CORR:COLL:SESS6:STEP"  
steps = scpi.Parse ("SENS:CORR:COLL:SESS6:STEP?")  
For i = 1 To steps  
'Display the prompt for each step  
desc = scpi.Parse ("SENS:CORR:COLL:SESS6:DESC? " & CStr(i))  
MsgBox (desc)  
'Perform the measurement for each step  
scpi.Parse "SENS:CORR:COLL:SESS6:ACQ " & CStr(i)  
Next  
Dim calset  
'Finish the cal and save the calset  
calset = scpi.Parse ("SENS:CORR:COLL:SESS6:SAVE?")  
scpi.Parse ("SENS:CORR:COLL:SESS6:DONE")  
Msgbox ("SMC Cal Complete!")

* * *


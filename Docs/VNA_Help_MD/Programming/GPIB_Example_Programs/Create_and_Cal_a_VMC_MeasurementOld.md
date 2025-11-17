# Create and Calibrate a VMC Measurement using "Session" commands \-
Superseded

* * *

Note: This example program uses SCPI commands that were used BEFORE VNA
release A.09.33. While these commands still work, we encourage you to use the
newer VMC commands that were introduced with the A.09.33 release. [See newer
commands](../GP-IB_Command_Finder/Sense/CorrCollGuidVMC.htm) and [example
program](Create_and_Cal_a_VMC_Measurement.htm).

This VB Script example creates and calibrates a Vector mixer measurement. To
run this example without modification you need the following:

  * A Mixer setup file saved on the VNA: C:\Program Files(x86)\Keysight\Network Analyzer\Documents\Mixer\MyMixer.mxr.

  * If the mixer file uses an external LO source, it must also be attached and configured.

  * An ECal module that covers the frequency range of the measurement.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example. However, some modification is necessary to make the program run on a
traditional GPIB Interface.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as VMC.vbs. Learn how to setup and run the macro.

Dim app  
Dim scpi  
' Create / Get the VNA application.  
Set app = CreateObject("AgilentPNA835x.Application")  
Set scpi = app.ScpiStringParser  
'\---Create a Vector Mixer Measurement  
'First, delete all measurements on the channel  
scpi.Parse "CALC:PAR:DEL:ALL"  
'Create a forward scalar mixer measurement and configure  
'it in channel 1.  
'The first parameter is a unique identifying string  
'(specified by the user) to allow subsequent  
'commands to be directed at this specific measurement.  
scpi.Parse "CALC:CUST:DEF 'My VC21', 'Vector Mixer/Converter', 'VC21'"  
'Setup the new measurement as the 2nd trace in the active window  
scpi.Parse "DISP:WIND:TRAC2:FEED 'My VC21'"  
'Make the new trace the active measurement  
scpi.Parse "CALC:PAR:SEL 'My VC21'"  
'The parameters of the mixer measurement can now be configured.  
'This can be done by either using the SENS:MIX commands  
'for each of the parameters or by loading a mixer setup file.  
'This example loads a mixer setup file. The path name  
'for the mixer file may be loaded from other mapped drives.  
scpi.Parse "SENS:MIXer:Load 'c:\users\public\network
analyzer\documents/Mixer/MyMixer.mxr'"  
  
'\--------------Perform A Vector Mixer Calibration-------------  
'Initialize an VMC guided calibration for session number 6  
scpi.Parse "SENS:CORR:COLL:SESS6:INIT ""VMC"""  
'This sets the VMC operation to full system cal as opposed to  
'performing a mixer characterization only.  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:OPER ""CAL"""  
'This example uses ECal for the 2-port cal portion of the procedure  
'To use a mechanical kit you will have to use the following command:  
'scpi.Parse "SENS:CORR:COLL:SESS6:SMC:TWOPort:OPTion""MECH"""  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:TWOPort:OPTion ""ECAL"""  
'If you select the mechanical method then you also have to  
'specify the connector types and the cal kits for each of the ports.  
'The comments below show an example of how that is done:  
'scpi.Parse "SENS:CORR:COLL:SESS6:CONN:PORT1:SEL ""APC 3.5 male"""  
'scpi.Parse "SENS:CORR:COLL:SESS6:CONN:PORT2:SEL ""APC 3.5 female"""  
'scpi.Parse "SENS:CORR:COLL:SESS6:CKIT:PORT1:SEL ""85052D"""  
'scpi.Parse "SENS:CORR:COLL:SESS6:CKIT:PORT2:SEL ""85052D"""  
'Choose the between ECal or Mechanical calibration for the  
'Mixer Characterization portion of the VMC cal.  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:MIX:CHAR:CAL:OPT ""ECAL"""  
'This command sets the port mapping for the ECal to be used  
'during the Mixer Characterization portion of the VMC cal.  
'It is a required command if in the previous command the option  
'was set to 'ECAL'. The only valid port maps are either 'A1'  
'or 'B1'.  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:MIX:ECAL:PORT 1, ""A1"""  
'Specify the ECal module and the ECal characterization for the  
'two port calibration portion of this session. FCA calibrations  
'currently only support ECal module number 1. In this example  
'the factory characterization is used by specifying 0 for the  
'characterization number.  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:TWOP:ECAL:CHAR 1,0"  
'Specify the ECal module and the ECal characterization for the  
'Mixer Characterization portion of this session. FCA calibrations  
'currently only support ECal module number 1. In this example  
'the factory characterization is used by specifying 0 for the  
'characterization number.  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:MIX:ECAL:CHAR 1,0"  
'Specify the thru measurement method. This applies to both ECal  
'and mechanical calibrations. For ECal 'DEFAULT' will use the ECal  
'thru. Other choices may be used depending on the genders and types  
'of the connectors on the test interface.  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:TWOP:METH ""DEFAULT"""  
'Omit the isolation part of the 2-port cal  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:TWOP:OMIT 1"  
'Turn on auto orientation for the ECal  
scpi.Parse "SENS:CORR:COLL:SESS6:VMC:TWOP:ECAL:ORI:STATE 1"  
  
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
Msgbox ("VMC Cal Complete!")  

* * *


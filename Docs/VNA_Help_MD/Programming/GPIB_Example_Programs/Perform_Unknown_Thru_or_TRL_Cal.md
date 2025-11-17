# Perform Unknown Thru or TRL Cal

* * *

The following program performs either a 2-port SOLT Unknown Thru Cal or a
2-port TRL Cal. The 85052C Cal Kit used in this program contains both types of
standards. This program can be run on 2-port or 4-port VNAs. When run on
[select PNA-L models](../../S3_Cals/Delta_Match_Calibration.md), a Delta
Match Cal is required.

  * [See Delta Match Cal example program](Perform_Global_Delta_Match_Cal.md)

  * [See the Guided Cal commands](../GP-IB_Command_Finder/Sense/CorrGuided.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Unknown.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

Sub PerformUnknownThruOrTRLCal() Set pna =
CreateObject("AgilentPNA835x.Application") Set scpi = pna.ScpiStringParser '
Specify connectors for Ports 1 and 2 scpi.Parse
"SENS:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 female'" scpi.Parse
"SENS:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 male'" 'If your VNA has 3 or 4 ports,
uncomment one or both of 'these next two lines, to explicitly specify this is
a 2-port cal. 'scpi.Parse "SENS:CORR:COLL:GUID:CONN:PORT3 'Not used'"
'scpi.Parse "SENS:CORR:COLL:GUID:CONN:PORT4 'Not used'" ' Specify cal kit for
Ports 1 and 2 scpi.Parse "SENS:CORR:COLL:GUID:CKIT:PORT1 '85052C'" scpi.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT2 '85052C'" ' Since the 85052C cal kit contains
SOLT standards and also TRL ' standards, these next two lines set cal and thru
method. ' Always send the init command before and after these two commands
scpi.Parse "SENS:CORR:COLL:GUID:INIT" scpi.Parse
"SENS:CORR:COLL:GUID:PATH:CMEThod 1,2,"SOLT" scpi.Parse
"SENS:CORR:COLL:GUID:PATH:TMEThod 1,2,"Undefined Thru" ' To set up the cal as
TRL, comment the previous 'CMET' line and uncomment ' this next line. The
TMEThod is set by default 'scpi.Parse "SENS:CORR:COLL:GUID:PATH:CMEThod
1,2,"TRL" ' Initiate the calibration scpi.Parse "SENS:CORR:COLL:GUID:INIT" '
Query the list of ports that need delta match retStr =
scpi.Parse("SENS:CORR:COLL:GUID:DMAT:APPL:PORT?") portList = Split(retStr,
",") ' If portList contains just one element and it's value is 0, then that
indicates ' none of the ports being calibrated require delta match data. '
Note: if each testport on the VNA has it's own reference receiver (R channel),
' then delta match is never needed, so portList will always be just 0.
lowerBound = LBound(portList)  
If (UBound(portList) <> lowerBound) Or (CInt( portList(lowerBound) ) <> 0)
Then ' Delta match data is required for at least one port. ' For this example,
we assume a Global Delta Match Cal has previously been ' performed so the
Global Delta Match CalSet exists. ' The Global Delta Match CalSet is used when
the APPL command is invoked ' without a specific calset ID (GUID). scpi.Parse
"SENS:CORR:COLL:GUID:DMAT:APPL" End If ' Query the number of calibration steps
retStr = scpi.Parse("SENS:CORR:COLL:GUID:STEP?") numSteps = CInt(retStr) '
Measure the cal standards For i = 1 To numSteps prompt =
scpi.Parse("SENS:CORR:COLL:GUID:DESC? " & CStr(i)) retVal = MsgBox(prompt,
vbOKCancel) If retVal = vbCancel Then Exit Sub retStr =
scpi.Parse("SENS:CORR:COLL:GUID:ACQ STAN" & CStr(i) & ";*OPC?") Next ' Compute
the error coefficients and save the cal to CalSet, and turn it on scpi.Parse
"SENS:CORR:COLL:GUID:SAVE" MsgBox "Cal is done!" End Sub  
---  
  
* * *


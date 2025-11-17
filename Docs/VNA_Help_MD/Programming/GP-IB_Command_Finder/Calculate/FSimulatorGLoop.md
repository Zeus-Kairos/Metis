# Calculate:FSimulator:GLOop Commands

Specifies settings and fixturing for ground loop de-embedding / embedding.

CALCulate:FSIMulator:GLOop: DEEMBed: | PARameters: | C | L | R | STATe | TYPE | USER:FILename EMBed: | PARameters: | C | L | R | STATe | TYPE | USER:FILename PORTs:  
---  
  
See Also

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:PARameters:C <value>

Applicable Models: All (Read-Write) Sets and returns the Capacitance, 'C'
value for the ground loop de-embedding of the specified channel. Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Capacitance value in farads. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:GLO:DEEM:PAR:C 0.00002  
calculate2:fsimulator:gloop:deembed:parameters:c 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:PARameters:C?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:PARameters:L <value>

Applicable Models: All (Read-Write) Sets and returns the Inductance, 'L' value
for the ground loop de-embedding of the specified channel. Note: This command
affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Inductance value in henries. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:GLO:DEEM:PAR:L 0.00002  
calculate2:fsimulator:gloop:deembed:parameters:l 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:PARameters:L?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:PARameters:R <value>

Applicable Models: All (Read-Write) Sets and returns the Resistance, 'R' value
for the ground loop de-embedding of the specified channel. Note: This command
affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Resistance value in ohms. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:GLO:DEEM:PAR:R 0.00002  
calculate2:fsimulator:gloop:deembed:parameters:r 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:PARameters:R?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:STATe <bool>

Applicable Models: All (Read-Write) Turns ON or OFF De-embedding for the
specified channel. Note: This command affects ALL measurements on the
specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | Choose from: ON or 1 - Turns De-embedding ON OFF or 0 - Turns De-embedding OFF  
Examples | CALC:FSIM:GLO:DEEM:STAT 1  
calculate2:fsimulator:gloop:deembed:state 0  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:TYPE <char>

Applicable Models: All (Read-Write) Specifies the circuit model type for
ground loop de-embedding.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Choose from: USER \- Loads s1p file specified using the CALC:FSIM:GLO:DEEM:USER command. RL \- Selects Shunt L circuit model. RC \- Selects Shunt C circuit mode.  
Examples | CALC:FSIM:GLO:DEEM:TYPE RL  
calculate2:fsimulator:gloop:deembed:type RC  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | RL  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:USER:FILename <filename>

Applicable Models: All (Read-Write) Specifies the filename of the s1p file to
load for ground loop de-embedding. Note: This command affects ALL measurements
on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<filename> | File name and extension (.s1P) of the de-embedding circuit. Files are stored in the default folder "D:\" To recall from a different folder, specify the full path name.  
Examples | CALC:FSIM:GLO:DEEM:USER:FIL 'myFile.s1P'  
calculate2:fsimulator:gloop:deembed:user:filename "D:\myFile.s1P"  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:DEEMbed:USER:FILename?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:EMBed:PARameters:C <value>

Applicable Models: All (Read-Write) Sets and returns the Capacitance, 'C'
value for the ground loop embedding of the specified channel. Note: This
command affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Capacitance value in farads. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:GLO:EMB:PAR:C 0.00002  
calculate2:fsimulator:gloop:embed:parameters:c 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:EMBed:PARameters:C?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:EMBed:PARameters:L <value>

Applicable Models: All (Read-Write) Sets and returns the Inductance, 'L' value
for the ground loop embedding of the specified channel. Note: This command
affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Inductance value in henries. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:GLO:EMB:PAR:L 0.00002  
calculate2:fsimulator:gloop:embed:parameters:l 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:EMBed:PARameters:L?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:EMBed:PARameters:R <value>

Applicable Models: All (Read-Write) Sets and returns the Resistance, 'R' value
for the ground loop embedding of the specified channel. Note: This command
affects ALL measurements on the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<value> | Resistance value in ohms. Choose a value between -1E18 to 1E18  
Examples | CALC:FSIM:GLO:EMB:PAR:R 0.00002  
calculate2:fsimulator:gloop:embed:parameters:r 0.00003  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:EMBed:PARameters:R?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:EMBed:STATe <bool>

Applicable Models: All (Read-Write) Turns ON or OFF Embedding for the
specified channel. Note: This command affects ALL measurements on the
specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<bool> | Choose from: ON or 1 - Turns Embedding ON OFF or 0 - Turns Embedding OFF  
Examples | CALC:FSIM:GLO:EMB:STAT 1  
calculate2:fsimulator:gloop:embed:state 0  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:EMBed:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:EMBed:TYPE <char>

Applicable Models: All (Read-Write) Specifies the circuit model type for
ground loop embedding. Learn more.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | Choose from: USER \- Loads s1p file specified using the CALC:FSIM:GLO:EMB:USER command. RL \- Selects Shunt L circuit model. RC \- Selects Shunt C circuit mode.  
Examples | CALC:FSIM:GLO:EMB:TYPE RL  
calculate2:fsimulator:gloop:embed:type RC  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:EMBed:TYPE?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | RL  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:EMBed:USER:FILename <filename>

Applicable Models: All (Read-Write) Specifies the filename of the s1p file to
load for ground loop embedding. Note: This command affects ALL measurements on
the specified channel.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<filename> | File name and extension (.s1P) of the embedding circuit. Files are stored in the default folder "D:\" To recall from a different folder, specify the full path name.  
Examples | CALC:FSIM:GLO:EMB:USER:FIL 'myFile.s1P'  
calculate2:fsimulator:gloop:embed:user:filename "D:\myFile.s1P"  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:EMBed:USER:FILename?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

CALCulate<cnum>:FSIMulator:GLOop:PORTs <p1>,<p2>,<p3>,<p4>

Applicable Models: All (Read-Write) Specifies the VNA port connections for
ground loop embedding/de-embedding. Ground loop ports are typically
automatically determined based on the requested measurements, fixturing ports,
and calibration ports. However, if it is desired to set them specifically, use
this command.  
---  
Parameters |   
<cnum> | Channel number of the measurement.  
<p1>,<p2>,<p3>,<p4> | VNA port number assignment.  
Examples | CALC:FSIM:GLO:PORT 1,2  
calculate2:fsimulator:gloop:ports 3,4  
Query Syntax | CALCulate<cnum>:FSIMulator:GLOop:PORTs?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *


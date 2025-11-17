# CALCulate:MEASure:Correction Commands

Controls error correction functions.

CALCulate:MEASure:CORRection EDELay | DISTance | MEDium | [:TIME] | UNIT | WGCutoff [:STATe] | INDicator? TYPE  
---  
  
Click a keyword to view the command details.

See Also

  * [Calibrating with SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay:DISTance <num>

Applicable Models: All (Read-Write) Sets the electrical delay in physical
length (distance) for the selected measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Electrical delay in distance. First Specify units using CALC:MEAS:CORR:EDEL:UNIT Use [SENS:CORR:RVEL:COAX](../Sense/Sense_Correction.md#scrc) <num> to set Velocity factor. This parameter supports MIN and MAX as arguments. [Learn more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min)  
Examples | CALC1:MEAS2:CORR:EDEL:DIST 5 calculate2:measure2:correction:edelay:distance .003  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay:DISTance?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay:MEDium <char>

Applicable Models: All (Read-Write) Sets the media used when calculating the
electrical delay.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Choose from: COAX for coaxial medium, WAVEguide for waveguide medium.  
Examples | CALC:MEAS2:CORR:EDEL:MED COAX calc3:measure2:correction:edelay:medium waveguide  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay:MEDium?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | COAX  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay[:TIME] <num>

Applicable Models: All (Read-Write) Sets the electrical delay for the selected
measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Electrical delay in seconds. Choose any number between:  
-10.00 and 10.00  
Use [SENS:CORR:RVEL:COAX](../Sense/Sense_Correction.md#scrc) <num> to set
Velocity factor. This parameter supports MIN and MAX as arguments. [Learn
more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)  
Examples | CALC1:MEAS2:CORR:EDEL:TIME 1NS  
calculate2:measure2:correction:time 0.5e-12  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay[:TIME]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 seconds  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay:UNIT <char>

Applicable Models: All (Read-Write) Sets and returns the units for specifying
electrical delay in physical length (distance).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<char> | Units for delay in distance. Choose from:

  * METer
  * FEET
  * INCH

  
Examples | CALC:MEAS2:CORR:EDEL:UNIT MET calc3:meas2:corr:edelay:unit inch  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay:UNIT?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | METer  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay:WGCutoff <num>

Applicable Models: All (Read-Write) Sets the waveguide cutoff frequency used
when the electrical delay media is set to WAVEguide. (See
CALCulate:MEAS:CORRection:EDELay:MEDium <char>.)  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<num> | Waveguide cutoff frequency used with the electrical delay calculation. This parameter supports MIN and MAX as arguments. [Learn more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min)  
Examples | CALC:MEAS2:CORR:EDEL:WGC 18.067 GHz calculate3:measure2:correction:edelay:wgcutoff 14.047 ghz  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:CORRection:EDELay:WGCutoff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 45 MHz  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:CORRection[:STATe] <bool>

Applicable Models: All (Read-Write) Turns error correction ON or OFF for the
selected measurement on the specified channel. To turn error correction ON or
OFF for a channel, use [SENS:CORR:STATe](../Sense/Sense_Correction.md#scs).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<bool> | Correction state. Choose from: 0 \- Correction OFF 1 \- Correction ON  
Examples | CALC:MEAS2:CORR ON calculate:measure2:correction:state off  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:CORRection:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:CORRection[:STATe]:INDicator?

Applicable Models: All (Read-only) Returns the error correction state for the
selected measurement on the specified channel.  To turn error correction ON or
OFF for a channel, use [SENS:CORR:STATe](../Sense/Sense_Correction.md#scs).  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
Examples | CALC:MEAS2:CORR:IND? calculate2:measure2:correction:state:indicator?  
Return Type | Character NONE \- No error correction MAST (Master) - Original error correction terms INT \- Error terms are interpolated. [Learn more](../../../S3_Cals/Error_Correction_and_Interpolation.md). DELT \- Delta Match calibration terms. [Learn more](../../../S3_Cals/Delta_Match_Calibration.md). INV \- Error terms are not valid  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NONE  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:CORRection:TYPE <string>

Applicable Models: All (Read-Write) Sets the Cal Type for the selected
measurement on the specified channel. This is used when a Cal Set is applied.
[Learn more about applying Cal
Types.](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm#Applying)

  * Use [SENS:CORR:TYPE:CAT?](../Sense/Sense_Correction.md#catalog) to list the Cal Types in the VNA.
  * Use [SENS:CORR:CSET:TYPE:CAT?](../Sense/CorrCset.md#catalog) to list the Cal Types contained in the active Cal Set for the channel.
  * Use [SENS:CORR:COLL:METH](../Sense/Sense_Correction.md#sccm) to set the Cal type to perform a new Unguided calibration,

  
---  
Parameters |   
<cnum> | Channel number of the measurement (optional).  
<mnum> | Measurement number for each measurement.   
<string> | (String) Cal type. Case sensitive. Use one of the following:

### For Full Calibrations (NO Power Cal included):

This command does not distinguish between TRL and SOLT. The same number of
error terms is applied for both Cal Types. "Full <n> Port(x,y,z...)" where <n>
= the number of ports to calibrate x,y,z = the port numbers to calibrate For
example: "Full 4 Port(1,2,3,4)"

### For Full Calibrations (including Power Cal):

After the Full <n> port, include the string, "with power" For example: "Full 4
Port with power(1,2,3,4)"

### For Response Calibrations:

"Response(param)" OR "ResponseAndIsolation(param)" Where param =

  * S-parameter. For example"
  *     * "Response(S21)"
    * "ResponseAndIsolation(A/R)"
  * Single or ratioed receivers using either [logical receiver notation](../../../S1_Settings/Measurement_Parameters.md#RecNotation) or physical receiver notation. For example:
  *     * "Response(A)"
    * "ResponseAndIsolation(a3/b4)"

### For Enhanced Response Calibrations:

"EnhancedResp(sourcePort, recPort) Where:

  * sourcePort = stimulus port number
  * recPort = receiver port number

### For FCA Calibrations:

[Learn more about this
setting.](../../../FreqOffset/SMC_Measurements.htm#SMCCalType)

  * "SMC_2P" (Response + Input + Output) All four sweeps required. Most accurate.

Note: The SMC_2P is the only correction type that automatically forces the
reverse measurements (SC12, RevOPwr, RevIPwr). If you require any of the
reverse measurements while using a lesser correction type, either include
those parameters in your channel or use the
[SENSe:MIXer:REVerse](../Sense/MIXerSCPI.md#Reverse) command. Keep in mind
that adding the reverse measurements or forcing the reverse sweep using the
[SENSe:MIXer:REVerse](../Sense/MIXerSCPI.md#Reverse) command will increase
the number of sweeps required in the channel.

  * "SMCRsp+IN" No Output match. Saves two sweeps.
  * "SMCRsp+OUT" No Output match. Saves one sweep.
  * "SMCRsp" No Input or Output match. Saves two sweeps.

For VMC, multiple Cal types are not available.

### For Gain Compression Cal

where r = receive port; s = source port

  * "GCA 2P (r,s) - full 2-port cal
  * GCA Enh Resp (r,s) - Enhanced Response Cal

  
Examples | CALC:MEAS2:CORR:TYPE "Scalar Mixer Cal"  
Query Syntax | CALCulate<cnum>:MEASure<mnum>:CORRection:TYPE?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *


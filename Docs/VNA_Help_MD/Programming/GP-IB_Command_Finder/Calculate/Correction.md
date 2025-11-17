# Calculate:Correction Commands

* * *

Controls error correction functions.

These commands are Superseded by the
[CALCulate:MEASure:CORRection](MeasureCorrection.md) commands.

CALCulate:CORRection EDELay | [DISTance](Correction.md#Delaydistance) | [TIME](Correction.md#EdelTime) | [MEDium](Correction.md#EdelMEDium) | [UNIT](Correction.md#edelUNIT) | [WGCutoff](Correction.md#EdelWGCutoff) ERRor | [:STATe] | TYPE [[STATe]](Correction.md#ErrorState) | [INDicator?](Correction.md#indicator) [TYPE](Correction.md#ErorType) OFFSet | [[MAGNitude]](Correction.md#OffsMagn) | [PHASe](Correction.md#OffsPhase)  
---  
  
Click on a keyword to view the command details.

Blue keywords are superseded.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Calibrating with SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## CALCulate<cnum>:CORRection:EDELay:DISTance <num>

Applicable Models: All (Read-Write) Sets the electrical delay in physical
length (distance) for the selected measurement. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Electrical delay in distance. First Specify units using [CALC:CORR:EDEL:UNIT](Correction.md#edelUNIT) Use [SENS:CORR:RVEL:COAX](../Sense/Sense_Correction.md#scrc) <num> to set Velocity factor. This parameter supports MIN and MAX as arguments. [Learn more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min)  
Examples | CALC1:CORR:EDEL:DIST 5 calculate2:correction:distance .003  
Query Syntax | CALCulate:CORRection:EDELay:DISTance?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## CALCulate<cnum>:CORRection:EDELay:MEDium <char>

Applicable Models: All (Read-Write) Sets the media used when calculating the
electrical delay.  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<num> | Choose from: COAX for coaxial medium, WAVEguide for waveguide medium.  
Examples | CALC:CORR:EDEL:MED COAX calc3:corr:edelay:medium waveguide  
Query Syntax | CALCulate<cnum>:CORRection:EDELay:MEDium?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | COAX  
  
* * *

## CALCulate<cnum>:CORRection:EDELay:UNIT <char>

Applicable Models: All (Read-Write) Sets and returns the units for specifying
electrical delay in physical length (distance).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<char> | Units for delay in distance. Choose from:

  * METer
  * FEET
  * INCH

  
Examples | CALC:CORR:EDEL:UNIT MET calc3:corr:edelay:unit inch  
Query Syntax | CALCulate<cnum>:CORRection:EDELay:UNIT?  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | METer  
  
* * *

## CALCulate<cnum>:CORRection:EDELay[:TIME] <num>

Applicable Models: All (Read-Write) Sets the electrical delay for the selected
measurement. See Critical Note  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Electrical delay in seconds. Choose any number between:  
-10.00 and 10.00  
Use [SENS:CORR:RVEL:COAX](../Sense/Sense_Correction.md#scrc) <num> to set
Velocity factor. This parameter supports MIN and MAX as arguments. [Learn
more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.htm#min)  
Examples | CALC1:CORR:EDEL:TIME 1NS  
calculate2:correction:time 0.5e-12  
Query Syntax | CALCulate:CORRection:EDELay[:TIME]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 seconds  
  
* * *

## CALCulate<cnum>:CORRection:EDELay:WGCutoff <num>

Applicable Models: All (Read-Write) Sets the waveguide cutoff frequency used
when the electrical delay media is set to WAVEguide. (See
CALCulate:CORRection:EDELay:MEDium <char>.)  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1.  
<num> | Waveguide cutoff frequency used with the electrical delay calculation. This parameter supports MIN and MAX as arguments. [Learn more.](../../Learning_about_GPIB/The_Rules_and_Syntax_of_SCPI_Commands.md#min)  
Examples | CALC:CORR:EDEL:WGC 18.067 GHz calculate3:correction:edelay:wgcutoff 14.047 ghz  
Query Syntax | CALCulate<cnum>:CORRection:EDELay:WGCutoff?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 45 MHz  
  
* * *

## CALCulate<cnum>:CORRection:ERRor[:STATe] <bool>

Applicable Models: All (Read-Write) Turns error correction ON or OFF on the
specified channel. To turn error correction ON or OFF for a channel, use
[SENS:CORR:STATe](../Sense/Sense_Correction.md#scs). See Critical Note  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Correction state. Choose from: 0 \- Correction OFF 1 \- Correction ON  
Examples | CALC:CORR:ERR ON calculate:correction:error:state off  
Query Syntax | CALCulate<cnum>:CORRection:ERRor:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:CORRection:ERRor:TYPE <string>

Applicable Models: All (Read-Write) Sets the Cal Type on the specified
channel. This is used when a Cal Set is applied. [Learn more about applying
Cal
Types.](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm#Applying)

  * Use [SENS:CORR:TYPE:CAT?](../Sense/Sense_Correction.md#catalog) to list the Cal Types in the VNA.
  * Use [SENS:CORR:CSET:TYPE:CAT?](../Sense/CorrCset.md#catalog) to list the Cal Types contained in the active Cal Set for the channel.
  * Use [SENS:CORR:COLL:METH](../Sense/Sense_Correction.md#sccm) to set the Cal type to perform a new Unguided calibration,

See Critical Note  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
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
  * "SMCRsp+IN" No Output match. All four sweeps required.
  * "SMCRsp+OUT" No Input match. All four sweeps required.
  * "SMCRsp" No Input or Output match. Saves two sweeps.

For VMC, multiple Cal types are not available.

### For Gain Compression Cal

where r = receive port; s = source port

  * "GCA 2P (r,s) - full 2-port cal
  * GCA Enh Resp (r,s) - Enhanced Response Cal

For Noise Figure Cal

  * VNC_2P \- full 2-port Vector Noise Figure correction (requires vector noise figure calset).
  * SNC_2P \- full 2-port Scalar Noise Figure correction (requires either scalar or vector noise figure calset).

  
Examples | CALC:CORR:ERR:TYPE "Scalar Mixer Cal"  
Query Syntax | CALCulate<cnum>:CORRection:ERRor:TYPE?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:CORRection[:STATe] <bool>

Applicable Models: All (Read-Write) Turns error correction ON or OFF for the
selected measurement on the specified channel. To turn error correction ON or
OFF for a channel, use [SENS:CORR:STATe](../Sense/Sense_Correction.md#scs).
See Critical Note  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<bool> | Correction state. Choose from: 0 \- Correction OFF 1 \- Correction ON  
Examples | CALC:CORR ON calculate:correction:state off  
Query Syntax | CALCulate<cnum>:CORRection:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:CORRection[:STATe]:INDicator?

Applicable Models: All (Read-only) Returns the error correction state for the
selected measurement on the specified channel.  To turn error correction ON or
OFF for a channel, use [SENS:CORR:STATe](../Sense/Sense_Correction.md#scs).
See Critical Note  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
Examples | CALC:CORR:IND? calculate2:correction:state:indicator?  
Return Type | Character NONE \- No error correction MAST (Master) - Original error correction terms INT \- Error terms are interpolated. [Learn more](../../../S3_Cals/Error_Correction_and_Interpolation.md). DELT \- Delta Match calibration terms. [Learn more](../../../S3_Cals/Delta_Match_Calibration.md). INV \- Error terms are not valid  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | NONE  
  
* * *

## CALCulate<cnum>:CORRection:TYPE <string>

Applicable Models: All (Read-Write) Sets the Cal Type for the selected
measurement on the specified channel. This is used when a Cal Set is applied.
[Learn more about applying Cal
Types.](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm#Applying)

  * Use [SENS:CORR:TYPE:CAT?](../Sense/Sense_Correction.md#catalog) to list the Cal Types in the VNA.
  * Use [SENS:CORR:CSET:TYPE:CAT?](../Sense/CorrCset.md#catalog) to list the Cal Types contained in the active Cal Set for the channel.
  * Use [SENS:CORR:COLL:METH](../Sense/Sense_Correction.md#sccm) to set the Cal type to perform a new Unguided calibration,

See Critical Note  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
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

"EnhancedResp(recPort, sourcePort) Where:

  * recPort = receiver port number
  * sourcePort = stimulus port number

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

  
Examples | CALC:CORR:TYPE "Scalar Mixer Cal"  
Query Syntax | CALCulate<cnum>:CORRection:TYPE?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:CORRection:OFFSet[:MAGNitude] <num> Superseded

Applicable Models: All Note: This command is replaced with
[SENS:CORR:RPOWer:OFFSet[:AMPLitude]](../Sense/Sense_Correction.md#RecPowerOffset).  
To set data trace magnitude offset, use [CALC:OFFS:MAGN](Offset.md#mag)  
This command does NOT function for FCA measurements. See an example of a
[Receiver Power
Calibration](../../GPIB_Example_Programs/Perform_a_Source_Cal_using_SCPI.htm#Receiver).
(Read-Write) For Receiver Power Calibration, specifies the power level to
which the selected (unratioed) measurement data is to be adjusted. This
command applies only when the selected measurement is of unratioed power.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Cal power level in dBm. No limits are enforced on this value, but the VNA receivers themselves have maximum and minimum power specifications (that may differ between VNA models) which this value must comply with for a valid receiver power cal.  
Examples | CALC:CORR:OFFS 10DBM  
calculate1:correction:offset:magnitude maximum  
Query Syntax | CALCulate<cnum>:CORRection:OFFSet[:MAGNitude]?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0dBm  
  
* * *

## CALCulate<cnum>:CORRection:OFFSet:PHASe <num>[<char>] Superseded

Applicable Models: All Note: This command is replaced with
[CALC:OFFS:PHASe](Correction.md#OffsPhase) (Read-Write) Sets the phase offset
for the selected measurement.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<num> | Offset phase value. Choose any number between:  
-360 and 360  
<char> | Units for phase. OPTIONAL. Choose either:  
DEG \- Degrees (default)  
RAD \- Radians  
Examples | CALC:CORR:OFFS:PHAS 10  
calculate:correction:offset:phase 20rad  
Query Syntax | CALCulate:CORRection:OFFSet:PHASe?  
Return Type | Numeric, returned value always in degrees  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 degrees  
  
* * *

* * *


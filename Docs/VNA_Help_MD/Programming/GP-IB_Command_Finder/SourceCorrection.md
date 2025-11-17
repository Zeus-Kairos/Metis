# Source:Power:Correction Commands

* * *

Used to perform source power calibration on internal and external sources.

Note: Only ONE Source Power Cal can be performed at a time.

SOURce:POWer:CORRection COLLect | [ABORt](SourceCorrection.md#abort) | [ACQuire](SourceCorrection.md#aquire) | AVERage | [[COUNt]](SourceCorrection.md#average) | [NTOLerance](SourceCorrection.md#averTol) | DISPlay | [[STATe]](SourceCorrection.md#display) | FCHeck] | [[STATe]](SourceCorrection.md#fcheck) | ITERation | [[COUNt]](SourceCorrection.md#IterCount) | [NTOLerance](SourceCorrection.md#iterTol) | [METHod](SourceCorrection.md#method) | [SAVE](SourceCorrection.md#save) | {A|B}SENSor | [[FRANge]](SourceCorrection.md#frange) | [RCFactor](SourceCorrection.md#Rfactor) | [SELect](SourceCorrection.md#SensorSelect) | TABLe | [DATA](SourceCorrection.md#tdata) | [FREQuency](SourceCorrection.md#RWfreq) | LOSS | [[STATe]](SourceCorrection.md#tloss) | [POINts?](SourceCorrection.md#points) | [[SELect]](SourceCorrection.md#tselect) | WARN [DATA](SourceCorrection.md#corrdata) | [PRIor](SourceCorrection.md#dataPrior) [LEVel [AMPlitude]](SourceCorrection.md#level) OFFSet | [[MAGNitude]](SourceCorrection.md#offset) [[STATe]](SourceCorrection.md#state)  
---  
  
Click on a keyword to view the command details.

Blue commands are superseded.

See Also

  * [Example program](../GPIB_Example_Programs/SCPI_Example_Programs.md) using these commands.

  * [Template](../GPIB_Example_Programs/CustomPowerMeterDriver.md) for creating your own Power Meter Driver

  * [Learn about Source Power Cal](../../S3_Cals/PwrCalibration.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

Note: The
[SOURce:POWer:CORRection:COLLect:ACQuire](SourceCorrection.md#aquire)
command, used to step the VNA and read a power meter, cannot be sent over the
GPIB unless the power meter is connected to a different GPIB interface. See
the alternative methods described in the command details.

* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:ABORt

Applicable Models: All excepts M937xA, P937xA (Write-only) Aborts a source
power calibration sweep that is in progress. To use this ABORt command, you
MUST use the ASYNchronous argument with
[SOUR:POW:CORR:COLL:ACQ](SourceCorrection.md#aquire) After aborting, this
message appears in the error log: +243,"Requested operation was canceled".  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  Port number to correct for source power. If unspecified, value is set to 1.  
Examples |  SOUR:POW:CORR:COLL:ABOR  
source1:power2:correction:collect:abort  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect[:ACQuire]
<char>,<id>[,src][,sync]

Applicable Models: All excepts M937xA, P937xA (Write-only) Initiates a source
power cal acquisition sweep using the power sensor attached to the specified
channel (A or B) on the power meter, using a USB power sensor, or using the
specified VNA receiver.  For source power cal, the power meter can NOT be
controlled by the VNA using the GPIB Talker/Listener interface. Instead use
one of the following methods:

  * If present, use the [GPIB dedicated controller port](../../Rear_Panel/XRtour.md#GPIB).
  * Connect the power meter to the VNA using a USB / GPIB interface (Keysight 82357A).
  * SCPI programming of the VNA using a LAN Client interface ([see example](../GPIB_Example_Programs/Perform_a_Source_Cal_using_SCPI.md)).
  * Send SCPI commands through the COM interface using the [SCPI String Parser](../COM_Reference/Objects/SCPIStringParser_Object.md) object.
  * Directly control the Power Meter and VNA to step frequency; then acquire and store the Power reading. ([see example](../GPIB_Example_Programs/Perform_a_Source_Cal_using_SCPI.md)).
  * Configure the Power Meter/Sensor as a PMAR Device. [Learn how](../../System/Configure_an_External_Device.md). [See SCPI commands](SystConfigExternalDevice.md).

  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  Port number to correct for source power. If unspecified, value is set to 1.  
<char> |  Acquisition Choose from:

  * PMETer \- Power Meter is used for all readings.
  * PMReceiver \- Power meter for the first iteration; then use the reference receiver for remaining readings if necessary (same as "fast iteration" box checked on [dialog box](../../S3_Cals/PwrCalibration.md#SourceDiag))
  * RECeiver - Use VNA measurement receiver for all readings.

  
<id> |  String (Not case sensitive). The power sensor or VNA receiver to use for measuring power. For PMETer or PMRECeiver, choose from:

  * "ASENSOR" or "BSENSOR". For U series USB sensors, always specify "ASENSOR"

For RECeiver, choose from:

  * Any VNA receiver to acquire readings using physical or [logical receiver notation](../../S1_Settings/Measurement_Parameters.md#RecNotation).
  * Any configured PMAR device name. [Learn more about PMAR Devices](../../System/Configure_an_External_Device.md). [See PMAR commands](SystConfigExternalDevice.md).

  
[src] |  Optional argument. String. (NOT case sensitive). Source port. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports that are not simple numbers, such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
[sync] |  If this argument is specified, must also specify [src]. Choose from:

  * SYNChronous \- Blocks SCPI commands during standard measurement (default behavior).
  * ASYNchronous \- Does NOT block SCPI commands during standard measurement.

[Learn more about this
argument](../Learning_about_GPIB/Understanding_Command_Synchronization.htm#Synch)  
Examples |  SYST:COMM:PSEN gpib, "13" SOURce:POWer:CORRection:COLLect:FCHeck:STATe ON sour:pow:corr:coll:ASEN:FRANge 4e9, 26.5e9 sour:pow:corr:coll:BSEN:FRANge 0, 4.2e9 SOUR:POW3:CORR:COLL:ACQ PMR,"BSENSOR";*OPC? SOUR:POW3:CORR:COLL:ACQ PMR,"ASENSOR";*OPC? SOUR:POW3:CORR:COLL:SAVE RREC  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce:POWer<port>:CORRection:COLLect:AVERage[:COUNt] <num>

Applicable Models: All excepts M937xA, P937xA (Read-Write) This command, along
with [SOUR:POW:CORR:COLL:AVER:NTOLerance](SourceCorrection.md#averTol),
allows for settling of the power sensor READINGS.  Note: This command is
global and does not depend on a specific channel number. Sets the _maximum
number of acquisitions that will be used to acquire one**settled reading**
from the power meter._ _These settings affect every use of the power meter
(PMAR and source power cal)._ _T_ his setting and corresponding
SOUR:POW:CORR:COLL:AVER:NTOLerance command only effect the settled reading of
the currently selected legacy power meter. Note: To set the COUNT/NTOLerance
of a specific PMAR, use the
[SYST:CONF:EDEV:PMAR:READ:COUNT](SystConfigExtPMAR.md#pmarReadCount) and
[SYST:CONF:EDEV:PMAR:READ:NTOLerance](SystConfigExtPMAR.md#pmarReadNtol)
commands. _Users may want to adjust this number if they know the signal is
noisy as these settings set a threshold that determines when the power meter
reading is done._ Each reading is averaged with the previous readings. When
this average meets the [Average:NTOLerance](SourceCorrection.md#averTol)
value or this number of readings has been made, the average is returned as the
valid reading. [Learn more.](../../S3_Cals/PwrCalibration.md#MeterSettings)  
---  
Parameters |   
<port> |  If provided, this argument is ignored by the VNA.  
<num> |  Maximum number of readings to make to allow for settling. Choose any number between 3 and 1000.  
Examples |  // configure the power meter settling (up to 2 acquisitions to produce one settled meter reading) SOUR:POW:CORR:COLL:AVER 2  
SOUR:POW:CORR:COLL:AVER:NTOL .05 // configure the number of (settled) readings
to acquire at each frequency point. // 3 settled readings are averaged to
produce one bucket of data per frequency SOUR:POW:CORR:COLL:ITER 3  
SOUR:POW:CORR:COLL:ITER:NTOL .005  
Query Syntax |  SOURce:POWer:CORRection:COLLect:AVERage[:COUNt]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  3  
  
* * *

## SOURce:POWer<port>:CORRection:COLLect:AVERage:NTOLerance <num>

Applicable Models: All excepts M937xA, P937xA (Read-Write) This command, along
with [SOUR:POW:CORR:COLL:AVER:COUNT](SourceCorrection.md#average), allows for
settling of the power sensor READINGS.  Note: This command is global and does
not depend on a specific channel number. This setting and corresponding
SOUR:POW:CORR:COLL:AVER:COUNT command only effect the settled reading of the
currently selected legacy power meter. Note: To set the COUNT/NTOLerance of a
specific PMAR, use the
[SYST:CONF:EDEV:PMAR:READ:COUNT](SystConfigExtPMAR.md#pmarReadCount) and
[SYST:CONF:EDEV:PMAR:READ:NTOLerance](SystConfigExtPMAR.md#pmarReadNtol)
commands. Each power reading is averaged with the previous readings. When the
average meets this nominal tolerance value or the [max number of
readings](SourceCorrection.htm#average) has been made, the average is returned
as the valid reading. [Learn
more.](../../S3_Cals/PwrCalibration.htm#MeterSettings)  
---  
Parameters |   
<port> |  If provided, this argument is ignored by the VNA.  
<num> |  Power measurement settling tolerance value in dB. Choose any number between 0 and 5.  
Examples |  // configure the power meter settling (up to 2 acquisitions to produce one settled meter reading) SOUR:POW:CORR:COLL:AVER 2  
SOUR:POW:CORR:COLL:AVER:NTOL .05 // configure the number of (settled) readings
to acquire at each frequency point. // 3 settled readings are averaged to
produce one bucket of data per frequency SOUR:POW:CORR:COLL:ITER 3  
SOUR:POW:CORR:COLL:ITER:NTOL .005  
Query Syntax |  SOURce:POWer:CORRection:COLLect:AVERage:NTOLerance?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  .050 dBm  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:DISPlay[:STATe] <ON | OFF>

Applicable Models: All excepts M937xA, P937xA (Read-Write) Enables and
disables the display of power readings on the VNA screen. Send this command
BEFORE you begin a source power cal acquisition. After the source power cal
data is acquired, this setting is reset to ON.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  If provided, this argument is ignored by the VNA.  
<ON|OFF> |  ON (1) Source power calibration dialog box is shown on the VNA screen. Power readings are plotted against the Tolerance value as limit lines. OFF (0) \- Source power calibration dialog box is NOT shown on the VNA screen.  
Examples |  SOUR:POW:CORR:COLL:DISP ON  
source1:power2:correction:collect:display:state off  
Query Syntax |  SOURce:POWer:CORRection:COLLect:DISPlay[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON (1)  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:FCHeck[:STATe] <ON | OFF>

Applicable Models: All excepts M937xA, P937xA (Read-Write) Enables and
disables frequency checking of source power cal acquisition sweeps. ONLY use
when you have more than one power sensor.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  If provided, this argument is ignored by the VNA.  
<ON|OFF> |  ON (1) turns source power cal frequency checking ON. A requested acquisition will only succeed for those frequency points which fall within a frequency range specified for the power sensor being used. An acquisition will pause in mid-sweep if the frequency is about to exceed the maximum frequency limit specified for that sensor. When the sweep is paused in this manner, a sensor connected to the other channel input of the power meter can be connected to the measurement port in place of the previous sensor, and used to complete the sweep. However, the maximum frequency specified for the second sensor would need to be sufficient for the sweep to complete. Frequency limits are specified using the [SOUR:POW:CORR:COLL:SEN](SourceCorrection.md#frange) command. OFF (0) \- turns source power cal frequency checking OFF. An acquisition will use just one power sensor for the entire sweep, regardless of frequency.  
Examples |  SOUR:POW:CORR:COLL:FCH ON  
source1:power2:correction:collect:fcheck:state off  
Query Syntax |  SOURce:POWer:CORRection:COLLect:FCHeck[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:ITERation[:COUNt] <num>

Applicable Models: All excepts M937xA, P937xA (Read-Write) This command, along
with [SOUR:POW:CORR:COLL:ITER:NTOL](SourceCorrection.md#iterTol) control the
number of settled readings taken to produce a single power point during source
power cal.  The source power cal reads the power (performed by
[SOUR:POW:CORR:COLL:AVER:COUNT](SourceCorrection.md#average) and
[SOUR:POW:CORR:COLL:AVER:NTOLerance](SourceCorrection.md#averTol)) and makes
internal adjustments to set the power to a desired level. These settings
determine how many attempts (COUNt) the analyzer will make in an attempt to
get close enough (NTOLerance) to the target power level. [Learn
more.](../../S3_Cals/PwrCalibration.htm#MeterSettings)  
---  
Parameters |   
<ch> |  If provided, this argument is ignored by the VNA.  
<port> |  If provided, this argument is ignored by the VNA.  
<num> |  Maximum number of readings. Choose any number between 1 and 1000.  
Examples |  // configure the power meter settling (up to 2 acquisitions to produce one settled meter reading) SOUR:POW:CORR:COLL:AVER 2  
SOUR:POW:CORR:COLL:AVER:NTOL .05 // configure the number of (settled) readings
to acquire at each frequency point. // 3 settled readings are averaged to
produce one bucket of data per frequency SOUR:POW:CORR:COLL:ITER 3  
SOUR:POW:CORR:COLL:ITER:NTOL .005  
Query Syntax |  SOURce:POWer:CORRection:COLLect:ITERation[:COUNt]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:ITERation:NTOLerance <num>

Applicable Models: All excepts M937xA, P937xA (Read-Write) This command, along
with [SOUR:POW:CORR:COLL:ITER:COUNT](SourceCorrection.md#IterCount) describes
the number of adjustments to make to the source power.  Sets the maximum
desired deviation from the sum of the [test port power](source.md#pwrval) and
the [offset](SourceCorrection.md#offset) value. Power READINGS (performed by
[SOUR:POW:CORR:COLL:AVER:COUNT](SourceCorrection.md#average) and
[SOUR:POW:CORR:COLL:AVER:NTOLerance](SourceCorrection.md#averTol)) will
continue to be made, and source power adjusted, until a measurement is within
this tolerance value or the max number of measurements has been met. The last
value is the valid measurement for that data point. [Learn
more.](../../S3_Cals/PwrCalibration.htm#MeterSettings)  
---  
Parameters |   
<ch> |  If provided, this argument is ignored by the VNA.  
<port> |  If provided, this argument is ignored by the VNA.  
<num> |  Tolerance value in dBm. Choose any number between 0 and 5  
Examples |  // configure the power meter settling (up to 2 acquisitions to produce one settled meter reading) SOUR:POW:CORR:COLL:AVER 2  
SOUR:POW:CORR:COLL:AVER:NTOL .05 // configure the number of (settled) readings
to acquire at each frequency point. // 3 settled readings are averaged to
produce one bucket of data per frequency SOUR:POW:CORR:COLL:ITER 3  
SOUR:POW:CORR:COLL:ITER:NTOL .005  
Query Syntax |  SOURce:POWer:CORRection:COLLect:ITERation:NTOLerance?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  .05  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:METHod <char> Superseded

Applicable Models: N522xB, N523xB, N524xB This command is replaced with
[SOUR:POW:CORR:COLLect[:ACQuire]](SourceCorrection.md#aquire) which now
specifies the method and the device. The only parameter required by that
command was either ASENsor or BSENsor which are still supported but not
documented. (Read-Write) Selects the calibration method to be used for the
source power cal acquisition.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  Port number to correct for source power. If unspecified, value is set to 1.  
<char> |  Choose from: NONE \- No Cal method PMETer \- Power Meter is used for all readings. (same as "fast iteration" box not checked on [dialog box](../../S3_Cals/PwrCalibration.md#SourceDiag)) PMReceiver \- Power meter for the first iteration; then use the reference receiver for remaining readings if necessary (same as "fast iteration" box checked on [dialog box](../../S3_Cals/PwrCalibration.md#SourceDiag))  
Examples |  SOUR:POW:CORR:COLL:METH PMET  
source1:power2:correction:collect:method pmreceiver  
Query Syntax |  SOURce:POWer:CORRection:COLLect:METHod?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SOURce<ch>:POWer<port:CORRection:COLLect:SAVE [<RREC>]

Applicable Models: All excepts M937xA, P937xA (Write-only) Applies the array
of correction values after a source power calibration sweep has completed. The
source power correction will then be active on the specified source port for
channel <ch>. This command does NOT save the correction values. To save
correction values, [save an instrument / calibration state](Memory.md#save)
(*.cst file) after performing a source power cal.  
---  
Parameters |   
<ch> |  If provided, this argument is ignored by the VNA.  
<port> |  If provided, this argument is ignored by the VNA.  
<RREC> |  Optional argument. RRECeiver In addition to a source Power Cal, perform a calibration of the reference receiver used in the measurement. ONLY the Reference Receiver calibration is then saved to a Cal Set or Cal Register as specified by the current setting of [SENS:CORR:PREF:CSET:SAVE](Sense/Sense_Correction.md#CsetSave). This argument only applies to standard S-parameter channels.  
Examples |  SOUR:POW:CORR:COLL:SAVE  
source:power:correction:collect:save rreceiver  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:<pmChan>SENsor[:FRANge]
<num1>,<num2>

Applicable Models: All excepts M937xA, P937xA (Read-Write) Specifies the
frequency range over which the power sensors connected to the specified
channels (A and B) of the power meter can be used (minimum frequency, maximum
frequency). If the power meter has only a single channel, that channel is
considered channel A.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  If provided, this argument is ignored by the VNA. (It is required for query).  
<pmChan> |  Power Meter channel. Choose from: A \- Channel A B - Channel B  
<num1> |  Minimum frequency for the sensor. If a frequency unit is not specified, Hz is assumed.  
<num2> |  Maximum frequency for the sensor. If a frequency unit is not specified, Hz is assumed.  
Examples |  SOUR:POW:CORR:COLL:ASEN 100E3, 3E9  
source1:power:correction:collect:bsensor:frange 10 MHz, 18 GHz  
Query Syntax |  SOURce<ch>:POWer<port>:CORRection:COLLect:ASENsor[:FRANge]? SOURce<ch>:POWer<port>:CORRection:COLLect:BSENsor[:FRANge]?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0,0  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:<pmChan>SENsor:RCFactor <num>

Applicable Models: All excepts M937xA, P937xA (Read-Write) ) Specifies the
reference cal factor for the power sensor connected to channel A or B of the
power meter. If the power meter has only a single channel, that channel is
considered channel A.  Note: If the sensor connected to the specified channel
of the power meter contains cal factors in EPROM (such as the Keysight
E-series power sensors), those will be the cal factors used during the
calibration sweep. The reference cal factor value associated with this
command, and any cal factors entered into the VNA for that sensor channel,
will not be used.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  If provided, this argument is ignored by the VNA.  
<pmChan> |  Power Meter channel. Choose from: A \- Channel A B - Channel B  
<num> |  Reference cal factor in percent. Choose any number between 1 and 150.  
Examples |  SOUR:POW:CORR:COLL:ASEN:RCF 98.7  
source1:power2:correction:collect:bsensor:rcfactor 105  
Query Syntax |  SOURce:POWer:CORRection:COLLect:ASENsor:RCFactor? SOURce:POWer:CORRection:COLLect:BSENsor:RCFactor?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  100  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:<pmChan>SENsor:SELect

Applicable Models: All excepts M937xA, P937xA (Read-Write) Sets and returns
the power sensor channel (A or B) to be used. This performs the same function
as the Use this sensor only checkbox in the [Power Sensor Settings
dialog](../../S3_Cals/PwrCalibration.htm#SensorDiag).  Notes:

  * This command is NOT necessary when performing a [Guided Power Cal using Multiple Sensors.](../../S3_Cals/Guided_Power_Calibration.md#MultipleSensors)
  * This command can be used with [Application channels](../../Applications/Applications.md).

  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  If provided, this argument is ignored by the VNA.  
<pmChan> |  Power Meter channel. Choose from: A \- Channel A B - Channel B  
Examples |  SOUR:POW:CORR:COLL:<pmChan>SEN:SEL 'Write source1:power2:correction:collect:bsensor:select? 1e9 'Read  
Query Syntax |  SOURce:POWer:CORRection:COLLect:ASENsor:SELect? <Frequency> SOURce:POWer:CORRection:COLLect:BSENsor:SELect? <Frequency> Returns a boolean 1 or 0 (ON or OFF) indicating whether the sensor is to be used at the specified frequency. If [frequency checking](SourceCorrection.md#fcheck) is OFF, then the <Frequency> parameter is ignored. The query returns if the sensor is selected for ALL frequencies.  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:TABLe:DATA <data>

Applicable Models: All excepts M937xA, P937xA (Read-Write) Read or write data
into the selected table. Use
[SOUR:POW:CORR:COLL:TABL:SELect](SourceCorrection.md#tselect) to select a
table.

  * When the power sensor table is selected, the data is interpreted as cal factors in percent.
  * When the loss table is selected, POSITIVE values in dB are interpreted as LOSS. To compensate for gain, use negative values. 
  * Each table can contain up to 9999 segments. Values can be loaded using the Characterize Adapter macro.
  * Learn more about [Power Loss Compensation](../../S3_Cals/PwrCalibration.md#LossCompDiag).

  
---  
Parameters |   
<ch> |  If provided, this argument is ignored by the VNA.  
<port> |  If provided, this argument is ignored by the VNA.  
<data> |  Data to write into the selected table.  
Examples |  SOURce:POWer:CORRection:COLLect:TABLe:DATA 0.12, 0.34, 0.56  
Query Syntax |  SOURce<ch>:POWer:CORRection:COLLect:TABLe:DATA? If the selected table is currently empty, no data is returned.  
Return Type |  Numeric - one number per table segment.  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:TABLe:FREQuency <data>

Applicable Models: All excepts M937xA, P937xA (Read-Write) Read or write
frequency values for the selected table (cal factor table for a power sensor,
or the loss compensation table). Use
[SOUR:POW:CORR:COLL:TABL:SELect](SourceCorrection.md#tselect) to select a
table.  
---  
Parameters |   
<ch> |  If provided, this argument is ignored by the VNA.  
<port> |  If provided, this argument is ignored by the VNA.  
<data> |  Frequency data to write into the selected table.  
Examples |  SOURce:POWer:CORRection:COLLect:TABLe:FREQuency 10E6, 1.5E9, 9E9  
Query Syntax |  SOURce<ch>:POWer:CORRection:COLLect:TABLe:FREQuency? If the selected table is currently empty, no data is returned.  
Return Type |  Numeric - one number per table segment  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:TABLe:LOSS[:STATe] <ON | OFF>

Applicable Models: All excepts M937xA, P937xA (Read-Write) Indicates whether
or not to adjust the power readings using the values in the loss table during
a source power cal sweep. Learn more about [Power Loss
Compensation](../../S3_Cals/PwrCalibration.htm#LossCompDiag).  
---  
Parameters |   
<ch> |  If provided, this argument is ignored by the VNA.  
<port> |  If provided, this argument is ignored by the VNA.  
<ON|OFF> |  ON (or 1) - turns use of the loss table ON. OFF (or 0) \- turns use of the loss table OFF.  
Examples |  SOUR:POW:CORR:COLL:TABL:LOSS ON  
source1:power2:correction:collect:table:loss:state off  
Query Syntax |  SOURce:POWer:CORRection:COLLect:TABLe:LOSS[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:TABLe:POINts?

Applicable Models: All excepts M937xA, P937xA (Read-only) Returns the number
of segments that are currently in the selected table.  
---  
Parameters |   
<ch> |  If provided, this argument is ignored by the VNA.  
<port> |  If provided, this argument is ignored by the VNA.  
Examples |  SOUR:POW:CORR:COLL:TABL:POIN?  
source1:power2:correction:collect:table:points?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:TABLe[:SELect] <char>

Applicable Models: All excepts M937xA, P937xA (Read-Write) Selects which table
you want to write to or read from. Read or write using
[SOURce:POWer:CORRection:COLLect:TABLe:FREQuency](SourceCorrection.md#RWfreq)
and [SOURce:POWer:CORRection:COLLect:TABLe:DATA](SourceCorrection.md#tdata)  
---  
Parameters |   
<ch> |  If provided, this argument is ignored by the VNA.  
<port> |  If provided, this argument is ignored by the VNA.  
<char> |  Choose from:  NONE \- No table selected ASENsor \- Cal Factor table for Power Sensor A BSENsor \- Cal Factor table for Power Sensor B LOSS \- Loss compensation table  
Examples |  SOUR:POW:CORR:COLL:TABL ASEN  
source1:power2:correction:collect:table:select bsensor  
Query Syntax |  SOURce:POWer:CORRection:COLLect:TABLe[:SELect]?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:COLLect:WARN <bool>

Applicable Models: All excepts M937xA, P937xA (Read-Write) Enables/disables
the use of error messages during a source calibration if the calibration fails
to achieve the desired power level at the power sensor.  This property affects
error reporting during the acquisition of a source power calibration. When the
power calibration sweep occurs, the tolerance set by 
SOUR:POW:CORR:COLL:ITER:NTOL  is indicated by a set of limit lines. When
those limits fail and SOUR:POW:CORR:COLL:WARN is set to OFF, the failure is
not reported. This is the default. When those limits fail and
SOUR:POW:CORR:COLL:WARN is set to ON, the failure is reported to the SCPI
error queue.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  If provided, this argument is ignored by the VNA.  
<bool> |  ON (or 1) - enables SCPI error on source power calibration failure. OFF (or 0) \- disables SCPI error on source power calibration failure.  
Examples |  SOUR:POW:CORR:COLL:WARN ON  
source1:power2:correction:collect:warn off  
Query Syntax |  SOURce:POWer:CORRection:COLLect:WARN?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:DATA <data>[,src]

Applicable Models: All (Read-Write) Writes and reads source power calibration
data. The effect from this command on the channel is immediate. Do NOT send
SOUR:POW:CORR:COLL:SAVE after this command as it may invalidate the uploaded
data. When querying source power calibration data, if no source power cal data
exists for the specified channel and source port, then no data is returned. If
a change in the instrument state causes interpolation and/or extrapolation of
the source power cal, the correction data associated with this command
correspond to the new instrument state (interpolated and/or extrapolated
data). If the channel is sweeping the source backwards, then the first data
point is the highest frequency value; the last data point is the lowest. Use
the [SENS:X:VALues?](Sense/X-Axis.md) command to return the X-axis values in
the displayed order.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  Port number to correct for source power. If unspecified, value is set to 1.  
<data> |  Correction Data  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports that are not simple numbers, such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOURce1:POWer2:CORRection:DATA 0.12, -0.34, 0.56  
Query Syntax |  SOURce<ch>:POWer<port>:CORRection:DATA? [src]  
Return Type |  Depends on [FORMat:DATA](Format_SCPI.md#fd) command  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:DATA:PRIor <data>[,src]

Applicable Models: All excepts M937xA, P937xA (Read-Write) Writes and reads
power correction values from the previous iteration of the source power cal.
Data for which the first power meter reading were within the tolerance limit,
the prior correction value is 0. In all other respects, this command is the
same as [SOUR:POW:CORR:DATA](SourceCorrection.md#corrdata). This command can
be used to determine the final power reading at each point of the power cal,
for a cal that did not pass tolerance limits. The formula for determining the
power reading (in dB): Power reading = Target power at the source port +
specified power cal offset value + prior iteration corr value actual power
corr value. The "actual" value in this equation is returned with
[SOUR:POW:CORR:DATA?](SourceCorrection.md#corrdata)  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  Port number to correct for source power. If unspecified, value is set to 1.  
<data> |  Correction Data  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports that are not simple numbers, such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOURce1:POWer2:CORRection:DATA:PRIor 0.12, -0.34, 0.56  
Query Syntax |  SOURce<ch>:POWer<port>:CORRection:DATA:PRIor? [src]  
Return Type |  Depends on [FORMat:DATA](Format_SCPI.md#fd) command  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:LEVel[:AMPLitude] <num>[,src]

Applicable ModelsAll excepts M937xA, P937xA (Read-Write) Specifies the power
level that is expected at the desired reference plane (DUT input or output).
This is not used for [segment sweep with independent power
levels](../../S1_Settings/Sweep.htm#segment) or [power
sweeps](../../S1_Settings/Sweep.htm#power).  Note: Although this command still
works, it is recommended that you specify cal power by setting the [test port
power](source.htm#pwrval) and [offset](SourceCorrection.md#offset) value.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  Port number to correct for source power. If unspecified, value is set to 1.  
<num> |  Cal power level in dBm. Because this could potentially be at the output of a device-under-test, no limits are placed on this value here. It is realistically limited by the specifications of the device (power sensor) that will be used for measuring the power. The power delivered to the VNA receiver must never exceed VNA specifications for the receiver!  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports that are not simple numbers, such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW:CORR:LEV 10  
source1:power2:correction:level:amplitude 0 dbm  
Query Syntax |  SOURce:POWer:CORRection:LEVel[:AMPLitude]? [src]  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 dBm  
  
* * *

## SOURce<ch>:POWer<port>:CORRection:OFFSet[:MAGNitude] <num>[,src]

Applicable Models: All excepts M937xA, P937xA (Read-Write) Sets or returns a
power level offset from the VNA test port power. This can be a gain or loss
value (in dB) to account for components you connect between the source and the
reference plane of your measurement. For example, specify 10 dB to account for
a 10 dB amplifier at the input of your DUT.  Cal power is the sum of the test
port power setting and this offset value. Following the calibration, the VNA
power readouts are adjusted to the cal power.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  Port number to correct for source power. If unspecified, value is set to 1.  
<num> |  Gain or loss value in dB. Choose a value between -200 and 200  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports that are not simple numbers, such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW:CORR:OFFS 10  
source1:power2:correction:offset:magnitude -3  
Query Syntax |  SOURce:POWer:CORRection:OFFSet[:MAGNitude]? [src]  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 dB  
  
* * *

## SOURce<ch>:POWer<port>:CORRection[:STATe] <bool>[,src]

Applicable Models: All excepts M937xA, P937xA (Read-Write) Enables and
disables source power correction for the specified port on the specified
channel.  
---  
Parameters |   
<ch> |  Channel number of the source power cal. If unspecified, value is set to 1  
<port> |  Port number to correct for source power. If unspecified, value is set to 1.  
<bool> |  ON (or 1) turns source power correction ON. OFF (or 0) - turns source power correction OFF.  
[src] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports that are not simple numbers, such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples |  SOUR:POW:CORR ON  
source1:power2:correction:state off, "MXG N5183A"  
Query Syntax |  SOURce:POWer:CORRection[:STATe]? "MXG N5183A"  
Return Type |  Boolean (1 = ON, 0 = OFF)  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF (0)  
  
* * *


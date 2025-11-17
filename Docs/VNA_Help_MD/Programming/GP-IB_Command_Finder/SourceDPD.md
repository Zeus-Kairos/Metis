# SourceDPD

These commands are used to set up and create a DPD (Digital Predistortion)
waveform.

SOURce: DPD | CORRection | COLLection | ACQuire | STATus? | DISTortion | ENABle | ITERations | SPAN | TOLerance | TYPE | DUT | ACP | ENABle | GBANd | ITERations | SPAN | TOLerance | EVM | ITERations | SPAN | TOLerance | LO | FTHRu | ENABle | ITERations | TOLerance | POWer | ENABle | [:FIXed] | ITERations | RECeiver | SPAN | TOLerance | DAC | SCALing | FILE | LOAD | IDEal | MODel | SAVE | MEASure | LINGain | ENABle | POWer:BACKoff | MODel | APPLy | CALibrate | CREate | DYNGain | INTerpolate | TYPE | MEMory | FUTure | OPERator:M [1-4]:ENABLe | PAST | STEP | OPTimize | ENABle | COMPact:AUTO | COMPact:LEVel | NMSE:GOAL | NMSE:INCLude | MEMory:OPERator:INCLude | POWer | SEGMent | COUNT | POINt::COUNt:MINimum | MEMPoly | CROSsterm | FUTure | PAST | ORDer | STATus? | TYPE | USE | DIRect | PAPR | EXPansion:MAXimum | PROCedure  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

  * [Remotely Specifying a Source Port](../Remotely_Specifying_a_Source_Port.md)

* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:ACQuire <enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Write-only) Sets the
collection acquire.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: SYNChronous ASYNchronous  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:CORR:COLL:ACQ SYNC  
Query Syntax |  Not applicable  
Default |  SYNChronous  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:ACQuire:STATus? [,srcPort]

Applicable Models:All with Option S93070xB/9x070A/B (Read-only) Returns a
message indicating if the calibration was successful or not.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD:CORR:COLL:ACQ:STAT? "Calibration succeeded."  
Return Type |  Comma-separated list of strings.  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Enable or
disable the distortion calibration state. The distortion calibration minimizes
the vector error of the modulation signal over the Cal Span.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable distortion calibration. **1 - ON** \- Enable distortion calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:DPD1:CORR:COLL:DIST:ENAB 1 source2:dpd:correction:collection:distortion:enable on  
**Query Syntax** |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:ENABle?  
**Return Type** |  Boolean  
**Default** |  ON  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the maximum number of distortion correction iterations used by the
calibration routine. The calibration routine uses successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of distortion correction iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DIST:ITER 3  
source2:dpd:correction:collection:distortion:iterations 3  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:ITERations?  
Return Type |  Numeric  
Default |  3  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:SPAN
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the calibration span for a distortion calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DIST:SPAN 1.5GHz  
source2:dpd:correction:collection:distortion:span 1.5ghz  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:SPAN?  
Return Type |  Numeric  
Default |  DUT default span (EVM plus ACP)  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:TOLerance
<num>[,srcPort]

Applicable Models:All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the desired distortion calibration tolerance.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Desired tolerance is the un-equalized EVM in dBc.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DIST:TOL -50 dBc  
source2:dpd:correction:collection:distortion:tolerance -50 dBc  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:TOLerance?  
Return Type |  Numeric  
Default |  -40  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:TYPE
<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the linear or nonlinear distortion correction of the source at the DUT
input.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: LINear TOTal  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:CORR:COLL:DIST:TYPE TOT  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DISTortion:TYPE?  
Return Type |  Enumeration  
Default |  TOTal  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Set and read
the ACP modulation calibration state.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable ACP calibration. **1 - ON** \- Enable ACP calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:DPD1:CORR:COLL:DUT:ACP:ENAB 1 source2:dpd:correction:collection:dut:acp:enable on  
**Query Syntax** |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:ENABle?  
**Return Type** |  Boolean  
**Default** |  ON  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:GBANd <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the frequency delta from the edge of the carrier to the beginning of the
ACP Span.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Guard band for ACP.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DUT:ACP:GBAN 0 Hz  
source2:dpd:correction:collection:dut:acp:gband 0 Hz  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:GBANd?  
Return Type |  Numeric  
**Default** |  0 Hz  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the maximum number of iterations used by the calibration routine. The
calibration routine uses successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DUT:ACP:ITER 2  
source2:dpd:correction:collection:dut:acp:iterations 2  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:ITERations?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  2  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:SPAN <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the calibration span for the ACP calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DUT:ACP:SPAN 100 MHz  
source2:dpd:correction:collection:dut:acp:span 100 MHz  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:SPAN?  
Return Type |  Numeric  
**Default** |  2 X Default EVM Span (If source does not have enough bandwidth to span all ACP frequencies, the default ACP span is set to Max Source Span - Default EVM Span / 2.)  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the desired ACP calibration tolerance for the ACP modulation
calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration tolerance in dBc.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DUT:ACP:TOL -40dBc  
source2:dpd:correction:collection:dut:acp:tolerance -40dBc  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:ACP:TOLerance?  
Return Type |  Numeric  
**Default** |  -40  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:EVM:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the maximum number of iterations used by the calibration routine. The
calibration routine uses successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DUT:EVM:ITER 2  
source2:dpd:correction:collection:dut:evm:iterations 2  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:EVM:ITERations?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  3  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:EVM:SPAN <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the calibration span of the EVM calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DUT:EVM:SPAN 100 MHz  
source2:dpd:correction:collection:dut:evm:span 100 MHz  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:EVM:SPAN?  
Return Type |  Numeric  
**Default** |  Signal Span  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:EVM:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the desired EVM calibration tolerance for the modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration tolerance in dBc.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:DUT:EVM:TOL -40dBc  
source2:dpd:correction:collection:dut:evm:tolerance -40dBc  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:DUT:EVM:TOLerance?  
Return Type |  Numeric  
**Default** |  -40  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:LO:FTHRu:ENABle
<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Enable or
disable the LO feedthru calibration state.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable LO feedthru calibration. **1 - ON** \- Enable LO feedthru calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:DPD1:CORR:COLL:LO:FTHR:ENAB 1 source2:dpd:correction:collection:lo:fthru:enable on  
**Query Syntax** |  SOURce<cnum>:DPD<port>:CORRection:COLLection:LO:FTHRu:ENABle?  
**Return Type** |  Boolean  
**Default** |  OFF  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:LO:FTHRu:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the maximum number of iterations used by the calibration routine. The
calibration routine uses successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:LO:FTHR:ITER 3  
source2:dpd:correction:collection:lo:fthru:iterations 3  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:LO:FTHRu:ITERations?  
Return Type |  Numeric  
Default |  6  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:LO:FTHRu:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the desired LO feedthru modulation calibration tolerance.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration LO feedthru tolerance in dBc  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:LO:FTHR:TOL -40.00  
source2:dpd:correction:collection:lo:fthru:tolerance -40.00  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:LO:FTHRu:TOLerance?  
Return Type |  Numeric  
Default |  -40.00 dBc  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:ENABle <bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Set and read
the power modulation calibration state.  
---  
**Parameters** |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable Power calibration. **1 - ON** \- Enable Power calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
**Examples** |  SOUR:DPD1:CORR:COLL:POW:ENAB 1 source2:dpd:correction:collection:power:enable on  
**Query Syntax** |  SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:ENABle?  
**Return Type** |  Boolean  
**Default** |  ON  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer[:FIXed] <num>[,srcPort]
OBSOLETE

Note: This command is no longer needed because the power is set using
[SENSe:DISTortion:SWEep:POWer:CARRier:LEVel](Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel).
Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads a fixed power level to use for the source modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Fixed power level to perform calibration.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:POW:FIX 0  
source2:dpd:correction:collection:power:fixed 0  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer[:FIXed]?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:ITERations
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the maximum number of iterations used by the calibration routine. The
calibration routine uses successive approximation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum number of iterations.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:POW:ITER 3  
source2:dpd:correction:collection:power:iterations 3  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:ITERations?  
Return Type |  Numeric  
Default |  3  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:RECeiver
<rcvr>[,srcPort] OBSOLETE

Note: This command is no longer needed because it is controlled using
[SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT](Sense/Distortion_Measurement.md#SENSe:DISTortion:SWEep:POWer:CARRier:LEVel:PORT).
Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the receiver for a power modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<rcvr> |  String. Calibration plane. For options S93070xB, choose from: DUTIn1, DUTOut2, DUTOut3, DUTOut4, DUTOut5.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:POW:REC "R1"  
source2:dpd:correction:collection:power:receiver "R1"  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:RECeiver?  
Return Type |  String  
Default |  DUTIn1 (options S93070xB)  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:SPAN <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the calibration span for a power modulation calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration span.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:POW:SPAN 1.5GHz  
source2:dpd:correction:collection:power:span 1.5ghz  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:SPAN?  
Return Type |  Numeric  
Default |  Signal Span  
  
* * *

## SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:TOLerance
<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the desired power calibration tolerance for the power modulation
calibration.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Calibration tolerance in dB.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:CORR:COLL:POW:TOL 0.100 dB  
source2:dpd:correction:collection:power:tolerance 0.100 dB  
Query Syntax |  SOURce<cnum>:DPD<port>:CORRection:COLLection:POWer:TOLerance?  
Return Type |  Numeric  
Default |  0.1  
  
* * *

## SOURce<cnum>:DPD<Port>:DAC:SCALing<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write)Sets and
reads the scaling factor used for the waveform.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<num> |  DAC scaling in %  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:DAC:SCAL 70  
Query Syntax |  SOURce<cnum>:DPD<port>:DAC:SCALing?  
Return Type |  Numeric  
Default |  70  
  
## SOURce<cnum>:DPD<port>:FILE:LOAD:IDEal <fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Specifies
the file path to recall an ideal modulation waveform file. The default file is
the modulation file currently selected in the Modulate tab of the Modulation
Distortion Setup dialog.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<fileName> |  String. Ideal waveform file name.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:FILE:LOAD:IDE "C:/dpd/MyIdealFile.csv"  
Query Syntax |  SOURce<cnum>:DPD<port>:FILE:LOAD:IDEal?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:DPD<port>:FILE:LOAD:MODel <fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Specifies a
DPD Model from a pre-existing file (*.mdpd).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<fileName> |  String. Model file name.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:FILE:LOAD:MOD "C:/dpd/16QAM_MemPoly.mdpd"  
Query Syntax |  SOURce<cnum>:DPD<port>:FILE:LOAD:MODel?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:DPD<port>:FILE:SAVE <fileName>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Specifies
the file path and file name to save the DPD Model as a *.mdpd file type
(zipped file). If the file exists, it is overwritten. The DPD Model contains
the following files:

  * MyDPD_IdealDPD.csv
  * MyDPD_CorrDPD.csv
  * DPDModel.csv
  * dpd.manifest

  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<fileName> |  String. DPD Model file name.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:FILE:SAVE "C:/dpd/MyModFile.mdpd"  
Query Syntax |  SOURce<cnum>:DPD<port>:FILE:SAVE?  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:DPD<Port>:MEASure:LINGain:ENABle<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Enable or
disable the DUT Linear Gain measurement during the DPD Direct. If ON, the DUT
Linear Gain will be measured and saved during the Direct DPD.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable the DUT Linear Gain **1 - ON** \- Enable the DUT Linear Gain.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MEAS:LING:MEM:ENAB 1 source:DPD1:measure:lingain:enable on  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DYNGain:MEMory:OPERator:M<num>:ENABle?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:DPD<Port>:MEASure:LINGain:POWer:BACKoff<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the backoff power level used during the linear gain S21 measurement for
the DPD Dynamic Gain model.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<num> |  Backoff power in the dB.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:DYNG:POW:BACK 10  
Query Syntax |  SOURce<cnum>:DPD<port>:MEASurel:LINGain:POWer:BACKoff?  
Return Type |  Numeric  
Default |  10 dB  
  
## SOURce<cnum>:DPD<port>:MODel:APPLy [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Write-only) Creates the
Modeled DPD Waveform from a user-supplied Ideal Waveform file and a DPD Model
file. The DPD Model will be applied to the Ideal Waveform to create the
Modeled DPD Waveform. If any calibration type is enabled, this command applies
the DPD model first then performs a calibration. If all calibration types are
disabled, then this command will only apply the DPD model.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:APPL  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:CALibrate [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Write-only) Calibrate
the DPD model from the setting define using the model commands. If requested,
will calibrate upper and lower ACP bands at the DUT output, source power level
at DUT input, source LO Feedthru, and linear and nonlinear distortion of the
source at the DUT input.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:CAL  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:CREate [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Write-only) Creates the
DPD Model from the settings defined using the model commands. The created
waveforms include "MyDPD_IdealDPD" and "MyDPD_CorrDPD".  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:CRE  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:DNYGain:INTerpolate:TYPE <enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the interpolation type used in the AM/AM and AM/PM segments for the
Dynamic Gain model.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: LINear \- Selects the Linear interpolation.  CUBic - Selects the Cubic interpolation. SPLine \- Selects the Spline interpolation.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:DNYG:INT:TYPE LIN  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DNYGain:INTerpolate:TYPE?  
Return Type |  Enumeration  
Default |  SPLine  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:DYNGain:MEMory:FUTure <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the number of input future time samples to use for calculating the
current output sample.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of future time samples.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:MEM:FUT 1  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DNYGain:MEMory:FUTure?  
Return Type |  Numeric  
Default |  1  
  
* * *

##
SOURce<cnum>:DPD<Port>:MODel:DYNGain:MEMory:OPERator:M<num>:ENABle<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the number of memory operators used for characterizing the device in the
Dynamic Gain model.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of memory operators. Choose from 1 to 4  
<bool> |  Choose from: **0 - OFF** -Disable Memory Operator. **1 - ON** \- Enable Memory Operator.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:MEM:OPER:M1:ENAB 1 source:DPD1:model:dyngain:memory:operator:m1:enable on  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DYNGain:MEMory:OPERator:M<num>:ENABle?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:DPD<Port>:MODel:DYNGain:MEMory:PAST<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the number of input past time samples to use for calculating the current
output sample in the Dynamic Gain model.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of past time samples.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:MEM:PAST -3  
source2:dpd:model:mempoly:memory:past -3  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DYNGain:MEMory:PAST?  
Return Type |  Numeric  
Default |  -3  
  
* * *

## SOURce<cnum>:DPD<Port>:MODel:DYNGain:MEMory:STEP<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the number of Memory Stepsize. A Memory Stepsize of 2 means every other
sample will be used. If (Future Memory - Past Memory)/(Memory Stepsize) is not
an integer, then (Future Memory) will be increased to make it an integer.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of Memory Stepsize.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:MEM:STEP 1  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DYNGain:MEMory:STEP?  
Return Type |  Numeric  
Default |  3  
  
* * *

## SOURce<cnum>:DPD<Port>:MODel:DYNGain:OPTimize:ENABle<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Enable or
disable the DPD model optimization.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable the optimization. **1 - ON** \- Enable the optimization.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:OPT:ENAB 1 source:DPD1:model:dyngain:optimize:enable on  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DYNGain:OPTimize:ENABle?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:DPD :MODel:DYNGain:OPTimize:COMPact:AUTO [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Enable or
disable automatic waveform compaction.  Auto is on by default. Selecting Auto
grays out the compacting value and compacts the signal to 3000 tones.
Compacting the waveform enables faster optimization.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable automatic waveform compaction. **1 - ON** \- Enable automatic waveform compaction.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:OPT:COMPact:AUTO 0  
Query Syntax |  SOURce<cnum>:DPD :MODel:DYNGain:OPTimize:COMPact:AUTO?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:DPD :MODel:DYNGain:OPTimize:COMPact:LEVel <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets the
waveform compaction level. Compacting the waveform enables faster
optimization.  Compact by 1 is equivalent to no compacting. This is not
recommended because it may result in over-fitting the equations, so the model
will fit the current waveform but will poorly fit other waveforms. The
waveform will not be compacted to have less than 3000 tones. If the user
chooses a sufficiently large compaction value then the number of tones will be
3000 but the compaction value shown in the entry box will not be changed. In
this way, the user may set compaction to a big value (1e6) and be assured that
the waveform will have 3000 tones.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Value of compaction level. Range is 1 to 1e6.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:OPT:COMP:LEV 2000  
Query Syntax |  SOURce<cnum>:DPD :MODel:DYNGain:OPTimize:COMPact:LEVel?  
Return Type |  Numeric  
Default |  10  
  
* * *

## SOURce<cnum>:DPD :MODel:DYNGain:OPTimize:NMSE:GOAL <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets the
NMSE Optimization Goal in dB.  If enabled, the optimizer attempts to minimize
parameters while still resulting in an NMSE less than the value entered.
Algorithm starts with the least complex model, then tries more complex models
until the NMSE value is below the goal value. If the goal cannot be achieved,
then the model with the lowest NMSE is chosen and an error message will be
displayed indicating that the goal was not achieved.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Value of NMSE goal in dB. Max is 0 dB.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:OPT:NMSE:GOAL -20  
Query Syntax |  SOURce<cnum>:DPD :MODel:DYNGain:OPTimize:NMSE:GOAL?  
Return Type |  Numeric  
Default |  -40 dB  
  
## SOURce<cnum>:DPD :MODel:DYNGain:OPTimize:NMSE:INCLude <bool> [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Enable or
disable the NMSE Optimization Goal.  If enabled, the optimizer attempts to
minimize parameters while still resulting in an NMSE less than the value
entered. Algorithm starts with the least complex model, then tries more
complex models until the NMSE value is below the goal value. If the goal
cannot be achieved, then the model with the lowest NMSE is chosen and an error
message will be displayed indicating that the goal was not achieved. If
disabled then the optimizer finds the parameters with the lowest NMSE. This
likely results in a very complex model. Reason: It is likely that there is
little practical difference between models that have very low NMSE. In those
cases, we want to have a "good enough" NMSE and the smallest model possible. ▪
Default value is -40dB  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Disable the optimization. **1 - ON** \- Enable the optimization.   
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:OPT:NMSE:INCL 1  
Query Syntax |  SOURce<cnum>:DPD :MODel:DYNGain:OPTimize:NMSE:INCLude?  
Return Type |  Numeric  
Default |  0  
  
* * *

##
SOURce<cnum>:DPD<Port>:MODel:DYNGain:OPTimize:MEMory:OPERator:INCLude<bool>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Include or
exclude memory operators when optimizing the DPD model. If enable, then DPD
will iterate the Past Memory, Future Memory, Number of Power Segments, and
combination of memory operators M1/M2/M3/M4.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<bool> |  Choose from: **0 - OFF** -Exclude the memory operators **1 - ON** \- Include the memory operators   
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:DYNG:OPT:MEM:OPER:INCL 1 source:DPD1:model:dyngain:optimize:memory:operator:include on  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DYNGain:OPTimize:FAST?  
Return Type |  Numeric  
Default |  0  
  
* * *

* * *

##
SOURce<cnum>:DPD<GuiActiveSourcePort>:MODel:DYNGain:POWer:SEGMent:COUNt<num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the number of power segments.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<num> |  Number of the power segments  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:DYNG:POW:SEGM:COUNT 5  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DYNGain:POWer:SEGMent:COUNt?  
Return Type |  Numeric  
Default |  5  
  
* * *

##
SOURce<cnum>:DPD<GuiActiveSourcePort>:MODel:DYNGain:POWer:SEGMent:POINt:COUNt:MINimum

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the minimum points per power segment  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1  
<num> |  Minimum points per power segment  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:DYNG:POW:SEGM:POIN:COUNT:MIN 100  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:DYNGain:POWer:SEGMent:POINt:COUNt:MINimum?  
Return Type |  Numeric  
Default |  100  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:MEMPoly:CROSsterm <enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads whether or not to perform crossterm calculations using default values
for the crossterm equation.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1  
<enum> |  Choose from: OFF \- Do not use crossterm calculations. AUTO \- Perform crossterm calculations using default values for the crossterm equation.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:MEMP:CROS AUTO  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:MEMPoly:CROSsterm?  
Return Type |  Enumeration  
Default |  AUTO  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:MEMPoly:MEMory:FUTure <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the number of input future time samples to use for calculating the
current output sample.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of future time samples.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:MEMP:MEM:FUT 1  
source2:dpd:model:mempoly:memory:future 1  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:MEMPoly:MEMory:FUTure?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:MEMPoly:MEMory:PAST <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the number of input past time samples to use for calculating the current
output sample.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Number of past time samples.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:MEMP:MEM:PAST -3  
source2:dpd:model:mempoly:memory:past -3  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:MEMPoly:MEMory:PAST?  
Return Type |  Numeric  
Default |  -3  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:MEMPoly:ORDer <num>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the order of the polynomial equation used to model the DUT nonlinearity.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Polynomial order.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:MOD:MEMP:ORD 5  
source2:dpd:model:mempoly:order 5  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:MEMPoly:ORDer?  
Return Type |  Numeric  
Default |  5  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:STATus? [,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-only) Returns a
message indicating if the calibration was successful or not.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD:MOD:STAT? "DPD source calibration failed. Desired tolerance could not be achieved."  
Return Type |  Comma-separated list of strings.  
Default |  Not applicable  
  
* * *

## SOURce<cnum>:DPD<port>:MODel:TYPE <enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads DPD Model type.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: MEMPoly\- Selects the memory polynomial DPD Model. DYNGain \- Selects the dynamic gain DPD Model.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:TYPE MEMP  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:TYPE?  
Return Type |  Enumeration  
Default |  MEMPoly  
  
* * *

## SOURce<cnum>:DPD<GuiActiveSourcePort>:MODel:USE:DIRect<enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Create the
model using Direct DPD from file or Direct DPD measurement.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: MEASurement \- The model is fit to the Direct DPD measurement.  FILE \- Direct DPD waveform from the file is used to fit the model.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:MOD:USE:DIR MEA  
Query Syntax |  SOURce<cnum>:DPD<port>:MODel:USE:DIRect?  
Return Type |  Enumeration  
Default |  MEASurement  
  
* * *

## SOURce<cnum>:DPD<Port>:PAPR:EXPansion:MAXimum<num>[srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the maximum PAPR Expansion.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, <port> is set to 1.  
<num> |  Maximum PAPR Expansion in dB.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR:DPD1:PAR:EXP:MAX 2  
Query Syntax |  SOURce<cnum>:DPD<port>:PAPR:EXPansion:MAXimum?  
Return Type |  Numeric  
Default |  2dB  
  
## SOURce<cnum>:DPD<port>:PROCedure <enum>[,srcPort]

Applicable Models: All with Option S93070xB/9x070A/B (Read-Write) Sets and
reads the type of DPD procedure to use.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<port> |  Source port number of the VNA. If unspecified, value is set to 1.  
<enum> |  Choose from: DIRect \- Creates a Direct DPD waveform without a model. MODel - Creates a DPD model and a Modeled DPD waveform. APPLy \- The user will supply an Ideal Waveform file and a DPD Model file.  
[srcPort] |  String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an [external source](../../System/Configure_an_External_Device.md#SelectExtSource), [true mode balanced port](../../Applications/iTMSA.md), or one of the Source 2 outputs on the 2-port 2-source PNA-X model such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [srcPort] takes priority.  
Examples |  SOUR1:DPD1:PROC MOD  
Query Syntax |  SOURce<cnum>:DPD<port>:PROCedure?  
Return Type |  Enumeration  
Default |  DIRect  
  
* * *


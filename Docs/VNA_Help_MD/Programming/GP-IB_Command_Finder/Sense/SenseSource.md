# Sense:Source Command

* * *

SENSe:SOURce | PLLBandwidth | [CATalog](SenseSource.md#PllbCat) | [[:VALue]](SenseSource.md#Pllb) | RECeiver | [GAIN[:VALue]](SenseSource.md#RecGain) |[ ALL[:VALUE]](SenseSource.md#RecGainAll) | [CATalog](SenseSource.md#RecGainCat) | COUPling | ALL[[:VALue]](SenseSource.md#RecGainCoupAll) | [[:STATe]](SenseSource.md#RecGainCoup) | [LIST](SenseSource.md#RecGainList)  
---  
  
  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:SOURce:PLLBandwidth:CATalog?

Applicable Models: M98xxA, P50xxA/B, P93xxB, E5080B, E5081A (Read-Write) Lists
PLL bandwidth type for SENSe<cnum>:SOURce:PLLBandwidth[:VALue].  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
Examples |  SENSe1:SOUR:PLLB:CAT?  
sense2:source:pllbandwidth:catalog?  
Query Syntax |  SENSe<cnum>:SOURce:PLLBandwidth:CATalog?  
Return Type |  <sting>, available setting list with comma separated chars  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not applicable  
  
* * *

## SENSe<cnum>:SOURce:PLLBandwidth[:VALue] <type>

Applicable Models: M98xxA, P50xxA/B, P93xxB, E5080B, E5081A (Read-Write) Sets
and read the settings for PLL bandwidth for RF source and LO. The source and
LO settings are coupled.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<type> |  choose from:

  * AUTO: Use an appropriate PLL bandwidth automatically.
  * NARRow: Use the narrow PLL bandwidth. The phase noise of the RF and local sources decreases while the cycle time increases.

  
Examples |  SENSe1:SOUR:PLLB NARR   
sense2:source:pllbandwidth narrow  
Query Syntax |  SENSe<cnum>:PLLBandwidth[:VALue]?  
Return Type |  Enumeration  
Default |  AUTO  
  
* * *

## SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN[:VALue] <string>

Applicable Models: M98xxA, P50xxA/B, P93xxB, E5080B, E5081A, (Read-Write) Sets
the gain settings to a specified port. Use SENS:SOUR:REC:GAIN:CAT? to return a
list of available gain states for the specified port.  Note: (M983xA) This
command works only when the gain coupling is enabled by
[:SENS:SOUR:REC:GAIN:COUP:ALL](SenseSource.md#RecGainCoupAll).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<sport> |  Source port number of the VNA. If unspecified, value is set to 1  
<rport> |  Receiver port number of the VNA. If unspecified, value is set to 1  
<string> |  Receiver gain state. Not case sensitive. choose from:

  * Auto
  * Low
  * High

  
Examples |  SENSe:SOUR1:REC2:GAIN "Low" ' Low for S21 measurement  
sense:source2:receiver2:gain:value "High" ' High for S22 measurement  
Query Syntax |  SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN[:VALue] ?  
Return Type |  <sting>, available setting list with comma separated chars  
Default |  Not  
  
* * *

## SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:ALL[:VALue] <string>

Applicable Models: M98xxA, P50xxA/B, P93xxB, E5080B, E5081A, (Read-Write) Sets
the gain settings to all ports. Use SENS:SOUR:REC:GAIN:CAT? to return a list
of available gain states for the VNA.  Note: (M983xA) This command works only
when the gain coupling is enabled by
[:SENS:SOUR:REC:GAIN:COUP:ALL.](SenseSource.md#RecGainCoupAll)  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<sport> |  Ignored  
<rport> |  Ignored  
<string> |  Receiver gain state. Not case sensitive. choose from:

  * Auto
  * Low
  * High

  
Examples |  SENSe:SOUR1:REC2:GAIN:ALL "Low" ' Low for all measurements  
sense:source2:receiver2:gain:all:value "High" ' High for all measurements  
Query Syntax |  SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:ALL[:VALue] ?  
Return Type |  String. "MIXED" is returned when the settings are not the same.  
Default |  Auto  
  
* * *

## SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:CATalog

Applicable Models: M98xxA, P50xxA/B, P93xxB, E5080B, E5081A, (Read only) Reads
a list of valid state for the receiver gain on the specified port.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<sport> |  Source port number of the VNA. If unspecified, value is set to 1  
<rport> |  Receiver port number of the VNA. If unspecified, value is set to 1  
Examples |  SENSe:SOUR1:REC2:GAIN:CAT?  
sense:source2:receiver2:gain:catalog?  
Query Syntax |  SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:CATalog?  
Return Type |  String (Comma-separated list of strings.) ("Auto,Low,High" is returned.)  
Default |  Auto  
  
* * *

## SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:COUPling:ALL[:VALue] <type>

Applicable Models: M983xA, (Read-Write) Set and read the setting for receiver
gain coupling for all port in the specified channel. This command does not wok
for NF, NFX, SA, MOD, and MODX measurement class.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<sport> |  Ignored  
<rport> |  Ignored  
<Type> |  choose from:

  * OFF
  * ON
  * Mixed (Read only) This is returned when the setting is not same in the multi-module configuration of M980xA and M983xA

  
Examples |  SENSe:SOUR1:REC:GAIN:COUP:ALL ON   
sense:source2:receiver:gain:coupling:all:value on  
Query Syntax |  SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:COUPling:ALL[:VALue]?  
Return Type |  Enum  
Default |  ON  
  
* * *

## SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:COUPling[:STATe]

Applicable Models: M983xA, (Read only) Returns the status per port for
receiver gain coupling.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<sport> |  Ignored  
<rport> |  Receiver port number of the VNA. If unspecified, value is set to 1  
Examples |  SENSe:SOUR1:REC:GAIN:COUP?   
sense:source2:receiver:gain:coupling:state?  
Query Syntax |  SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:COUPling[:STATe]?  
Return Type |  Boolean (0: OFF, 1: ON)  
Default |  ON  
  
* * *

## SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:LIST?

Applicable Models: M98xxA, P50xxA/B, P93xxB, E5080B, E5081A, (Read only) Gets
the data array for actual gain setting of each measurement points. High: 1,
Low: 0. The number of returned data is the same as the NOP.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<sport> |  Source port number of the VNA. If unspecified, value is set to 1  
<rport> |  Receiver port number of the VNA. If unspecified, value is set to 1  
Examples |  SENSe:SOUR1:REC2:GAIN:LIST?  
sense:source2:receiver2:gain:list?  
Query Syntax |  SENSe<cnum>:SOURce<sport>:RECeiver<rport>:GAIN:LIST?  
Return Type |  Data block  
Default |  Not Applicable  
  
* * *


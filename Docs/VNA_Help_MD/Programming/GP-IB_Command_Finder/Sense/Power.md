# Sense:Power Command - Superseded

* * *

This command is superseded by the
[SOURce:POWer:ATTenuation:RECeiver:TEST](../source.md#SOURce:POWer:ATTenuation:RECeiver:TEST)
command.

[Learn about Receiver
Attenuation](../../../S1_Settings/Power_Level.htm#Receiver_Atten)

## SENSe<cnum>:POWer:ATTenuator <recvr>,<num>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets the attenuation
level for the specified receiver. Note: Attenuation cannot be set with Sweep
Type set to Power Note: For M980xA/P50xxA/E5080B Receiver Gain, use
[:SENS:SOUR:REC:GAIN](SenseSource.md#RecGain).  
---  
Parameters |   
<cnum> | Any existing channel number. If unspecified, value is set to 1  
<recvr> | Receiver to get attenuation. Choose from:

  * ARECeiver \- receiver A
  * BRECeiver \- receiver B
  * CRECeiver \- receiver C
  * DRECeiver \- receiver D

Receiver attenuation can NOT be set using [logical receiver
notation](../../../S1_Settings/Measurement_Parameters.htm#RecNotation).  
<num> | Attenuation value in dB. To determine how many receiver attenuators, the maximum receiver attenuation, and attenuation step size, for a VNA model, see [VNA Models and Options](../../../Support/Configurations.md). If a number other than these is entered, the analyzer will select the next lower valid value. For example, if 19 is entered for the E8361A/C, then 10 dB attenuation will be selected.  
Examples | SENS:POW:ATT AREC,10  
sense2:power:attenuator breceiver,30  
Query Syntax | SENSe<cnum>:POWer:ATTenuator? <rec>  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *


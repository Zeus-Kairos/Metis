# Sense Attenuator

When you use the PXI VNAs, you can control the M9168C/E program Step
Attenuator module through the VNA firmware. The following commands are
available when the launcher includes the M9168C/E.

SENSe:ATTenuatorr:M91Xx | [COUNt?](Atten.md#Count) | MODule | [ATTnuation](Atten.md#ModAtt) | [CHASsis](Atten.md#ModChas) | [CONTrol[:STATe]](Atten.md#ModCont) | [PATH](Atten.md#ModPath) | [RESet:IMMediate](Atten.md#ResImm) | [SLOT](Atten.md#ModSlot)  
---  
  
Click on a keyword to view the command details.

* * *

## SENSe<cnum>:ATTenuator:M91Xx:COUNt?

Applicable Models: PXI VNAs (Read-only) Returns the total number of M9168C/E
Attenuator that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:ATT:M91X:COUN?  
sense2:attenuator:m91xx:count?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:ATTenuator:M91Xx:MODule<mod>:ATTenuation<id> <val>

Applicable Models: PXI VNAs (Read-Write) Sets and reads the attenuation of the
M9168C/E.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9168C/E. The number starts from 1 for the leftmost module of M9168C/E.  
<id> | Id of the attenuation value, if unspecified, value is set to 1 1: for S parameter sweep  2: for Noise Figure Sweep  
<val> | Attenuation in dB from 0 to 101dB with 1 dB step.  
Examples | SENS:ATT:M91X:MOD1:ATT1 10  
sense2:attenuator:m91xx:module2:attenuation2 5  
Query Syntax | SENSe<cnum>:ATTenuator:M91Xx::MODule<mod>:ATTenuation<id>?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<cnum>:ATTenuator:M91Xx:MODule<mod>:CHASsis?

Applicable Models: PXI VNAs (Read Only) Returns the chassis number where the
specified M9168C/E module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9168C/E. The number starts from 1 for the leftmost module of M9168C/E.  
Examples | SENS:ATT:M91X:MOD1:CHAS? sense2:attenuator:m91xx:module2:chassis?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe<cnum>:ATTenuator:M91Xx:MODule<mod>:CONTrol[:STATe] <bool>

Applicable Models: PXI VNAs (Read-Write) Sets and reads the status of M9168C/E
control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9168x. The number starts from 1 for the leftmost module M9168x  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9168C/E at the specified channel. 1 or ON \- Enables to control the M9168C/E at the specified channel.  
Examples | SENS:ATT:M91X:MOD1:CONT ON sense2:attenuator:m91xx:module2:control 0  
Query Syntax | SENSe<cnum>:ATTenuator:M91Xx:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<cnum>:ATTenuator:M91Xx:MODule<mod>:PATH <char>

Applicable Models: PXI VNAs (Read-Write) Sets and reads the path for the
M9168C/E.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9168C/E. The number starts from 1 for the leftmost module of M9168C/E.  
<char> | Path. Choose from: ANY \- Fixed attenuator setting  NFSource \- 

  * Attenuation value of ID 1 is used for the source path in S-Parameter sweep 
  * Attenuation value of ID 2 is used for the source path in Noise Figure sweep

NFReceiver - Receiver path during NF measurement

  * Attenuation value of ID 1 is used for the receiver path in S-Parameter sweep 
  * Attenuation value of ID 2 is used for the receiver path in Noise Figure sweep

See [SENSe:ATT:M91X::MOD:ATT](Atten.md#ModAtt) for ID1 and 2  
Examples | SENS:ATT:M91X:MOD1:PATH ANY sense2:ATT:M91X:module2:path NFSource  
Query Syntax | SENSe<cnum>:ATTenuator:M91Xx:MODule<mod>:PATH?  
Return Type | Char  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ANY  
  
* * *

## SENSe<cnum>:ATTenuator:M91Xx:MODule<mod>:RESet:IMMediate

Applicable Models: PXI VNAs (Write Only) Reset the M9168C/E setting at the
default value.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9168C/E. The number starts from 1 for the leftmost module of M9168C/E.  
Examples | SENS:ATT:M91X:MOD1:RES:IMM sense2:ATT:M91X:module2:reset:immediate  
Return Type | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe<cnum>:ATTenuator:M91Xx:MODule<mod>:SLOT?

Applicable Models: PXI VNAs (Read Only) Reads the slot number where the
M9168C/E is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9168C/E. The number starts from 1 for the leftmost module of M9168C/E.  
Examples | SENS:ATT:M91X:MOD1:SLOT? sense2:ATT:M91X:module2:slot?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *


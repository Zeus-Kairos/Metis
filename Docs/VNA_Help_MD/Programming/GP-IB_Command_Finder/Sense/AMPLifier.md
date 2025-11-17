# Sense Amplifier

When you use the PXI VNAs, you can control the M9379A amplifier through the
VNA firmware. The following commands are available when the launcher includes
the M9379A.

SENSe:AMPLifier:M9379 | [COUNt?](AMPLifier.md#Count) | MODule | [:ATTenuation](AMPLifier.md#ModAtt) | [:CHASsis](AMPLifier.md#ModChas) | [:CONTrol[:STATe]](AMPLifier.md#ModCont) | [:PATH](AMPLifier.md#ModPath) | [:POWer[:STATe]](AMPLifier.md#ModPow) | [:SLOT](AMPLifier.md#ModSlot) | [:SWITch:PATH](AMPLifier.md#ModSwitPath)  
---  
  
Click on a keyword to view the command details.

* * *

## SENSe<cnum>:AMPLifier:M9379:COUNt?

Applicable Models: PXI VNAs (Read-only) Returns the total number of M9379A
amplifier modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:AMPL:M9379:COUN?  
sense2:amplifier:m9379:count  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:AMPLifier:M9379:MODule<mod>:ATTenuation <att>

Applicable Models: PXI VNAs (Read-Write) Sets and reads the attenuation of the
M9379A amplifier 1.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9379A. The number starts from 1 for the leftmost module of M9379A.  
<att> | Attenuation in dB from 0 to 28 with 2 step  
Examples | SENS:AMPL:M9379:MOD1:ATT 10  
sense2:amplifier:m9379:module2:attenuation 5  
Query Syntax | SENSe<cnum>:AMPLifier:M9379:MODule<mod>:ATTenuation?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 28  
  
* * *

## SENSe<cnum>:AMPLifier:M9379:MODule<mod>:CHASsis?

Applicable Models: PXI VNAs (Read Only) Returns the chassis number where the
specified M9379A module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9379A. The number starts from 1 for the leftmost module of M9379A.  
Examples | SENS:AMPL:M9379:MOD1:CHAS? sense2:amplifier:m9379:module2:chassis?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe<cnum>:AMPLifier:M9379:MODule<mod>:CONTrol[:STATe] <bool>

Applicable Models: PXI VNAs (Read-Write) Sets and reads the status of M9379A
control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9379A. The number starts from 1 for the leftmost module of M9379A.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9379A at the specified channel. 1 or ON \- Enables to control the M9379A at the specified channel.  
Examples | SENS:AMPL:M9379:MOD1:CONT ON sense2:amplifier:m9379:module2:control 0  
Query Syntax | SENSe<cnum>:AMPLifier:M9379:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1 or ON  
  
* * *

## SENSe<cnum>:AMPLifier:M9379:MODule<mod>:PATH <char>

Applicable Models: PXI VNAs (Read-Write) Sets and reads the path for the
M9379A amplifier 1.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9379A. The number starts from 1 for the leftmost module of M9379A.  
<char> | Path. Choose from: THRU \- Through. AMPLifier \- amplifier 1. NFReceiver - NF receiver switch (NF measurement only)  
Examples | SENS:AMPL:M9379:MOD1:PATH THRU sense2:amplifier:m9379:module2:path amplifier  
Query Syntax | SENSe<cnum>:AMPLifier:M9379:MODule<mod>:PATH?  
Return Type | Char  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | THRU  
  
* * *

## SENSe<cnum>:AMPLifier:M9379:MODule<mod>:POWer[:STATe] <bool>

Applicable Models: PXI VNAs (Read-Write) Sets and reads the status of M9379A
power.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9379A. The number starts from 1 for the leftmost module of M9379A.  
<bool> | power control state. Choose from: 0 or OFF \- Power off 1 or ON \- Power on  
Examples | SENS:AMPL:M9379:MOD1:POW ON sense2:amplifier:m9379:module2:power 0  
Query Syntax | SENSe<cnum>:AMPLifier:M9379:MODule<mod>:POWer[:STATe]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0 or OFF  
  
* * *

## SENSe<cnum>:AMPLifier:M9379:MODule<mod>:SLOT?

Applicable Models: PXI VNAs (Read Only) Reads the slot number where the M9379A
is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9379A. The number starts from 1 for the leftmost module of M9379A.  
Examples | SENS:AMPL:M9379:MOD1:SLOT? sense2:amplifier:m9379:module2:slot?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe<cnum>:AMPLifier:M9379:MODule<mod>:SWITch:PATH <char>

Applicable Models: PXI VNAs (Read-Write) Sets and reads the path for the
M9379A switch  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9379A. The number starts from 1 for the leftmost module of M9379A.  
<char> | Path. Choose from: A \- Path A B \- Path B NFSource \- NF source switch (NF measurement only) NFLO \- NF LO switch (Option 720 only) NFReceiver - NF receiver switch (NF measurement only)  
Examples | SENS:AMPL:M9379:MOD1:SWIT:PATH A sense2:amplifier:m9379:module2:switch:path b  
Query Syntax | SENSe<cnum>:AMPLifier:M9379:MODule<mod>:SWITch:PATH?  
Return Type | <char>  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | A  
  
* * *


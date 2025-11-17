# Sense Switch

When you use the PXIe VNA, you can control the PXIe switch module through the
VNA firmware. The following commands are available when the launcher includes
the PXIe switch module.

SENSe:SWITch :L8990M | :CHAR | :ABORt | :INIT | :SAVE | :STEP | :ACQ | :COUNt? | :DESC? | :LOAD | :PATH | :**DEEMbed** | :CALSet | :NAME | :STATe | :STIMulus | :STATe | :VNA | :PORT | :CATalog? | :PORT | :LABel  
:M9161 | :COUNt? | :MODule | :CHASsis | :CONTrol[:STATe] | :RESet:IMMediate | :SLOT | :SWITch:PATH | :SWITch:PATH:CATalog :M9155 | [:COUNt?](SWITch.md#Count9155) | :MODule | [:CHASsis](SWITch.md#ModChas9155) | [:CONTrol[:STATe]](SWITch.md#ModCont9155) | RESet:IMMediate | [:SLOT](SWITch.md#ModSlot9155) | [:SWITch:PATH](SWITch.md#ModSwitPath9155) | [:SWITch:PATH:CATalog](SWITch.md#ModSwitPathCat9155) :M9156 | :COUNt? | :MODule |[ :CHASsis](SWITch.md#ModChas9156) | [:CONTrol[:STATe]](SWITch.md#ModCont9156) | RESet:IMMediate | [:SLOT](SWITch.md#ModSlot9156) | [:SWITch:PATH](SWITch.md#ModSwitPath9156) | [:SWITch:PATH:CATalog](SWITch.md#ModSwitPathCat9156) :M9157 | [:COUNt?](SWITch.md#Count9157) | :MODule | [:CHASsis](SWITch.md#ModChas9157) | [:CONTrol[:STATe]](SWITch.md#ModCont9157) | [:RESet:IMMediate](SWITch.md#ResImm9157) | [:SLOT](SWITch.md#ModSlot9157) | [:SWITch:PATH](SWITch.md#ModSwitPath9157) | [:SWITch:PATH:CATalog](SWITch.md#ModSwitPathCat9157) :M9164 | :COUNt? | :MODule | :CHASsis | :CONTrol[:STATe] | RESet:IMMediate | :SLOT | :SWITch:PATH | :MODel? :M9165 | :COUNt? | :MODule | :CHASsis | :CONTrol[:STATe] | RESet:IMMediate | :SLOT | :SWITch:PATH | :MODel? :P9164 | :COUNt? | :MODule | :CHASsis | :CONTrol[:STATe] | :SLOT | :SWITch:PATH | :MODel? :P9165 | :COUNt? | :MODule | :CHASsis | :CONTrol[:STATe] | :SLOT | :SWITch:PATH | :MODel?  
---  
  
Click on a keyword to view the command details.

* * *

## **SENSe<cnum>:SWITch:L8990M:CHAR:ABORt <devname>**

Applicable Models: All VNAs with option 011 (Write Only) Aborts current switch
matrix characterization.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
Examples | **SENS:SWIT:L8990M:CHAR:ABOR 'L8990MUSBTDR'  
sense:switch:L8990M:char:abort 'L8990MUSBTDR'**  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:CHAR:INIT <devname>, <calset>**

Applicable Models: All VNAs with option 011 (Write Only) Initiates a guided
switch matrix characterization.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
<calset> | String. Tier1 Cal Set Name.  
Examples | **SENS:SWIT:L8990M:CHAR:INIT 'L8990MUSBTDR','L8990Mtier1'** **sense:switch:L8990M:char:init 'L8990MUSBTDR', 'L8990Mtier1'**  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:CHAR:SAVE <devname>**

Applicable Models: All VNAs with option 011 (Write Only) Completes current
switch matrix characterization, S2P files saved.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
Examples | **SENS:SWIT:L8990M:CHAR:SAVE 'L8990MUSBTDR'  
sense:switch:L8990M:char:save 'L8990MUSBTDR'**  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:CHAR:STEP<num>:ACQ <devname>**

Applicable Models: All VNAs with option 011 (Write Only) Initiates the
measurement of the specified characterization step.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<num> | step number  
<devname> | String. Device Name for L8990M.  
Examples | **SENS:SWIT:L8990M:CHAR:STEP2:ACQ 'L8990MUSBTDR'  
sense:switch:L8990M:char:step2:acq 'L8990MUSBTDR'**  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:CHAR:STEP:COUNt? <devname>**

Applicable Models: All VNAs with option 011 (Read-only) Returns the number of
measurement steps required to complete the current guided switch matrix
characterization.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
Examples | **SENS:SWIT:L8990M:CHAR:STEP:COUN? 'L8990MUSBTDR'  
sense:switch:L8990M:char:step:count ****' L8990MUSBTDR'**  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:CHAR:STEP<num>:DESC? <devname>**

Applicable Models: All VNAs with option 011 (Read-only) Returns the step
description.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<num> | step number  
<devname> | String. Device Name for L8990M.  
Examples | **SENS:SWIT:L8990M:CHAR:STEP1:DESC? 'L8990MUSBTDR' ** **sense:switch:L8990M:char:step2:desc****' L8990MUSBTDR'**  
Return Type | Character  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:LOAD <devname>,<swpFileName> **

Applicable Models: All VNAs with option 011 (Write Only) Load a switch config
.swp file (actually in xml format), which is saved from the External Switch
Matrix properties dialog.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
<swpFileName> | String.File name for the .swp file.  
Examples | **SENS:SWIT:L8990M:LOAD 'L8990MUSBTDR','L8990MCONFIG'** **sense:switch:L8990M:load 'L8990MUSBTDR','L8990MCONFIG'**  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:PATH <devname>,<num>,[<num>,<num>,<num>]**

Applicable Models: All VNAs with option 011 (Write Only) Sets switch matrix
positions, let VNA ports thru to the switch test ports in the specified order.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
**< num>,[<num>,<num>,<num>]** | switch test port numbers. They are mapped to the order of VNA port list, which can be returned by command SENS:SWIT:L8990M:PATH:VNA:PORT:CAT?  
Examples | **SENS:SWIT:L8990M:PATH L8990MUSBTDR, 1,2,3,4  
sense:switch:L8990M:path L8990MUSBTDR, , 1,2,3,4**  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:PATH:DEEMbed:CALSet:NAME <devname>, <calset>**

Applicable Models: All VNAs with option 011 (Read-Write) Sets Tier 1 Cal Set
name.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
<calset> | String. Tier1 Cal Set Name.  
Examples | **SENS:SWIT:L8990M:PATH:DEEM:CALS:NAME 'L8990MUSBTDR','L8990Mtier1'** **sense2:switch:L8990M:path:deembed:calset:name 'L8990MUSBTDR','L8990Mtier1'**  
Query Syntax |  | SENSe<cnum>:SWITch:L8990M:PATH:DEEMbed:CALSet:Name?  
---  
Return Type | Character  
Default | Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:PATH:DEEMbed:CALSet:STATe <devname>****, <**
char>

Applicable Models: All VNAs with option 011 (Read-Write) Sets and returns
enable de-embedding state.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
<char> | De-embedding state. Choose from: ON  enable de-embedding state OFF  Disable de-embedding state  
Examples | **SENS:SWIT:L8990M:PATH:DEEM:CALS:STAT 'L8990MUSBTDR',ON** **sense:switch:L8990M:path:deembed:calset:state 'L8990MUSBTDR',OFF**  
Query Syntax | SENSe<cnum>:SWITch:L8990M:PATH:DEEMbed:CALSet:STATe?  
Return Type |  Character  
Default |  OFF  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:PATH:DEEMbed:CALSet:STIMulus:STATe
<devname>,<** char>

Applicable Models: All VNAs with option 011 (Read-Write) Should the Cal Set
stimulus values be applied to the channel.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<devname> | String. Device Name for L8990M.  
<char> | ON  Apply Cal Set stimulus values to the channel OFF  Cal Set stimulus values will not applied to the channel  
Examples | **SENS:SWIT:L8990M:PATH:DEEM:CALS:STIM:STAT 'L8990MUSBTDR',ON** **sense:switch:L8990M:path:deembed:calset:stimulus:state 'L8990MUSBTDR',OFF**  
Query Syntax | SENSe<cnum>:SWITch:L8990M:PATH:DEEMbed:CALSet:STIMulus:STATe?  
Return Type |  Character  
Default |  OFF  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:PORT<pnum>:LABel <devname>****, <portLabel>**

Applicable Models: All VNAs with option 011 (Read-Write) Sets and returns port
label on each switch test port.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<pnum> | Port numbers.  
<devname> | String. Device Name for L8990M.  
<portLabel> | String. Port Label.  
Examples | **SENS:SWIT:L8990M:PORT:LAB 'L8990MUSBTDR','TX1(L)'** **sense:switch:L8990M:path2:label 'L8990MUSBTDR','TX1(L)'**  
Query Syntax | SENSe<cnum>:SWITch:L8990M:PATH:DEEMbed:CALSet:STIMulus:STATe?  
Return Type |  Character  
Default |  Not applicable  
  
* * *

## **SENSe<cnum>:SWITch:L8990M:PATH:VNA:PORT:CATalog? ****< devname>**

Applicable Models: All VNAs with option 011 (Read-only) Returns the configured
VNA port list.  For example, if VNA port 1,2,3 and 4 are configured, it
returns 1,2,3,4; if VNA port 1 and 3 are configured, it returns 1,3; if
only VNA port 1 is configured, it returns 1.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<devname> | String. Device Name for L8990M.  
Examples | **SENS:SWIT:L8990M:PATH:VNA:PORT:CAT?  
sense:switch:L8990M:path:vna:port:catalog?**  
Return Type | Comma-separated string  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9161:COUNt?

Applicable Models: All PXIe VNAs (Read-only) Returns the total number of
M9161D switch modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:SWIT:M9161:COUN?  
sense:switch:m9161:count  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9161:MODule<mod>:CHASsis?

Applicable Models: All PXIe VNAs (Read Only) Returns the chassis number where
the specified M9161D module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9161D. The number starts from 1 for the left most module of M9161D.  
Examples | SENS:SWIT:M9161:MOD1:CHAS? sense:SWITch:m9161:module2:chassis?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9161:MODule<mod>:CONTrol[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the status of
M9161D control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9161D. The number starts from 1 for the leftmost module of M9161D.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9161D at the specified channel. 1 or ON \- Enables to control the M9161D at the specified channel.  
Examples | SENS:SWIT:M9161:MOD1:CONT ON sense2:SWITch:M9161:module2:control 0  
Query Syntax | SENSe<cnum>:SWITch:M9161:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
Default | 1 or ON  
  
* * *

## SENSe<cnum>:SWITch:M9161:MODule<mod>:RESet:IMMediate

Applicable Models: All PXIe VNAs (Write Only) Resets the switches in the
specified module to "All Open" state immediately.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9161D. The number starts from 1 for the leftmost module of M9161D.  
Examples | SENS:SWIT:M9161:MOD1:RES:IMM sense:SWITch:M9161:module2:reset:immediate  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9161:MODule<mod>:SLOT?

Applicable Models: All PXIe VNAs (Read Only) Reads the slot number where the
specified M9161D is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9161D. The number starts from 1 for the leftmost module of M9161D.  
Examples | SENS:SWIT:M9161:MOD1:SLOT? sense:SWITch:M9161:module2:slot?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9161:MODule<mod>:SWITch:PATH <char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the path for the
M9161D switch.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9161D. The number starts from 1 for the left most module of M9161D.  
<char> | Path. Choose from: STATe1 to STATe4 \- State 1 to 4 NFSource \- NF source switch (NF measurement only) NFLO \- NF LO switch (Option 720 only) NFReceiver - NF receiver switch (NF measurement only)  
Examples | SENS:SWIT:M9161:MOD1:SWIT:PATH STAT1 sense2:SWITch:M9161:module2:switch:path state4  
Query Syntax | SENSe<cnum>:SWITch:M9161:MODule<mod>:SWITch:PATH?  
Return Type | <char>  
Default | STATe1  
  
* * *

## SENSe<cnum>:SWITch:M9161:MODule<mod>:SWITch:PATH:CAalog?

Applicable Models: All PXIe VNAs (Read-Write) Lists the path of the M9161D for
SENS:SWIT:M9161:MOD:SWIT:PATH.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9161D. The number starts from 1 for the left most module of M9161D.  
Examples | SENS:SWIT:M9161:MOD1:SWIT:PATH:CAT? sense2:SWITch:M9161:module2:switch:path:catalog?  
Query Syntax | SENSe<cnum>:SWITch:M9161:MODule<mod>:SWITch:PATH:CAT?  
Return Type | Comma-separated string   
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9155:COUNt?

Applicable Models: All PXIe VNAs (Read-only) Returns the total number of
M9155C/M9155CH40 switch modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:SWIT:M9155:COUN?  
sense:switch:m9155:count  
Return Type | Numeric  
Default |   
  
* * *

## SENSe<cnum>:SWITch:M9155:MODule<mod>:CHASsis?

Applicable Models: All PXIe VNAs (Read Only) Returns the chassis number where
the specified M9155C/M9155CH40 module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9155C/M9155CH40. The number starts from 1 for the left most module of M9155C/M9155CH40.  
Examples | SENS:SWIT:M9155:MOD1:CHAS? sense:SWITch:m9155:module2:chassis?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9155:MODule<mod>:CONTrol[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the status of
M9155C/M9155CH40 control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9155C/M9155CH40. The number starts from 1 for the leftmost module of M9155C/M9155CH40.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9155C/M9155CH40 at the specified channel. 1 or ON \- Enables to control the M9155C/M9155CH40 at the specified channel.  
Examples | SENS:SWIT:M9155:MOD1:CONT ON sense2:SWITch:M9155:module2:control 0  
Query Syntax | SENSe<cnum>:SWITch:M9155:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
Default | 1 or ON  
  
* * *

## SENSe<cnum>:SWITch:M9155:MODule<mod>:RESet:IMMediate

Applicable Models: All PXIe VNAs (Write Only) Resets the switches in the
specified module to "All Open" state immediately.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9155C/M9155CH40 The number starts from 1 for the leftmost module of M9155C/M9155CH40.  
Examples | SENS:SWIT:M9155:MOD1:RES:IMM sense:SWITch:M9155:module2:reset:immediate  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9155:MODule<mod>:SLOT?

Applicable Models: All PXIe VNAs (Read Only) Reads the slot number where the
specified M9155C/M9155CH40 is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9155C/M9155CH40 The number starts from 1 for the leftmost module of M9155C/M9155CH40.  
Examples | SENS:SWIT:M9155:MOD1:SLOT? sense:SWITch:M9155:module2:slot?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9155:MODule<mod>:SWITch:PATH <char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the path for the
M9155C/M9155CH40 switch.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9155C/M9155CH40. The number starts from 1 for the left most module of M9155C/M9155CH40.  
<char> | Path. Choose from: STATe1 or STATe2 \- State 1 or 2 NFSource \- NF source switch (NF measurement only) NFLO \- NF LO switch (Option 720 only) NFReceiver - NF receiver switch (NF measurement only)  
Examples | SENS:SWIT:M9155:MOD1:SWIT:PATH STAT1 sense2:SWITch:M9155:module2:switch:path state2  
Query Syntax | SENSe<cnum>:SWITch:M9155:MODule<mod>:SWITch:PATH?  
Return Type | <char>  
Default | STATe1  
  
* * *

## SENSe<cnum>:SWITch:M9155:MODule<mod>:SWITch:PATH:CAalog?

Applicable Models: All PXIe VNAs (Read-Write) Lists the path of the
M9155C/M9155CH40 for SENS:SWIT:M9155:MOD:SWIT:PATH.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9155C/M9155CH40. The number starts from 1 for the left most module of M9155C/M9155CH40.  
Examples | SENS:SWIT:M9155:MOD1:SWIT:PATH:CAT? sense2:SWITch:M9155:module2:switch:path:catalog?  
Query Syntax | SENSe<cnum>:SWITch:M9155:MODule<mod>:SWITch:PATH:CAT?  
Return Type | Comma-separated string   
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9156:COUNt?

Applicable Models: All PXIe VNAs (Read-only) Returns the total number of
M9156C/M9156CH40 switch modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:SWIT:M9156:COUN?  
sense:switch:m9156:count  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9156:MODule<mod>:CHASsis?

Applicable Models: All PXIe VNAs (Read Only) Returns the chassis number where
the specified M9156C/M9156CH40 module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9156C/M9156CH40. The number starts from 1 for the left most module of M9156C/M9156CH40.  
Examples | SENS:SWIT:M9156:MOD1:CHAS? sense:SWITch:m9156:module2:chassis?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9156:MODule<mod>:CONTrol[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the status of
M9156C/M9156CH40 control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9156C/M9156CH4. The number starts from 1 for the leftmost module of M9156C/M9156CH40.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9165C/M9156CH40 at the specified channel. 1 or ON \- Enables to control the M9156C/M9156CH40 at the specified channel.  
Examples | SENS:SWIT:M9156:MOD1:CONT ON sense2:SWITch:M9156:module2:control 0  
Query Syntax | SENSe<cnum>:SWITch:M9156:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
Default | 1 or ON  
  
* * *

## SENSe<cnum>:SWITch:M9156:MODule<mod>:RESet:IMMediate

Applicable Models: All PXIe VNAs (Write Only) Resets the switches in the
specified module to "All Open" state immediately.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9156C/M9156CH40 The number starts from 1 for the leftmost module of M9156C/M9156CH40.  
Examples | SENS:SWIT:M9156:MOD1:RES:IMM sense:SWITch:M9156:module2:reset:immediate  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9156:MODule<mod>:SLOT?

Applicable Models: All PXIe VNAs (Read Only) Reads the slot number where the
specified M9156C/M9155CH40 is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9156C/M9156CH40 The number starts from 1 for the leftmost module of M9156C/M9156CH40.  
Examples | SENS:SWIT:M9156:MOD1:SLOT? sense:SWITch:M9156:module2:slot?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9156:MODule<mod>:SWITch:PATH <char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the path for the
M9156C/M9156CH40 switch.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9156C/M9156CH40. The number starts from 1 for the left most module of M9156C/M9156CH40.  
<char> | Path. Choose from: STATe1 or STATe2 \- State 1 or 2 NFSource \- NF source switch (NF measurement only) NFLO \- NF LO switch (Option 720 only) NFReceiver - NF receiver switch (NF measurement only)  
Examples | SENS:SWIT:M9156:MOD1:SWIT:PATH STAT1 sense2:SWITch:M9156:module2:switch:path state2  
Query Syntax | SENSe<cnum>:SWITch:M9156:MODule<mod>:SWITch:PATH?  
Return Type | <char>  
Default | STATe1  
  
* * *

## SENSe<cnum>:SWITch:M9156:MODule<mod>:SWITch:PATH:CAalog?

Applicable Models: All PXIe VNAs (Read-Write) Lists the path of the
M9156C/M9156CH40 for SENS:SWIT:M9156:MOD:SWIT:PATH.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9156C/M9156CH40. The number starts from 1 for the left most module of M9156C/M9156CH40.  
Examples | SENS:SWIT:M9156:MOD1:SWIT:PATH:CAT? sense2:SWITch:M9156:module2:switch:path:catalog?  
Query Syntax | SENSe<cnum>:SWITch:M9156:MODule<mod>:SWITch:PATH:CAT?  
Return Type | Comma-separated string   
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9157:COUNt?

Applicable Models: All PXIe VNAs (Read-only) Returns the total number of
M9157C/M9157CH40 switch modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:SWIT:M9157:COUN?  
sense:switch:m9157:count  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9157:MODule<mod>:CHASsis?

Applicable Models: All PXIe VNAs (Read Only) Returns the chassis number where
the specified M9157C/M9157CH40 module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9157C/M9157CH40. The number starts from 1 for the left most module of M9157C/M9157CH40.  
Examples | SENS:SWIT:M9157:MOD1:CHAS? sense:SWITch:m9157:module2:chassis?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9157:MODule<mod>:CONTrol[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the status of
M9157C/M9157CH40 control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9157C/M9157CH4. The number starts from 1 for the leftmost module of M9157C/M9157CH40.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9167C/M9157CH40 at the specified channel. 1 or ON \- Enables to control the M9157C/M9157CH40 at the specified channel.  
Examples | SENS:SWIT:M9157:MOD1:CONT ON sense2:SWITch:M9157:module2:control 0  
Query Syntax | SENSe<cnum>:SWITch:M9157:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
Default | 1 or ON  
  
* * *

## SENSe<cnum>:SWITch:M9157:MODule<mod>:RESet:IMMediate

Applicable Models: All PXIe VNAs (Write Only) Resets the switches in the
specified module to "All Open" state immediately.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9157C/M9157CH40. The number starts from 1 for the leftmost module of M9157C/M9157CH40.  
Examples | SENS:SWIT:M9157:MOD1:RES:IMM sense:SWITch:M9157:module2:reset:immediate  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9157:MODule<mod>:SLOT?

Applicable Models: All PXIe VNAs (Read Only) Reads the slot number where the
specified M9157C/M9157CH40 is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9157C/M9157CH40 The number starts from 1 for the leftmost module of M9157C/M9157CH40.  
Examples | SENS:SWIT:M9157:MOD1:SLOT? sense:SWITch:M9157:module2:slot?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9157:MODule<mod>:SWITch:PATH <char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the path for the
M9157C/M9157CH40 switch.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9157C/M9157CH40. The number starts from 1 for the left most module of M9157C/M9157CH40.  
<char> | Path. Choose from: STATe1 to STATe6 \- State 1 to 6 NFSource \- NF source switch (NF measurement only) NFLO \- NF LO switch (Option 720 only) NFReceiver - NF receiver switch (NF measurement only)  
Examples | SENS:SWIT:M9157:MOD1:SWIT:PATH STAT1 sense2:SWITch:M9157:module2:switch:path state2  
Query Syntax | SENSe<cnum>:SWITch:M9157:MODule<mod>:SWITch:PATH?  
Return Type | <char>  
Default | STATe1  
  
* * *

## SENSe<cnum>:SWITch:M9157:MODule<mod>:SWITch:PATH:CAalog?

Applicable Models: All PXIe VNAs (Read-Write) Lists the path of the
M9157C/M9157CH40 for SENS:SWIT:M9157:MOD:SWIT:PATH.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9157C/M9157CH40. The number starts from 1 for the left most module of M9157C/M9157CH40.  
Examples | SENS:SWIT:M9157:MOD1:SWIT:PATH:CAT? sense2:SWITch:M9157:module2:switch:path:catalog?  
Query Syntax | SENSe<cnum>:SWITch:M9157:MODule<mod>:SWITch:PATH:CAT?  
Return Type | Comma-separated string   
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9164:COUNt?

Applicable Models: All PXIe VNAs (Read-only) Returns the total number of
M9164x switch modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:SWIT:M9164:COUN? sense:switch:m9164:count  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9164:MODules<mod>:CHASsis?

Applicable Models: All PXIe VNAs (Read Only) Returns the chassis number where
the specified M9164x module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9164x. The number starts from 1 for the left most module of M9164x.  
Examples | SENS:SWIT:M9164:MOD1:CHAS? sense:SWITch:m9164:module2:chassis?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9164:MODules<mod>:CONTrol[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the status of
M9164x control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9164x. The number starts from 1 for the left most module of M9164x.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9164x at the specified channel. 1 or ON \- Enables to control the M9164x at the specified channel.  
Examples | SENS:SWIT:M9164:MOD1:CONT ON sense2:SWITch:M9164:module2:control 0  
Query Syntax | SENSe<cnum>:SWITch:M9164:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
Default | 1 or ON  
  
* * *

## SENSe<cnum>:SWITch:M9164:MODule<mod>:RESet:IMMediate

Applicable Models: All PXIe VNAs (Write Only) Resets the switches in the
specified module to "All Open" state immediately.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9164x. The number starts from 1 for the left most module of M9164x.  
Examples | SENS:SWIT:M9164:MOD1:RES:IMM sense:SWITch:M9164:module2:reset:immediate  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9164:MODules<mod>:SLOT?

Applicable Models: All PXIe VNAs (Read Only) Reads the slot number where the
specified M9164x is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9164x. The number starts from 1 for the left most module of M9164x.  
Examples | SENS:SWIT:M9164:MOD1:SLOT? sense:SWITch:M9164:module2:slot?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9164:MODules<mod>:SWITch<1-2>:PATH <char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the path for the
M9164x switch.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9164x. The number starts from 1 for the left most module of M9164x.  
<char> | Path. Choose from: STATe0 to STATe16 \- State 0 to 16  
Examples | SENS:SWIT:M9164:MOD1:SWIT:PATH STAT1 sense2:SWITch:M9164:module2:switch:path state4  
Query Syntax | SENSe<cnum>:SWITch:M9164:MODule<mod>:SWITch:PATH?  
Return Type | <enum>  
Default | STATe1 or STATe2  
  
* * *

## SENSe<cnum>:SWITch:M9164:MODules<mod>:MODel?

Applicable Models: All PXIe VNAs (Read Only) Returns the model number of
M9164x.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9164x. The number starts from 1 for the left most module of M9164x  
Examples | SENS:SWIT:M9164:MOD1:MOD? sense:SWITch:M9164:module2:model?  
Return Type |  string   
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9165:COUNt?

Applicable Models: All PXIe VNAs (Read-only) Returns the total number of
M9165x switch modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:SWIT:M9165:COUN?  
sense:switch:m9165:count  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9165:MODules<mod>:CHASsis?

Applicable Models: All PXIe VNAs (Read Only) Returns the chassis number where
the specified M9165x module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9165x. The number starts from 1 for the left most module of M9165x.  
Examples | SENS:SWIT:M9165:MOD1:CHAS? sense:SWITch:m9165:module2:chassis?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9165:MODules<mod>:CONTrol[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the status of
M9165x control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9165x. The number starts from 1 for the left most module of M9165x.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the M9165x at the specified channel. 1 or ON \- Enables to control the M9165x at the specified channel.  
Examples | SENS:SWIT:M9165:MOD1:CONT ON sense2:SWITch:M9165:module2:control 0  
Query Syntax | SENSe<cnum>:SWITch:M9165:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
Default | 1 or ON  
  
* * *

## SENSe<cnum>:SWITch:M9165:MODule<mod>:RESet:IMMediate

Applicable Models: All PXIe VNAs (Write Only) Resets the switches in the
specified module to "All Open" state immediately.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9165x. The number starts from 1 for the left most module of M9165x.  
Examples | SENS:SWIT:M9165:MOD1:RES:IMM sense:SWITch:M9165:module2:reset:immediate  
Query Syntax | Not applicable  
Return Type | Not applicable  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9165:MODules<mod>:SLOT?

Applicable Models: All PXIe VNAs (Read Only) Reads the slot number where the
specified M9165x is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of M9165x. The number starts from 1 for the left most module of M9165x.  
Examples | SENS:SWIT:M9165:MOD1:SLOT? sense:SWITch:M9165:module2:slot?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:M9165:MODules<mod>:SWITch<1-2>:PATH <char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the path for the
M9165x switch.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9165x. The number starts from 1 for the left most module of M9165x.  
<char> | Path. Choose from: STATe0 to STATe16 \- State 0 to 16  
Examples | SENS:SWIT:M9165:MOD1:SWIT:PATH STAT1 sense2:SWITch:M9165:module2:switch:path state4  
Query Syntax | SENSe<cnum>:SWITch:M9165:MODule<mod>:SWITch:PATH?  
Return Type | <enum>  
Default | STATe1 or STATe2  
  
* * *

## SENSe<cnum>:SWITch:M9165:MODules<mod>:MODel?

Applicable Models: All PXIe VNAs (Read Only) Returns the model number of
M9165x.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of M9165x. The number starts from 1 for the left most module of M9165x  
Examples | SENS:SWIT:M9165:MOD1:MOD? sense:SWITch:M9165:module2:model?  
Return Type |  string   
Default | Not applicable  
  
* * *

* * *

## SENSe<cnum>:SWITch:P9164:COUNt?

Applicable Models: All PXIe VNAs (Read-only) Returns the total number of
P9164x switch modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:SWIT:P9164:COUN?  
sense:switch:p9164:count  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:P9164:MODules<mod>:CHASsis?

Applicable Models: All PXIe VNAs (Read Only) Returns the chassis number where
the specified P9164x module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of P9164x. The number starts from 1 for the left most module of P9164x.  
Examples | SENS:SWIT:P9164:MOD1:CHAS? sense:SWITch:p9164:module2:chassis?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:P9164:MODules<mod>:CONTrol[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the status of
P9164x control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of P9164x. The number starts from 1 for the left most module of P9164x.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the P9164x at the specified channel. 1 or ON \- Enables to control the P9164x at the specified channel.  
Examples | SENS:SWIT:P9164:MOD1:CONT ON sense2:SWITch:p9164:module2:control 0  
Query Syntax | SENSe<cnum>:SWITch:P9164:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
Default | 1 or ON  
  
* * *

## SENSe<cnum>:SWITch:P9164:MODules<mod>:SLOT?

Applicable Models: All PXIe VNAs (Read Only) Reads the slot number where the
specified P9164x is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of P9164x. The number starts from 1 for the left most module of P9164x.  
Examples | SENS:SWIT:P9164:MOD1:SLOT? sense:SWITch:p9164:module2:slot?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:P9164:MODules<mod>:SWITch<1-2>:PATH <char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the path for the
P9164x switch.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of P9164x. The number starts from 1 for the left most module of P9164x.  
<char> | Path. Choose from: STATe0 to STATe16 \- State 0 to 16  
Examples | SENS:SWIT:P9164:MOD1:SWIT:PATH STAT1 sense2:SWITch:p9164:module2:switch:path state4  
Query Syntax | SENSe<cnum>:SWITch:P9164:MODule<mod>:SWITch:PATH?  
Return Type | <enum>  
Default | STATe1 or STATe2  
  
* * *

## SENSe<cnum>:SWITch:P9164:MODules<mod>:MODel?

Applicable Models: All PXIe VNAs (Read Only) Returns the model number of
P9164x.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of P9164x. The number starts from 1 for the left most module of P9164x  
Examples | SENS:SWIT:P9164:MOD1:MOD? sense:SWITch:p9164:module2:model?  
Return Type |  string   
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:P9165:COUNt?

Applicable Models: All PXIe VNAs (Read-only) Returns the total number of
P9165x switch modules that are connected to the VNA firmware.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
Examples | SENS:SWIT:P9165:COUN?  
sense:switch:p9165:count  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:P9165:MODules<mod>:CHASsis?

Applicable Models: All PXIe VNAs (Read Only) Returns the chassis number where
the specified P9165x module is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of P9165x. The number starts from 1 for the left most module ofP9165x.  
Examples | SENS:SWIT:P9165:MOD1:CHAS? sense:SWITch:p9165:module2:chassis?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:P9165:MODules<mod>:CONTrol[:STATe] <bool>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the status of
P9165x control.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of P9165x. The number starts from 1 for the left most module of P9165x.  
<bool> | Module control state. Choose from: O or OFF \- Skips to control the P9165x at the specified channel. 1 or ON \- Enables to control the P9165x at the specified channel.  
Examples | SENS:SWIT:P9165:MOD1:CONT ON sense2:SWITch:p9165:module2:control 0  
Query Syntax | SENSe<cnum>:SWITch:P9165:MODule<mod>:CONTrol[:STATe]?  
Return Type | Boolean  
Default | 1 or ON  
  
* * *

## SENSe<cnum>:SWITch:P9165:MODules<mod>:SLOT?

Applicable Models: All PXIe VNAs (Read Only) Reads the slot number where the
specifiedP9165x is located.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1. This command is common for all channels and the setting is ignored.  
<mod> | Module number of P9165x. The number starts from 1 for the left most module of P9165x.  
Examples | SENS:SWIT:P9165:MOD1:SLOT? sense:SWITch:p9165:module2:slot?  
Return Type | Numeric  
Default | Not applicable  
  
* * *

## SENSe<cnum>:SWITch:P9165:MODules<mod>:SWITch<1-2>:PATH <char>

Applicable Models: All PXIe VNAs (Read-Write) Sets and reads the path for the
P9165x switch.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of P9165x. The number starts from 1 for the left most module of P9165x.  
<char> | Path. Choose from: STATe0 to STATe16 \- State 0 to 16  
Examples | SENS:SWIT:P9165:MOD1:SWIT:PATH STAT1 sense2:SWITch:p9165:module2:switch:path state4  
Query Syntax | SENSe<cnum>:SWITch:P9165:MODule<mod>:SWITch:PATH?  
Return Type | <enum>  
Default | STATe1 or STATe2  
  
* * *

## SENSe<cnum>:SWITch:P9165:MODules<mod>:MODel?

Applicable Models: All PXIe VNAs (Read Only) Returns the model number of
P9165x.  
---  
Parameters |   
<cnum> | Any existing channel number; if unspecified, value is set to 1.  
<mod> | Module number of P9165x. The number starts from 1 for the left most module of P9165x  
Examples | SENS:SWIT:P9165:MOD1:MOD? sense:SWITch:p9165:module2:model?  
Return Type |  string   
Default | Not applicable


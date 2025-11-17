# Automatic Fixture Removal (AFR)

* * *

These commands are used to control the Automatic Fixture Removal (AFR)
capabilities in the VNA.

AFR: ADVanced: | AUTO | ITERate | METHod | CHECk | [:STATe] | REFZ | SET | [:STATe] **| DUTGate** | COEFficient | DOMAin | ILFitting | MANual | [:STATe] | MANual | [:STATe] | REFLection | MANual | [:STATe] | FIXTure | IMPedance | FTUNe | [:STATe] | MCONversion | [:STATe] | REFLection | GATing | MODE | CUSTom | POSition | MINimum | NVALue | SPIKe | TOLerance | ILFitting | HIGH | MCENter | MSPan | STARt | STOP | LOW | MCENter | MSPan | STARt | STOP | RESet | TIME | STARt | STOP | VERSion? FIXTure: | ADVanced | MCONversion | [:STATe] | RESet | TIME | STARt | STOP | WINDow | COEFficient | MANual | [:STATe] | BLIMited[:STATe] | CDUT[:STATe] | CLENgth[:STATe] | CMATch[:STATe] | INPuts | MEASurement | PREView | DATA | [:IMPedance]? | MARKer:Y? | REFZ | SET | SYSZ | [:STATe] | USE | THRUs | [:STATe] INITialize SAVE: | FILename | IMPedance | NORMalize | [:STATe] | PORTs | TYPE STANdard: | ALLOpen[:STATe] | ALLShort[:STATe] | DATA | [:IMPedance]? | MARKer:Y? | EDIT: | FLENgth | GATE | IMPedance: | METHod | LOAD | MEASure | THRU | USE  
---  
  
Click on a keyword to view the command details.

See Also

  * [Example Programs](../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## AFR:ADVanced:AUTO:ITERate:METHod:CHECk[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) Turns on or off the option "Automatically iterate when Impedance
Method Auto is checked.".  
---  
Parameters |   
<bool> |  Choose from: **ON or 1** \- Turns the option on.  **OFF or 0** \- Turns the option off.  
Examples |  AFR:ADVanced:AUTO:ITERate:METHod:CHECk OFF  
Query Syntax |  AFR:ADVanced:AUTO:ITERate:METHod:CHECk:STATe?  
Return Type |  Boolean  
Default |  On or 1  
  
* * *

## AFR:ADVanced:AUTO:ITERate:REFZ:SET[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) Turns on or off the option "Automatically iterate when
Calibration Reference Z0 is set to System Z0 or custom value."  
---  
Parameters |   
<bool> |  Choose from: **ON or 1** \- Turns the option on.  **OFF or 0** \- Turns the option off.  
Examples |  AFR:ADVanced:AUTO:ITERate:REFZ:SET OFF  
Query Syntax |  AFR:ADVanced:AUTO:ITERate:REFZ:SET:STATe?  
Return Type |  Boolean  
Default |  On or 1  
  
* * *

## AFR:ADVanced:DUTGate:COEFficient <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) Gets or sets the DUT gate coefficient.  
---  
Parameters |   
<numl> |  Coefficient  
Examples |  AFR:ADVanced:DUTGate:COEFficient 3.6  
Query Syntax |  AFR:ADVanced:DUTGate:COEFficient?  
Return Type |  String  
Default |  3.6  
  
* * *

## AFR:ADVanced:DUTGate:DOMain <char>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) Sets or gets the description of the AFR DUT Gate Domain (single-
ended or differential).  
---  
Parameters |   
<char> |  Choose from: **SENDed** **DIFFerential**  
Examples |  AFR:ADVanced:DUTGate:DOMain SENDed  
Query Syntax |  AFR:ADVanced:DUTGate:DOMain?  
Return Type |  String  
Default |  SEND  
  
* * *

## AFR:ADVanced:DUTGate:ILFitting:MANual[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) Turns ON or OFF the Fitting Thru after AFR DUT Gate.  
---  
Parameters |   
<bool> |  Choose from: ******ON (or 1)** \- Turns AFR DUT Gate Fitting loss channel on.  **OFF (or 0)** \- Turns AFR DUT Gate Fitting loss channel off.  
Examples |  AFR:ADVanced:DUTGate:ILFitting:MANual ON  
Query Syntax |  AFR:ADVanced:DUTGate:ILFitting:MANual:STATe?  
Return Type |  Boolean  
Default |  OFF or 0  
  
* * *

## AFR:ADVanced:DUTGate:MANual[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) Turns ON or OFF AFR DUTGate  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) - Turns AFR DUTGate on. OFF (or 0) \- Turns AFR DUTGate off.  
Examples |  AFR:ADVanced:DUTGate:MANual ON  
Query Syntax |  AFR:ADVanced:DUTGate:MANual?  
Return Type |  Boolean  
Default |  OFF or 0  
  
* * *

## AFR:ADVanced:DUTGate:REFLection:MANual[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) Turns ON or OFF AFR DUTGate Only Reflection Option  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) - Turns AFR DUTGate Only Reflection on. OFF (or 0) \- Turns AFR DUTGate Only Reflection off.  
Examples |  AFR:ADVanced:DUTGate:REFLection:MANual ON  
Query Syntax |  AFR:ADVanced:DUTGate:REFLection:MANual?  
Return Type |  Boolean  
Default |  ON or 1  
  
* * *

## AFR:ADVanced:FIXTure:IMPedance:FTUNe[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) Applies advanced algorithm to fixture impedance mismatching cases
for better results.  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) - Applies advanced algorithm. OFF (or 0) -  Turns off advanced algorithm.  
Examples |  AFR:ADVanced:FIXT:IMP:FTUN ON  
Query Syntax |  AFR:ADVanced:FIXTure:IMPedance:FTUNe?  
Return Type |  Boolean  
Default |  OFF or 0  
  
* * *

## AFR:ADVanced:MCONversion[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command turns ON or OFF AFR mode conversion.  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) \- Turns mode conversion on. OFF (or 0) \- Turns mode conversion off.  
Examples |  AFR:ADVanced:MCONversion ON  
Query Syntax |  AFR:ADVanced:MCONversion[:STATe]?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## AFR:ADVanced:REFLection:GATing:MODE <char>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command sets or reads the gating mode in 1-port
characterization.  
---  
Parameters |   
<char> |  Choose from: NORMal  MINimum  CUSTom  
Examples |  AFR:ADVanced:REFLection:GATing:MODE NORMal  
Query Syntax |  AFR:ADVanced:REFLection:GATing:MODE?  
Return Type |  String  
Default |  MINimum  
  
* * *

##

## AFR:ADVanced:REFLection:GATing:MODE:CUSTom:POSition<pnum> <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the position parameter in 1-port
characterization.  
---  
Parameters |   
<pnum> |  The position number. Choose from 1 or 2.  
<num> |  The position parameter value in ns.  
Examples |  AFR:ADVanced:REFLection:GATing:MODE:CUSTom:POSition2 1.0  
Query Syntax |  AFR:ADVanced::REFLection:GATing:MODE:CUSTom:POSition2?  
Return Type |  Numeric  
Default |  -1  
  
* * *

## AFR:ADVanced:REFLection:GATing:MODE:MINimum:NVALue <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the N parameter in 1-port
characterization.  
---  
Parameters |   
<num> |  The N parameter value.  
Examples |  AFR:ADVanced:REFLection:GATing:MODE:MINimum:NVALue 4  
Query Syntax |  AFR:ADVanced:REFLection:GATing:MODE:MINimum:NVALue?  
Return Type |  Numeric  
Default |  4  
  
* * *

##

## AFR:ADVanced:REFLection:GATing:SPIKe:TOLerance <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the spike tolerance parameter in 1-port
characterization.  
---  
Parameters |   
<num> |  The spike tolerance parameter value.  
Examples |  AFR:ADVanced:REFLection:GATing:SPIKe:TOLerance 3  
Query Syntax |  AFR:ADVanced:REFLection:GATing:SPIKe:TOLerance?  
Return Type |  Numeric  
Default |  3  
  
* * *

##

## AFR:ADVanced:REFLection:ILFitting:HIGH:MCENter <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the ratio of the merge center for IL
fitting at high frequency range 1-port characterization.  
---  
Parameters |   
<num> |  The ratio of the merge center.  
Examples |  AFR:ADVanced:REFLection:ILFitting:HIGH:MCENter 0.85  
Query Syntax |  AFR:ADVanced:REFLection:ILFitting:HIGH:MCENter?  
Return Type |  Numeric  
Default |  0.85  
  
* * *

##

## AFR:ADVanced:REFLection:ILFitting:HIGH:MSPan <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the ratio of the merge span for IL
fitting at high frequency range 1-port characterization.  
---  
Parameters |   
<num> |  The ratio of the merge span.  
Examples |  AFR:ADVanced:REFLection:ILFitting:HIGH:MSPan 0.1  
Query Syntax |  AFR:ADVanced:REFLection:ILFitting:HIGH:MSPan?  
Return Type |  Numeric  
Default |  0.1  
  
* * *

##

## AFR:ADVanced:REFLection:ILFitting:HIGH:STARt <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the start ratio for IL fitting at high
frequency range 1-port characterization.  
---  
Parameters |   
<num> |  The start ratio value.  
Examples |  AFR:ADVanced:REFLection:ILFitting:HIGH:STARt 0.7  
Query Syntax |  AFR:ADVanced:REFLection:ILFitting:HIGH:STARt?  
Return Type |  Numeric  
Default |  0.7  
  
* * *

##

## AFR:ADVanced:REFLection:ILFitting:HIGH:STOP <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the stop ratio for IL fitting at high
frequency range 1-port characterization.  
---  
Parameters |   
<num> |  The stop ratio value.  
Examples |  AFR:ADVanced:REFLection:ILFitting:HIGH:STOP 0.9  
Query Syntax |  AFR:ADVanced:REFLection:ILFitting:HIGH:STOP?  
Return Type |  Numeric  
Default |  0.9  
  
* * *

##

## AFR:ADVanced:REFLection:ILFitting:LOW:MCENter <num

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the ratio of the merge center for IL
fitting at low frequency range 1-port characterization.  
---  
Parameters |   
<num> |  The ratio of the merge center.  
Examples |  AFR:ADVanced:REFLection:ILFitting:LOW:MCENter 0.1  
Query Syntax |  AFR:ADVanced:REFLection:ILFitting:LOW:MCENter?  
Return Type |  Numeric  
Default |  0.1  
  
* * *

## AFR:ADVanced:REFLection:ILFitting:LOW:MSPan <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the ratio of the merge span for IL
fitting at low frequency range 1-port characterization.  
---  
Parameters |   
<num> |  The ratio of the merge span.  
Examples |  AFR:ADVanced:REFLection:ILFitting:LOW:MSPan 0.1  
Query Syntax |  AFR:ADVanced:REFLection:ILFitting:LOW:MSPan?  
Return Type |  Numeric  
Default |  0.1  
  
* * *

## AFR:ADVanced:REFLection:ILFitting:LOW:STARt <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the start ratio for IL fitting at low
frequency range 1-port characterization.  
---  
Parameters |   
<num> |  The start ratio value.  
Examples |  AFR:ADVanced:REFLection:ILFitting:LOW:STARt 0.0  
Query Syntax |  AFR:ADVanced:REFLection:ILFitting:LOW:STARt?  
Return Type |  Numeric  
Default |  0.0  
  
* * *

##

## AFR:ADVanced:REFLection:ILFitting:LOW:STOP <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the stop ratio for IL fitting at low
frequency range 1-port characterization.  
---  
Parameters |   
<num> |  The stop ratio value.  
Examples |  AFR:ADVanced:REFLection:ILFitting:LOW:STOP 0.25  
Query Syntax |  AFR:ADVanced:REFLection:ILFitting:LOW:STOP?  
Return Type |  Numeric  
Default |  0.25  
  
* * *

##

## AFR:ADVanced:RESet

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Write-only) This command resets the AFR configuration.  
---  
Parameters |  None  
Examples |  AFR:ADVanced:RESet5  
Query Syntax |  Not Applicable  
Default |  Not Applicable  
  
* * *

## AFR:ADVanced:TIME:STARt <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the manual start time in the AFR
configuration.  
---  
Parameters |   
<num> |  Start time in ns.  
Examples |  AFR:ADVanced:TIME:STARt -0.2  
Query Syntax |  :AFR:ADVanced:TIME:STARt?  
Return Type |  Numeric  
Default |  -0.2  
  
* * *

## AFR:ADVanced:TIME:STOP <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the manual stop time in the AFR
configuration.  
---  
Parameters |   
<num> |  Stop time in ns.  
Examples |  AFR:ADVanced:TIME:STOP 5.0  
Query Syntax |  :AFR:ADVanced:TIME:STOP?  
Return Type |  Numeric  
Default |  5  
  
* * *

## AFR:ADVanced:VERSion?

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-only) Gets the AFR Version.  
---  
Parameters |  Not Applicable  
Examples |  AFR:ADVanced:VERSion?  
Return Type |  String  
Default |  Not Applicable  
  
* * *

## AFR:ADVanced:WINDow:COEFficient <char>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command gets or sets the manual window type in AFR
configuration.  
---  
Parameters |   
<char> |  Window coefficient. Choose from: MAXWin WIDWin NORMWin MINWin  
Examples |  AFR:ADVanced:WINDow:COEFficient WIDWin  
Query Syntax |  AFR:ADVanced:WINDow:COEFficient?  
Return Type |  String  
Default |  NORMWin  
  
* * *

## AFR:ADVanced:WINDow:MANual[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command turns ON of OFF the manual window coefficient of the
AFR.  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) \- Turns manual window coefficient on. OFF (or 0) \- Turns manual window coefficient off.  
Examples |  AFR:ADVanced:MANual:STATe ON  
Query Syntax |  AFR:ADVanced:WINDow:MANual[:STATe]?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## AFR:FIXTure:BLIMited[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command selects whether the fixture is band limited or not.  
---  
Parameters |   
<bool> |  Band limited or not. Choose from: ON (or 1) \- Band limited. OFF (or 0) \- Not band limited.  
Examples |  AFR:FIXTure:BLIMited ON  
Query Syntax |  AFR:FIXTure:BLIMited?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## AFR:FIXTure:CDUT[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command selects whether to use DUT correction or not when
the characterization fixture is not equal to the DUT measurement fixture.  
---  
Parameters |   
<bool> |  DUT correction state. Choose from: ON (or 1) \- Use DUT correction. OFF (or 0) \- Do not use DUT correction.  
Examples |  AFR:FIXTure:CDUT ON  
Query Syntax |  AFR:FIXTure:CDUT?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## AFR:FIXTure:CLENgth[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command selects Fixture Length A not equal to B correction.  
---  
Parameters |   
<bool> |  Correction match state. Choose from: ON (or 1) \- Correct. OFF (or 0) \- Do not correct.  
Examples |  AFR:FIXTure:CLENgth ON  
Query Syntax |  AFR:FIXTure:CLENgth?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## AFR:FIXTure:CMATch[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command selects Fixture Match A not equal to B correction.  
---  
Parameters | 

#  
  
<bool> |  Correction match state. Choose from: ON (or 1) \- Correct. OFF (or 0) \- Do not correct.  
Examples |  AFR:FIXTure:CMATch ON  
Query Syntax |  AFR:FIXTure:CMATch?  
Return Type |  Boolean  
Default |  ON  
  
* * *

##

## AFR:FIXTure:INPuts <char>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command describes the fixture inputs (single ended or
differential).  
---  
Parameters |   
<char> |  Choose from: SENDed \- Single ended fixture inputs. DIFFerential \- Differential fixture inputs.  
Examples |  AFR:FIXTure:INPuts SENDed  
Query Syntax |  AFR:FIXTure:INPuts?  
Return Type |  String  
Default |  SENDed  
  
* * *

## AFR:FIXTure:MEASurement <num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command selects the number of fixtures to be characterized.  
---  
Parameters |   
<num> |  Choose from 1, 2, or 4.  
Examples |  AFR:FIXTure:MEASurement 2  
Query Syntax |  AFR:FIXTure:MEASurement?  
Return Type |  Numeric  
Default |  2  
  
* * *

## AFR:FIXTure:PREView

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Write-only) This command refreshes preview data. It is required that this
command be sent before a query gate, fixture length, and impedance data.  
---  
Parameters |  None  
Examples |  AFR:STANdard:EDIT:GATE AFIX,0.485  
AFR:FIXTure:PREView  
AFR:STANdard:EDIT:GATE? AFIX  
Query Syntax |  Not Applicable  
Default |  Not Applicable  
  
* * *

## AFR:FIXTure:PREView:DATA[:IMPedance]? <char_param>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-only) This command reads the impedance profile of the calculated fixture
model.  
---  
Parameters |   
<char_param> |  Selected impedance term. Choose from: ASENded \- Single-Ended ZA BSENded \- Single-Ended ZB ADIFf \- Differential ZA BDIFf \- Differential ZB ACOMm \- Common mode ZA BCOMm \- Common mode ZB  
Examples |  AFR:FIXTure:PREView:DATA:IMPedance? ADIF  
Return Type |  Block Data  
Default |  Not Applicable  
  
* * *

## AFR:FIXTure:PREView:DATA[:IMPedance]:MARKer:Y? <char_param>,<num_x>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-only) This command reads the impedance profile of the calculated fixture
model at a specified position.  
---  
Parameters |   
<char_param> |  Selected impedance term. Choose from: ASENded \- Single-Ended ZA BSENded \- Single-Ended ZB ADIFf \- Differential ZA BDIFf \- Differential ZB ACOMm \- Common mode ZA BCOMm \- Common mode ZB  
<num_x> |  The X-axis position (ns), where the Y-axis value will be returned.  
Examples |  AFR:FIXTure:PREView:DATA:IMPedance:MARKer:Y? ADIF,0.5  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## AFR:FIXTure:REFZ <char>[,<num>]

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command chooses the calibration reference Z0 after fixture
removal.  
---  
Parameters |   
<char> |  Choose from: SYSZ\- System Z0. MEAZ \- Measured fixture Z0. CUSTom \- User input.  
<num> |  Optional argument. If <char> is set to CUST, this is the user input vale for Z0.  
Examples |  AFR:FIXTure:REFZ SYSZ AFR:FIXTure:REFZ CUST,52.0  
Query Syntax |  AFR:FIXTure:REFZ?  
Return Type |  String (SYSZ, MEAZ, or CUST)  
Default |  SYSZ  
  
* * *

## AFR:FIXTure:SET:SYSZ[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command sets "System Z0" to Calibration Reference Z0.  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) \- Sets "System Z0" to Calibration Reference Z0. OFF (or 0) \- Do not set "System Z0" to Calibration Reference Z0.  
Examples |  AFR:FIXTure:SET:SYSZ ON  
Query Syntax |  AFR:FIXTure:SET:SYSZ[:STATe]?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## AFR:FIXTure:USE:THRUs[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command specifies whether thrus are used in case of multi-
port fixtures.  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) \- Use thrus. OFF (or 0) \- Do not use thrus.  
Examples |  AFR:FIXTure:USE:THRUs ON  
Query Syntax |  AFR:FIXTure:USE:THRUs[:STATe]?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## AFR:INITialize

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Write-only) Restores the default AFR settings.  
---  
Parameters |  None  
Examples |  AFR:INIT  
Query Syntax |  Not Applicable  
Default |  Not Applicable  
  
* * *

## AFR:SAVE:FILename <string>[,<string>]

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command specifies the file paths of saved fixture data.  
---  
Parameters |   
<string> |  Fixture A path.  
<string> |  Fixture B path.  
Examples |  AFR:SAVE:FILename 'C:\fixA.s2p','C:\fixB.s2p'  
Query Syntax |  AFR:SAVE:FILename?  
Return Type |  String  
Default |  "C:\fixA.s2p,C:\fixB.s2p"  
  
* * *

## AFR:SAVE:IMPedance:NORMalize[:STATe]

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Write-only) This command specifies whether the port impedances are normalized
in saving the AFR fixture files.  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) \- Normalize the port impedances when they are not equal. OFF (or 0) \- Do not normalize the port impedances.  
Examples |  AFR:SAVE:IMPedance:NORMalize 1  
Return Type |  Not Applicable  
Default |  ON  
  
* * *

## AFR:SAVE:PORTs <char>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command assigns the ports for saved fixture data in several
formats.  
---  
Parameters |   
<char> |  Port assignment. Choose from: PLTS \- PLTS format. VNA \- VNA format. ADS \- ADS format.  
Examples |  AFR:SAVE:PORTs VNA  
Query Syntax |  AFR:SAVE:PORTs?  
Return Type |  String  
Default |  VNA  
  
* * *

## AFR:SAVE:TYPE <char>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command sets the file type to save fixture data.  
---  
Parameters |   
<char> |  Impedance method. Choose from: TSONe \- Touchstone file type. TSTWo \- Touchstone 2 file type. CITifile \- Citifile file type.  
Examples |  AFR:SAVE:TYPE TSONe  
Query Syntax |  AFR:SAVE:TYPE?  
Return Type |  String  
Default |  TSONe  
  
* * *

## AFR:STANdard:ALLOpen[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command selects all OPEN standards.  
---  
Parameters |   
<bool> |  Select all OPEN standards or not. Choose from: ON (or 1) \- Use all OPEN standards. OFF (or 0) \- Do not use all OPEN standards.  
Examples |  AFR:STANdard:ALLOpen ON  
Query Syntax |  AFR:STANdard:ALLOpen?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## AFR:STANdard:ALLShort[:STATe] <bool>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command selects all SHORT standards.  
---  
Parameters |   
<bool> |  Select all SHORT standards or not. Choose from: ON (or 1) \- Use all SHORT standards. OFF (or 0) \- Do not use all SHORT standards.  
Examples |  AFR:STANdard:ALLShort ON  
Query Syntax |  AFR:STANdard:ALLShort?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## AFR:STANdard:DATA[:IMPedance]? <char_std>,<char_param>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-only) This command reads the impedance profile of the measured standard.  
---  
Parameters |   
<char_std> |  Selected standard. Choose from: THRU \- 2X Thru STHRu \- Second 2X Thru FDUT \- Fixtured DUT AOPen \- Fixture A Open BOPen \- Fixture B Open ASHort \- Fixture A Short BSHort \- Fixture B Short  
<char_param> |  Selected impedance term. Choose from: ASENded \- Single-Ended ZA BSENded \- Single-Ended ZB ADIFf \- Differential ZA BDIFf \- Differential ZB ACOMm \- Common mode ZA BCOMm \- Common mode ZB  
Examples |  AFR:STANdard:DATA:IMPedance? AOP,ADIF  
Return Type |  Block Data  
Default |  Not Applicable  
  
* * *

## AFR:STANdard:DATA[:IMPedance]:MARKer:Y? <char_std>,<char_param>,<num_x>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-only) This command reads the impedance of the measured standard at a
specified position.  
---  
Parameters |   
<char_std> |  Selected standard. Choose from: THRU \- 2X Thru STHRu \- Second 2X Thru FDUT \- Fixtured DUT AOPen \- Fixture A Open BOPen \- Fixture B Open ASHort \- Fixture A Short BSHort \- Fixture B Short  
<char_param> |  Selected impedance term. Choose from: ASENded \- Single-Ended ZA BSENded \- Single-Ended ZB ADIFf \- Differential ZA BDIFf \- Differential ZB ACOMm \- Common mode ZA BCOMm \- Common mode ZB  
<num_x> |  The X-axis position (ns), where the Y-axis value will be returned.  
Examples |  AFR:STANdard:DATA:IMPedance:MARKer:Y? AOP,ADIF,0.5  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## AFR:STANdard:EDIT:FLENgth <char>,<num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) For the selected fixture, this command reads the fixture length
for both 1X or 2X AFR, or sets the fixture length for 1X AFR.  Note: After
setting fixture length to a new value, the preview command must be sent to
apply the value.  
---  
Parameters |   
<char> |  Selected fixture. Choose from: AFIXture \- Fixture A. BFIXture \- Fixture B.  
<num> |  Fixture length value. Unit is ns.  
Examples |  AFR:STANdard:EDIT:FLENgth AFIX,0.3273  
AFR:FIXTure:PREView  
Query Syntax |  AFR:STANdard:EDIT:FLENgth? AFIX  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## AFR:STANdard:EDIT:GATE <char>,<num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command sets or reads the gate position for the selected
fixture.  Note: After setting a new gate position, the preview command must be
sent to apply the new position.  
---  
Parameters |   
<char> |  Selected fixture. Choose from: AFIXture \- Fixture A. BFIXture \- Fixture B.  
<num> |  Gate position value. Unit is ns.  
Examples |  AFR:STANdard:EDIT:GATE AFIX,0.485  
AFR:FIXTure:PREView  
Query Syntax |  AFR:STANdard:EDIT:GATE? AFIX  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## AFR:STANdard:EDIT:IMPedance <char>,<num>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Write-only) This command sets the impedance for the selected term.  
---  
Parameters |   
<char> |  Impedance term. Choose from: ASENded \- Single-Ended ZA. BSENded \- Single-Ended ZB. ADIFf \- Differential ZA. BDIFf \- Differential ZB. ACOMm \- Common mode ZA. BCOMm \- Common mode ZB.  
<num> |  Impedance value. Unit is Ohms.  
Examples |  AFR:STANdard:EDIT:IMPedance ASEN,52.5  
Default |  ASENded, 50  
  
* * *

## AFR:STANdard:EDIT:IMPedance:METHod <char>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command sets the impedance method.  
---  
Parameters |   
<char> |  Impedance method. Choose from: DEFault AUTO USER  
Examples |  AFR:STANdard:EDIT:IMPedance:METHod AUTO  
Query Syntax |  AFR:STANdard:EDIT:IMPedance:METHod?  
Return Type |  Character  
Default |  DEFault  
  
* * *

## AFR:STANdard:LOAD <char>,<string>

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command loads the calibration standards data from a file.  
---  
Parameters |   
<char> |  Standards type. Choose from: THRU\- 2X Thru. STHRu \- Second 2X Thru. FDUT \- Fixtured DUT. AOPen \- Fixture A Open. BOPen \- Fixture B Open. ASHort \- Fixture A Short. BSHort \- Fixture B Short.  
<string> |  File path of existing measurement data (touchstone 1.0, touchstone 2.0, or citifile).  
Examples |  AFR:STANdard:LOAD AOPen,'C:\open.s1p'  
Query Syntax |  AFR:STANdard:LOAD? AOPen  
Return Type |  String  
Default |  Not Applicable  
  
* * *

## AFR:STANdard:MEASure <char>[,<p1>][,<p2>][,<p3>][,<p4>]

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Write-only) This command measures the calibration standards.  
---  
Parameters |   
<char> |  Standards type. Choose from: THRU- 2X Thru. STHRu - Second 2X Thru. FDUT \- Fixtured DUT. AOPen \- Fixture A Open. BOPen \- Fixture B Open. ASHort \- Fixture A Short. BSHort \- Fixture B Short. <p1> \- Mapped PNA Port 1. Optional parameter. <p2> \- Mapped PNA Port 2. Optional parameter. <p3> \- Mapped PNA Port 3. Optional parameter. <p4> \- Mapped PNA Port 4. Optional parameter.  
Examples |  AFR:STANdard:MEASure AOPen  
Default |  Not Applicable  
  
* * *

## AFR:STANdard:THRU <char>[,<num>]

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command specifies fixture thru settings.  
---  
Parameters |   
<char> |  Thru type. Choose from: KNOWn \- Known thru, flush thru, or user input length. UNKNown \- Unknown thru length computed using reflects.  
<num> |  User input thru length. Default is 0.  
Examples |  AFR:STANdard:THRU KNOW,0  
Query Syntax |  AFR:STANdard:THRU?  
Return Type |  String  
Default |  "KNOW,0"  
  
* * *

## AFR:STANdard:USE <char>[,<bool>]

Applicable Models: All with Automatic Fixture Removal Option (S9x007A/B, 007)
(Read-Write) This command chooses the calibration standards.  
---  
Parameters |   
<char> |  Choose from: THRU\- 2X Thru. STHRu \- Second 2X Thru. FDUT \- Fixtured DUT. AOPen \- Fixture A Open. BOPen \- Fixture B Open. ASHort \- Fixture A Short. BSHort \- Fixture B Short.  
<bool> |  Use calibration standards or not. Choose from: ON (or 1) \- Use calibration standards. OFF (or 0) \- Do not use calibration standards.  
Examples |  AFR:STANdard:USE AOPen,ON  
Query Syntax |  AFR:STANdard:USE?  
Return Type |  String of used standards, separated by commas. For example, use AOPen and BOPen returns: "AOPen,BOPen"  
Default |  'THRU' \- ON


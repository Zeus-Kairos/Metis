# SYSTem:UNCertainty

* * *

Contains the settings to create and control Dynamic Uncertainty for
S-Parameters (Opt. S93015A/B).

Setup Options  
---  
![](../../assets/images/UncertOpts.gif) | [SYST:UNC:ETER:NOIS:ENAB](SystUncertainty.md#EtermNoiseEnable)  
[SYST:UNC:ETER:CABL:REP](SystUncertainty.md#EtermCableRepeatEnab)  
[SYST:UNC:ETER:SDEF](SystUncertainty.md#EtermSdef)  
[SYST:UNC:POIN:MAX](SystUncertainty.md#PointsMAX)  
Noise Characterization  
---  
Clear noise data on specified port | [SYST:UNC:PORT<p>:NOISe:RESet](SystUncertainty.md#NOISeRESet)  
Clear noise data on all ports | [SYST:UNC:PORT:NOISe:RESet](SystUncertainty.md#NOISeRESet)  
Copy noise from a port to all ports | [SYST:UNC:PORT:NOISe:ALL:COPY](SystUncertainty.md#NoiseAllCopy)  
Start Noise char | [SENS:CORR:COLL:GUIDed:UNC:CHAR:NOISe](Sense/CorrGuided.md#UncertNoiseInit)  
Cables Characterization  
---  
List cables | [SYST:UNC:CABLe:CATalog?](SystUncertainty.md#CABLeCAT)  
Assign Cable to all ports | [SYST:UNC:PORT:CABLe:ALL](SystUncertainty.md#CABLeSelALL)  
Assign Cable to specified port | [SYST:UNC:PORT<p>:CABLe](SystUncertainty.md#CABLeSELect)  
Reset repeatability | [SYST:UNC:CABL:REP:RES](SystUncertainty.md#CABLeRESet)  
Start Cable char | [SENS:CORR:COLL:GUIDed:UNC:CHAR:CABLe](Sense/CorrGuided.md#UncertCableINIT)  
Uncertainty workspace  
---  
Load workspace | [SYST:UNC:LOAD](SystUncertainty.md#LOAD)  
Save workspace | [SYST:UNC:STORe](SystUncertainty.md#STORe)  
Enable a Guided Cal to include Uncertainties  
---  
Checkbox on [Guided Cal Select Ports](../../S3_Cals/Calibration_Wizard.md#GuidedSelCalType) page | [SENS:CORR:COLL:GUID:UNC](Sense/CorrGuided.md#UncertEnab)  
Trace Properties  
---  
![](../../assets/images/UncertTracePropDiag.gif) | [CALC:MEAS:UNC:DISP:TYPE](Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:DISPlay:TYPE)  
[CALC:MEAS:UNC:DISP:CFAC](Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:DISPlay:CFACtor)  
[CALC:MEAS:UNC:MOD:NOIS](Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:NOISe)  
[CALC:MEAS:UNC:MODE:CABL:REP](Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:CABLe:REPeat)  
[CALC:MEAS:UNC:MOD:ETER](Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:MODE:ETERm)  
Apply to all traces | None  
Add Trace | None  
Save uncertainty data | [CALC:MEAS:UNC:SAVE](Calculate/MeasureUncertainty.md#CALCulate:MEASure:UNCertainty:SAVE)  
  
####

#### Limitations

  * Calibrations can be performed for ONLY ONE channel at a time.

  * Putting Error Term data into Uncertainty Cal Sets using [remote commands](../DataTopic.md#putCalData) is NOT supported.

### See Also

  * [Trace Commands for Dynamic Uncertainty](Calculate/Uncertainty.md)

  * [Learn more about Dynamic Uncertainty](../../S3_Cals/Dynamic_Uncertainty.md)

  * [Example Program](../GPIB_Example_Programs/Dynamic_Uncertainty.md)

  * [Guided Cal commands](Sense/CorrGuided.md)

  * [Synchronizing the Analyzer and Controller](../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:UNCertainty:CABLe:CATalog?

Applicable Models: N522xB, N523xB, N524xB, M983xA (Read-only) Returns a comma-
delimited list of names of cables that are defined in the Uncertainty Manager
application.  
---  
Parameters | None  
Examples | SYST:UNC:CABL:CAT?  
Return Type | Comma-delimited string  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:UNCertainty:CABLe:REPeat:RESet <cableName>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-only) Resets (clears)
the characterized repeatability data associated with the specified cable.  
---  
Parameters |   
<cableName> | String. Name of the cable for which data is to be reset.  
Examples | SYST:UNC:CABL:REP:RES "MyCable"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:UNCertainty:PORT:CABLe:ALL[:SELect] <cableName>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-only) Sets the name
of the cable to be associated with all the ports currently enabled on the VNA  
---  
Parameters |   
<cableName> | String. Name of the cable.  
Examples | SYST:UNC:PORT:CABL:ALL "MyCable"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
## SYSTem:UNCertainty:PORT<pNum>:CABLe[:SELect] <cableName>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the name of the cable to be associated with the specified port number
on the VNA  
---  
Parameters |   
<pNum> | VNA port number.  
<cableName> | String. Name of the cable.  
Examples | SYST:UNC:PORT3:CABL "MyCable"  
Query Syntax | SYSTem:UNCertainty:PORT<pNum>:CABLe[:SELect]?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:UNCertainty:PORT:NOISe:ALL:COPY <pNum>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-only) Copies the
characterized noise data associated with the specified port, to all the other
ports  
---  
Parameters |   
<pNum> | VNA port number for which noise data will be copied.  
Examples | SYST:UNC:PORT:NOIS:ALL:COPY 2  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:UNCertainty:PORT:NOISe:ALL:RESet

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-only) Resets (clears)
the characterized noise data for all currently enabled VNA ports.  
---  
Parameters | None  
Examples | SYST:UNC:PORT:NOIS:ALL:RESet  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:UNCertainty:PORT<pNum>:NOISe:RESet

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-only) Resets (clears)
the characterized noise data for the specified VNA port.  
---  
Parameters | None  
<pNum> | VNA port number for which noise data will be reset.  
Examples | SYST:UNC:PORT2:NOIS:RESet  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:UNCertainty:LOAD <filename>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-only) Loads an
uncertainty workspace (*.ml4) file into the Uncertainty Manager.  
---  
Parameters | None  
<filename> | String. Full path, filename, and extension of the uncertainty workspace file, enclosed in quotes.  
Examples | SYST:UNC:LOAD "C:\MyUncert.ml4"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:UNCertainty:STORe [filename]

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-only) Saves the
current uncertainty workspace of the Uncertainty Manager to a (.ml4) file.  
---  
Parameters | None  
<filename> | String. Optional argument. Full path, filename, and extension of the uncertainty workspace file, enclosed in quotes.  If filename is not specified, the current workspace is saved to the default workspace (*.ml4) file.  
Examples | SYST:UNC:STORe "C:\MyUncert.ml4"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SYSTem:UNCertainty:POINts:MAXimum <num>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the maximum number of points (decimation value) for which
uncertainties are to be computed for subsequent calibrations that are
performed using Dynamic Uncertainty for S-Parameters.  
---  
Parameters |   
<num> | Max number of points. Specify an integer between 0 and 501.  
Examples | SYST:UNC:POIN:MAX 201  
Query Syntax | SYSTem:UNCertainty:POINts:MAXimum?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 500  
  
* * *

## SYSTem:UNCertainty:ETERm:NOISe:ENABle <bool>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the ON/OFF state of allowing noise data to contribute to the
uncertainty of a calibration performed using Dynamic Uncertainty for
S-Parameters. Noise data must also be present for the ports at the time the
calibration is performed.  
---  
Parameters |   
<bool> | Enable ON/OFF state. Choose from: ON or 1 \- Noise uncertainty ON. OFF or 0 \- Noise uncertainty OFF.  
Examples | SYST:UNC:ETER:NOIS:ENAB ON  
Query Syntax | SYSTem:UNCertainty:ETERm:NOISe:ENABle?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SYSTem:UNCertainty:ETERm:CABLe:REPeat[:ENABle] <bool>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the ON/OFF state of allowing cable repeatability data to contribute to
the uncertainty of a calibration performed using Dynamic Uncertainty for
S-Parameters. Repeatability data must also be present for the ports at the
time the calibration is performed.  
---  
Parameters |   
<bool> | Enable ON/OFF state. Choose from: ON or 1 \- Cable repeatability uncertainty ON. OFF or 0 \- Cable repeatability uncertainty OFF.  
Examples | SYST:UNC:ETER:CABL:REP ON  
Query Syntax | SYSTem:UNCertainty:ETERm:CABLe:REPeat[:ENABle]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SYSTem:UNCertainty:ETERm:SDEFinitions[:ENABle] <bool>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the ON/OFF state of allowing the uncertainty associated with the
standard definitions in the cal kits to contribute to the uncertainty of a
calibration performed using Dynamic Uncertainty for S-Parameters. The
uncertainty data for the Cal standards must also be present at the time the
calibration is performed.  
---  
Parameters |   
<bool> | Enable ON/OFF state. Choose from: ON or 1 \- Standard definition uncertainty ON. OFF or 0 \- Standard definition uncertainty OFF.  
Examples | SYST:UNC:ETER:SDEF ON  
Query Syntax | SYSTem:UNCertainty:ETERm:SDEFinitions[:ENABle]?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *


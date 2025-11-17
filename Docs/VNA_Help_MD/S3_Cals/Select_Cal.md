# Select a Calibration Type

* * *

The following calibration types are available in the VNA.

Cal Type | Interface | Accuracy | [Thru Methods](Calibration_THRU_Methods.md) allowed  
---|---|---|---  
[TRL Family](Select_Cal.md#trl) | Basic Cal Cal All SmartCal ECal | Very High | All except Unknown Thru  
[SOLT](Select_Cal.md#SOLT) | Basic Cal Cal All SmartCal ECal | High | All  
SOLR | Basic Cal Cal All SmartCal ECal | High | Unknown Thru  
[Enhanced Response](Select_Cal.md#Enhanced) | Basic Cal SmartCal | High | Defined Thru or Flush Thru  
[QSOLT](Select_Cal.md#QSOLT) (Quick SOLT) | Basic Cal SmartCal | Medium | Defined Thru or Flush Thru  
[1-Port Reflection](Select_Cal.md#1port) | Basic Cal Cal All SmartCal ECal | High | Not Applicable  
[Open/Short](Select_Cal.md#openshort) Response | Basic Cal Response Cal | Low | Not Applicable  
[Thru](Select_Cal.md#thru) Response | Basic Cal Response Cal | Low | Known Thru or Flush Thru  
  
[Learn how to select a default Cal Type.](Calibration_Preferences.md#CalType)

### Other Cal Types (Separate Topic)

  * [Source and Receiver Power Cals](PwrCalibration.md)

[See other Calibration Topics](Calibration.md)

TRL Family  
---  
  
#### Application: Used to accurately calibrate any pair of ports when
calibration standards are not readily available.

Note: A [Delta Match Cal](Delta_Match_Calibration.md) may be required. 
[Learn more about TRL family cal](TRL_Calibration.md)  For more information
on modifying standards, see [Calibration Standards](ModifyCalKits.md).  
  
#### Calibration Method: [Basic
Cal](Calibration_Wizard.htm#Basic_Cal_dialogbox),
[SmartCal](Calibration_Wizard.md#Calibration_Wiz_help), [Cal
All](Calibrate_All_Channels.htm)  
  
#### General Accuracy: Very High  
  
#### Standards Required: THRU, REFLECT, LINE or similar combination  
  
#### Systematic Errors Corrected:

####  Directivity

####  Source match

####  Isolation ([see exceptions](Accurate.md#iso))

####  Load match

####  Frequency response transmission tracking

####  Frequency response reflection tracking  
  
SOLT  
---  
  
#### Application: Used to accurately calibrate any number of ports.  
  
#### General Accuracy: High  
  
#### Calibration Method: [Basic
Cal](Calibration_Wizard.htm#Basic_Cal_dialogbox),
[SmartCal](Calibration_Wizard.md#Calibration_Wiz_help), [Cal
All](Calibrate_All_Channels.htm), [ECal](Using_ECal.md)  
  
#### Standards Required: (SHORT, OPEN, LOAD, THRU) or ECal module  
  
#### Systematic Errors Corrected (on all ports):

####  Directivity

####  Source match

####  Isolation ([see exceptions](Accurate.md#iso))

####  Load match

####  Frequency response transmission tracking

####  Frequency response reflection tracking  
  
SOLR  
---  
  
#### Application: Used to accurately calibrate any two ports.  
  
#### General Accuracy: High  
  
#### Calibration Method: [Basic
Cal](Calibration_Wizard.htm#Basic_Cal_dialogbox),
[SmartCal](Calibration_Wizard.md#Calibration_Wiz_help), [Cal
All](Calibrate_All_Channels.htm), [ECal](Using_ECal.md)  
  
#### Standards Required: (SHORT, OPEN, LOAD, Reciprocal THRU) or ECal module  
  
#### Systematic Errors Corrected (on all ports):

####  Directivity

####  Source match

####  Isolation ([see exceptions](Accurate.md#iso))

####  Load match

####  Frequency response transmission tracking

####  Frequency response reflection tracking  
  
Enhanced Response  
---  
  
#### Application: Used to calibrate two ports when only measurements in one
direction (forward OR reverse) are required. Measurements are faster because a
second sweep is NOT required.

####  Reflection Standards (OPEN, SHORT, LOAD) are connected to the source
port to be calibrated.

 [Defined THRU](Calibration_THRU_Methods.md#Defined) or [Flush
THRU](Calibration_THRU_Methods.htm#Flush) standard is connected between port
pairs.

####  Much quicker than SOLT when using a mechanical cal kit. ECal can also
be used.

To select Enhanced Response: For a standard S-parameter Cal, select Cal > Main
> Basic Cal.... Then, In the Basic Cal dialog box:

  1. Under 'Cal Type', select Enh Response 1-> 2 Enh or Response 2-> 1.

  
  
#### General Accuracy: High  
  
#### Calibration Method: [Basic
Cal](Calibration_Wizard.htm#Basic_Cal_dialogbox),
[SmartCal](Calibration_Wizard.md#Calibration_Wiz_help),
[ECal](Using_ECal.md)  
  
#### Standards Required: (SHORT, OPEN, LOAD, [Defined
THRU](Calibration_THRU_Methods.htm#Defined) or [Flush
THRU](Calibration_THRU_Methods.htm#Flush))  
  
#### Systematic Errors Corrected:

####  Directivity (source port)

####  Source match (source port)

####  Isolation ([see exceptions](Accurate.md#iso))

####  Load match (receiver port) - used only to produce transmission tracking
term.

####  Frequency response transmission tracking (receiver port).

####  Frequency response reflection tracking (source port).  
  
QSOLT (Quick SOLT)  
---  
  
#### Application: Used to quickly calibrate any number of ports. Developed
specifically for use with [external multiport test
sets](../System/External_Testset_Control.htm).

Note: A [Delta Match Cal](Delta_Match_Calibration.md) is required to cal test
ports that do not have a dedicated reference receiver.

####  Reflection Standards (OPEN, SHORT, LOAD) are connected to only ONE of
the ports to be calibrated. The lower port number of the ports to be
calibrated is selected by default. This can be changed through the [Modify Cal
/ Cal Type](Calibration_Wizard.htm#ModifyCal) setting.

 [Defined THRU](Calibration_THRU_Methods.md#Defined) or [Flush
THRU](Calibration_THRU_Methods.htm#Flush) standards are connected from the
reflection standard port to the remaining ports to be calibrated.

####  Much quicker than SOLT when using a mechanical cal kit.

 Based on TRL math.  
  
#### General Accuracy: Not as high as SOLT  
  
#### Calibration Method: [Basic
Cal](Calibration_Wizard.htm#Basic_Cal_dialogbox),
[SmartCal](Calibration_Wizard.md#Calibration_Wiz_help),
[ECal](Using_ECal.md)  
  
#### Standards Required: (SHORT, OPEN, LOAD, [Defined
THRU](Calibration_THRU_Methods.htm#Defined) or [Flush
THRU](Calibration_THRU_Methods.htm#Flush))  
  
#### Systematic Errors Corrected:

####  Directivity

####  Source match

####  Isolation ([see exceptions](Accurate.md#iso))

####  Load match

####  Frequency response transmission tracking

####  Frequency response reflection tracking  
  
1-Port (Reflection)  
---  
  
#### Application: Used to accurately calibrate any single test port for
reflection measurements only.  
  
#### Calibration Method: [Basic
Cal](Calibration_Wizard.htm#Basic_Cal_dialogbox),
[SmartCal](Calibration_Wizard.md#Calibration_Wiz_help), [Cal
All](Calibrate_All_Channels.htm), [ECal](Using_ECal.md)  
  
#### General Accuracy: High  
  
#### Standards Required: (SHORT, OPEN, LOAD) or ECal module  
  
#### Systematic Errors Corrected:

####  Directivity

####  Source match

####  Frequency response reflection tracking  
  
Open / Short Response  
---  
  
#### Application: Used to quickly calibrate any single test port for
reflection measurements only.  
  
#### Calibration Method: [Basic
Cal](Calibration_Wizard.htm#Basic_Cal_dialogbox), [Response
Cal](Calibration_Wizard.htm#mechanical)  
  
#### General Accuracy: Low  
  
#### Standards Required: OPEN or SHORT  
  
#### Systematic Errors Corrected:

#### Frequency response reflection tracking  
  
Thru / Transmission Response (Isolation Optional)  
---  
  
#### Application: Used to quickly calibrate any pair of test ports for
transmission measurements only.

#### Isolation is not usually recommended. Learn more about
[Isolation](Accurate.md#iso)  
  
#### Calibration Method: [Basic
Cal](Calibration_Wizard.htm#Basic_Cal_dialogbox), [Response
Cal](Calibration_Wizard.htm#mechanical), and Guided Cal from the 'Select DUT
Connectors page', check [Modify Cal](Calibration_Wizard.md#ModifyCal), then
click Next.  
  
#### General Accuracy: Low  
  
#### Standards Required: THRU

Isolation: One LOAD for each VNA test port.  
  
#### Systematic Errors Corrected:

####  Frequency response transmission tracking

####  Isolation  
  
* * *


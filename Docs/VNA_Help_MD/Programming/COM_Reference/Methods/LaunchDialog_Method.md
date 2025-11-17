##### Write-only  
  
---  
  
## LaunchDialog Method

* * *

#### Description

|  Launches the specified dialog box. The Calibration Wizard dialog that
appears depends on the active channel. For example, if a Gain Compression
channel is active, then the GCA Cal Wizard appears. Use
[meas.Activate](Activate_Method.md) to activate a measurement and channel.
Remote operation returns after the dialog is dismissed. To invoke the Cal
Wizard and have it return immediately, then use [Syst:Corr:Wiz](../../GP-
IB_Command_Finder/System.htm#wiz) with the [SCPI Parser
object](../Objects/SCPIStringParser_Object.htm).  
---|---  
  
####  VB Syntax

|  app.LaunchDialog dialog, [data]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
dialog |  (String) Dialog box to launch. Choose from: "SourcePowerCal" [See this dialog.](../../../S3_Cals/PwrCalibration.md#SourceDiag) "PowerMeterSettings" [See this dialog.](../../../S3_Cals/PwrCalibration.md#MeterSettings) PathConfiguration [See this dialog](../../../S1_Settings/Path_Configurator.md#PathConfDiag). CalibrationWizard Depends on the channel CalibrationSelection" [See this dialog](../../../S3_Cals/Cal_Sets.md#HowApply). "CalibrateAll" launches the [Cal All wizard](../../../S3_Cals/Calibrate_All_Channels.md) dialog. "ConfigurePowerSensors" Starts the [external device dialog](../../../System/Configure_an_External_Device.md#ExtDevConfig) for configuring power sensors for use with PMAR  
[data] |  (Optional argument) Reserved for future use.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.LaunchDialog "SourcePowerCal"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  LaunchDialog( BSTR dialog, [defaultvalue(0)] VARIANT dialogData)  
  
#### Interface

|  IApplication11  
  
[See the VNA Object Model](../Objects/The_Analyzer_Object_Model.md)

* * *


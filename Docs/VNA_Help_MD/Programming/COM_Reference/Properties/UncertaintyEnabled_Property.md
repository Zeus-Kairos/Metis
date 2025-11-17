##### Read/Write

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
# UncertaintyEnabled Property

* * *

#### Description

| Sets and returns the ON/OFF state which determines if the calibration that
is about to be performed will support Dynamic Uncertainty for S-Parameters
(Opt. S93015A/B). Dynamic Uncertainty for S-Parameters is supported ONLY for
calibrations on standard S-Parameter channels. Calibrations performed with
that feature enabled do NOT support the use of ALL traditional Guided
calibration commands.  These existing commands are used for the performing of
the calibration: [CalKitType](CalKitType_Property.md)
[Initialize](../Methods/Initialize_Method.md)
[GenerateSteps](../Methods/GenerateSteps_Method.md)
[GetStepDescription](../Methods/Get_StepDescription_Method.md)
[AcquireStep](../Methods/AcquireStep_Method.md)
[GenerateErrorTerms](../Methods/GenerateErrorTerms_Method.md) These commands
might also optionally be used in performing the cal:
[GetCompatibleCalKits](../Methods/GetCompatibleCalKits_Method.md)
[OrientECALModule](OrientECALModule_Property.md)
[ECALPortMapEx](ECALPortMapEx_Property.md) Dynamic Uncertainty must be
enabled using this command before starting the calibration procedure because
this command controls the way connectors and calkits are assigned to ports
during calibration. Therefore, this command must be enabled before any of the
following commands to ensure that the connector and calkit settings will be
set/queried correctly: [CalKitType](CalKitType_Property.md)
[GetCompatibleCalKits](../Methods/GetCompatibleCalKits_Method.md)
[ConnectorType](ConnectorType_Property.md)
[ValidConnectorTypes](ValidConnectorType_Property.md)  
---|---  
  
#### VB Syntax

| guidedCal.UncertaintyEnabled = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidedCal | An [GuidedCalibration](../Objects/GuidedCalibration_Object.md) Object  
value | (Boolean) Enable state. Choose from: True \- The next calibration initialized for the channel will support Dynamic Uncertainties for S-Parameters. False \- The next calibration initialized for the channel will NOT support Dynamic Uncertainties for S-Parameters.  
  
#### Return Type

| Boolean  
  
#### Default

| False  
  
#### Examples

| guided.UncertaintyEnabled = True [See example
program](../../COM_Example_Programs/Dynamic_Uncertainty.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_UncertaintyEnabled(VARIANT_BOOL* pState); HRESULT
put_UncertaintyEnabled(VARIANT_BOOL state);  
  
#### Interface

| IGuidedCalibration11  
  
* * *


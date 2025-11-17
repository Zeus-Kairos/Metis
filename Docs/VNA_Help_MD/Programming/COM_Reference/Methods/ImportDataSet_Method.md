##### Write only

## ImportDataSet Method

* * *

#### Description

|  Imports the Guided Power Cal Set (from an existing SMC Cal) or Phase
Reference Cal into the current SMC calibrations. For the Guided Power Cal: The
port of the mixer input must have the same source attenuator setting between
the SMC channel and the Guided Power Cal Set. The frequencies of the Guided
Power Cal must include all the mixer frequencies. Interpolation will be
applied to the Guided Power Cal frequencies if they do not exactly match. For
the Phase Reference Cal: The port of the mixer input must have the same source
attenuator setting as used in the phase reference cal. The phase reference cal
must include all the mixer frequencies. Interpolation will be applied to the
phase reference cal frequencies if they do not exactly match. [Learn more
about Phase Reference
Cal](../../../FreqOffset/Phase_Reference_Calibration.htm). The following error
message may appear (it is not written to the VNA Error Log): Interpolation
target is out of range. Cannot interpolate when incompatible frequency ranges
occur.  
---|---  
  
####  VB Syntax

|  smc.ImportDataSet (calset, dataName)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
smc |  [SMCType](../Objects/SMC_Type_Object.md) (object)  
  
#### calset

|  (String) Name of existing SMC Cal Set from which cal data is imported.  
  
#### dataName

|  (String) Name of the data set. Choose from:

  * POWER_STEP - Import Guided Power Cal data.
  * "POWER_AND_PHASE" \- Import the Phase Reference + power cal data. When this command is sent, the SMC Cal Method is automatically set to Use Phase Reference Cal Set. [Learn more](../../../FreqOffset/SMC_plus_Phase.md#SMCCalSetup). There is no other command to set this.

  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  smc.ImportDataSet("MySMCCal","POWER_STEP") [See example
program](../../COM_Example_Programs/Use_Existing_Power_Cal_for_SMC.htm)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT ImportDataSet(BSTR csName, BSTR dataset);  
  
#### Interface

|  SMCType4  
  
* * *


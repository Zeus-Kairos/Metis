##### Write/Read  
  
---  
  
## SeparatePowerCal Property

* * *

#### Description

|  Specifies whether to use a Thru standard or to use two power sensor
connections during the power cal of an SMC calibration. [Learn
more.](../../../FreqOffset/SMC_Measurements.htm#CalSetupDiag) This command
must be sent immediately after the Initialize command, but before all other
calibration properties.  
---|---  
  
####  VB Syntax

|  smc.SeparatePowerCal = bool  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
smc |  An [SMCType](../Objects/SMC_Type_Object.md) (object)  
  
#### bool

|  (Boolean) True \- Do NOT use a Thru, but instead perform separate power
cals on Input and Output reference planes. False \- Perform Cal with Thru
standard.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Example

|  FCAppLib.ISMCType4 SMC = (FCAppLib.ISMCType4)CalMgr.CreateCustomCal("SMC");  
SMC.Initialize(chan, true);  
if (separatePowerCalIsDesired)  
SMC.SeparatePowerCal = true;  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SeparatePowerCal(VARIANT_BOOL bValue); HRESULT
get_SeparatePowerCal(VARIANT_BOOL *bValue);  
  
#### Interface

|  SMCType4  
  
* * *


##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## LastCalPassedTolerance Property

* * *

#### Description

|  Returns the pass / fail status of the tolerance limits of the target power
from the most recent source power cal.  
---|---  
  
####  VB Syntax

|  value = pwrCal.LastCalPassedTolerance  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrCal |  (object)  A [SourcePowerCalibrator](../Objects/SourcePowerCalibrator_Object.md) (object)  
value |  (boolean) -  False  Source power cal did NOT achieve the specified tolerance limits. True  Source power cal DID achieve the specified tolerance limits.  
  
#### Return Type

|  Boolean  
  
#### Default

|  Not Applicable  
  
#### Examples

|  status = powerCal.LastCalPassedTolerance 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LastCalPassedTolerance(VARIANT_BOOL *bState);  
  
#### Interface

|  ISourcePowerCalibrator7  
  
* * *

  


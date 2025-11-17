##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## SaveCalSets Method Superseded

* * *

#### Description

|  This command is replaced by [ICalSet::Save](Save_CalSet_Method.md) which
saves the data for only the current Cal Set to the disk. Writes new or changed
Cal Sets to disk. All Cal Sets are saved in a single file. This file is
updated at the following times:

  * When a Cal Set has been deleted.
  * When a calibration has been performed through the front panel interface.
  * When this method is called.
  * When [ICalSet::Save](Save_CalSets_Method.md) is called.

Learn more about [reading and writing Cal data using
COM](../../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)  
---|---  
  
####  VB Syntax

|  object.SaveCalSets  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  (object) - A CalManager object or a Calibrator object  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Example

|  calMgr.SaveCalSets  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SaveCalSets( );  
  
#### Interface

|  ICalManager  
ICalibrator


##### Read/Write

|

##### Learn about [Calibration Thru
Methods](../../../S3_Cals/Calibration_THRU_Methods.htm)  
  
---|---  
  
## ThruCalMethod Property Superseded

* * *

#### Description

|  This command is replaced by [PathThruMethod
Property](PathThruMethod_Property.htm). Sets and returns the method for
performing the Cal Method and the THRU portion of the calibration.  
---|---  
  
#### VB Syntax

|  guidedCal.ThruCalMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guidedCal |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
value |  (Enum as NAThruCalMethod) Choose from: 0 - naDefaultCalMethod \- allow the VNA to choose the best possible method (from the following) depending on whether the device or ECal module is insertable or non-insertable and given the model number of the VNA. (default selection if omitted.) 1 - naAdapterRemoval \- Perform Adapter removal calibration. 2 - naFlushThru \- Perform Flush Thru calibration. 3 - naDefinedThru - Perform Defined Thru calibration. If performing an ECal, this is the Thru standard in the ECal module. 4 - naUnknownThru \- Perform Unknown Thru calibration. 5 - naSOLT \- Perform SOLT calibration 6 - naTRL \- Perform TRL calibration 7 - naQSOLT \- Perform QSOLT calibration. [Learn more about Cal Methods](../../../S3_Cals/Select_Cal.md)  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naDefaultCalMethod  
  
#### Examples

|  guided.ThruCalMethod = naDefinedThru  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ThruCalMethod(enum NAThruCalMethod *thruMethod); HRESULT
put_ThruCalMethod(enum NAThruCalMethod thruMethod);  
  
#### Interface

|  IGuidedCalibration  
  
* * *


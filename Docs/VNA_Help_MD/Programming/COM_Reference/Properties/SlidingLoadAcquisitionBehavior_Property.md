##### Write-Read  
  
---  
  
## SlidingLoadAcquisitionBehavior Property

* * *

#### Description

|  Specifies the behavior for guided cal steps that involve a sliding load in
a cal that is about to be performed.  Send this command BEFORE sending the
[Initialize](../Methods/Initialize_Method.md) command  
---|---  
  
####  VB Syntax

|  guided.SlidingLoadAcquisitionBehavior = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
guided |  [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
value |  (Enum as NASlidingLoadAcquisitionBehavior) Choose from: 0 - naShowDialog - The Move Sliding Load prompt is presented on the VNA screen. All slide positions are measured from a single invocation of the acquire command. 1 - naMeasureSlidePosition \- Each invocation of the acquire command for a sliding load step measures a single slide position and increments the slide position counter. No Move Sliding Load prompt is presented on the VNA screen.  
  
#### Return Type

|  Enum  
  
#### Default

|  0  naShowDialog  
  
#### Examples

|  obj.SlidingLoadAcquisitionBehavior = naMeasureSlidePosition  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_SlidingLoadAcquisitionBehavior(enum
NASlidingLoadAcquisitionBehavior behavior); HRESULT
get_SlidingLoadAcquisitionBehavior(enum NASlidingLoadAcquisitionBehavior
*behavior);  
  
#### Interface

|  IGuidedCalibration10  
  
* * *


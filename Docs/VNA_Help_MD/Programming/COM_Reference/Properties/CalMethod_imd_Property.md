##### Write/Read

|

##### [About SweptIMDCal](../../../Applications/Swept_IMD.md#CalOverview)  
  
---|---  
  
## CalMethod Property

* * *

#### Description

|  Sets and returns the method by which the match-correction portion of an IMD
calibration is performed. [Learn
more.](../../../Applications/Swept_IMD.htm#CalSelectTones)  
---|---  
  
####  VB Syntax

|  imd.CalMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMDCal](../Objects/SweptIMDCal_Object.md) (object)  
value |  (Enum as NAIMDCalMethod) Choose from: 0 - naIMDMatchCorrectedResponse -Performs a full 2-port cal for full match-correction. 1 - naIMDResponseOnly \- Performs only a response cal instead of a full 2-port cal.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naIMDMatchCorrectedResponse  
  
#### Examples

|  imd.CalMethod = naIMDMatchCorrectedResponse 'Write  
calMeth = imd.CalMethod 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalMethod(tagNAIMDCalMethod * Val) HRESULT
put_CalMethod(tagNAIMDCalMethod newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *


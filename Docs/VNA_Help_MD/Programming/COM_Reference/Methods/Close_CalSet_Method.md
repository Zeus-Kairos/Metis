##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## CloseCalSet Method Superseded

* * *

#### Description

|  This command is no longer necessary. The CalSet.get... and put... commands
that required this command have been replaced, Closes read/write access to the
Cal Set. See _**[OpenCalSet](Open_CalSet_Method.md)**_ for an explanation of
gaining access to the Cal Set. When you are finished reading and writing data
from or to the Cal Set, close the Cal Set. Subsequent read/writes will require
a new OpenCal Set call. Reading and writing Cal Set data is performed with the
PutStandard, GetStandard, PutErrorTerm, GetErrorTerm method calls. These
methods are provided by the [ICal Set](../Objects/CalSet_Object.md) and
ICalData2 interfaces.  
---|---  
  
#### VB Syntax

|  CalSet.CloseCalSet  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A [Cal Set](../Objects/CalSet_Object.md) object  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  CSet.CloseCalSet  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT CloseCalSet  
  
#### Interface

|  ICalSet


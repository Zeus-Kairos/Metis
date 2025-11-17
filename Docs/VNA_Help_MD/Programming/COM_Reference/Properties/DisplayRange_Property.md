##### Write/Read

|

##### [About FOM](../../../FreqOffset/Frequency_Offset_Mode.md)  
  
---|---  
  
## DisplayRange Property

* * *

#### Description

|  Sets or returns the range to be displayed on the VNA x-axis. All traces in
the channel have this same x-axis scaling.  
---|---  
  
####  VB Syntax

|  FOM.DisplayRange = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  An [FOM](../Objects/FOM_Collection.md) (object)  
value |  (string) \- Range to be displayed on the VNA x-axis. Case insensitive.  
  
#### Return Type

|  String  
  
#### Default

|  "Receivers"  
  
#### Examples

|  fom.DisplayRange = "Source" 'sets the x-axis to the frequency range of
"source"  
disprange = fom.DisplayRange 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_DisplayRange(BSTR *pDspRange)  
HRESULT put_DisplayRange(BSTR pDspRange)  
  
#### Interface

|  IFOM  
  
* * *


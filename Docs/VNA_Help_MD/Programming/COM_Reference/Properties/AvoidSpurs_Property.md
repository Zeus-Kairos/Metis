##### Write/Read

|

##### [About Avoid Spurs Feature](../../../FreqOffset/FCA_Use.md#Avoid)  
  
---|---  
  
## AvoidSpurs Property

* * *

#### Description

|  Sets and returns the state of the avoid spurs feature.  
---|---  
  
####  VB Syntax

|  mixer.AvoidSpurs = boolean  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
mixer |  A [Mixer](../Objects/IMixer_Interface.md) (object) A [Converter](../Objects/Converter_Object.md) (object)  
value |  (Boolean) \- State of avoid spurs feature. Choose from False Avoid spurs OFF True Avoid spurs ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  conv.AvoidSpurs = True 'Write variable = conv.AvoidSpurs 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AvoidSpurs(Bool *bVal) HRESULT put_AvoidSpurs(Bool newVal)  
  
#### Interface

|  IMixer3 IConverter5  
  
* * *


##### Write/Read

|

##### [About Noise Figure](../../../Applications/Noise_Figure.md)  
  
---|---  
  
## NarrowBand Property

* * *

#### Description

|  Turns narrowband noise figure compensation ON and OFF.  
---|---  
  
####  VB Syntax

|  noise.NarrowBand = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
noise |  A [NoiseFigure](../Objects/NoiseFigure_Object.md) (object)  
value |  (boolean) - Narrowband compensation state. False - Narrowband compensation OFF True - Narrowband compensation ON  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  noise.NarrowBand = OFF 'Write  
Narrowband = noise.NarrowBand 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_NarrowBand(VARIANT_BOOL* on); HRESULT
put_NarrowBand(VARIANT_BOOL on);  
  
#### Interface

|  INoiseFigure  
  
* * *


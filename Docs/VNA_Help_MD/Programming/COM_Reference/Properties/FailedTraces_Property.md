##### Write / Read

|

##### [About Display Colors](../../../System/Display_Colors.md)  
  
---|---  
  
## FailedTraces Property

* * *

#### Description

| Set and return the limit line color of failed traces or failure indicators
(dots) and the word Fail.  
---|---  
  
#### VB Syntax

| colors.FailedTraces = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
colors | A [ComColors](../Objects/ComColors_Object.md) (object)  
value | (Long Integer) \- RGB color of the FailedTraces pen. Convert the three RGB colors to an integer as follows: RGB = R+(G*2^8)+(B*2^16) To find the three RGB values from the [Display Colors dialog](../../../System/Display_Colors.md), click Change Color, then Define Custom Color.  
  
#### Return Type

| Long  
  
#### Default

| Display = 255,20,20 Print = 255,20,20  
  
#### Examples

| R = 10  
G = 10  
B = 10  
RGB = R+(G*2^8)+(B*2^16)  
colors.FailedTraces = RGB 'Write  
color = colors.FailedTraces 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_FailedTraces(long* pVal); HRESULT put_FailedTraces(long newVal);  
  
#### Interface

| IColors  
  
* * *


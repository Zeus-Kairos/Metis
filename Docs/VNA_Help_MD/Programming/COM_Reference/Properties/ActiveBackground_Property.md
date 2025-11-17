##### Write / Read

|

##### [About Display Colors](../../../System/Display_Colors.md)  
  
---|---  
  
## ActiveBackground Property

* * *

#### Description

| Set and return the background color of the active window for the VNA display
or hardcopy print.  
---|---  
  
#### VB Syntax

| colors.ActiveBackground = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
colors | A [ComColors](../Objects/ComColors_Object.md) (object)  
value | (Long Integer) \- RGB color of the ActiveBackground pen. Convert the three RGB colors to an integer as follows: RGB = R+(G*2^8)+(B*2^16) To find the three RGB values from the [Display Colors dialog](../../../System/Display_Colors.md), click Change Color, then Define Custom Color.  
  
#### Return Type

| Long  
  
#### Default

| Display = 0,0,24  
  
#### Examples

| R = 10  
G = 10  
B = 10  
RGB = R+(G*2^8)+(B*2^16)  
colors.ActiveBackground = RGB 'Write  
color = colors.ActiveBackground 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_ActiveBackground(long* pVal); HRESULT put_ActiveBackground(long
newVal);  
  
#### Interface

| IColors2  
  
* * *


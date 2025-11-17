##### Write / Read

|

##### [About Display Colors](../../../System/Display_Colors.md)  
  
---|---  
  
## ActiveLabels Property

* * *

#### Description

| Set and return the labels and grid frame colors in the active window for the
VNA display or hardcopy print. (Active labels, Grid frame)  
---|---  
  
#### VB Syntax

| colors.ActiveLabels = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
colors | A [ComColors](../Objects/ComColors_Object.md) (object)  
value | (Long Integer) \- RGB color of the ActiveLabels pen. Convert the three RGB colors to an integer as follows: RGB = R+(G*2^8)+(B*2^16) To find the three RGB values from the [Display Colors dialog](../../../System/Display_Colors.md), click Change Color, then Define Custom Color.  
  
#### Return Type

| Long  
  
#### Default

| Display = 175,175,175 Print = 0,0,0 (Black)  
  
#### Examples

| R = 10  
G = 10  
B = 10  
RGB = R+(G*2^8)+(B*2^16)  
colors.ActiveLabels = RGB 'Write  
color = colors.ActiveLabels 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_ActiveLabels(long* pVal); HRESULT put_ActiveLabels(long newVal);  
  
#### Interface

| IColors  
  
* * *


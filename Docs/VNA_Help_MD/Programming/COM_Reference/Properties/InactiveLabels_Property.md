##### Write / Read

|

##### [About Display Colors](../../../System/Display_Colors.md)  
  
---|---  
  
## InactiveLabels Property

* * *

#### Description

| Set and return the Inactive (not selected) Window Labels for the VNA display
or hardcopy print.  
---|---  
  
#### VB Syntax

| colors.InactiveLabels = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
colors | A [ComColors](../Objects/ComColors_Object.md) (object)  
value | (Long Integer) \- RGB color of the Inactive Labels pen. Convert the three RGB colors to an integer as follows: RGB = R+(G*2^8)+(B*2^16) To find the three RGB values from the [Display Colors dialog](../../../System/Display_Colors.md), click Change Color, then Define Custom Color.  
  
#### Return Type

| Long  
  
#### Default

| Display = 160,160,160 Print = 0,0,0 (Black)  
  
#### Examples

| R = 10  
G = 10  
B = 10  
RGB = R+(G*2^8)+(B*2^16)  
colors.InactiveLabels = RGB 'Write  
color = colors.InactiveLabels 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_InactiveLabels(long* pVal); HRESULT put_InactiveLabels(long
newVal);  
  
#### Interface

| IColors  
  
* * *


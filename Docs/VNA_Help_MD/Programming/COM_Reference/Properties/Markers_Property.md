##### Write / Read

|

##### [About Display Colors](../../../System/Display_Colors.md)  
  
---|---  
  
## Markers Property

* * *

#### Description

| Set and return the color of data trace markers for nth trace in a window.  
---|---  
  
#### VB Syntax

| trace(n).Markers = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
trace(n) | One of the 8 [ComTraceColors](../Objects/ComTraceColors_Object.md) objects  
value | (Long Integer) \- RGB color of the Markers pen. Convert the three RGB colors to an integer as follows: RGB = R+(G*2^8)+(B*2^16) To find the three RGB values from the [Display Colors dialog](../../../System/Display_Colors.md), click Change Color, then Define Custom Color.  
  
#### Return Type

| Long  
  
#### Default

| Varies for each trace.  
  
#### Examples

| R = 10  
G = 10  
B = 10  
RGB = 10+(10*2^8)+(10*2^16)  
trace1.Markers = RGB 'Write  
color = trace1.Markers 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT get_Markers(long* pVal); HRESULT put_Markers(long newVal);  
  
#### Interface

| ITraceColors  
  
* * *


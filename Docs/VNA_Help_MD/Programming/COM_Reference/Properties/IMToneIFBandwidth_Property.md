##### Write/Read

|

##### [About Swept IMD](../../../Applications/Swept_IMD.md)  
  
---|---  
  
## IMToneIFBandwidth Property

* * *

#### Description

|  Sets and returns the IF Bandwidth for measurement of the intermodulation
products.  
---|---  
  
####  VB Syntax

|  imd.IMToneIFBandwidth = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
imd |  A [SweptIMD](../Objects/SweptIMD_Object.md) Object  
value |  (Double) IF Bandwidth in Hz. Choose from: 1 | 2 | 3 | 5 | 7 | 10 | 15 | 20 | 30 | 50 | 70 | 100 | 150 | 200 | 300 | 500 | 700 | 1k | 1.5k | 2k | 3k | 5k | 7k | 10k | 15k | 20k | 30k | 50k | 70k | 100k | 150k| 200k | 280k | 360k | 600k [Learn more about setting IFBW for IMD.](../../../Applications/Swept_IMD.md#IFBW) If an invalid number is specified, the analyzer will round up to the closest valid number.  
  
#### Return Type

|  Double  
  
#### Default

|  1 kHz  
  
#### Examples

|  imd.IMToneIFBandwidth = 2e3 'Write  
value = imd.IMToneIFBandwidth 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_IMToneIFBandwidth(double *pVal)  
HRESULT put_IMToneIFBandwidth(double newVal)  
  
#### Interface

|  ISweptIMD  
  
* * *


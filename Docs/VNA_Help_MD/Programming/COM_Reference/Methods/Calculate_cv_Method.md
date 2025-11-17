##### Write only

## Calculate Method

* * *

#### Description

|  Calculates the Input or Output frequencies of the mixer setup, applies the
mixer setup to the mixer object, and turns the channel ON. Note: There is also
a [Calculate Method](Calculate_Method.md) on the IMixer Interface.  
---|---  
  
####  VB Syntax

|  obj.Calculate (port)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  A [Converter Object](../Objects/Converter_Object.md)  
  
#### port

|  (enum as ConverterCalculation) Port of the mixer for which to calculate start and stop frequencies. Choose from: |  |  enum |  1st or only stage requires: |  In addition, 2nd stage requires:  
---|---|---|---  
0 |  naCalculateINPUT | 

  * Output Start and Stop frequencies
  * LO frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
1 |  naCalculateINPUT AndOUTPUT (2 stage mixers ONLY) |  NA | 

  * IF Start and Stop frequencies
  * Both LO frequencies

  
2 |  naCalculateOUTPUT | 

  * Input Start and Stop frequencies
  * LO frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
3 |  naCalculateLO1 | 

  * Input Start and Stop frequencies
  * Output frequency
  * Output sideband (High or Low)

|

  * IF Start and Stop frequencies
  * 2nd LO frequency
  * IF sideband (High or Low)

  
4 |  naCalculateLO2 |  NA | 

  * Input Start and stop frequencies
  * 1st LO start and stop frequencies
  * Output frequency
  * IF sideband(High or Low
  * Output sideband(High or Low)

  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  obj.Calculate (naCalculateOUTPUT)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Calculate()  
  
#### Interface

|  IConverter  
  
* * *


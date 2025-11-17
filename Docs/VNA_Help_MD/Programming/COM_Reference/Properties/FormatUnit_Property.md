##### Write/Read

|

##### [About Data Format](../../../S1_Settings/Data_Format.md)  
  
---|---  
  
## FormatUnit Property

* * *

#### Description

| Sets and returns the units for the specified data format. Measurements with
display formats other than those specified are not affected.  
---|---  
  
####  VB Syntax

| meas.FormatUnit (format) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas | A [Measurement](../Objects/Measurement_Object.md) (object)  
format | (enum NADataFormat) \- Choose from: 0 - naDataFormat_LinMag 1 - naDataFormat_LogMag  
value | (enum naFormatUnit) For LogMag, choose from:

  * 0 - naFormatUnit_dBm Units are displayed in dBm. 0 dBm = 0.001 watt
  * 1 \- naFormatUnit_dBmV Units are displayed in dBmV. 0 dBmV = 0.001 volt  
DBmV value depends on the reference impedance: dBmV = dBm + 30 + 10*log10(Z0)

  * 2 \- naFormatUnit_dBmA Units are displayed in dBmA. 0 dBmA = 0.001 Ampere
  * 6 \- naFormatUnit_dBuV Units are displayed in dBuV. 0 dBuV = 1 uV  
DBuV value depends on the reference impedance: dBuV = dBm + 90 + 10*log10(Z0)

For LinMag, choose from:

  * 3 - naFormatUnit_W \- Watts
  * 4 - naFormatUnit_V \- Volts
  * 5 - naFormatUnit_A \- Amperes

  
  
#### Return Type

| Enum  
  
#### Default

| 0 - naFormatUnit_dBm  
  
#### Examples

| meas.FormatUnit(1)= naFormatUnit_dBmV 'Write  
units = meas.FormatUnit(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_FormatUnit(tagDataFormat format, tagFormatUnit unit) HRESULT
get_FormatUnit(tagDataFormat format, tagFormatUnit* unit)  
  
#### Interface

| IMeasurement9  
  
* * *


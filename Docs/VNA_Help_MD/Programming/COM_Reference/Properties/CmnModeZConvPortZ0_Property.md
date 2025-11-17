##### Write/Read

|

##### About Fixturing  
  
---|---  
  
## CmnModeZConvPortZ0 Property

* * *

#### Description

| Sets the impedance value for the common port impedance conversion function.
Set either this single value or set the
[real](CmnModeZConvPortReal_Property.md) and
[imaginary](CmnModeZConvPortImag_Property.md) parts separately. The imaginary
part is set to 0.0 using this command.  
---|---  
  
####  VB Syntax

| fixture.CmnModeZConvPortZ0(portNum) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
fixture | A [Fixturing](../Objects/Fixturing_Object.md) (object)  
portNum | (Integer) The number of balanced ports. For example, if the device topology is SE-BAL-SE-BAL-SE-BAL, then this configuration would have 6 logical ports and 3 balanced ports. [Learn more about logical and balanced ports.](../../../S1_Settings/Balanced_Measurements.md#mapping)  
value | (Double) Impedance value. Choose a value between 0 and 1E7.  
  
#### Return Type

| Double  
  
#### Default

| See Common Mode Port Z Conversion Default  
  
#### Examples

| fixture.CmnModeZConvPortZ0(2) = 75 'Write  
value = fixture.CmnModeZConvPortZ0(1) 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT get_CmnModeZConvPortZ0( short portNum, double *pVal) HRESULT
put_CmnModeZConvPortZ0( short portNum, double newVal)  
  
#### Interface

| IFixturing2  
  
* * *


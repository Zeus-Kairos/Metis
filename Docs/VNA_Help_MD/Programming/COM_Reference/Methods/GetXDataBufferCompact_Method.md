##### Read-only

|

##### [Data Access Map](../../DataMapSet.md)  
  
---|---  
  
# GetXDataBufferCompact Method

* * *

#### Description

| Retrieves compact signal frequency tone data from the modulation distortion
measurement.  
---|---  
  
####  VB Syntax

| data = meas.GetXDataBufferCompact DataBufferName  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data | (variant) \- Array to store the data.  
meas | (object) - A [Measurement](../Objects/Measurement_Object.md) object  
DataBufferName | (string)  Name of the buffer to be read.  Note: The following names assume a 2-port VNA. Also, by default, the parameter names assume that VNA Port 1 is connected to the DUT input and VNA Port 2 is connected to the DUT output. If the RF Path settings are changed from the default, the names will change accordingly. For example, if the VNA has 4 ports and Port 4 is connected to the DUT output, the names will change to "PIn1", "POut4", "S11", "S41", etc. Choose from: "POut2" \- Power Out "PIn1" \- Power In "MSig2" \- Modulation Signal Out "MDist2" \- Modulation Distortion Out "MGain21" \- Modulation Gain "MComp21" \- Modulation Compression "PGain21" \- Power Gain "S11" \- Linear Input Match "S21" \- Linear Gain "LPin1" \- Linear Power In "LPOut1" \- Linear Reflected Power In "LPOut2" \- Linear Power Out  
  
#### Return Type

| Variant array  
  
#### Default

| Not Applicable  
  
#### Examples

| meas.GetXDataBufferCompact "S21"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT GetXDataBufferCompact(BSTR DataBufferName, VARIANT* Data );  
  
#### Interface

| IMeasurement19  
  
* * *


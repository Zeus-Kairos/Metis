##### Write/Read

|

##### [About Compression
Mode](../../../Applications/Gain_Compression_Application.htm#CompressionMethods)  
  
---|---  
  
## AcquisitionMode Property

* * *

#### Description

|  Set and read the method by which gain compression data is acquired.  
---|---  
  
####  VB Syntax

|  gca.AcquisitionMode = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
gca |  A [GainCompression](../Objects/GainCompression_Object.md) (object)  
value |  (NAGCAAcquisitionMode)  Choose from:

  * naSmartSweep (0) Iterate quickly to find compression point
  * naSweepPowerAtEachFreq2D (1) Sweep power at each frequency
  * naSweepFreqAtEachPower2D (2) Sweep frequency at each power level

  
  
#### Return Type

|  Enum  
  
#### Default

|  naSmartSweep  
  
#### Examples

|  gca.AcquisitionMode = naSmartSweep 'Write  
acqMode = gca.AcquisitionMode 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_AcquisitionMode(tagNAGCAAcquisitionMode* mode) HRESULT
put_AcquisitionMode(tagNAGCAAcquisitionMode mode)  
  
#### Interface

|  IGainCompression  
  
* * *


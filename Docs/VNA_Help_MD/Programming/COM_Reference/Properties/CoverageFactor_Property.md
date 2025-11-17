##### Write/Read

|

##### [About Dynamic Uncertainty](../../../S3_Cals/Dynamic_Uncertainty.md)  
  
---|---  
  
## CoverageFactor Property

* * *

#### Description

|  Sets and returns the coverage factor value to apply to the displayed
uncertainty for the selected measurement trace. Coverage Factor corresponds to
the level of confidence used in computing the specified measurement
uncertainties.  
---|---  
  
#### VB Syntax

|  uncert.CoverageFactor = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
uncert |  An [Uncertainty](../Objects/Uncertainty_Object.md) (object)  
value |  Long. Choose from: |  Coverage Factor |  Approximate confidence level  
---|---  
1 |  67%  
2 |  95%  
3 |  99%  
4 |  >99%  
  
#### Return Type

|  Long  
  
#### Default

|  2  
  
#### Examples

|  uncert.CoverageFactor = True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CoverageFactor(long *pSigma); HRESULT put_CoverageFactor(long
sigma);  
  
#### Interface

|  IUncertainty  
  
* * *


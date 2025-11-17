##### Read-only

|

##### [About Limit
Testing](../../../S4_Collect/Use_Limits_to_Test_Devices.htm)  
  
---|---  
  
## GetTestResult Method

* * *

#### Description

|  Returns the result of limit line testing. There are three ways to use this
command:

  * If neither optional parameter is specified, limit results for ALL data is returned.
  * If one parameter is specified (start), the limit result for that data point is returned.
  * If both parameters are specified, limit results are returned beginning with start, and ending with (start+size)-1

Note: In 'strongly-typed' languages such as C#, all parameters must be
specified.  
---|---  
  
####  VB Syntax

|  testRes = limts.GetTestResult [start,size]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
testRes |  (enum NALimitTestResult) \- A dimensioned variable to store test results. If a limit line is not tested, a PASS is returned. 0 - naLimitTestResult_None  
1 - naLimitTestResult_Fail  
2 - naLimitTestResult_Pass  
limts |  A LimitTest (object)  
start |  (long) - Optional argument. A start data point number to return limit test results.  
size |  (long) - Optional argument. Number of data points from start to return limit test results.  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim testRes As NALimitTestResult  
testRes = limts.GetTestResult  
Select Case testRes  
  
Case 1  
Print "Fails"  
  
Case 2  
Print "Pass"  
  
End Select  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetTestResult(long lStart, long lSize, tagNALimitTestResult *pVal)  
  
#### Interface

|  ILimitTest  
  
* * *

* * *


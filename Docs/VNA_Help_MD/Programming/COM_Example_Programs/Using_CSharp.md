# Using C#

* * *

The following are common C# examples:

### Connecting to a specific VNA via DCOM:

public AgilentPNA835x.Application Connect(string hostname) {
AgilentPNA835x.Application pna = null; try { Type t =
Type.GetTypeFromProgID("AgilentPNA835x.Application", hostname, true); pna =
(AgilentPNA835x.Application) Activator.CreateInstance(t); } catch (Exception
e) { HandleExceptions(e); } return pna; }  
---  
  
### Using the GetData Interface

AgilentPNA835x.IMeasurement meas = app.ActiveMeasurement; object[]
dataArrayAsObj; dataArrayAsObj =
(object[])meas.getData(AgilentPNA835x.NADataStore.naMeasResult,
AgilentPNA835x.NADataFormat.naDataFormat_LogMag); float[] dataArray = new
float[dataArrayAsObj.Length]; for (int j = 0; j < dataArrayAsObj.Length; j++)
{ dataArray[j] = (float)dataArrayAsObj[j]; }  
---  
  
### 2-dimensional GetData

AgilentPNA835x.IMeasurement meas = app.ActiveMeasurement;
app.ActiveChannel.Single(true); object[,] dataArrayAsObj; dataArrayAsObj =
(object[,])meas.getData(AgilentPNA835x.NADataStore.naRawData,
AgilentPNA835x.NADataFormat.naDataFormat_Smith); float[,] dataArray = new
float[dataArrayAsObj.Length,2]; for (int j = 0; j < dataArrayAsObj.Length;
j++) { dataArray[j,0] = (float)dataArrayAsObj[j,0]; dataArray[j,1] =
(float)dataArrayAsObj[j,1]; }  
---  
  
###

### Other C# / .NET Topics

[Perform a Guided Cal with CSharp](Perform_a_Guided_Cal_with_CSharp.md)

[Getting a handle to the Noise Figure Cal
object.](Create_and_Cal_a_NoiseFigure_Measurement.htm)

[Using .NET](../Learning_about_COM/Using_NET.md)

* * *


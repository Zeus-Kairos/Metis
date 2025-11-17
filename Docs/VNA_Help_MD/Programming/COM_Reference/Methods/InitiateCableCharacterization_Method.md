##### Write only

## InitiateCableCharacterization Method

* * *

#### Description

|  Initializes a cable repeatability characterization for the specified
channel and port.  
---|---  
  
####  VB Syntax

|  UncertChar.InitiateCableCharacterization (chan, port,iterations)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
UncertChar |  A [Characterizer](../Objects/Characterizer_Object.md) (object)  
  
#### chan

|  (Long) Channel number to calibrate. Note: chan MUST be the active channel.  
  
#### port

|  (Long) Port number to use in the characterization.  
  
#### iterations

|  (Long) Number of Iterative connections of the standards to be measured for
the characterization.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  oUncerChar.InitiateCableCharacterization(2,2,20)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT InitiateCableCharacterization([in] long channel, [in] long portNum,
[in] long numIterationsPerStep, [out,retval] long* pNumSteps);  
  
#### Interface

|  IUncertaintyCharacterizer  
  
The following existing commands on the [GuidedCal
object](../Objects/GuidedCalibration_Object.htm) are used to perform the
initialized cable repeatability characterization:

[GenerateSteps Method](GenerateSteps_Method.md)

[Get StepDescription Method](Get_StepDescription_Method.md)

[MinimumIterationsForStep
Property](../Properties/MinimumIterationsForStep_Property.htm)

[AcquireStep Method](AcquireStep_Method.md)

[IterationCountForStep
Property](../Properties/IterationCountForStep_Property.htm)

[ResetStep Method](ResetStep_Method.md)

[Save (CalSet) Method](Save_CalSet_Method.md)

[Abort Method](Abort_Method.md)

* * *


##### Write only

## InitiateNoiseCharacterization Method

* * *

#### Description

|  Initializes a noise characterization for the specified channel and port.  
---|---  
  
####  VB Syntax

|  UncertChar.InitiateNoiseCharacterization (chan, firstPort, secondPort,
iterations)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
UncertChar |  A [Characterizer](../Objects/Characterizer_Object.md) (object)  
  
#### chan

|  (Long) Channel number to calibrate. Note: chan MUST be the active channel.  
  
#### firstPort

|  (Long) First VNA port number on which the noise characterization is to be
performed.  
  
#### secondPort

|  (Long) Second VNA port number on which the noise characterization is to be
performed.  
  
#### iterations

|  (Long) Number of Iterative connections of the standards to be measured for
the characterization.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  oUncerChar.InitiateNoiseCharacterization(2,1,2,20)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT InitiateNoiseCharacterization([in] long channel, [in] long
firstPort, [in] long secondPort, [in] long numIterationsPerStep, [out,retval]
long* pNumSteps);  
  
#### Interface

|  IUncertaintyCharacterizer  
  
The following existing commands on the [GuidedCal
object](../Objects/GuidedCalibration_Object.htm) are used to perform the
initialized noise characterization:

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


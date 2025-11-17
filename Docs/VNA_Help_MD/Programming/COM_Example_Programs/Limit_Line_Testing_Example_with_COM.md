##### [Intro to Examples](COM_Example_Intro.md)

# Limit Line Testing with COM

* * *

This Visual Basic program:

  * Turns off existing Limit Lines

  * Establishes Limit Lines with the following settings:

  *     * Frequency range - 4 GHz to 8 GHz

    * Maximum value - (10dB)

    * Minimum value - (-30dB)

  * Turns on Lines, Testing, and Sound

If using [Global
Pass/Fail](../COM_Reference/Objects/HWMaterialHandlerIO_Object.htm) to report
limit results, trigger the VNA after configuring and enabling Limit lines.

Public limts As LimitTest  
Set limts = meas.LimitTest  
'All Off  
For i = 1 To 20  
limts(i).Type = naLimitSegmentType_OFF  
Next i  
  
'Set up Limit Lines  
limts(1).Type = naLimitSegmentType_Maximum  
limts(1).BeginResponse = 10  
limts(1).EndResponse = 10  
limts(1).BeginStimulus = 4000000000#  
limts(1).EndStimulus = 8000000000#  
limts(2).Type = naLimitSegmentType_Minimum  
limts(2).BeginResponse = -30  
limts(2).EndResponse = -30  
limts(2).BeginStimulus = 4000000000#  
limts(2).EndStimulus = 8000000000#  
  
'Turn on Lines, Testing, and Sound  
limts.LineDisplay = 1  
limts.State = 1  
limts.SoundOnFail = 1

* * *


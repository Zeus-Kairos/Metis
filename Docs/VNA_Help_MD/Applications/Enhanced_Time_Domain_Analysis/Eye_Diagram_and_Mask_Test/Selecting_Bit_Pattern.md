# Selecting Bit Pattern

  * Overview

  * Bit Pattern Type

  * Settings Parameters of Bit Stream

[Other topics about Eye Diagram and Mask Test](Eye_Diagram_and_Mask_Test.md)

## Overview

TDR can provide simulated eye diagram analysis capability, eliminating the
need for a hardware pulse pattern generator. The virtual bit pattern can be
selected from:

  * Pseudo-Random Bit Sequence

  * K 28.5

  * User Custom

  * Statistical

## Bit Pattern Type

The following Bit Patterns can be used to develop an Eye Diagram:

Bit Pattern |  Description  
---|---  
PRBS  |  Pseudo-Random Bit Sequence. An industry standard created from a specified pattern length. For example, when 2^7 is selected, 127 [(2^7) -1] unique data 'words' are assembled according to the industry standard.   
K 28.5 |  Industry standard developed by IBM which includes comma (control) characters. The pattern is "00111110101100000101" (20 bits).  
User |  Bit Patterns that you have created.  
Statistical |  Bit Patterns produced via statistical calculations of jitter specification. When this option is selected, the eye diagram is displayed as "statistical" type. When Jitter Injection is turned ON, this option is set as the default selection. Refer to [Using Jitter Injection](../Advanced_Waveform_Analysis/Using_Jitter_Injection.md).  
  
In the user bit pattern, you can set the same bit pattern as the Pseudo-Random
Bit Sequence. However you can get much better resolution in result when you
use PRBS.

### Selecting Bit Pattern

  1. Select the Eye/Mask ab.

  2. Select your desired bit pattern at Type under Bit Pattern.

  3. If you select the PRBS option, length is activated. Then, select length under Bit Pattern.

### Using a User Bit Pattern

You can easily create user (custom) bit patterns. The length of bit should be
from 2 to 32768 (2^15). The pattern with only either 0 or 1 can not be
accepted (ex. 00, 111, 0000).

#### Defining/Saving User Bit Pattern

  1. Select the Eye/Mask tab.

  2. Select User at Type under Bit Pattern, then User Pattern is activated.

  3. Click User Pattern, then Bit Pattern Editor is displayed.

  4. Type "0" or "1" to create your bit pattern.

  5. Click OK, then the Save Bit Pattern dialog box is displayed.

  6. Type your desired file name, then click Save.

  7. Saving pattern to the file must be required when you use the user pattern.

#### Recalling User Bit Pattern

  1. Select the Eye/Mask tab.

  2. Click User Pattern, then Bit Pattern Editor is displayed.

  3. Click Load, then Load Bit Pattern dialog box is displayed.

  4. Select your desired file name, then click Open.

  5. Click Ok to exit Bit Pattern Editor.

## Settings Parameters of Bit Stream

The following parameter can be set for the bit stream.

Label |  Description  
---|---  
One Lv. |  Eye Diagram Y-axis scaling for bit "1" in volts. Negative voltages are allowed. For Differential Eye Diagrams, these scale values are doubled.  
Zero Lv. |  Eye Diagram Y-axis scaling for bit "0" in volts. Negative voltages are allowed. For Differential Eye Diagrams, these scale values are doubled.  
Data Rate |  The speed in bits/second which data is transferred over a circuit or a communications line.  
Rise Time |  The time that it takes a signal to transition from a low to a high condition. Maximum value is 40% of Bit width (Bit width =1/Bit Rate). The time can be defined by either "10-90%" or "20-80%". The rise time settings in EYE/MASK mode and TDR/TDT mode are independent.  
  
### Defining the parameters

  1. Select the Eye/Mask tab.

  2. Click the text box of desired parameter under Stimulus, then the Entry dialog box is displayed.

  3. Type your desired number by clicking numeric keys on the Entry dialog box.


# Setting System Impedance

* * *

The system impedance can be changed for measuring devices with an impedance
other than 50 ohms, such as waveguide devices. The VNA mathematically
transforms and displays the measurement data as though the VNA ports were the
specified impedance value. Physically, the test ports are always about 50
ohms.

#### How to change the System Impedance  
  
---  
Using Hardkey/SoftTab/Softkey  
  
  1. Press Scale > Constants > System Z0

  
[![](../assets/images/SeeProg.gif)](../Programming/CF_Scale_Commands.md#Constants_Tab_Commands)  
System Z0 softtab help  
---  
Allows you to change the system impedance (default setting is 50 ohms). Z0
Displays the current system impedance. For 75 ohm devices:

  1. Change the system Z0 to 75 ohms.
  2. Connect minimum loss pads (75 ohm impedance) between the analyzer and the DUT to minimize the physical mismatch.
  3. Perform a calibration with 75 ohm calibration standards.

For waveguide devices When selecting a Cal Kit with an impedance other than 50
ohms (Waveguide = 1 ohm), it is NO LONGER NECESSARY to change the [System
Impedance](System_Impedance.htm) setting before performing a calibration. The
impedance for the calibration is now derived from the Cal Kit
['Connector'](../S3_Cals/Connectors_Tab.md) impedance setting.  
  
* * *


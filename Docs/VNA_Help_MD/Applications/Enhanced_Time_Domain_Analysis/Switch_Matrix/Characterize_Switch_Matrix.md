# Characterize Switch Matrix

## Characterize Method

Extract S2P files, which characterize Switch Matrix paths + user test cables

![](../../../assets/images/characterize%20switch%20matrix.png)

  * Tier1 Cal is performed at the end of switch matrix test ports 1 - 4,  which is one full 4-port calibration;

  * Tier2 Cals are performed at the end of switch matrix test ports 5 - 20, which are multiple 1-port calibrations.

  * Number of ports connections and number of calibrations depend on the number of switch matrix test ports; in 4-Port VNA + L8990M-0LZ 20-Ports Switch Matrix configuration, using a 4-port ECal, need connect the ECal 5 times in total; behind the scenes, there are one 4-port ECal calibration and thirty-two 1-port  ECal calibrations performed.

  * With Tier1 cal set and Tier2 cal sets, VNA Cal Plane Manager can extract s2p files, which represent the differences (switch paths and user test cables) between Tier 1 cal plane and Tier2 cal planes; by de-embedding there s2p files from Tier 1 cal set, and save as a new cal set, the 4-port cal plane can be moved.

  * Characterization sweep setup settings is decided by Tier 1 cal set. By default, the Tier 1 Cal is a full-range cal on the Characterize External Switch Matrix wizard, which is same as E-TDR ECal. But user could do on-point characterization as long as they perform the Tier 1 calibration on-point.

## **_Characterize External Switch Matrix Wizard_**

Characterize External Switch Matrix dialog box help  
---  
This is a two steps wizard.
![](../../../assets/images/charac_switch%20matrix1.png)

### Step 1/2, Tier Cal

Select Tier 1 Cal Set \- Select an existing Cal Set as the Tier1 Cal Set. Ecal
\- Click and open VNA ECal dialog to perform a new calibration, the new Cal
Set will be selected as the Tier 1 Cal Set. Cover full frequency ranges of the
switch matrix. Leverage the stimulus settings from E-TDR implementation
(leverage E-TDR implementation of SCPI
[_SENS:CORR:TDR:COLL:ECAL:IMMediate_)](../../../Programming/GP-
IB_Command_Finder/Sense/TDR_Correction.htm#SENSe:CORRection:TDR:COLLection:ECAL:IMMediate).
Ecal Module \- Support N4433x, 300 kHz (or DC) to 20 GHz (or higher), four
3.5mm female connectors on module.
![](../../../assets/images/charac_switch%20matrix2.png)

### Step 2/2, Tier Cal

Measure \- Follow up the description to connect switch test port cables to
ECal, then click a Measure button Finish \- Complete the characterization.
The result s2p files will be saved in the app data folder for all users,
C:\ProgramData\Keysight\Network
Analyzer\SwitchMatrixCharacterizations\<ExtDeviceName>\.


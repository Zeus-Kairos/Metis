# User Defined Power Meter Uncertainty File

The following text is an example of the content of a user defined power meter
uncertainty file.

This simple ascii file contains the power meter uncertainty contributions
summarized in the following table. Any user defined file with this format can
be loaded by setting the model as Custom File.

Standard Uncertainties  
---  
Standard Uncertainty | Source  
u_Pm | Power meter instrumentation uncertainty.  
u_Pmc | Power meter instrumentation uncertainty (during calibration).  
u_D | Power meter drift uncertainty.  
u_Pcal | Calibrator output power level uncertainty.  
u_Zs | Power meter zero set uncertainty.  
u_N | Power meter and sensor noise uncertainty.  
u_Zc | Power meter zero carryover uncertainty.  
u_Mu | Mismatch gain uncertainty between the sensor and the generator. The standard uncertainty is dependent upon the reflection coefficients of the sensor and the generator.  
u_Muc | Mismatch gain uncertainty between the sensor and the calibrator output of the power meter. The standard uncertainty is dependent upon the reflection coefficients of the sensor and the calibrator output.  
u_Kc | Sensor calibration factor uncertainty at the frequency of the power meter calibrator output.  
  
### See Also

[ExternalDevices
Collection](../COM_Reference/Objects/ExternalDevices_Collection.htm)

[ExternalDevice Object](../COM_Reference/Objects/ExternalDevice_Object.md)

[PowerSensor Object](../COM_Reference/Objects/PowerSensor_Object.md)

[PowerSensorAsReceiver
Object](../COM_Reference/Objects/PowerSensorAsReceiver_Object.htm)

[PowerSensorCalFactorSegmentPMAR
Object](../COM_Reference/Objects/PowerSensorCalFactorSegmentPMAR_Object.htm)

[PowerLossSegmentsPMAR_Collection](../COM_Reference/Objects/PowerLossSegmentsPMAR_Collection.md)

[PowerLossSegmentPMAR
Object](../COM_Reference/Objects/PowerLossSegmentPMAR_Object.htm)

[Uncertainty on Power Meter](Uncertainty_on_Power_Meter.md)

[Power Meter Uncertainty
dialog](../../System/Configure_a_Power_Meter_As_Receiver.htm#Power_Meter_Uncertainties)
description

[Application Note
(5988-9215EN)](https://www.keysight.com/main/gated.jspx?lb=1&gatedId=287962&cc=US&lc=eng&parentContId=worldwide_home&parentContType=sr&fileType=VIEWABLE&searchType=GR)

// // This file is an example  // of pwrmtr-sensor uncertainty data //
[PwrMtr] SerialNumber=NOTSET // Power Meter Measurement // Uncertainty (%)
u_Pm=0.21 // Power Meter Measurement // Uncertainty during calibration (%) //
If not specified we use the same as u_Pm  u_Pmc=0.21 // Zero drift Uncertainty
(W) u_D=5.5E-9  //Internal output power level //uncertianty, ie. //Internal
calibration accuracy (%) // ±0.59% (0 to 55 °C) u_Pcal=0.59 // // Pcal //
Power used for the // mtr calibration (dBm) Pcal=0.0 // Zero set Uncertainty
(W) u_Zs=25E-9 // // Measurement Noise (W) u_N=45E-9 // // Zero Carryover
u_Zc=0.0 [SensGen] SerialNumber=NOTSET // // MismAtch Gain // NOT TO BE SET
u_Mu=0.000000 //Mismatch gain from // the sensor and the ref source // NOT TO
BE SET FOR USB u_Muc=0.0 // // Sensor CalFactor uncertainty // @ the cal
output frequency // For usb 50MHz (%) u_Kc=0.0198 // // Sensor CalFactor  // @
the cal output frequency // For usb 50MHz  Kc=100 m_TargetPwr=0.000000
[CalFact] // // CalFactor vs Frequency // IN this case is directly // read
from the sensor // This is left for example // as comment // Nele=2 Number of
Freqs //0=1.000000,1.00000 frq,value //1=2.000000,2.100000 [CalFactUnc] // //
Cal Factor UNcertainty (%) vs Freq Nele=18 0=0.000000,2.88 1=0.010000,2.88
2=0.010000,2.04 3=0.030000,2.04 4=0.030000,1.98 5=0.50000,1.98 6=0.50000,2.07
7=1.20000,2.07 8=1.20000,2.40 9=6.0000,2.40 10=6.0000,2.99 11=14.0000,2.99
12=14.0000,3.35 13=18.0000,3.35 14=18.0000,4.70 15=26.5000,4.70
16=26.5000,6.41 17=33.0000,6.41 [LinFactUnc] // // Power Sensor Linearity //
vs power // Array of Nele as: // pwr (dBm),unc (%) // Full temperature range
//(0 to 55 C) Nele=4 0=-1.000000,0.55 1=15.000000,0.55 2=15.000000,0.60
3=20.000000,0.60  
---


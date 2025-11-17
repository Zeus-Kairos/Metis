# Set Up the External Source

Perform the following steps to set up an external MXG signal generator:

Note: If you are setting up an M8190A Arbitrary Waveform Generator with E8267D
PSG Vector Signal Generator, refer to [Drivers for External Compound
Sources](../../System/Configure_an_External_Device.htm#Compound_Sources) for
information about setting up compound sources.

  1. On the VNA front panel, press Setup > External Hardware > External Device....

  2. Click on the New button.

  3. Click in the Name field and type a name for the source. For example, myMXG.

  4. For Device Type, select Source.

  5. For the Driver, select MXG_Vector. [See a list of supported external source drivers.](../../System/Configure_an_External_Device.md#Supported)

  6. Select Active - Show in UI.

  7. Ensure that Enable IO is checked.

  8. In the I/O Configuration field, type the VISA address of the MXG.

  9. Click on the OK button. The following is an example:  
  
![](../../assets/images/ModDistortion_ExternalDeviceSetup.png)


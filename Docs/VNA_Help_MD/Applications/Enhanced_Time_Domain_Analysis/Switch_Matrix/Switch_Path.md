# Switch Path

Switch Path dialog box help  
---  
![](../../../assets/images/switch%20path%20dialog.png)

### Switch Path

By Test Port Number  Set displaying port number in the Test Port combo-
Boxes By Test Port Label  Set displaying port label in the Test Port Combo-
boxes VNA Port \- Shows the VNA port number Test Port \- Select test port by
number or label from the pulldown list.  Note: The path will not be switched
until user click the Apply button, in order to save the switch matrix
service lifetime.

### Test Port Label

Test Port Number \- Shows switch matrix test port numbers Test Port Label \-
User can edit port labels. They are per-channel settings, different channels
can have different port labels. Labels will be saved in state file.

### De-embedding

Enable De-embedding Switch Paths \- Sets de-embedding switch matrix state
on/off. By default, it is checked. Apply the Cal Set stimulus to the channel
\- Check to apply the Cal Set stimulus values to the channel. Tier 1 Cal Set
\- Selects Tier 1 Cal Set. Channel \- Default channel is E-TDR. User can
select another Standard channel if exists. Apply \- Apply settings:

  * Switch path
  * Apply test port label settings
  * If Enable De-embedding Switch Paths checked, a new Cal Set will be created with corresponding S2P files de-embedded from the Tier 1 Cal Set, the new Cal Set will be applied to selected Channel. The new Cal Set will be named as <Tier1 Cal Set Name>_<External Device Name>_<test port num>_<test port num>_<test port num>_<test port num>; for example, my Tier 1 Cal Set name is UsbCtTdr, my external device named L8990mUsbTdr, a new Cal Set UsbCtTdr_L8990mUsbTdr_17_18_19_20 will be created when user switch paths to the switch matrix test ports 17, 18, 19 and 20.

OK \- Apply settings and close dialog.


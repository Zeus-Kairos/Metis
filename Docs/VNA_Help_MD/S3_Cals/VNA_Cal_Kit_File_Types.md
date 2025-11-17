# VNA Cal Kit File Types

* * *

The VNA Cal Kit editor can open the following types of Cal Kit files:

VNA Families |  File Type  
---|---  
Cal Kits supported by current firmware of these VNA models: PNA Series, E5080A/B, FieldFox, and PXI Series |  *.xkt  
Old PNA Series Cal Kits (PNA Firmware A.07.50 to A.09.90) |  *.ckt  
Old PNA Series Cal Kit (before A.07.50) |  *.ck1  
Previous FieldFox format Cal Kits |  *.xml  
Previous ENA format Cal Kits |  *.ckx  
8510 Cal Kit |  .CK_*  
8753, 8752, 8719, 8720, or 8722 Cal Kit |  *.ck  
  
Download a zipped folder of the latest revision of [VNA Calibration Kit
Definitions](https://www.keysight.com/us/en/library/idx/miscellaneous/vna-
calibration-kit-definitions.html).

### File Save (As)

The VNA Cal Kit Editor can save Cal Kits in one of three file formats:

  * *.xkt \- Newer format that is based on xml and is shared among VNA families.

  * *.ckt \- VNA binary format, provided for backwards compatibility with older VNA firmware revisions and may not support future new cal kit capabilities, which is expected of the *.xkt format.

  * *.prn \- Cal kit print files. This is a text file format which can be read into spreadsheets, but the Cal Kit Editor does not read-in these files. These files are only produced as a form of documentation.

### About Opening Legacy VNA Kits

Cal kit files from Keysight "legacy" network analyzers (listed above) may not
contain information that the VNA requires. When loaded into the VNA Cal Kit
Editor, the cal kit name and description, the cal standards, and the cal class
assignments will be modified in a best effort manner. You may need to correct
these modifications after importing your legacy cal kit to meet your specific
requirements.

  * "Legacy" cal kit files are based on the analyzer test port sex. Modern VNA cal kits are based on the Device Under Test (DUT) connector sex. Therefore, when the kit is imported the standard's label and description are reversed and are noted as F- (female) and M- (male) .

  * When a Coaxial standard is detected in the kit file, a pair of male/female connectors is typically created.

  * Waveguide standards that are created as connector have no gender.

### File Association

With the exception of *.xml, the above file types are automatically associated
with the CalKit Editor if they are not already associated with a different
program. That means, after running CalKit Editor, double-clicking any of the
above file types (except *.xml) will open the file using CalKit Editor.

If you have already associated one of these file types with a different
program and would like to change it to CalKit Editor, do the following:

  1. Right-click the file, then click Open With

  2. Browse to the CalKitEditor install folder.

     * C:\Program Files (x86)\Agilent\VNA Cal Kit Editor

  3. Check Always use the selected program to open this kind of file.

  4. Select CalKit Editor.

* * *


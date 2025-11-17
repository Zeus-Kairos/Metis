# TRL Calibration

* * *

TRL (Thru, Reflect, Line) represents a family of calibration techniques that
measure two transmission standards and one reflection standard to determine
the 2-port 12-term error coefficients. For example, TRM (Thru, Reflect,
Match), LRL (Line, Reflect, Line), LRM (Line, Reflect, Match) are all included
in this family.

The traditional SOLT calibration measures one transmission standard (T) and
three reflection standards (SOL) to determine the same error coefficients.

  * [Why Perform a TRL Cal?](TRL_Calibration.md#Why)

  * [The TRL Calibration Process](TRL_Calibration.md#process)

  * [TRL Cal Kits](TRL_Calibration.md#calkits)

  * [Cal Standards Used in TRL](TRL_Calibration.md#Standards)

  * [TRL on 4-port PNA-L and ALL Models with an External Test Set](TRL_Calibration.md#4Port)

[See other Calibration Topics](Calibration.md)

Why Perform a TRL Cal?

TRL calibration is extremely accurate, in most cases more accurate than an
SOLT cal. However, very few calibration kits contain TRL standards. TRL Cal is
most often performed when you require a high level of accuracy and do not have
calibration standards in the same connector type as your DUT. This is usually
the case when using test fixtures, or making on-wafer measurements with
probes. Therefore, in some cases you must construct and characterize standards
in the same media type as your DUT configuration. It is easier to manufacture
and characterize three TRL standards than the four SOLT standards.

Another advantage of TRL calibration is that the TRL standards need not be
defined as completely and accurately as the SOLT standards. While SOLT
standards are completely characterized and stored as the standard definition,
TRL standards are modeled, and not completely characterized. However, TRL cal
accuracy is directly proportional to the quality and repeatability of the TRL
standards. Physical discontinuities, such as bends in the transmission lines
and beads in coaxial structures, will degrade the TRL calibration. The
connectors must be clean and allow repeatable connections.

To learn more about Cal Standard requirements, see [Cal Standards Used in
TRL](TRL_Calibration.htm#Standards).

Note: Virtual Device describes a non-physical (connect the two test port
reference planes together) type of connection description during the
calibration. So, in a cal kit definition, you should not define more than one
Thru standard with the _same connector/gender pairing_ to each Virtual Device.
This could cause those Thru standards to all be treated as the same physical
connection step during a calibration, which would especially be a problem for
TRL calibrations if a Thru standard and Line standard were measured as the
same connection step.

The TRL Cal Process

Although TRL can be performed using the Cal Wizard Unguided Cal selection, the
following process uses the easier [SmartCal](Calibration_Wizard.md#GuidedCal)
selection. Both selections require that you already have TRL calibration
standards defined and included in a VNA cal kit.

  1. Preset the VNA

  2. Set up a measurement and the desired stimulus settings.

  3. Press Cal > Main > Other Cals > Smart Cal....

  4. [Select the DUT connectors and Cal Kit](Calibration_Wizard.md#GuidConnKit) for each port. The LOWEST port number of each [port pair](Calibration_Wizard.md#ModifyCal) MUST include TRL standards. TRL appears as the Cal Method.

  5. Check Modify Cal, Next, then View/Modify to change [default TRL options](TRL_Tab.md) if necessary.

  6. Follow the prompts to complete the calibration.

  7. [Check the accuracy](Quest_Cal.md#PerformQuickCheck) of the calibration

TRL Cal Kits

Keysight Technologies offers two cal kits that include the required standards
to perform a TRL calibration: 85050C (APC 7mm) and 85052C (3.5mm). Both kits
include the traditional Short, Open, and Load standards. (The Thru standard,
not actually supplied, assumes a [zero-length
Thru](Calibration_THRU_Methods.htm#Flush)). In addition, the kits include an
airline which is used as the LINE standard. To use the airline, the kits
include an airline body, center conductor, and insertion / extraction tools.
The APC 7 kit includes an adapter to connect the airline to the APC connector.

Cal Standards Used in TRL

These standards must be defined in your TRL cal kit:

### THRU

Note: All [THRU calibration methods](Calibration_THRU_Methods.md) are
supported in a TRL Cal EXCEPT Unknown Thru.

  * The THRU standard can be either a zero-length or non-zero length. However, a zero-length THRU is more accurate because it has zero loss and no reflections, by definition.

  * The THRU standard cannot be the same electrical length as the LINE standard.

  * If the insertion phase and electrical length are well-defined, the THRU standard may be used to [set the reference plane](TRL_Tab.md#Reference).

  * Characteristic impedance of the THRU and LINE standards defines the reference impedance of the calibration.

  * If a THRU standard with the correct connectors is NOT available, an adapter removal cal can be performed.

### REFLECT

  * The REFLECT standard can be anything with a high reflection, as long as it is the same when connected to both VNA ports.

  * The actual magnitude of the reflection need not be known.

  * The phase of the reflection standard must be known within 1/4 wavelength.

  * If the magnitude and phase of the reflection standard are well-defined, the standard may be used to [set the reference plane](TRL_Tab.md#Reference).

### LINE

The LINE and THRU standards establish the reference impedance for the
measurement after the calibration is completed. TRL calibration is limited by
the following restrictions of the LINE standard:

  * Must be of the same impedance and propagation constant as the THRU standard.

  * The electrical length need only be specified within 1/4 wavelength.

  * Cannot be the same length as the THRU standard.

  * A TRL cal with broad frequency coverage requires multiple LINE standards. For example, a span from 2 GHz to 26 GHz requires two line standards.

  * Must be an appropriate electrical length for the frequency range: at each frequency, the phase difference between the THRU and the LINE should be greater than 20 degrees and less than 160 degrees. This means in practice that a single LINE standard is only usable over an 8:1 frequency range (Frequency Span / Start Frequency). Therefore, for broad frequency coverage, multiple lines are required.

  * At low frequencies, the LINE standard can become too long for practical use. The optimal length of the LINE standard is 1/4 wavelength at the geometric mean of the frequency span (square root of f1 x f2).

Note: The TRL LINE standard must have a delay that is greater than 0 (zero)
ps. Otherwise, calibration correction calculations will contain unpredictable
results.

### MATCH

If the LINE standard of appropriate length or loss cannot be fabricated, a
MATCH standard may be used instead of the LINE.

  * The MATCH standard is a low-reflection termination connected to both Port 1 and Port 2.

  * The MATCH standard may be defined as an infinite length transmission line OR as a 1-port low reflect termination, such as a load.

  * When defined as an infinite length transmission line, both test ports must be terminated by a MATCH standard at the same time. When defined as a 1-port load standard, the loads are measured separately. The loads are assumed to have the same characteristics.

  * The impedance of the MATCH standard becomes the reference impedance for the measurement. For best results, use the same load on both ports. The load may be defined using the data-based definition, the arbitrary impedance definition, or the fixed load definition.

### See Also

  * See [Modify Calibration Kits](ModifyCalKits.md) for detailed information about creating and modifying Calibration kit definitions.

  * For more information, read [Specifying Calibration Standards and Kits for Keysight Vector Network Analyzers (Application Note 1287-11](http://literature.cdn.Keysight.com/litweb/pdf/5989-4840EN.pdf))

TRL on a 4-port PNA-L and ALL VNA Models with an External Test Set

Beginning with the VNA code revision 5.25, TRL CAN be performed on a 4-port
PNA-L and ALL VNA Models with an [External Test
Set](../System/External_Testset_Control.htm) enabled. Previously, a TRL
calibration required a VNA with a reference receiver for each test port. With
the new TRL method, a Delta Match Calibration is first performed and applied.

Note: See [Delta Match Calibration](Delta_Match_Calibration.md) to learn
which models require this.

The accuracy of this TRL cal greatly depends on the accuracy of the Delta
Match Calibration. With an accurate Delta Match Calibration, the difference in
accuracy between a traditional TRL cal and this TRL cal is negligible.

### How to Perform a TRL Cal in these cases

  1. Press Cal > Main > Other Cals > Smart Cal....

  2. Select a TRL cal kit for the ports to be calibrated.

  3. During the calibration, the Cal Wizard prompts you for a [valid Delta Match Cal.](Calibration_Wizard.md#SelectDMCalSet)

* * *


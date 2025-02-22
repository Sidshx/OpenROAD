from openroad import Design, Tech
import helpers
import pdnsim_aux

tech = Tech()
tech.readLef("Nangate45.lef")
tech.readLiberty("NangateOpenCellLibrary_typical.lib")

design = Design(tech)
design.readDef("gcd.def")
design.evalTclString("read_sdc gcd.sdc")

voltage_file = helpers.make_result_file("gcd_voltage_vdd.rpt")
error_file = helpers.make_result_file("gcd_error_vdd.rpt")
pdnsim_aux.check_power_grid(design, net="VDD")

pdnsim_aux.analyze_power_grid(design, vsrc="Vsrc_gcd_vdd.loc", net="VDD",
                              outfile=voltage_file,
                              error_file=error_file)

helpers.diff_files(voltage_file, "gcd_voltage_vdd.rptok")
helpers.diff_files(error_file, "gcd_error_vdd.rptok")

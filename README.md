# pim-dram

## Project
Implement Processing using Memory (PuM) in COTS DRAM on an FPGA development board. This processing should allow for the quicker calculation of trigger signal, indicating that the data entering the SDRAM should be retained. A faster trigger should allow for a smaller buffer of data to be kept, reducing the memory requirements for a project.

## Target users
Users in the business of data acquisition with large data volumes that include irrelevant data that must be discarded to allow for the capture of important time frames.

## User Stories
- As the management of a business with data acquisition needs, I want to reduce the materials costs while not introducing high engineering costs. An example of a reduced cost could be switching from custom FPGAs to development boards if memory limitations are no longer the main constraint.
- As a high-speed data acquisition firmware engineer, I want to create functional systems without the need for writing complicated custom blocks. I only want to use IP that has been robustly tested, especially if it is violating standard timing requirements.

## MVP
- Simulation for performing processing using memory
- Modeling showing write cycle comparison for time frames

## Plan for Sprints 4 & 5
- Finish DRAM controller functionality
- Integrate with DRAM-Voltage SPICE MODEL using ngspice
- Perform Monte-Carlo sim for various operations

## Plan for Sprint 3
- Re-evaluate boards due to Micron DRAM issue
- Rewrite documentation to include needed information
- Outline Python section of controller

## Plan for Sprint 2
- Select board options and determine feasibility/costs
- Evaluate differences between LiteDRAM and PiDRAM options
- (Stretch) Run RowClone simulation with selected controller in Vivado
- Draft message to send to Prof. Herbordt

## Board Feasibility

| Name            | Price Feasible | Vendor       | Chip                       | Chip Vendor | DRAM Type | DRAM Manufacturer | DRAM P/N            | Cost    | Notes                              |
|-----------------|----------------|--------------|----------------------------|-------------|-----------|-------------------|---------------------|---------|------------------------------------|
| ZCU102          | Y              | Xilinx/AMD   | Zynq UltraScale+ XCZU9EG   | AMD         | DDR4      | Micron            | MT40A256M16GE-075E  | N/A     |                                    |
| Arria V GX Dev  | Y              | Altera/Intel | Arria V GX 5AGXFB3H4F35C4N | Intel       | DDR3      | Micron            | MT41J64M16LA-15E    | N/A     | 2 DRAMs on board                   |
| Arty S7         | Y              | Diligent     | XC7S25-CSGA324             | AMD         | DDR3      | Micron            | MT41K128M16JT-125:K |    $119 | Also available with XC7S50-CSGA324 |
| Bittware XUSP3S | N/A            | Obsolete :(  |                            |             |           |                   |                     |         | From DRAMBender Supported List     |
| Bittware XUPP3R | N              |              |                            |             |           |                   |                     | $10,321 | From DRAMBender Supported List     |
| Bittware XUPVVH | N              |              |                            |             |           |                   |                     | $15,000 | From DRAMBender Supported List     |
| Alveo™ U200     | N              |              |                            |             |           |                   |                     |  $5,000 | From DRAMBender Supported List     |
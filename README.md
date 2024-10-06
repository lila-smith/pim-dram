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

## Plan for Sprint 2
- Select board options and determine feasibility/costs
- Evaluate differences between LiteDRAM and PiDRAM options
- (Stretch) Run RowClone simulation with selected controller in Vivado
- Draft message to send to Prof. Herbordt

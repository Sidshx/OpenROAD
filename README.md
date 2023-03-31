# The OpenROAD 7nm Physical Design Contest
![image](https://user-images.githubusercontent.com/73933646/229139296-880b3b65-d2af-433e-97ed-804112b0a4d4.png)

## Design Name: gcd
## Literature Survey Report:
## Final Report: 
## Machine specifications
![image](https://user-images.githubusercontent.com/73933646/229139551-a519f7dc-0e37-487f-8628-327fa67b3411.png)

## Important Links 
- [OpenROAD Modified Code](https://github.com/Sidshx/OpenROAD/tree/7nmcontest/src)
## Steps followed:
1. Open OpenROAD-flow script and navigate to flow
2. Run make ```make clean_all DESIGN_CONFIG=./designs/asap7/gcd/config.mk```
3. Run ```make DESIGN_CONFIG=./designs/asap7/gcd/config.mk```
4. Return to  OpenROAD-flow script.
5. Build and install using ```./build_openroad.sh --local```
6. Note the timings from the logs
7. Change the Cpp code in the OpenROAD-flow-scripts/tools/OpenROAD/tools
8. Repeat from **Step 1** again
## Final Run Time after code modifications
![image](https://user-images.githubusercontent.com/58599984/228294893-6f5bfca1-6386-42da-9984-0972c6a86e2b.png)
## Changes made in the [gpuSolver.cu](https://github.com/Eyantra698Sumanto/OpenROAD-flow-scripts/tree/7nmcontest/tools/OpenROAD1/src/gpl/src)
![image](https://user-images.githubusercontent.com/58599984/228294648-7c1df1da-ca05-454f-8cf7-8aec489ac4b5.png)


### Improvement in the Placement Stage timing
![image](https://user-images.githubusercontent.com/58599984/228300190-5390745f-affb-45b8-99f0-7465afaf3bba.png)

## Changes made in [nesterovPlace.cpp](https://github.com/Eyantra698Sumanto/OpenROAD-flow-scripts/tree/7nmcontest/tools/OpenROAD1/src/gpl/src)
![image](https://user-images.githubusercontent.com/58599984/228318635-0d807721-50e5-43c9-8b89-e968c676301a.png)

### Improvement in the Placement Stage timing
![image](https://user-images.githubusercontent.com/58599984/228318784-6d66e01f-953c-4f8b-95b7-022c0f16a582.png)

## Changes made in [solver.cpp](https://github.com/Eyantra698Sumanto/OpenROAD-flow-scripts/tree/7nmcontest/tools/OpenROAD1/src/gpl/src)
![image](https://user-images.githubusercontent.com/58599984/228338100-e357c884-8731-41ab-96a8-e6cfcba29169.png)

### Improvement in the Placement Stage timing
![image](https://user-images.githubusercontent.com/58599984/228324932-738966d1-c5aa-481c-849c-eb550c3a912e.png)

## Changes made in [fftsg.cpp](https://github.com/Eyantra698Sumanto/OpenROAD-flow-scripts/tree/7nmcontest/tools/OpenROAD1/src/gpl/src) rdft() function
![image](https://user-images.githubusercontent.com/58599984/228340068-a972819b-7efd-45c1-8b33-170c0901b5f5.png)

### Improvement in the Placement Stage timing
![image](https://user-images.githubusercontent.com/58599984/228339817-daa6aee9-70d0-46d2-8ded-62c77061b3eb.png)

## Conclusion and Future Scope
Thus, we have obtained considerable improvement in the timings by makinf changes in the C code of each block.

Further Optimization can be done by changing the other blocks of the code and reducing the complexity of codes.

Thank You!
# Acknowledgement
1. OpenROAD Team
2. VSD and team

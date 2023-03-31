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
![image](https://user-images.githubusercontent.com/73933646/229144094-27e4023c-49ae-44fe-b394-60e9ae72eb53.png)

## Improvements made in the [Clustering.cpp](https://github.com/Sidshx/OpenROAD/blob/7nmcontest/src/cts/src/Clustering.cpp)
![image](https://user-images.githubusercontent.com/73933646/229144240-20e68fc5-7e37-477b-82ba-00eea02b38d3.png)


### Changes in the [maze.cpp](https://github.com/Sidshx/OpenROAD/blob/7nmcontest/src/grt/src/fastroute/src/maze.cpp)
![image](https://user-images.githubusercontent.com/73933646/229144560-08cc98ab-8b05-4605-89eb-2332b0f81a11.png)

## Changes made in [TritonCTS.cpp](https://github.com/Sidshx/OpenROAD/blob/7nmcontest/src/cts/src/TritonCTS.cpp)
![image](https://user-images.githubusercontent.com/73933646/229145126-f19cfdb2-da50-417b-bc3c-8cdbc4a222b8.png)

## Conclusion and Future Scope
Thus, we have obtained considerable improvement in the timings by makinf changes in the C code of each block.

Further Optimization can be done by changing the other blocks of the code and reducing the complexity of codes.

Thank You!
# Acknowledgement
1. OpenROAD Team
2. VSD and team

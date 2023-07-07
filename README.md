![openroad_cerificate](https://github.com/Sidshx/OpenROAD/assets/73933646/f689b6b8-f6c5-4cb3-b60e-b1e90052b465)


# The OpenROAD 7nm Physical Design Contest
![image](https://user-images.githubusercontent.com/73933646/229139296-880b3b65-d2af-433e-97ed-804112b0a4d4.png)

## Design Name: gcd
## [Literature Survey Report](https://docs.google.com/document/d/1_EmDNZOXrt2lwTWwUcMA-rv0W4KkOsrSRfKJxpDRPps/edit?usp=sharing)
## [Final Report](https://docs.google.com/document/d/1Y1fpabV6v860-7_wdSvFU7Y5UtaJgEVNsNxSbfJNCIw/edit?usp=sharing)
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

## Run Time before code modifications
![image](https://user-images.githubusercontent.com/73933646/229151955-fc61d944-3a63-4dd8-ae45-51c14dbafab7.png)

## Final Run Time after code modifications
![image](https://user-images.githubusercontent.com/73933646/229144094-27e4023c-49ae-44fe-b394-60e9ae72eb53.png)

## 1. Changes made in the [Clustering.cpp](https://github.com/Sidshx/OpenROAD/blob/7nmcontest/src/cts/src/Clustering.cpp)
![image](https://user-images.githubusercontent.com/73933646/229144240-20e68fc5-7e37-477b-82ba-00eea02b38d3.png)

1. Means is copied to tmp_means and is unnecessarily leading to memory consumption, so we are calling means directly, 
2. Here Kmeans is called for each iteration of i, but its result remains the same if the means value hasn't changed. So we instead do a check ‘means == prev_means’, if true, the current value of max_silh is not updated, and the previous value of prev_silh is used instead; otherwise, the Kmeans function is used, and the silh score is updated appropriately.

### Runtime before making code changes
![image](https://user-images.githubusercontent.com/73933646/229146789-b700a9e1-c102-49fb-9cec-011c7894ed21.png)

### Runtime improvements post code changes
![image](https://user-images.githubusercontent.com/73933646/229147207-c849e95a-c580-49fd-bb42-4295a3684633.png)

## 2. Changes in the [maze.cpp](https://github.com/Sidshx/OpenROAD/blob/7nmcontest/src/grt/src/fastroute/src/maze.cpp)
![image](https://user-images.githubusercontent.com/73933646/229144560-08cc98ab-8b05-4605-89eb-2332b0f81a11.png)
1. Ternary operators changed to if else statements in line 240 and 260

### Runtime before making code changes
![image](https://user-images.githubusercontent.com/73933646/229147638-e41d3444-493a-4713-8ae4-56d362e8f880.png)


### Runtime improvements post code changes
![image](https://user-images.githubusercontent.com/73933646/229147736-f528fd98-5cf8-4a7b-b033-0e6eadf58829.png)



## 3. Changes made in [TritonCTS.cpp](https://github.com/Sidshx/OpenROAD/blob/7nmcontest/src/cts/src/TritonCTS.cpp)
![image](https://user-images.githubusercontent.com/73933646/229145126-f19cfdb2-da50-417b-bc3c-8cdbc4a222b8.png)
1. Converted Ternary Operator to simple If-else statement as an attempt to improve  runtime. Expected better results in runtime in this code due to the presence of ternary block which is in a for loop iterating over each object in a leaf pin.


### Runtime before making code changes
![image](https://user-images.githubusercontent.com/73933646/229148103-46936e38-e7f3-449b-8b25-c844dee7c357.png)



### Runtime improvements post code changes
![image](https://user-images.githubusercontent.com/73933646/229148226-de53a8c8-413e-4c53-b162-7adef2a67d46.png)


## Conclusion and Future Scope
Thus, we have obtained considerable improvement in the timings by making changes in the Cpp code of majorly the cts and grt tool.

Further Optimization can be done by changing the other blocks of the code and reducing the complexity of codes.

Thank You!
# Acknowledgement
1. OpenROAD Team
2. VSD and team

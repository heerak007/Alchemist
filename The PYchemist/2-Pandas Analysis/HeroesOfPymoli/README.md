
### Heroes Of Pymoli Data Analysis
* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
-----

### Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.


```python
# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
GameDF = pd.read_csv(file_to_load)

# Printing the count and data types to see what is an object vs float vs int
print(f'{GameDF.count()}\n')
print(GameDF.dtypes)

GameDF.head()
```

    Purchase ID    780
    SN             780
    Age            780
    Gender         780
    Item ID        780
    Item Name      780
    Price          780
    dtype: int64
    
    Purchase ID      int64
    SN              object
    Age              int64
    Gender          object
    Item ID          int64
    Item Name       object
    Price          float64
    dtype: object





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count


```python
TotalPlayers = GameDF["SN"].unique()
len(TotalPlayers)
```




    576



## Purchasing Analysis (Total)


```python
# Taking original DataFrame and condensing it(unique values, or groupby) based on the goal
Unique = GameDF["Item ID"].unique()
Average = GameDF["Price"].mean()
NumofPur = len(GameDF["Purchase ID"])
TotalRev = GameDF["Price"].sum()

#creating the dataframe for the values calculated above
SumTotal = pd.DataFrame([{
            'Unique Items':len(Unique), 
            'Avg Price':Average, 
            "Number of Purchases":NumofPur, 
            "Total Revenue":TotalRev
            }])

# Possible way to do formats like below, keeping it for future reference
# SumTotal.style.format({
#             'Avg price': "${:,.2f}",  
#             'Total Revenue': '${:,.2f}'
#             })

# Using the mapping function to format the values to desired result
SumTotal["Avg Price"] = SumTotal["Avg Price"].map("${:.2f}".format)
SumTotal["Total Revenue"] = SumTotal["Total Revenue"].map("${:.2f}".format)

#organizing the data columns
SumTotal = SumTotal[["Unique Items","Avg Price","Number of Purchases","Total Revenue"]]

SumTotal
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unique Items</th>
      <th>Avg Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>183</td>
      <td>$3.05</td>
      <td>780</td>
      <td>$2379.77</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics


```python
# Taking original DataFrame and condensing it(unique values, or groupby) based on the goal
# Important to note of using count() vs value_counts(). count() can be used for counting the grouped by DF,
# Whereas value_counts() should be used from a NON-groupedby DF, such as the original DF
GenderVCount = GameDF["Gender"].value_counts()
GenderPercent = GenderVCount/GenderVCount.sum()

# Finding the non repetative values and its associated calculations
UniqueGender = GameDF.drop_duplicates("SN")
UniqueGenCount = UniqueGender["Gender"].value_counts()
UniquePercent = UniqueGenCount/len(TotalPlayers)

# Differenciating the repeat buys based on the total buys
RepeatBuy = GenderVCount-UniqueGenCount
RepeatPercent = RepeatBuy/GenderVCount

GenderDemo = pd.DataFrame({"Total Purchase Count": GenderVCount,
                            "Percentage": GenderPercent,
                            "Unique Player Count": UniqueGenCount,
                            "Unique Percentage": UniquePercent,
                            "Repeat Buy": RepeatBuy,
                            "Repeat Percentage": RepeatPercent

                          
                          }) 
GenderDemo["Percentage"] = GenderDemo["Percentage"].map('{:.1%}'.format)
GenderDemo["Unique Percentage"] = GenderDemo["Unique Percentage"].map('{:.1%}'.format)
GenderDemo["Repeat Percentage"] = GenderDemo["Repeat Percentage"].map('{:.1%}'.format)

GenderDemo = GenderDemo[["Total Purchase Count","Percentage","Unique Player Count","Unique Percentage","Repeat Buy","Repeat Percentage"]]


GenderDemo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Count</th>
      <th>Percentage</th>
      <th>Unique Player Count</th>
      <th>Unique Percentage</th>
      <th>Repeat Buy</th>
      <th>Repeat Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>83.6%</td>
      <td>484</td>
      <td>84.0%</td>
      <td>168</td>
      <td>25.8%</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>113</td>
      <td>14.5%</td>
      <td>81</td>
      <td>14.1%</td>
      <td>32</td>
      <td>28.3%</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>15</td>
      <td>1.9%</td>
      <td>11</td>
      <td>1.9%</td>
      <td>4</td>
      <td>26.7%</td>
    </tr>
  </tbody>
</table>
</div>



Table 1

The table above shows us the total number of purchases based on gender, and then adds the individual player count based on gender. In other words, amongst the players of the game the vast majority is made up of Males (84%), where males also make up the largest percentage of sales (83.6%). However, when considereing repeat buys, Females are more likely to buy a product again than the Male counterpart. This tells us that Males are a strong target market for the game and its products, while Females make the most "loyal" customers. 


## Purchasing Analysis (Gender)


```python
GenderGroup = GameDF.groupby(["Gender"])
GenTotalPurchase = GenderGroup["Price"].sum()
GenAvgPurchase = GenTotalPurchase/ UniqueGenCount

MaxGender = GenderGroup["Price"].max()
MinGender = GenderGroup["Price"].min()
GenNormalize = GenTotalPurchase/ GenderVCount

GenderAnalysis = pd.DataFrame({ "Purchase Count": GenderVCount,
                                "Average Purchase": GenAvgPurchase,
                                "Total Purchase": GenTotalPurchase,
                                "Normalized Avg": GenNormalize})

GenderAnalysis["Average Purchase"] = GenderAnalysis["Average Purchase"].map('${:,.2f}'.format)
GenderAnalysis["Total Purchase"] = GenderAnalysis["Total Purchase"].map('${:,.2f}'.format)
GenderAnalysis["Normalized Avg"] = GenderAnalysis["Normalized Avg"].map('${:,.2f}'.format)

GenderAnalysis = GenderAnalysis[["Purchase Count","Total Purchase","Average Purchase","Normalized Avg"]]


GenderAnalysis

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase</th>
      <th>Average Purchase</th>
      <th>Normalized Avg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>113</td>
      <td>$361.94</td>
      <td>$4.47</td>
      <td>$3.20</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>652</td>
      <td>$1,967.64</td>
      <td>$4.07</td>
      <td>$3.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>15</td>
      <td>$50.19</td>
      <td>$4.56</td>
      <td>$3.35</td>
    </tr>
  </tbody>
</table>
</div>



Table 2

The table above shows us Males again make up the vast majority of purchase value. However an individual Female on average spends about $4.47, with each purchase averaging to $3.20. Which is higher than her counterparts, Male($4.07, $3.02) and Other($4.56, $3.35) respectively. Thus combining the results from Table 1 and Table 2, it shows that Females are likely to spend more, and be more loyal customers in terms of repeat buys. 

## Age Demographics


```python
# Establish bins for ages, and pd.cut() for making the list
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Adding a list called Age Range to the origianl DF, which later will be used to groupby
GameDF["Age Range"] = pd.cut(GameDF["Age"], age_bins, labels=group_names)

AgeVCount = GameDF["Age Range"].value_counts()
AgePercent = AgeVCount/AgeVCount.sum()

UniqueAge = GameDF.drop_duplicates("SN")
UniqueAgeCount = UniqueAge["Age Range"].value_counts()
UniqueAgePercent = UniqueAgeCount/len(TotalPlayers)

RepeatAgeBuy = AgeVCount-UniqueAgeCount
RepeatAgePercent = RepeatAgeBuy/AgeVCount


AgeDemo = pd.DataFrame({"Total Count": AgeVCount,
                        "Percentage": AgePercent,
                        "Unique Player Count": UniqueAgeCount,
                        "Unique Percentage": UniqueAgePercent,
                        "Repeat Buy": RepeatAgeBuy,
                        "Repeat Percentage": RepeatAgePercent}) 

AgeDemo["Percentage"] = AgeDemo["Percentage"].map('{:.1%}'.format)
AgeDemo["Unique Percentage"] = AgeDemo["Unique Percentage"].map('{:.1%}'.format)
AgeDemo["Repeat Percentage"] = AgeDemo["Repeat Percentage"].map('{:.1%}'.format)

AgeDemo = AgeDemo[["Total Count","Percentage","Unique Player Count","Unique Percentage","Repeat Buy","Repeat Percentage"]]

AgeDemo
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Count</th>
      <th>Percentage</th>
      <th>Unique Player Count</th>
      <th>Unique Percentage</th>
      <th>Repeat Buy</th>
      <th>Repeat Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>46.8%</td>
      <td>258</td>
      <td>44.8%</td>
      <td>107</td>
      <td>29.3%</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>17.4%</td>
      <td>107</td>
      <td>18.6%</td>
      <td>29</td>
      <td>21.3%</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>12.9%</td>
      <td>77</td>
      <td>13.4%</td>
      <td>24</td>
      <td>23.8%</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>9.4%</td>
      <td>52</td>
      <td>9.0%</td>
      <td>21</td>
      <td>28.8%</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>5.3%</td>
      <td>31</td>
      <td>5.4%</td>
      <td>10</td>
      <td>24.4%</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>3.6%</td>
      <td>22</td>
      <td>3.8%</td>
      <td>6</td>
      <td>21.4%</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>2.9%</td>
      <td>17</td>
      <td>3.0%</td>
      <td>6</td>
      <td>26.1%</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>1.7%</td>
      <td>12</td>
      <td>2.1%</td>
      <td>1</td>
      <td>7.7%</td>
    </tr>
  </tbody>
</table>
</div>



Table 3

By grouping the dataset into age ranges, it can give insight as to what age range is best the best and most loyal range. Table 3 shows us that 20-24 year olds make up the largest percentage of 44.8%, followed by 15-19 year olds (18.6%) and 25-29 year olds (13.4%). 20-24 year olds also make up the largest percentage of repeat buys (29.3%), making them the most loyal age range, followed by the 30-34 age range (28.8%). Hence showing 20-24 year olds to be the largest and most loyal players, making them the primary target age range. 

## Purchasing Analysis (Age)


```python
AgeGroup = GameDF.groupby(["Age Range"])
AgeTotalPurchase = AgeGroup["Price"].sum()
AgeAvgPurchase = AgeTotalPurchase/UniqueAgeCount
AgeNormalize = AgeTotalPurchase/AgeVCount

AgeAnalysis = pd.DataFrame({ "Purchase Count": AgeVCount,
                                "Average Purchase": AgeAvgPurchase,
                                "Total Purchase": AgeTotalPurchase,
                                "Normalized Avg": AgeNormalize})

# Sorting the Table based on criteria, which has to happen before formatting the dataframe
AgeAnalysis = AgeAnalysis.sort_values("Average Purchase", ascending=False)

AgeAnalysis["Average Purchase"] = AgeAnalysis["Average Purchase"].map('${:,.2f}'.format)
AgeAnalysis["Total Purchase"] = AgeAnalysis["Total Purchase"].map('${:,.2f}'.format)
AgeAnalysis["Normalized Avg"] = AgeAnalysis["Normalized Avg"].map('${:,.2f}'.format)

AgeAnalysis = AgeAnalysis[["Purchase Count","Total Purchase","Average Purchase","Normalized Avg"]]
AgeAnalysis
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Total Purchase</th>
      <th>Average Purchase</th>
      <th>Normalized Avg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>35-39</th>
      <td>41</td>
      <td>$147.67</td>
      <td>$4.76</td>
      <td>$3.60</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>23</td>
      <td>$77.13</td>
      <td>$4.54</td>
      <td>$3.35</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>365</td>
      <td>$1,114.06</td>
      <td>$4.32</td>
      <td>$3.05</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>73</td>
      <td>$214.00</td>
      <td>$4.12</td>
      <td>$2.93</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>136</td>
      <td>$412.89</td>
      <td>$3.86</td>
      <td>$3.04</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>101</td>
      <td>$293.00</td>
      <td>$3.81</td>
      <td>$2.90</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>28</td>
      <td>$82.78</td>
      <td>$3.76</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>13</td>
      <td>$38.24</td>
      <td>$3.19</td>
      <td>$2.94</td>
    </tr>
  </tbody>
</table>
</div>



Table 4

Table 4 shows us that although 20-24 year olds spend the most as a total, individually 35-39 year olds spend the most on average being $4.76 with an average of $3.60 for each purchase. Making them the highest spenders, though important to keep in mind they have a fairly low total purchase value and constitute for only 5% of the demographic. 

## Top Spenders


```python
TopSpenders = GameDF.groupby(["SN"])
TopCount = TopSpenders["SN"].count()
TopTotalPurchase = TopSpenders["Price"].sum()
TopAvgPurchase = TopSpenders["Price"].mean()

TopTable = pd.DataFrame({   "Purchase Count": TopCount,
                            "Average Purchase": TopAvgPurchase,
                            "Total Purchase": TopTotalPurchase
                            })

# Sorting the Table based on criteria, which has to happen before formatting the dataframe
TopTable = TopTable.sort_values("Total Purchase", ascending=False)

TopTable["Average Purchase"] = TopTable["Average Purchase"].map('${:,.2f}'.format)
TopTable["Total Purchase"] = TopTable["Total Purchase"].map('${:,.2f}'.format)

TopTable = TopTable[["Purchase Count","Average Purchase","Total Purchase"]]

print(TopTable["Purchase Count"].value_counts())
TopTable.head(10)
```

    1    414
    2    124
    3     35
    4      2
    5      1
    Name: Purchase Count, dtype: int64





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase</th>
      <th>Total Purchase</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>5</td>
      <td>$3.79</td>
      <td>$18.96</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>4</td>
      <td>$3.86</td>
      <td>$15.45</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>3</td>
      <td>$4.61</td>
      <td>$13.83</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>4</td>
      <td>$3.40</td>
      <td>$13.62</td>
    </tr>
    <tr>
      <th>Iskadarya95</th>
      <td>3</td>
      <td>$4.37</td>
      <td>$13.10</td>
    </tr>
    <tr>
      <th>Ilarin91</th>
      <td>3</td>
      <td>$4.23</td>
      <td>$12.70</td>
    </tr>
    <tr>
      <th>Ialallo29</th>
      <td>3</td>
      <td>$3.95</td>
      <td>$11.84</td>
    </tr>
    <tr>
      <th>Tyidaim51</th>
      <td>3</td>
      <td>$3.94</td>
      <td>$11.83</td>
    </tr>
    <tr>
      <th>Lassilsala30</th>
      <td>3</td>
      <td>$3.84</td>
      <td>$11.51</td>
    </tr>
    <tr>
      <th>Chadolyla44</th>
      <td>3</td>
      <td>$3.82</td>
      <td>$11.46</td>
    </tr>
  </tbody>
</table>
</div>



Table 5

This shows us that the most number of repeat buys is 5, coming from Lisosia93. The relationship between Repeat buys(Purchase Count) and its count seems to behave like an exponential decay function. Where one buy consitiutes for a count of 414, and 5 buys for only 1 occurance. 

## Most Popular Items


```python
TopItems = GameDF.groupby(["Item ID","Item Name"])
TopItemCount = TopItems["Item ID"].count()
ItemTotalPurchase = TopItems["Price"].sum()
ItemAvgPurchase = TopItems["Price"].mean()

TopItemTable = pd.DataFrame({   "Purchase Count": TopItemCount,
                            "Average Purchase": ItemAvgPurchase,
                            "Total Purchase": ItemTotalPurchase
                            })

TopItemDF = TopItemTable.sort_values("Purchase Count", ascending=False)

TopItemDF["Average Purchase"] = TopItemDF["Average Purchase"].map('${:,.2f}'.format)
TopItemDF["Total Purchase"] = TopItemDF["Total Purchase"].map('${:,.2f}'.format)

TopItemDF = TopItemDF[["Purchase Count","Average Purchase","Total Purchase"]]

TopItemDF.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase</th>
      <th>Total Purchase</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>$3.53</td>
      <td>$31.77</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>19</th>
      <th>Pursuit, Cudgel of Necromancy</th>
      <td>8</td>
      <td>$1.02</td>
      <td>$8.16</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>8</td>
      <td>$4.35</td>
      <td>$34.80</td>
    </tr>
    <tr>
      <th>75</th>
      <th>Brutality Ivory Warmace</th>
      <td>8</td>
      <td>$2.42</td>
      <td>$19.36</td>
    </tr>
    <tr>
      <th>72</th>
      <th>Winter's Bite</th>
      <td>8</td>
      <td>$3.77</td>
      <td>$30.16</td>
    </tr>
    <tr>
      <th>60</th>
      <th>Wolf</th>
      <td>8</td>
      <td>$3.54</td>
      <td>$28.32</td>
    </tr>
    <tr>
      <th>59</th>
      <th>Lightning, Etcher of the King</th>
      <td>8</td>
      <td>$4.23</td>
      <td>$33.84</td>
    </tr>
  </tbody>
</table>
</div>



Table 6

## Most Profitable Items


```python
TopProfitTable = TopItemTable.sort_values("Total Purchase", ascending=False)

TopProfitTable["Average Purchase"] = TopProfitTable["Average Purchase"].map('${:,.2f}'.format)
TopProfitTable["Total Purchase"] = TopProfitTable["Total Purchase"].map('${:,.2f}'.format)

TopProfitTable = TopProfitTable[["Purchase Count","Average Purchase","Total Purchase"]]

TopProfitTable.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase</th>
      <th>Total Purchase</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>12</td>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>9</td>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>9</td>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>92</th>
      <th>Final Critic</th>
      <td>8</td>
      <td>$4.88</td>
      <td>$39.04</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>8</td>
      <td>$4.35</td>
      <td>$34.80</td>
    </tr>
    <tr>
      <th>59</th>
      <th>Lightning, Etcher of the King</th>
      <td>8</td>
      <td>$4.23</td>
      <td>$33.84</td>
    </tr>
    <tr>
      <th>108</th>
      <th>Extraction, Quickblade Of Trembling Hands</th>
      <td>9</td>
      <td>$3.53</td>
      <td>$31.77</td>
    </tr>
    <tr>
      <th>78</th>
      <th>Glimmer, Ender of the Moon</th>
      <td>7</td>
      <td>$4.40</td>
      <td>$30.80</td>
    </tr>
    <tr>
      <th>72</th>
      <th>Winter's Bite</th>
      <td>8</td>
      <td>$3.77</td>
      <td>$30.16</td>
    </tr>
    <tr>
      <th>60</th>
      <th>Wolf</th>
      <td>8</td>
      <td>$3.54</td>
      <td>$28.32</td>
    </tr>
  </tbody>
</table>
</div>



Table 7

Table 6 and 7 shows us that item "Oathbreaker, Last Hope of the Breaking Storm" is the most popular with a count of 12 and the most profitible item generating $50.76. The second most popular and profitable is Nirvana with a profit of $41.22 and purchase count of 9. 

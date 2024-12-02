# pittsburgh_iz
The Effects of Inclusionary Zoning on New Housing Construction in Pittsburgh

About this Repository:
We collected data on zoning applications, building permits, and occupancy permits on all buildings of 20 units or more built within the Pittsburgh city limits since 2012. This data was collected from City of Pittsburgh's public databases of permits, archived by the Western Pennsylvania Regional Data Center (https://data.wprdc.org/dataset/pli-permits). We have made the results of our data collection available in this public repository (See “2024.12.01 Buildings of 20 units or more built in Pittsburgh since 2012.csv”). Buildings were considered "complete" when a Certificate of Occupancy was issued by the city. To double check our results, we looked up each building of 20 units or more on Agency Counter (https://pittsburghpa.agencycounter.com) to confirm the beginning and end dates of the project.  We further looked up the floorplans of each building, when publicly available, to confirm that the number of units in the Certificate of Occupancy matched the number of units in the building.

We considered a building to be subject to the IZ ordinance based on the dates for a completed Zoning application. We defined a Zoning application as complete based on the dates that Agency Counter indicated "Zoning Review Accepted" and "Zoning Review Approved."

We only counted market-rate buildings with 20 or more units, because those buildings would be the only ones subject to the IZ ordinance. Dormitories and hotels are excluded, as they are not subject to the IZ ordinance.

We run a Difference-in-difference on our dataset to estimate the effect of IZ on construction of buildings of 20 units or more in Lawrenceville as compared to the Strip District and South Side Flats. We chose Lawrenceville as our treatment group since buildings have been completed there since IZ went into effect. We chose the Strip District and South Side Flats as our control group since they had similar patterns of construction to Lawrenceville prior to the implementation of IZ and are geographically and demographically similar to Lawrenceville, as well as having similar zoning (with the exception of IZ). 

This analysis is limited by the small size of our dataset, as only 109 buildings of 20 units or more were completed citywide between January 2012 and November 2024, with only 29 of those buildings in Lawrenceville, South Side Flats, and Strip District.

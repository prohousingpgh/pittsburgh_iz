# pittsburgh_iz
[The Effects of Inclusionary Zoning on New Housing Construction in Pittsburgh](The_Effects_of_Inclusionary_Zoning_on_New_20__Unit_Housing_Projects_in_Pittsburgh_FINAL_01262024.pdf)

**Abstract**

The City of Pittsburgh is in the midst of a housing crisis. To address the housing crisis, Pittsburgh has proposed expanding its Inclusionary Zoning (‘IZ’) overlay citywide.  This overlay was initially implemented in 2019 in Lawrenceville, in 2021 in Polish Hill and Bloomfield, and in 2022 in Oakland, and mandates that 10\% of units in projects of 20 units or more be rented or sold as Affordable Housing. Critics of this policy argue that as it is a mandate without sufficient offsetting subsidies, the overlay acts as a tax on new development, which constrains the housing supply and drives rents up further.  Using a difference-in-differences approach on building permit data in Lawrenceville, the Strip District, and South Side Flats from 2012 to the present day, we find that following the implementation of IZ, the rate of new housing construction in Lawrenceville decreased by 30\%, while the rate of new housing construction in the Strip District and South Side Flats, where IZ was not implemented, increased by 36\% and 18\%, respectively.

**About this Repository**

This respository contains the dataset we used in our study, along with associated difference-in-difference math, and the research paper itself.

For our research, we collected data on zoning applications, building permits, and occupancy permits on all buildings of 20 units or more built within the Pittsburgh city limits since 2012. This data was collected from City of Pittsburgh's public databases of permits, archived by the Western Pennsylvania Regional Data Center (https://data.wprdc.org/dataset/pli-permits). We have made the results of our data collection available in this public repository (See “2024.12.01 Buildings of 20 units or more built in Pittsburgh since 2012.csv”). Buildings were considered "complete" when a Certificate of Occupancy was issued by the city. To double check our results, we looked up each building of 20 units or more on Agency Counter (https://pittsburghpa.agencycounter.com) to confirm the beginning and end dates of the project.  We further looked up the floorplans of each building, when publicly available, to confirm that the number of units in the Certificate of Occupancy matched the number of units in the building.

We considered a building to be subject to the IZ ordinance based on the dates for a completed Zoning application. We defined a Zoning application as complete based on the dates that Agency Counter indicated "Zoning Review Accepted" and "Zoning Review Approved."

We only counted market-rate buildings with 20 or more units, because those buildings would be the only ones subject to the IZ ordinance. Dormitories and hotels are excluded, as they are not subject to the IZ ordinance.

We run a Difference-in-difference on our dataset to estimate the effect of IZ on construction of buildings of 20 units or more in Lawrenceville as compared to the Strip District and South Side Flats. We chose Lawrenceville as our treatment group since buildings have been completed there since IZ went into effect. We chose the Strip District and South Side Flats as our control group since they had similar patterns of construction to Lawrenceville prior to the implementation of IZ and are geographically and demographically similar to Lawrenceville, as well as having similar zoning (with the exception of IZ). 

This analysis is limited by the small size of our dataset, as only 109 buildings of 20 units or more were completed citywide between January 2012 and November 2024, with only 29 of those buildings in Lawrenceville, South Side Flats, and Strip District.

**The research study was authored by**

Jack Billings (University of East Anglia, Pro-Housing Pittsburgh) and David Vatz (Pro-Housing Pittsburgh)

**Special Thanks To**

Volunteers from Pro-Housing Pittsburgh, including: Chris Beam, Jack Billings, John Dellape, Lucas Godshalk, Kuanyu Lai, Nick Rizzio, David Vatz, and Amy Zaiss; from the
City Controller’s office, Controller Rachael Heisler and Research Director Mark Ptak; and The Western Pennsylvania Regional Data Center for their archive of permit data

&copy; 2024 Pro-Housing Pittsburgh

**License**

Shield: [![CC BY-NC 4.0][cc-by-nc-shield]][cc-by-nc]

This work is licensed under a
[Creative Commons Attribution-NonCommercial 4.0 International License][cc-by-nc].

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: https://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
[cc-by-nc-shield]: https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg

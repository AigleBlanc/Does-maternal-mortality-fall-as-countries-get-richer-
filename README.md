Does-maternal-mortality-fall-as-countries-get-richer?

We explored the above question by plotting the average annual change in GDP per capita against the
average annual change in maternal mortality ratio.

The maternal mortality ratio is the number of women who die from pregnancy-related
causes while pregnant or within 42 days of pregnancy termination per 100,000 live
births. 
The GDP per capita of a country is the GDP of that country divided by its
population. 

We improve on the author’s visualisation to allow interesting observations on the
interaction between maternal mortality ratio and income change. We do not
limit our discussion to analysing only the rate of income change; because a country’s
income level might affect how its maternal mortality ratio changes as it gets richer.
SO, we assigned each country to an income level group for analysis. We used the World Bank’s
classification of countries into income groups (based on their GNI per capita) and
data from the World Bank and OWiD. The four groups are:
1. Low Income: countries that were classified as low income countries in 1990
and also in 2015

2. Middle Income: countries that were classified as lower-middle income or
upper-middle income countries both in 1990 and in 2015
3. High Income: countries that were classified as high income countries in 1990
and also in 2015
4. Transitioned: countries whose classification has moved from low to middle or
high income, or from middle to high income.

Also note:

● Only countries for which we have data for 1990 and 2015 on all variables (for
our analysis) are included in the visualisation

● A linear regression line has been added to illustrate possible relationships
between the two variables. This helps us illustrate the relationship between the two ratios of change These relationships are otherwise harder to observe, since the number of countries visualised is not very large

● P-values are reported, to evaluate the fitted regression models. We will examine how the income group of a country affect its fall in
maternal mortality ratio as it gets richer

● Each income group is represented in a unique plot (graph)


Results:

We observe a relationship between the rate of change in GDP per capita and the
rate of change in maternal mortality ratio, although the relationship is not statistically
strong. There is a negative correlation between the two variables in low income
and middle income countries, and countries that transitioned. However, the
correlation is not negative in high income countries. 

The (p-value,slope)'s of the regressions are given for low income, middle income, transitioned, and high income groups as follows: (0.0148, -0.48), (0.0617, -0.38), (0.0080, -0.29), (0.1573, +0.56)

In the cases where we observed a negative correlation, it is also (sufficiently)
statistically significant to deduce that the faster a country&#39;s income increases the
faster its maternal mortality ratio falls. This is likely due to the fact that in lower
income countries, the increase in income improves living conditions, nutrition,
healthcare and education - factors that also affect maternal mortality. Although the
result is not statistically significant (due to a high p-value), we can argue that the rate
at which a high income country gets richer does not affect the fall in its maternal
mortality ratio. With healthcare and education already developed, more wealth may
in fact lead to bad consumption choices and exposure to different health hazards
during pregnancy - slowing the fall in maternal mortality ratio.

Data: 

Data on maternal mortality ratio and gdp per capita: OWiD https://ourworldindata.org/grapher/the-maternal-mortality-ratio-in-2000-and-2017

Data on historical GNI per capita: Word Bank (scroll down to source at the end of
the page) https://datatopics.worldbank.org/world-development-indicators/the-world-by-income-and-region.html

Word Bank thresholds for income group classification: World Bank https://datatopics.worldbank.org/world-development-indicators/stories/the-classification-of-countries-by-income.html

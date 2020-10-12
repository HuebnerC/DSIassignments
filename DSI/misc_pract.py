import pandas as pd
reviews = pd.read_csv('/Users/carlahuebner/Documents/databases/archive/winemag.csv')
new_df = reviews.loc[reviews['points'] >= 95]
final = new_df.loc[new_df['country'].isin(['Australia', 'New Zealand' ])]
country_list = []
for item in reviews.country: 
    country_list.append(item)
country_list = set(list(country_list))
country_count = reviews.groupby(by='country').count()

s = country_count.iloc[:,3]


# price with mean price subtracted

mean_price = reviews.loc[:, 'price'].mean()
centered_price = reviews.loc[:, 'price'].apply(lambda x: x-mean_price)


bargain_price = reviews.loc[:, 'points']/reviews.loc[:, 'price']
df = pd.concat((reviews, bargain_price), axis=1)
row_id_of_max = df[0].argmax()
row_max = df.iloc[row_id_of_max]
t_row_max = row_max.transpose()


# bargain_idx = (reviews.points / reviews.price).idxmax()
# bargain_wine = reviews.loc[bargain_idx, 'title']

trop_counts = reviews.description.str.count('tropical').sum()
fruit_counts = reviews.description.str.count('fruity').sum()

descriptor_counts = pd.Series([trop_counts, fruit_counts], index=['tropical', 'fruity'])


n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts1 = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 
# points is too hard to understand - we'd like to translate them into simple star ratings. A 
# score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. 
# Any other score is 1 star.

# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from 
# Canada should automatically get 3 stars, regardless of points.

# Create a series star_ratings with the number of stars corresponding to each review in the 
# dataset.

# for col in country_count.columns:
#     print(col)
# def star_func(x): 
#     if x >=95: 
#         return 3
#     if 85 <= x and x < 95:
#         return 2
#     else: 
#         return 1

# stars_nums = reviews.points.map(star_func)

# print(stars_nums)
# # print(reviews.loc[reviews['winery'] == 'Canadian Vintners Association'], ['winery'])
# print(reviews.loc[reviews['winery'].isin(['Canadian Vintners Association' ])])


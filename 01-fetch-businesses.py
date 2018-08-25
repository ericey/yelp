# Which data set to use
DATA_SET = 'sfRestaurants';

# The definining parameters for data sets. To add a new one, you must specify
# origin, padding, and categories.
#
# origin: the latitude and longitude of the center of the region
# padding: how far north, south, east and west to go from the origin.

DATA_SETS = {
    'sfRestaurants': {
        'origin': (37.75, -122.45),
        'padding': 20,
        'categories': 'restaurants'
    }
}

# How much latitude and longitude to traverse per step of padding.
PADDING_AMOUNT = 1/200

# The maximum distance covered by 1 degree latitude is 111.694km.
# The maximum distance covered by 1 degree longitude is 111.320 km.
# The max radius in yelp search queries is 40000m.
# Use 500m for yelp queries
# If lattice step = s, then padding needs to be bigger than sqrt(2)/2 * s

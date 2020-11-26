

### GCP Storage - - - - - - - - - - - - - - - - - - - - - -

PROJECT_NAME = 'star-project-296512'
BUCKET_NAME = 'data-475'
# os.getenv('MAPBOX_API_KEY')
BUCKET_TRAIN_DATA_PATH = 'data/jan'
LISTINGS_COLUMNS = ['id',
             'name',
             'summary',
             'space',
             'description',
             'experiences_offered',
             'neighborhood_overview',
             'notes',
             'transit',
             'access',
             'interaction',
             'house_rules',
             'host_since',
             'host_location',
             'host_about',
             'host_response_time',
             'host_response_rate',
             'host_neighbourhood',
             'host_listings_count',
             'host_total_listings_count',
             'host_verifications',
             'host_identity_verified',
             'street',
             'neighbourhood_cleansed',
             'zipcode',
             'latitude',
             'longitude',
             'is_location_exact',
             'property_type',
             'room_type',
             'accommodates',
             'bathrooms',
             'bedrooms',
             'beds',
             'bed_type',
             'amenities',
             'price',
             'weekly_price',
             'monthly_price',
             'security_deposit',
             'cleaning_fee',
             'guests_included',
             'extra_people',
             'minimum_nights',
             'maximum_nights',
             'availability_30',
             'availability_60',
             'availability_90',
             'availability_365',
             'number_of_reviews',
             'number_of_reviews_ltm',
             'first_review',
             'last_review',
             'review_scores_rating',
             'review_scores_accuracy',
             'review_scores_cleanliness',
             'review_scores_checkin',
             'review_scores_communication',
             'review_scores_location',
             'review_scores_value',
             'instant_bookable',
             'cancellation_policy',
             'require_guest_profile_picture',
             'require_guest_phone_verification',
             'reviews_per_month']

KEY_AMENITIES = ['Free parking on premises', ['Hot tub','shared hot tub','private hot tub'],
                        ['Gym','shared gym'], ['Pool','private pool','shared pool'],
                        ['Kitchen','kitchenette','full kitchen',"chef's kitchen"],'Shampoo','Heating','Air conditioning',
                        ['Washing machine','Washer','Washer / Dryer'],'Dryer','Wifi','Breakfast',
                        'Indoor fireplace','Hangers','Iron','Hair dryer',['Dedicated workspace','laptop friendly workspace'],
                        ['TV', 'cable tv'],['Cot',"Pack 'n Play/travel crib', 'crib"],'High chair',
                        'Self check-in',['Smoke alarm','Smoke detector'],['Carbon monoxide alarm','carbon monoxide detector'],
                        'Private bathroom']

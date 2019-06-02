BRAND_TYPE = (
    (0, '-'),
    (1, 'NISSAN'),
    (2, 'TOYOTO')
)

MODEL_TYPE = (
    (0, '-'),
    (1, 'XTRAIL'),
    (2, 'NOVADO'),
    (3, 'CAMRY')
)


CAR_TYPE = (
    (1, 'SUV'),
    (2, 'ROAD')
)

TRIP_TYPE = (
    (1, 'ONE WAY'),
    (2, 'ROUND')
)

ACTIONS = (
    (0, 're-open'),
    (1, 'assign'),
    (2, 'accept'),
    (3, 'discard'),
    (4, 'close')
)

STATUSES = (
    (0, 'open'),
    (1, 'assigned'),
    (2, 'accepted'),
    (3, 'discarded'),
    (4, 'close')
)

PRIORITY_SCALES = (
    (0, 'No'),
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High'),
    (4, 'Urgent'),
)


REASONS = (
    (0,  '-'),
    (1,  'PERSONAL REASON'),
    (2,  'BASE VISIT'),
    (3,  'PLATFORM VISIT'),
    (3,  'DELIVERY'),
)

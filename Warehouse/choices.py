STATUSES = (
    (0, 'open'),
    (1, 'assigned'),
    (2, 'accepted'),
    (3, 'discarded'),
    (4, 'close')
)

ACTIONS = (
    (0, 're-open'),
    (1, 'assign'),
    (2, 'accept'),
    (3, 'discard'),
    (4, 'close')
)

CATEGORIES = (
    (0,  '-'),
    (1,  'Office materials'),
    (2,  'Hardware parts'),
)

SUBJECTS = (
    (0,  '-'),
    (1,  'Laptop/PC'),
    (2,  'Software problem'),
    (3,  'Software request'),

)

PRIORITY_SCALES = (
    (0, '-'),
    (1, 'No'),
    (2, 'Low'),
    (3, 'Medium'),
    (4, 'High'),
    (5, 'Urgent'),
)


REASONS = (
    (0,  '-'),
    (1,  'Laptop/PC'),
    (2,  'Software problem'),
    (3,  'Software request'),
    (4,  'Printer problem'),
    (5,  'Network/Internet problem'),
    (6,  'General incident'),
    (7,  'FileServer access'),
    (8,  'MediaServer access'),
    (9,  'WiFi guest access'),
    (10, 'Network access'),
    (11, 'VPN access'),
    (12, 'Mail issue'),
    (13, 'MailonMobile'),
    (14, 'Other')
)

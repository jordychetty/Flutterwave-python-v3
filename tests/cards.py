# contains test cards and bank accounts from
# https://developer.flutterwave.com/docs/test-cards for sake of ease

from typing import (
    Dict,
    NewType
)

BankCard = NewType('BankCard', Dict[str, str])

MASTERCARD_PIN_AUTHENTICATION: Dict[str, str] = frozenset({
    'card_number': '5531886652142950',
    'cvv': '564',
    'expiry': '09/32',
    'pin': '3310',
    'otp': '12345'
})

VISA_CARD_3DSECURE_VBVSECURECODE: Dict[str, str] = frozenset({
    'card_number': '4187427415564246',
    'cvv': '828',
    'expiry': '09/32',
    'pin': '3310',
    'otp': '12345'
})

AVS_CARD: Dict[str, str] = frozenset({
    'card_number': '4556052704172643',
    'cvv': '899',
    'expiry': '09/32',
    'pin': '3310',
    'otp': '12345'
})

MASTERCARD_3DSECURE_VBVSECURECODE: Dict[str, str] = frozenset({
    'card_number': '5438898014560229',
    'cvv': '564',
    'expiry': '10/31',
    'pin': '3310',
    'otp': '12345'
})

MASTERCARD_PIN_2: Dict[str, str] = frozenset({
    'card_number': '5399838383838381',
    'cvv': '470',
    'expiry': '10/31',
    'pin': '3310',
    'otp': '12345'
})


VBVSECURECODE_CARD: Dict[str, str] = frozenset({
    'card_number': '4751763236699647',
    'cvv': '470',
    'expiry': '09/35',
    'pin': '3310',
    'otp': '12345'
})

VISACARD_3DSECURE: Dict[str, str] = frozenset({
    'card_number': '4242424242424242',
    'cvv': '812',
    'expiry': '01/31',
    'pin': '3310',
    'otp': '12345'
})

VERVE_CARD_PIN: Dict[str, str] = frozenset({
    'card_number': '5061460410120223210',
    'cvv': '780',
    'expiry': '12/31',
    'pin': '3310',
    'otp': '12345'
})

CARD_DECLINED_ADDRESS_VERIFICATION: Dict[str, str] = frozenset({
    'card_number': '5143010522339965',
    'cvv': '276',
    'expiry': '08/32',
    'pin': '3310',
    'otp': '12345'
})

CARD_FRAUDULENT: Dict[str, str] = frozenset({
    'card_number': '5590131743294314',
    'cvv': '887',
    'expiry': '11/32',
    'pin': '3310',
    'otp': '12345'
})

CARD_INSUFFICIENT_FUNDS: Dict[str, str] = frozenset({
    'card_number': '5258585922666506',
    'cvv': '883',
    'expiry': '09/31',
    'pin': '3310',
    'otp': '12345'
})

PRE_AUTHORIZATION_CARD: Dict[str, str] = frozenset({
    'card_number': '5377283645077450',
    'cvv': '789',
    'expiry': '09/31',
    'pin': '3310',
    'otp': '12345'
})

CARD_DO_NOT_HONOUR: Dict[str, str] = frozenset({
    'card_number': '5143010522339965',
    'cvv': '276',
    'expiry': '08/31',
    'pin': '3310',
    'otp': '12345'
})

CARD_INVALID_TRANSACTION: Dict[str, str] = frozenset({
    'card_number': '5551658157653822',
    'cvv': '276',
    'expiry': '08/31',
    'pin': '3310',
    'otp': '12345'
})

RESTRICTED_RETAIN_CARD: Dict[str, str] = frozenset({
    'card_number': '5551651630381384',
    'cvv': '276',
    'expiry': '08/31',
    'pin': '3310',
    'otp': '12345'
})

FUNCTION_NOT_PERMITTED_TO_CARDHOLDER_CARD: Dict[str, str] = frozenset({
    'card_number': '5258582054729020',
    'cvv': '887',
    'expiry': '11/30',
    'pin': '3310',
    'otp': '12345'
})

FUNCTION_NOT_PERMITTED_TO_TERMINAL_CARD: Dict[str, str] = frozenset({
    'card_number': '5258588264565682',
    'cvv': '887',
    'expiry': '11/30',
    'pin': '3310',
    'otp': '12345'
})

TRANSACTION_ERROR: Dict[str, str] = frozenset({
    'card_number': '5258589130149016',
    'cvv': '887',
    'expiry': '11/30',
    'pin': '3310',
    'otp': '12345'
})

INCORRECT_PIN: Dict[str, str] = frozenset({
    'card_number': '5399834697894723',
    'cvv': '883',
    'expiry': '09/31',
    'pin': '3310',
    'otp': '12345'
})

VERVE_CARD_CARD_ENROLMENT: Dict[str, str] = frozenset({
    'card_number': '5531882884804517',
    'cvv': '564',
    'expiry': '10/32',
    'pin': '3310',
    'otp': '12345'
})

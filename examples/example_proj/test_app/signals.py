from django.dispatch import Signal


test_signal = Signal(providing_args=['instance', 'test_arg'])

Saits)) + digits[-l:])
    return sep.join(reversed(groups))

def _format_sign(is_negative, spec):
    """Determine sign character."""

    if is_negative:
        return '-'
    elif spec['sign'] in ' +':
        return spec['sign']
    else:
        return ''

def _format_number(is_negative, intpart, fracpart, exp, spec):
    """Format a number, given the following data:

    is_negative: true if the number is negative, else false
    intpart: string of digits that must appear before the decimal point
    fracpart: string of digits that must come after the point
    exp: exponent, as an integer
    spec: dictionary resulting from parsing the format specifier

    This function uses the information in spec to:
      insert separators (decimal separator and thousands separators)
      format the sign
      format the exponent
      add trailing '%' for the '%' type
      zero-pad if necessary
      fill and align if necessary
    """

    sign = _format_sign(is_negative, spec)

    if fracpart:
        fracpart = spec['decimal_point'] + fracpart

    if exp != 0 or spec['type'] in 'eE':
        echar = {'E': 'E', 'e': 'e', 'G': 'E', 'g': 'e'}[spec['type']]
        fracpart += "{0}{1:+}".format(echar, exp)
    if spec['type'] == '%':
        fracpart += '%'

    if spec['zeropad']:
        min_width = spec['minimumwidth'] - len(fracpart) - len(sign)
    else:
        min_width = 0
    intpart = _insert_thousands_sep(intpart, spec, min_width)

    return _format_align(sign, intpart+fracpart, spec)


##### Useful Constants (internal use only) ################################

# Reusable defaults
_Infinity = Decimal('Inf')
_NegativeInfinity = Decimal('-Inf')
_NaN = Decimal('NaN')
_Zero = Decimal(0)
_One = Decimal(1)
_NegativeOne = Decimal(-1)

# _SignedInfinity[sign] is infinity w/ that sign
_SignedInfinity = (_Infinity, _NegativeInfinity)



if __name__ == '__main__':
    import doctest, sys
    doctest.testmod(sys.modules[__name__])
  iterable of integers representing group lengths.

    """
    # The result from localeconv()['grouping'], and the input to this
    # function, should be a list of integers in one of the
    # following three forms:
    #
    #   (1) an empty list, or
    #   (2) nonempty list of positive integers + [0]
    #   (3) list of positive integers + [locale.CHAR_MAX], or

    from itertools import chain, repeat
    if not grouping:
        return []
    elif grouping[-1] == 0 and len(grouping) >= 2:
        return chain(grouping[:-1], repeat(grouping[-2]))
    elif grouping[-1] == _locale.CHAR_MAX:
        return grouping[:-1]
    else:
        raise ValueError('unrecognised format for grouping')

def _insert_thousands_sep(digits, spec, min_width=1):
    """Insert thousands separators into a digit string.

    spec is a dictionary whose keys should include 'thousands_sep' and
    'grouping'; typically it's the result of parsing the format
    specifier using _parse_format_specifier.

    The min_width keyword argument gives the minimum length of the
    result, which will be padded on the left with zeros if necessary.

    If necessary, the zero padding adds an extra '0' on the left to
    avoid a leading thousands separator.  For example, inserting
    commas every three digits in '123456', with min_width=8, gives
    '0,123,456', even though that has length 9.

    """

    sep = spec['thousands_sep']
    grouping = spec['grouping']

    groups = []
    for l in _group_lengths(grouping):
        if l <= 0:
            raise ValueError("group length should be positive")
        # max(..., 1) forces at least 1 digit to the left of a separator
        l = min(max(len(digits), min_width, 1), l)
        groups.append('0'*(l - len(digits)) + digits[-l:])
        digits = digits[:-l]
        min_width -= l
        if not digits and min_width <= 0:
            break
        min_width -= len(sep)
    else:
        l = max(len(digits), min_width, 1)
        groups.append('0'*(l - len(d
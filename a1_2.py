#a1.py
#Emma Vedock-Gross ev225, Trey Aguirre tea42
#9/17/2016

"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange."""

#Part A
def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    space=s.index(' ')
    result=s[0:space]
    return result
    
def after_space(s):
    """Returns: Substring of s after the first space
    Parameter s: the string to slice
    Precondition: s has at least one space in it"""
    space=s.index(' ')
    result=s[space+1:]
    return result

#Part C
import urllib2

def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'
    
    where the values old-amount and new-amount contain the value and name 
    for the original and new currencies. If the query is invalid, both 
    old-amount and new-amount will be empty, while "valid" will be followed 
    by the value false.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)
    webPage = urllib2.urlopen(url)
    json = webPage.read()
    return json

#Part D
def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    
    json = currency_response(currency, currency, 1)
    return has_error(json) == False

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    
    json = currency_response(currency_from, currency_to, amount_from)
    convertedAmount = get_to(json)
    convertedFloat = before_space(convertedAmount)
    return float(convertedFloat)  
#a1.py
#Emma Vedock-Gross ev225
#6/8/2016

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
    
#Part B
#def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote characters
    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if we want to use a double quote character (") inside of it.
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C' because it only picks the first such substring.
    Parameter s: a string to search
    Precondition: s a string with at least two (double) quote characters."""
   
   #finds first double quote
 #   start=s.index('"')
    #finds part after double quote
 #   tail=s[start+1:]
    #finds second double quote
 #   end=tail.index('"')
    #defines result as part the part within double quotes
 #   result=tail[:end]
   #returns part of string within double quotes
 #   return result

#def exchange(currency_from, currency_to, amount_from):
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

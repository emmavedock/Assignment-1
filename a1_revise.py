#a1.py
#Emma Vedock-Gross ev225, Trey Aguirre tea42
#9/18/2016

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
def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote characters
    
    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if we want to use a double quote character (") inside of it.
    
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C' because it only picks the first such substring.
    
    Parameter s: a string to search
    Precondition: s a string with at least two (double) quote characters."""
    
    start=s.index('"')
    tail=s[start+1:]
    end=tail.index('"')
    result=tail[:end]
    return result


def get_from(json):
    """Returns: The FROM value in the response to a currency query.
    
    Given a JSON response to a currency query, this returns the string inside double quotes (")
    immediately following the keyword "from". For example, if the JSON is
    '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    It returns the empty string if the JSON is the result of on invalid query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    
    return first_inside_quotes(json[json.index('"from"')+6:])


def get_to(json):
    """Returns: The TO value in the response to a currency query.
    
    Given a JSON response to a currency query, this returns the string inside double quotes (")
    immediately following the keyword "to". For example, if the JSON is
    '{"from":"2 United States Dollars","to":"1.825936 Euros","success":true,"error":""}'
    then this function returns '1.825936 Euros' (not '"1.825936 Euros"').
    It returns the empty string if the JSON is the result of on invalid query.
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""    
    
    return first_inside_quotes(json[json.index('"to"')+4:])


def has_error(json):
    """Returns: True if the query has an error; False otherwise.
    
    Given a JSON response to a currency query, this returns the opposite of the value following the keyword "valid". For example, if the JSON is
    '{"from":"","to":"","success":false,"error":"Source currency code is invalid."}'
    then the query is not valid, so this function returns True (It does NOT return the message 'Source currency code is invalid').
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    
    start=json.index('success')
    end=json.index('error')
    result=json[start+11:end-3]
    return result == 'false'


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
    
    url = ('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to +
           '&amt=' + str(amount_from))
    webPage = urllib2.urlopen(url)
    json = webPage.read()
    return json

#Part D
def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.
    
    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    
    json = currency_response('USD', currency, 1.0)
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